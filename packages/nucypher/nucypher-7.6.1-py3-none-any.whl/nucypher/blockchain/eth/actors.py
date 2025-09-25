import json
import random
import time
import traceback
from collections import defaultdict
from decimal import Decimal
from typing import Dict, List, Optional, Union

import maya
from atxm.exceptions import InsufficientFunds
from atxm.tx import AsyncTx, FaultedTx, FinalizedTx, FutureTx, PendingTx
from eth_typing import ChecksumAddress
from nucypher_core import (
    EncryptedThresholdDecryptionRequest,
    EncryptedThresholdDecryptionResponse,
    SessionStaticKey,
    ThresholdDecryptionRequest,
    ThresholdDecryptionResponse,
)
from nucypher_core.ferveo import (
    AggregatedTranscript,
    CiphertextHeader,
    DecryptionSharePrecomputed,
    DecryptionShareSimple,
    DkgPublicKey,
    FerveoVariant,
    HandoverTranscript,
    Transcript,
    Validator,
    ValidatorMessage,
)
from web3 import HTTPProvider, Web3
from web3.types import TxReceipt

from nucypher.acumen.nicknames import Nickname
from nucypher.blockchain.eth.agents import (
    ContractAgency,
    CoordinatorAgent,
    TACoApplicationAgent,
    TACoChildApplicationAgent,
)
from nucypher.blockchain.eth.constants import (
    NULL_ADDRESS,
    PUBLIC_CHAINS,
)
from nucypher.blockchain.eth.decorators import validate_checksum_address
from nucypher.blockchain.eth.domains import TACoDomain
from nucypher.blockchain.eth.interfaces import (
    BlockchainInterface,
    BlockchainInterfaceFactory,
)
from nucypher.blockchain.eth.models import (
    HANDOVER_AWAITING_BLINDED_SHARE,
    HANDOVER_AWAITING_TRANSCRIPT,
    PHASE1,
    PHASE2,
    Coordinator,
)
from nucypher.blockchain.eth.registry import ContractRegistry
from nucypher.blockchain.eth.signers import Signer
from nucypher.blockchain.eth.trackers import dkg
from nucypher.blockchain.eth.trackers.bonding import OperatorBondedTracker
from nucypher.blockchain.eth.utils import (
    get_healthy_default_rpc_endpoints,
    rpc_endpoint_health_check,
    truncate_checksum_address,
)
from nucypher.crypto.ferveo.exceptions import FerveoKeyMismatch
from nucypher.crypto.powers import (
    CryptoPower,
    RitualisticPower,
    ThresholdRequestDecryptingPower,
    TransactingPower,
)
from nucypher.datastore.dkg import DKGStorage
from nucypher.policy.conditions.utils import (
    ConditionProviderManager,
    evaluate_condition_lingo,
)
from nucypher.policy.payment import ContractPayment
from nucypher.types import PhaseId
from nucypher.utilities.emitters import StdoutEmitter
from nucypher.utilities.logging import Logger
from nucypher.utilities.warnings import render_ferveo_key_mismatch_warning


class BaseActor:
    """
    Concrete base class for any actor that will interface with NuCypher's ethereum smart contracts.
    """

    class ActorError(Exception):
        pass

    @validate_checksum_address
    def __init__(
        self,
        domain: TACoDomain,
        registry: ContractRegistry,
        transacting_power: Optional[TransactingPower] = None,
        checksum_address: Optional[ChecksumAddress] = None,
    ):
        if not (bool(checksum_address) ^ bool(transacting_power)):
            error = f"Pass transacting power or checksum address, got {checksum_address} and {transacting_power}."
            raise ValueError(error)

        try:
            parent_address = self.checksum_address
            if checksum_address is not None:
                if parent_address != checksum_address:
                    raise ValueError(
                        f"Can't have two different ethereum addresses. "
                        f"Got {parent_address} and {checksum_address}."
                    )
        except AttributeError:
            if transacting_power:
                self.checksum_address = transacting_power.account
            else:
                self.checksum_address = checksum_address

        self.transacting_power = transacting_power
        self.registry = registry
        self.domain = domain
        self._saved_receipts = list()  # track receipts of transmitted transactions

    def __repr__(self):
        class_name = self.__class__.__name__
        r = "{}(address='{}')"
        r = r.format(class_name, self.checksum_address)
        return r

    def __eq__(self, other) -> bool:
        """Actors are equal if they have the same address."""
        try:
            return bool(self.checksum_address == other.checksum_address)
        except AttributeError:
            return False

    @property
    def eth_balance(self) -> Decimal:
        """Return this actor's current ETH balance"""
        blockchain = (
            BlockchainInterfaceFactory.get_interface()
        )  # TODO: EthAgent?  #1509
        balance = blockchain.client.get_balance(self.wallet_address)
        return Web3.from_wei(balance, "ether")

    @property
    def wallet_address(self):
        return self.checksum_address


class NucypherTokenActor(BaseActor):
    """
    Actor to interface with the NuCypherToken contract
    """

    def __init__(self, registry: ContractRegistry, **kwargs):
        super().__init__(registry=registry, **kwargs)
        self.__token_agent = None


class Operator(BaseActor):
    READY_TIMEOUT = None  # (None or 0) == indefinite
    READY_POLL_RATE = 120  # seconds
    AGGREGATION_SUBMISSION_MAX_DELAY = 60
    LOG = Logger("operator")

    class OperatorError(BaseActor.ActorError):
        """Operator-specific errors."""

    class RitualNotFoundException(Exception):
        """Ritual is not found."""

    class UnauthorizedRequest(Exception):
        """Request is not authorized."""

    class DecryptionFailure(Exception):
        """Decryption failed."""

    def __init__(
        self,
        eth_endpoint: str,
        polygon_endpoint: str,
        pre_payment_method: ContractPayment,
        transacting_power: TransactingPower,
        signer: Signer = None,
        crypto_power: CryptoPower = None,
        client_password: str = None,
        operator_address: Optional[ChecksumAddress] = None,
        condition_blockchain_endpoints: Optional[Dict[int, List[str]]] = None,
        publish_finalization: bool = True,  # TODO: Remove this
        *args,
        **kwargs,
    ):
        # Falsy values may be passed down from the superclass
        if not eth_endpoint:
            raise ValueError("Ethereum endpoint URI is required to init an operator.")
        if not polygon_endpoint:
            raise ValueError("Polygon endpoint URI is required to init an operator.")
        if not pre_payment_method:
            raise ValueError("PRE payment method is required to init an operator.")

        if not transacting_power:
            transacting_power = TransactingPower(
                account=operator_address,
                password=client_password,
                signer=signer,
                cache=True,
            )

        # We pass the newly instantiated TransactingPower into consume_power_up here, even though it's accessible
        # on the instance itself (being composed in the __init__ of the base class, which we will call shortly)
        # because, given the need for initialization context, it's far less melodramatic
        # to do it here, and it's still available via the public crypto powers API.
        crypto_power.consume_power_up(transacting_power)

        self.pre_payment_method = pre_payment_method
        self._operator_bonded_tracker = OperatorBondedTracker(ursula=self)

        super().__init__(transacting_power=transacting_power, *args, **kwargs)
        self.log = Logger("operator")

        self.__staking_provider_address = None  # set by block_until_ready

        self.application_agent = ContractAgency.get_agent(
            TACoApplicationAgent,
            blockchain_endpoint=eth_endpoint,
            registry=self.registry,
        )

        registry = ContractRegistry.from_latest_publication(domain=self.domain)
        self.child_application_agent = ContractAgency.get_agent(
            TACoChildApplicationAgent,
            registry=registry,
            blockchain_endpoint=polygon_endpoint,
        )

        self.coordinator_agent = ContractAgency.get_agent(
            CoordinatorAgent,
            registry=registry,
            blockchain_endpoint=polygon_endpoint,
        )

        # track active onchain rituals
        self.ritual_tracker = dkg.ActiveRitualTracker(
            operator=self,
        )

        self.publish_finalization = (
            publish_finalization  # publish the DKG final key if True
        )

        self.ritual_power = crypto_power.power_ups(
            RitualisticPower
        )  # ferveo material contained within
        self.threshold_request_power = crypto_power.power_ups(
            ThresholdRequestDecryptingPower
        )  # used for secure decryption request channel

        self.condition_provider_manager = self.get_condition_provider_manager(
            condition_blockchain_endpoints
        )

        self.dkg_storage = DKGStorage()

    def set_provider_public_key(self) -> Union[TxReceipt, None]:
        # TODO: Here we're assuming there is one global key per node. See nucypher/#3167
        node_global_ferveo_key_set = self.coordinator_agent.is_provider_public_key_set(
            self.staking_provider_address
        )
        if not node_global_ferveo_key_set:
            receipt = self.coordinator_agent.set_provider_public_key(
                self.ritual_power.public_key(), transacting_power=self.transacting_power
            )
            return receipt

    @staticmethod
    def _make_condition_provider(uri: str) -> HTTPProvider:
        provider = HTTPProvider(endpoint_uri=uri)
        return provider

    def get_condition_provider_manager(
        self, operator_configured_endpoints: Dict[int, List[str]]
    ) -> ConditionProviderManager:

        # check that we have mandatory user configured endpoints
        mandatory_configured_chains = {
            self.domain.eth_chain.id,
            self.domain.polygon_chain.id,
        }
        if mandatory_configured_chains != set(operator_configured_endpoints):
            raise self.ActorError(
                f"Operator-configured condition endpoints for chains don't match mandatory chains: "
                f"{set(operator_configured_endpoints)} vs expected {mandatory_configured_chains}"
            )

        providers = defaultdict(list)  # use list to maintain order

        # ensure that no endpoint uri for a specific chain is repeated
        duplicated_endpoint_check = defaultdict(set)

        # Operator-configured endpoints for chains
        for chain_id, chain_rpc_endpoints in operator_configured_endpoints.items():
            if not chain_rpc_endpoints:
                raise self.ActorError(
                    f"Operator-configured condition endpoint is missing for the required chain {chain_id}"
                )
            # connect to each endpoint and check that they are on the correct chain
            for uri in chain_rpc_endpoints:
                if uri in duplicated_endpoint_check[chain_id]:
                    self.log.warn(
                        f"Operator-configured condition endpoint {uri} is duplicated for condition evaluation on chain {chain_id}; skipping."
                    )
                    continue

                provider = self._make_condition_provider(uri)
                if int(Web3(provider).eth.chain_id) != int(chain_id):
                    raise self.ActorError(
                        f"Operator-configured RPC condition endpoint {uri} does not belong to chain {chain_id}"
                    )
                healthy = rpc_endpoint_health_check(endpoint=uri)
                if not healthy:
                    self.log.warn(
                        f"Operator-configured RPC condition endpoint {uri} is unhealthy"
                    )
                providers[int(chain_id)].append(provider)
                duplicated_endpoint_check[chain_id].add(uri)

        # Ingest default/fallback RPC providers for each chain
        default_endpoints = get_healthy_default_rpc_endpoints(self.domain)
        for chain_id, chain_rpc_endpoints in default_endpoints.items():
            # randomize list so that the same fallback RPC endpoints aren't always used by all nodes
            random.shuffle(chain_rpc_endpoints)
            for uri in chain_rpc_endpoints:
                if uri in duplicated_endpoint_check[chain_id]:
                    self.log.warn(
                        f"Fallback blockchain endpoint, {uri}, is duplicated for condition evaluation on chain {chain_id}; skipping"
                    )
                    continue
                provider = self._make_condition_provider(uri)
                providers[chain_id].append(provider)
                duplicated_endpoint_check[chain_id].add(uri)

        self.log.info(
            f"Connected to {sum(len(v) for v in providers.values())} RPC endpoints for condition "
            f"checking on chain IDs {providers.keys()}"
        )

        return ConditionProviderManager(providers=providers)

    def _resolve_ritual(self, ritual_id: int) -> Coordinator.Ritual:
        if not self.coordinator_agent.is_ritual_active(ritual_id=ritual_id):
            self.dkg_storage.clear(ritual_id)
            raise self.ActorError(f"Ritual #{ritual_id} is not active.")

        ritual = self.dkg_storage.get_active_ritual(ritual_id)
        if not ritual:
            ritual = self.coordinator_agent.get_ritual(ritual_id)
            self.dkg_storage.store_active_ritual(active_ritual=ritual)

        return ritual

    def _resolve_validators(
        self,
        ritual: Coordinator.Ritual,
    ) -> List[Validator]:
        validators = self.dkg_storage.get_validators(ritual.id)
        if validators:
            return validators

        result = list()
        for i, staking_provider_address in enumerate(ritual.providers):
            if self.checksum_address == staking_provider_address:
                # Local
                public_key = self.ritual_power.public_key()
            else:
                # Remote
                # TODO optimize rpc calls by obtaining public keys altogether
                #  instead of one-by-one?
                public_key = self.coordinator_agent.get_provider_public_key(
                    provider=staking_provider_address, ritual_id=ritual.id
                )
            self.log.debug(
                f"Validator #{i}: {staking_provider_address}, public key: {bytes(public_key).hex()[:10]}"
            )
            validator = Validator(
                address=staking_provider_address,
                public_key=public_key,
                share_index=i,
            )
            result.append(validator)

        self.dkg_storage.store_validators(ritual.id, result)

        return result

    def _setup_async_hooks(
        self, phase_id: PhaseId, *args
    ) -> BlockchainInterface.AsyncTxHooks:

        TX_TYPES = {
            PHASE1: "POST_TRANSCRIPT",
            PHASE2: "POST_AGGREGATE",
            HANDOVER_AWAITING_TRANSCRIPT: "HANDOVER_AWAITING_TRANSCRIPT",
            HANDOVER_AWAITING_BLINDED_SHARE: "HANDOVER_POST_BLINDED_SHARE",
        }

        tx_type = TX_TYPES[phase_id.phase]

        def resubmit_tx():
            if phase_id.phase == PHASE1:
                # check status of ritual before resubmitting; prevent infinite loops
                if not self._is_phase_1_action_required(ritual_id=phase_id.ritual_id):
                    self.log.info(
                        f"No need to resubmit tx: additional action not required for ritual #{phase_id.ritual_id} "
                        f"(status={self.coordinator_agent.get_ritual_status(phase_id.ritual_id)})"
                    )
                    return
                async_tx = self.publish_transcript(*args)
            elif phase_id.phase == PHASE2:
                # check status of ritual before resubmitting; prevent infinite loops
                if not self._is_phase_2_action_required(ritual_id=phase_id.ritual_id):
                    self.log.info(
                        f"No need to resubmit tx: additional action not required for ritual #{phase_id.ritual_id} "
                        f"(status={self.coordinator_agent.get_ritual_status(phase_id.ritual_id)})"
                    )
                    return
                async_tx = self.publish_aggregated_transcript(*args)
            elif phase_id.phase == HANDOVER_AWAITING_TRANSCRIPT:
                # check status of handover before resubmitting; prevent infinite loops
                _, departing_validator, _ = args
                if not self._is_handover_transcript_required(
                    ritual_id=phase_id.ritual_id,
                    departing_validator=departing_validator,
                ):
                    self.log.info(
                        f"No need to resubmit tx: additional action not required for handover in ritual #{phase_id.ritual_id}"
                    )
                    return
                async_tx = self._publish_handover_transcript(*args)
            elif phase_id.phase == HANDOVER_AWAITING_BLINDED_SHARE:
                # check status of handover before resubmitting; prevent infinite loops
                if not self._is_handover_blinded_share_required(
                    ritual_id=phase_id.ritual_id
                ):
                    self.log.info(
                        f"No need to resubmit tx: additional action not required for handover in ritual #{phase_id.ritual_id}"
                    )
                    return
                async_tx = self._publish_blinded_share_for_handover(*args)
            else:
                raise ValueError(
                    f"Unsupported phase {phase_id.phase} for async tx resubmission"
                )

            self.log.info(
                f"{self.transacting_power.account[:8]} resubmitted a new async tx {async_tx.id} "
                f"of type {tx_type} for DKG ritual #{phase_id.ritual_id}."
            )

        def on_broadcast_failure(tx: FutureTx, e: Exception):
            # although error, tx was not removed from atxm
            self.log.warn(
                f"{tx_type} async tx {tx.id} for DKG ritual# {phase_id.ritual_id} "
                f"failed to broadcast {e}; the same tx will be retried"
            )
            # either multiple retries already completed for recoverable error,
            # or simply a non-recoverable error - remove and resubmit
            # (analogous action to a node restart of old)
            self.coordinator_agent.blockchain.tx_machine.remove_queued_transaction(tx)

            # submit a new one
            resubmit_tx()

        def on_fault(tx: FaultedTx):
            # fault means that tx was removed from atxm
            error = f"({tx.error})" if tx.error else ""
            self.log.warn(
                f"{tx_type} async tx {tx.id} for DKG ritual# {phase_id.ritual_id} "
                f"failed with fault {tx.fault.name}{error}; resubmitting a new one"
            )

            # submit a new one.
            resubmit_tx()

        def on_finalized(tx: FinalizedTx):
            # finalized means that tx was removed from atxm
            if not tx.successful:
                self.log.warn(
                    f"{tx_type} async tx {tx.id} for DKG ritual# {phase_id.ritual_id} "
                    f"was reverted; resubmitting a new one"
                )

                # submit a new one.
                resubmit_tx()
            else:
                # success and blockchain updated - no need to store tx anymore
                self.dkg_storage.clear_ritual_phase_async_tx(
                    phase_id=phase_id, async_tx=tx
                )

        def on_insufficient_funds(tx: Union[FutureTx, PendingTx], e: InsufficientFunds):
            # although error, tx was not removed from atxm
            self.log.error(
                f"{tx_type} async tx {tx.id} for DKG ritual# {phase_id.ritual_id} "
                f"cannot be executed because {self.transacting_power.account[:8]} "
                f"has insufficient funds {e}"
            )

        async_tx_hooks = BlockchainInterface.AsyncTxHooks(
            on_broadcast_failure=on_broadcast_failure,
            on_fault=on_fault,
            on_finalized=on_finalized,
            on_insufficient_funds=on_insufficient_funds,
        )

        return async_tx_hooks

    def publish_transcript(self, ritual_id: int, transcript: Transcript) -> AsyncTx:
        identifier = PhaseId(ritual_id, PHASE1)
        async_tx_hooks = self._setup_async_hooks(identifier, ritual_id, transcript)
        async_tx = self.coordinator_agent.post_transcript(
            ritual_id=ritual_id,
            transcript=transcript,
            transacting_power=self.transacting_power,
            async_tx_hooks=async_tx_hooks,
        )
        self.dkg_storage.store_ritual_phase_async_tx(
            phase_id=identifier, async_tx=async_tx
        )
        return async_tx

    def publish_aggregated_transcript(
        self,
        ritual_id: int,
        aggregated_transcript: AggregatedTranscript,
        public_key: DkgPublicKey,
    ) -> AsyncTx:
        """Publish an aggregated transcript to publicly available storage."""
        # look up the node index for this node on the blockchain
        participant_public_key = self.threshold_request_power.get_pubkey_from_ritual_id(
            ritual_id
        )
        identifier = PhaseId(ritual_id=ritual_id, phase=PHASE2)
        async_tx_hooks = self._setup_async_hooks(
            identifier, ritual_id, aggregated_transcript, public_key
        )
        async_tx = self.coordinator_agent.post_aggregation(
            ritual_id=ritual_id,
            aggregated_transcript=aggregated_transcript,
            public_key=public_key,
            participant_public_key=participant_public_key,
            transacting_power=self.transacting_power,
            async_tx_hooks=async_tx_hooks,
        )
        self.dkg_storage.store_ritual_phase_async_tx(
            phase_id=identifier, async_tx=async_tx
        )
        return async_tx

    def _is_phase_1_action_required(self, ritual_id: int) -> bool:
        """Check whether node needs to perform a DKG round 1 action."""

        # check ritual status from the blockchain
        status = self.coordinator_agent.get_ritual_status(ritual_id=ritual_id)
        if status != Coordinator.RitualStatus.DKG_AWAITING_TRANSCRIPTS:
            # This is a normal state when replaying/syncing historical
            # blocks that contain StartRitual events of pending or completed rituals.
            self.log.debug(
                f"ritual #{ritual_id} is not waiting for transcripts; status={status}; skipping execution"
            )
            return False

        # check the associated participant state
        participant = self.coordinator_agent.get_participant(
            ritual_id=ritual_id, provider=self.staking_provider_address, transcript=True
        )
        if participant.transcript:
            # This verifies that the node has not already submitted a transcript for this
            # ritual as read from the CoordinatorAgent.  This is a normal state, as
            # the node may have already submitted a transcript for this ritual.
            self.log.info(
                f"Node {self.transacting_power.account} has already posted a transcript for ritual "
                f"{ritual_id}; skipping execution"
            )
            return False

        return True

    def perform_round_1(
        self,
        ritual_id: int,
        authority: ChecksumAddress,
        participants: List[ChecksumAddress],
        timestamp: int,
    ) -> Optional[AsyncTx]:
        """
        Perform phase 1 of the DKG protocol for a given ritual ID on this node.

        This method is idempotent and will not submit a transcript if one has
        already been submitted. It is dispatched by the EventActuator when it
        receives a StartRitual event from the blockchain.  Since the EventActuator
        scans overlapping blocks, it is possible that this method will be called
        multiple times for the same ritual.  This method will check the state of
        the ritual and participant on the blockchain before submitting a transcript.

        If there is a tracked AsyncTx for the given ritual and round
        combination, this method will return the tracked transaction.  If there is
        no tracked transaction, this method will submit a transcript and return the
        resulting FutureTx.

        Returning None indicates that no action was required or taken.

        Errors raised by this method are not explicitly caught and are expected
        to be handled by the EventActuator.
        """

        try:
            self.check_ferveo_public_key_match()
        except FerveoKeyMismatch:
            # crash this node
            self.stop(halt_reactor=True)
            return

        if self.checksum_address not in participants:
            message = (
                f"{self.checksum_address}|{self.wallet_address} "
                f"is not a member of ritual {ritual_id}"
            )
            stack_trace = traceback.format_stack()
            self.log.critical(f"{message}\n{stack_trace}")
            return

        # check phase 1 contract state
        if not self._is_phase_1_action_required(ritual_id=ritual_id):
            self.log.debug(
                "No action required for phase 1 of DKG protocol for some reason or another."
            )
            return

        # check if there is already pending tx for this ritual + round combination
        async_tx = self.dkg_storage.get_ritual_phase_async_tx(
            phase_id=PhaseId(ritual_id, PHASE1)
        )
        if async_tx:
            self.log.info(
                f"Active ritual in progress: {self.transacting_power.account} has submitted tx "
                f"for ritual #{ritual_id}, phase #{PHASE1} (final: {async_tx.final})"
            )
            return async_tx

        #
        # Perform phase 1 of the DKG protocol
        #

        ritual = self.coordinator_agent.get_ritual(
            ritual_id=ritual_id,
            transcripts=False,
        )

        self.log.debug(
            f"performing round 1 of DKG ritual "
            f"#{ritual_id} from blocktime {timestamp} "
            f"with authority {authority}."
        )

        # generate a transcript
        validators = self._resolve_validators(ritual)
        try:
            transcript = self.ritual_power.generate_transcript(
                nodes=validators,
                threshold=ritual.threshold,
                shares=ritual.shares,
                checksum_address=self.checksum_address,
                ritual_id=ritual.id,
            )
        except Exception as e:
            stack_trace = traceback.format_stack()
            self.log.critical(
                f"Failed to generate a transcript for ritual #{ritual.id}: {str(e)}\n{stack_trace}"
            )
            return

        # publish the transcript and store the receipt
        self.dkg_storage.store_validators(ritual_id=ritual.id, validators=validators)
        async_tx = self.publish_transcript(ritual_id=ritual.id, transcript=transcript)

        # logging
        arrival = ritual.total_transcripts + 1
        self.log.debug(
            f"{self.transacting_power.account[:8]} submitted a transcript for "
            f"DKG ritual #{ritual.id} ({arrival}/{ritual.dkg_size}) with authority {authority}."
        )
        return async_tx

    def _is_phase_2_action_required(self, ritual_id: int) -> bool:
        """Check whether node needs to perform a DKG round 2 action."""

        # check ritual status from the blockchain
        status = self.coordinator_agent.get_ritual_status(ritual_id=ritual_id)
        if status != Coordinator.RitualStatus.DKG_AWAITING_AGGREGATIONS:
            # This is a normal state when replaying/syncing historical
            # blocks that contain StartRitual events of pending or completed rituals.
            self.log.debug(
                f"ritual #{ritual_id} is not waiting for aggregations; status={status}."
            )
            return False

        # check the associated participant state
        participant = self.coordinator_agent.get_participant(
            ritual_id=ritual_id,
            provider=self.staking_provider_address,
            transcript=False,
        )
        if participant.aggregated:
            # This is a normal state, as the node may have already submitted an aggregated
            # transcript for this ritual, and it's not necessary to submit another one. Carry on.
            self.log.debug(
                f"Node {self.transacting_power.account} has already posted an "
                f"aggregated transcript for ritual {ritual_id}."
            )
            return False

        return True

    def perform_round_2(self, ritual_id: int, timestamp: int) -> Optional[AsyncTx]:
        """Perform round 2 of the DKG protocol for the given ritual ID on this node."""
        # check phase 2 state
        if not self._is_phase_2_action_required(ritual_id=ritual_id):
            return

        # check if there is a pending tx for this ritual + round combination
        async_tx = self.dkg_storage.get_ritual_phase_async_tx(
            phase_id=PhaseId(ritual_id, PHASE2)
        )
        if async_tx:
            self.log.info(
                f"Active ritual in progress: {self.transacting_power.account} has submitted tx "
                f"for ritual #{ritual_id}, phase #{PHASE2} (final: {async_tx.final})."
            )
            return async_tx

        ritual = self.coordinator_agent.get_ritual(
            ritual_id=ritual_id,
            transcripts=True,
        )

        # prepare the DKG artifacts and aggregate transcripts
        self.log.debug(
            f"{self.transacting_power.account[:8]} performing phase 2 "
            f"of DKG ritual #{ritual.id} from blocktime {timestamp}"
        )
        validators = self._resolve_validators(ritual)

        transcripts = list(Transcript.from_bytes(bytes(t)) for t in ritual.transcripts)
        messages = [ValidatorMessage(v, t) for v, t in zip(validators, transcripts)]
        try:
            aggregated_transcript = self.ritual_power.aggregate_transcripts(
                threshold=ritual.threshold,
                shares=ritual.shares,
                checksum_address=self.checksum_address,
                ritual_id=ritual.id,
                validator_messages=messages,
            )
            dkg_public_key = aggregated_transcript.public_key
            # FIXME: Workaround: remove the public key (last 8 + 48 bytes of the aggregated transcript)
            # to pass size validation check on contract publish. See ferveo#209
            aggregated_transcript = bytes(aggregated_transcript)[: -8 - 48]
        except Exception as e:
            stack_trace = traceback.format_stack()
            self.log.critical(
                f"Failed to aggregate transcripts for ritual #{ritual.id}: {str(e)}\n{stack_trace}"
            )
            return

        # publish the transcript with network-wide jitter to avoid tx congestion
        time.sleep(random.randint(0, self.AGGREGATION_SUBMISSION_MAX_DELAY))
        async_tx = self.publish_aggregated_transcript(
            ritual_id=ritual.id,
            aggregated_transcript=aggregated_transcript,
            public_key=dkg_public_key,
        )

        # logging
        total = ritual.total_aggregations + 1
        self.log.debug(
            f"{self.transacting_power.account[:8]} aggregated a transcript for "
            f"DKG ritual #{ritual.id} ({total}/{ritual.dkg_size})"
        )
        if total >= ritual.dkg_size:
            self.log.debug(f"DKG ritual #{ritual.id} should now be finalized")

        return async_tx

    def _is_handover_applicable_to_node(
        self,
        ritual_id: int,
        departing_validator: ChecksumAddress,
        expected_handover_status: int,
        require_incoming_validator_match: bool = False,
    ) -> bool:
        """
        Determines if the handover phase is applicable to this node for a given ritual.
        Checks ritual status, handover request presence, and handover status.
        If require_incoming_validator_match is True, also checks if this node is the incoming validator.
        """

        # check ritual status
        status = self.coordinator_agent.get_ritual_status(ritual_id=ritual_id)
        if status != Coordinator.RitualStatus.ACTIVE:
            # This is a normal state when replaying/syncing historical
            # blocks that contain StartRitual events of pending or completed rituals.
            self.log.info(
                f"Ritual #{ritual_id} is not active so handover is not possible; dkg status={status}."
            )
            return False

        # check handover request present for the ritual
        handover_request = self.coordinator_agent.get_handover(
            ritual_id=ritual_id, departing_validator=departing_validator
        )
        # empty handover object could be returned - check departing_validator
        if handover_request.departing_validator != departing_validator:
            # handover request not found for departing validator
            if departing_validator == self.checksum_address:
                self.log.debug(
                    f"Handover request for ritual #{ritual_id} is not for this node."
                )
            else:
                self.log.debug(
                    f"No handover request for ritual #{ritual_id} with departing validator {departing_validator}."
                )
            return False

        # Optionally check incoming validator
        if (
            require_incoming_validator_match
            and handover_request.incoming_validator != self.checksum_address
        ):
            self.log.debug(
                f"Handover request for ritual #{ritual_id} is not for this node."
            )
            return False

        # Check handover status
        handover_status = self.coordinator_agent.get_handover_status(
            ritual_id=ritual_id,
            departing_validator=departing_validator,
        )
        if handover_status != expected_handover_status:
            self.log.info(
                f"Handover status ({handover_status}) for ritual #{ritual_id} is not in the "
                f"expected state ({expected_handover_status})."
            )
            return False

        self.log.info(
            f"Handover applicable to node: status={handover_status}, "
            f"ritual=#{ritual_id}, departing_validator={departing_validator}."
        )
        return True

    def _is_handover_transcript_required(
        self,
        ritual_id: int,
        departing_validator: ChecksumAddress,
    ) -> bool:
        """Check whether node needs to act as the incoming validator in a handover."""
        return self._is_handover_applicable_to_node(
            ritual_id=ritual_id,
            departing_validator=departing_validator,
            expected_handover_status=Coordinator.HandoverStatus.HANDOVER_AWAITING_TRANSCRIPT,
            require_incoming_validator_match=True,
        )

    def _produce_handover_transcript(
        self, ritual_id: int, departing_validator: ChecksumAddress
    ) -> HandoverTranscript:
        ritual = self._resolve_ritual(ritual_id)
        validators = self._resolve_validators(ritual)

        # Raises ValueError if departing_validator is not in the providers list
        handover_slot_index = ritual.providers.index(departing_validator)

        self.log.info(
            f"Producing handover transcript for ritual #{ritual_id}, departing validator {departing_validator}, "
            f"and handover slot index {handover_slot_index}."
        )

        # FIXME: Workaround: add serialized public key to aggregated transcript.
        # Since we use serde/bincode in rust, we need a metadata field for the public key, which is the field size,
        # as 8 bytes in little-endian. See ferveo#209
        public_key_metadata = b"0\x00\x00\x00\x00\x00\x00\x00"
        transcript = (
            bytes(ritual.aggregated_transcript)
            + public_key_metadata
            + bytes(ritual.public_key)
        )
        aggregated_transcript = AggregatedTranscript.from_bytes(transcript)

        handover_transcript = self.ritual_power.produce_handover_transcript(
            nodes=validators,
            aggregated_transcript=aggregated_transcript,
            handover_slot_index=handover_slot_index,
            ritual_id=ritual_id,
            shares=ritual.dkg_size,
            threshold=ritual.threshold,
        )
        self.log.info(
            f"Resulting handover transcript (first 10 bytes): {bytes(handover_transcript)[:10].hex()}"
        )
        return handover_transcript

    def _publish_handover_transcript(
        self,
        ritual_id: int,
        departing_validator: ChecksumAddress,
        handover_transcript: HandoverTranscript,
    ) -> AsyncTx:
        """Publish a handover transcript to the Coordinator."""
        participant_public_key = self.threshold_request_power.get_pubkey_from_ritual_id(
            ritual_id
        )
        handover_transcript = bytes(handover_transcript)
        identifier = PhaseId(ritual_id=ritual_id, phase=HANDOVER_AWAITING_TRANSCRIPT)
        async_tx_hooks = self._setup_async_hooks(
            identifier, ritual_id, departing_validator, handover_transcript
        )

        self.log.info(
            f"Publishing handover transcript ({handover_transcript[:10].hex()}) "
            f"for ritual #{ritual_id} and departing validator {departing_validator}"
        )

        async_tx = self.coordinator_agent.post_handover_transcript(
            ritual_id=ritual_id,
            departing_validator=departing_validator,
            handover_transcript=handover_transcript,
            participant_public_key=participant_public_key,
            transacting_power=self.transacting_power,
            async_tx_hooks=async_tx_hooks,
        )
        self.dkg_storage.store_ritual_phase_async_tx(
            phase_id=identifier, async_tx=async_tx
        )
        return async_tx

    def perform_handover_transcript_phase(
        self,
        ritual_id: int,
        departing_participant: ChecksumAddress,
        **kwargs,
    ) -> Optional[AsyncTx]:
        if not self._is_handover_transcript_required(
            ritual_id=ritual_id, departing_validator=departing_participant
        ):
            self.log.info(
                f"No action required for handover transcript for ritual #{ritual_id}"
            )
            return None

        # check if there is a pending tx for this phase
        async_tx = self.dkg_storage.get_ritual_phase_async_tx(
            phase_id=PhaseId(ritual_id, HANDOVER_AWAITING_TRANSCRIPT)
        )
        if async_tx:
            self.log.info(
                f"Active handover in progress: {self.transacting_power.account} has submitted tx "
                f"for ritual #{ritual_id}, handover transcript phase, (final: {async_tx.final})."
            )
            return async_tx

        try:
            handover_transcript = self._produce_handover_transcript(
                ritual_id=ritual_id,
                departing_validator=departing_participant,
            )
        except Exception as e:
            stack_trace = traceback.format_stack()
            message = (
                f"Failed to produce handover transcript for ritual #{ritual_id} and "
                f"departing validator {departing_participant}: {str(e)}\n{stack_trace}"
            )
            self.log.critical(message)
            return None

        async_tx = self._publish_handover_transcript(
            ritual_id=ritual_id,
            departing_validator=departing_participant,
            handover_transcript=handover_transcript,
        )
        self.log.info(
            f"{self.transacting_power.account[:8]} created a handover transcript for "
            f"DKG ritual #{ritual_id} and departing validator {departing_participant}."
        )
        return async_tx

    def _is_handover_blinded_share_required(self, ritual_id: int) -> bool:
        """Check whether node needs to post a blind share for handover"""
        return self._is_handover_applicable_to_node(
            ritual_id=ritual_id,
            departing_validator=self.checksum_address,
            expected_handover_status=Coordinator.HandoverStatus.HANDOVER_AWAITING_BLINDED_SHARE,
            require_incoming_validator_match=False,
        )

    def _produce_blinded_share_for_handover(self, ritual_id: int) -> bytes:
        ritual = self._resolve_ritual(ritual_id)
        # FIXME: Workaround: add serialized public key to aggregated transcript.
        # Since we use serde/bincode in rust, we need a metadata field for the public key, which is the field size,
        # as 8 bytes in little-endian. See ferveo#209
        public_key_metadata = b"0\x00\x00\x00\x00\x00\x00\x00"
        transcript = (
            bytes(ritual.aggregated_transcript)
            + public_key_metadata
            + bytes(ritual.public_key)
        )
        aggregated_transcript = AggregatedTranscript.from_bytes(transcript)
        handover = self.coordinator_agent.get_handover(
            ritual_id=ritual_id,
            departing_validator=self.checksum_address,
        )
        self.log.info(
            f"{self.transacting_power.account[:8]} producing a new blinded share "
            f"for handover at ritual #{ritual_id}."  # and validator index #{handover.share_index}." # TODO: See ferveo#210
        )

        handover_transcript = HandoverTranscript.from_bytes(bytes(handover.transcript))
        try:
            new_aggregate = self.ritual_power.finalize_handover(
                aggregated_transcript=aggregated_transcript,
                handover_transcript=handover_transcript,
            )
        except Exception as e:
            stack_trace = traceback.format_stack()
            self.log.critical(
                f"Failed to produce blinded share for ritual #{ritual_id}: {str(e)}\n{stack_trace}"
            )
            return

        # extract blinded share from aggregate
        # TODO: This is a temporary workaround to extract the blinded share
        # See https://github.com/nucypher/nucypher-contracts/issues/400
        aggregate_bytes = bytes(new_aggregate)

        # TODO: Workaround to find the share index of the current validator. This was supposed to be
        # in the handover request, but the rust implementation does not expose it. See ferveo#210
        for v in self._resolve_validators(ritual):
            if v.address == self.checksum_address:
                share_index = v.share_index
                break
        else:
            raise ValueError(
                f"Validator {self.checksum_address} not found in ritual #{ritual_id} providers."
            )
        start = 32 + 48 * ritual.threshold + 96 * share_index
        length = 96
        blinded_share = aggregate_bytes[start : start + length]
        self.log.info(
            f"Resulting blinded share: {blinded_share.hex()} (share_index: {share_index}, start: {start})"
        )
        return blinded_share

    def _publish_blinded_share_for_handover(
        self,
        ritual_id: int,
        blinded_share: bytes,
    ) -> AsyncTx:
        """Publish a handover blinded share to the Coordinator."""
        blinded_share = bytes(blinded_share)
        identifier = PhaseId(ritual_id=ritual_id, phase=HANDOVER_AWAITING_BLINDED_SHARE)
        async_tx_hooks = self._setup_async_hooks(
            identifier,
            ritual_id,
            blinded_share,
        )

        self.log.info(
            f"Publishing handover blinded share ({blinded_share[:10].hex()}) for ritual #{ritual_id}"
        )

        async_tx = self.coordinator_agent.post_blinded_share_for_handover(
            ritual_id=ritual_id,
            blinded_share=blinded_share,
            transacting_power=self.transacting_power,
            async_tx_hooks=async_tx_hooks,
        )
        self.dkg_storage.store_ritual_phase_async_tx(
            phase_id=identifier, async_tx=async_tx
        )
        return async_tx

    def perform_handover_blinded_share_phase(
        self, ritual_id: int, **kwargs
    ) -> Optional[AsyncTx]:
        if not self._is_handover_blinded_share_required(ritual_id=ritual_id):
            self.log.info(
                f"No action required for handover blinded share for ritual #{ritual_id}"
            )
            return None

        # check if there is a pending tx for this phase
        async_tx = self.dkg_storage.get_ritual_phase_async_tx(
            phase_id=PhaseId(ritual_id, HANDOVER_AWAITING_BLINDED_SHARE)
        )
        if async_tx:
            self.log.info(
                f"Active handover in progress: {self.transacting_power.account} has submitted tx "
                f"for ritual #{ritual_id}, blinded share phase, (final: {async_tx.final})."
            )
            return async_tx

        if not self._is_handover_blinded_share_required(ritual_id=ritual_id):
            self.log.info(
                f"No action required for handover blinded share for ritual #{ritual_id}"
            )
            return None

        try:
            blinded_share = self._produce_blinded_share_for_handover(
                ritual_id=ritual_id,
            )
        except Exception as e:
            stack_trace = traceback.format_stack()
            self.log.critical(
                f"Failed to produce handover blinded share for ritual #{ritual_id}: {e}\n{stack_trace}"
            )
            return None

        async_tx = self._publish_blinded_share_for_handover(
            ritual_id=ritual_id,
            blinded_share=blinded_share,
        )
        self.log.info(
            f"{self.transacting_power.account[:8]} created a handover blinded share for "
            f"DKG ritual #{ritual_id}."
        )
        return async_tx

    def prune_ritual_metadata_due_to_handover(self, ritual_id: int) -> None:
        # clear ritual object and validators since handover modifies ritual
        self.dkg_storage.clear_active_ritual_object(ritual_id)
        self.dkg_storage.clear_validators(ritual_id)

    def produce_decryption_share(
        self,
        ritual_id: int,
        ciphertext_header: CiphertextHeader,
        aad: bytes,
        variant: FerveoVariant,
    ) -> Union[DecryptionShareSimple, DecryptionSharePrecomputed]:
        ritual = self._resolve_ritual(ritual_id)
        validators = self._resolve_validators(ritual)
        # FIXME: Workaround: add serialized public key to aggregated transcript.
        # Since we use serde/bincode in rust, we need a metadata field for the public key, which is the field size,
        # as 8 bytes in little-endian. See ferveo#209
        public_key_metadata = b"0\x00\x00\x00\x00\x00\x00\x00"
        transcript = (
            bytes(ritual.aggregated_transcript)
            + public_key_metadata
            + bytes(ritual.public_key)
        )
        aggregated_transcript = AggregatedTranscript.from_bytes(transcript)
        decryption_share = self.ritual_power.produce_decryption_share(
            nodes=validators,
            threshold=ritual.threshold,
            shares=ritual.shares,
            checksum_address=self.checksum_address,
            ritual_id=ritual.id,
            aggregated_transcript=aggregated_transcript,
            ciphertext_header=ciphertext_header,
            aad=aad,
            variant=variant,
        )
        return decryption_share

    def decrypt_threshold_decryption_request(
        self, encrypted_request: EncryptedThresholdDecryptionRequest
    ) -> ThresholdDecryptionRequest:
        return self.threshold_request_power.decrypt_encrypted_request(
            encrypted_request=encrypted_request
        )

    def encrypt_threshold_decryption_response(
        self,
        decryption_response: ThresholdDecryptionResponse,
        requester_public_key: SessionStaticKey,
    ) -> EncryptedThresholdDecryptionResponse:
        return self.threshold_request_power.encrypt_decryption_response(
            decryption_response=decryption_response,
            requester_public_key=requester_public_key,
        )

    def _verify_active_ritual(self, decryption_request: ThresholdDecryptionRequest):
        # check that ritual is active
        if not self.coordinator_agent.is_ritual_active(
            ritual_id=decryption_request.ritual_id
        ):
            raise self.UnauthorizedRequest(
                f"Ritual #{decryption_request.ritual_id} is not active",
            )

        # enforces that the node is part of the ritual
        participating = self.coordinator_agent.is_participant(
            ritual_id=decryption_request.ritual_id, provider=self.checksum_address
        )
        if not participating:
            raise self.UnauthorizedRequest(
                f"Node not part of ritual {decryption_request.ritual_id}",
            )

    def _verify_encryption_authorization(
        self, decryption_request: ThresholdDecryptionRequest
    ) -> None:
        """Check that the encryption is authorized for this ritual"""
        ciphertext_header = decryption_request.ciphertext_header
        authorization = decryption_request.acp.authorization
        if not self.coordinator_agent.is_encryption_authorized(
            ritual_id=decryption_request.ritual_id,
            evidence=authorization,
            ciphertext_header=bytes(ciphertext_header),
        ):
            raise self.UnauthorizedRequest(
                f"Encrypted data not authorized for ritual {decryption_request.ritual_id}",
            )

    def _evaluate_conditions(
        self, decryption_request: ThresholdDecryptionRequest
    ) -> None:
        # requester-supplied condition eval context
        context = None
        if decryption_request.context:
            # nucypher_core.Context -> str -> dict
            context = json.loads(str(decryption_request.context)) or dict()

        # obtain condition from request
        condition_lingo = json.loads(
            str(decryption_request.acp.conditions)
        )  # nucypher_core.Conditions -> str -> Lingo
        if not condition_lingo:
            # this should never happen for CBD - defeats the purpose
            raise self.UnauthorizedRequest(
                "No conditions present for ciphertext.",
            )

        # evaluate the conditions for this ciphertext; raises if it fails
        evaluate_condition_lingo(
            condition_lingo=condition_lingo,
            context=context,
            providers=self.condition_provider_manager,
        )

    def _verify_decryption_request_authorization(
        self, decryption_request: ThresholdDecryptionRequest
    ) -> None:
        """check that the decryption request is authorized for this ritual"""
        self._verify_active_ritual(decryption_request)
        self._verify_encryption_authorization(decryption_request)
        self._evaluate_conditions(decryption_request)

    def _produce_decryption_share_for_request(
        self,
        decryption_request: ThresholdDecryptionRequest,
    ) -> Union[DecryptionShareSimple, DecryptionSharePrecomputed]:
        """Derive a decryption share for a given request"""
        self._verify_decryption_request_authorization(
            decryption_request=decryption_request
        )
        try:
            decryption_share = self.produce_decryption_share(
                ritual_id=decryption_request.ritual_id,
                ciphertext_header=decryption_request.ciphertext_header,
                aad=decryption_request.acp.aad(),
                variant=decryption_request.variant,
            )
        except Exception as e:
            self.log.warn(f"Failed to derive decryption share: {e}")
            raise self.DecryptionFailure(f"Failed to derive decryption share: {e}")
        return decryption_share

    def _encrypt_decryption_share(
        self,
        ritual_id: int,
        decryption_share: Union[DecryptionShareSimple, DecryptionSharePrecomputed],
        public_key: SessionStaticKey,
    ) -> EncryptedThresholdDecryptionResponse:
        # TODO: #3098 nucypher-core#49 Use DecryptionShare type
        decryption_response = ThresholdDecryptionResponse(
            ritual_id=ritual_id,
            decryption_share=bytes(decryption_share),
        )
        encrypted_response = self.encrypt_threshold_decryption_response(
            decryption_response=decryption_response,
            requester_public_key=public_key,
        )
        return encrypted_response

    def _local_operator_address(self):
        return self.__operator_address

    @property
    def wallet_address(self):
        return self.operator_address

    @property
    def staking_provider_address(self) -> ChecksumAddress:
        if not self.__staking_provider_address:
            self.__staking_provider_address = self.get_staking_provider_address()
        return self.__staking_provider_address

    def get_staking_provider_address(self) -> ChecksumAddress:
        self.__staking_provider_address = (
            self.child_application_agent.staking_provider_from_operator(
                self.operator_address
            )
        )
        self.checksum_address = self.__staking_provider_address
        self.nickname = Nickname.from_seed(self.checksum_address)
        return self.__staking_provider_address

    @property
    def is_confirmed(self) -> bool:
        return self.child_application_agent.is_operator_confirmed(self.operator_address)

    def block_until_ready(self, poll_rate: int = None, timeout: int = None):
        emitter = StdoutEmitter()
        poll_rate = poll_rate or self.READY_POLL_RATE
        timeout = timeout or self.READY_TIMEOUT
        start, funded, bonded = maya.now(), False, False

        taco_child_client = self.child_application_agent.blockchain.client
        taco_child_pretty_chain_name = PUBLIC_CHAINS.get(
            taco_child_client.chain_id, f"chain ID #{taco_child_client.chain_id}"
        )

        taco_root_chain_id = self.application_agent.blockchain.client.chain_id
        taco_root_pretty_chain_name = PUBLIC_CHAINS.get(
            taco_root_chain_id, f"chain ID #{taco_root_chain_id}"
        )
        while not (funded and bonded):
            if timeout and ((maya.now() - start).total_seconds() > timeout):
                message = f"x Operator was not qualified after {timeout} seconds"
                emitter.message(message, color="red")
                raise self.ActorError(message)

            if not funded:
                # check for funds
                matic_balance = taco_child_client.get_balance(self.operator_address)
                if matic_balance:
                    # funds found
                    funded, balance = True, Web3.from_wei(matic_balance, "ether")
                    emitter.message(
                        f"✓ Operator {self.operator_address} is funded with {balance} MATIC",
                        color="green",
                    )
                else:
                    emitter.message(
                        f"! Operator {self.operator_address} is not funded with MATIC",
                        color="yellow",
                    )

            if not bonded:
                # check root
                taco_root_bonded_address = (
                    self.application_agent.get_staking_provider_from_operator(
                        self.operator_address
                    )
                )
                if taco_root_bonded_address == NULL_ADDRESS:
                    emitter.message(
                        f"! Operator {self.operator_address} is not bonded to a staking provider",
                        color="yellow",
                    )
                else:
                    # check child
                    taco_child_bonded_address = self.get_staking_provider_address()
                    if taco_child_bonded_address == taco_root_bonded_address:
                        bonded = True
                        emitter.message(
                            f"✓ Operator {self.operator_address} is bonded to staking provider {self.staking_provider_address}",
                            color="green",
                        )
                    else:
                        child_bonded_address_info = (
                            f"({truncate_checksum_address(taco_child_bonded_address)})"
                            if taco_child_bonded_address != NULL_ADDRESS
                            else ""
                        )
                        emitter.message(
                            f"! Bonded staking provider address {truncate_checksum_address(taco_root_bonded_address)} on {taco_root_pretty_chain_name} not yet synced to child application on {taco_child_pretty_chain_name} {child_bonded_address_info}; waiting for sync",
                            color="yellow",
                        )

            if not (funded and bonded):
                time.sleep(poll_rate)

        coordinator_address = self.coordinator_agent.contract_address
        emitter.message(
            f"! Checking provider's DKG participation public key for {self.staking_provider_address} "
            f"on {taco_child_pretty_chain_name} at Coordinator {coordinator_address}",
            color="yellow",
        )
        receipt = self.set_provider_public_key()  # returns None if key already set
        if receipt:
            txhash = receipt["transactionHash"].hex()
            emitter.message(
                f"✓ Successfully published provider's DKG participation public key"
                f" for {self.staking_provider_address} on {taco_child_pretty_chain_name} with txhash {txhash})",
                color="green",
            )

        else:
            # this node's ferveo public key is already published
            self.check_ferveo_public_key_match()
            emitter.message(
                f"✓ Provider's DKG participation public key already set for "
                f"{self.staking_provider_address} on Coordinator {coordinator_address}",
                color="green",
            )

    def check_ferveo_public_key_match(self) -> None:
        latest_ritual_id = self.coordinator_agent.number_of_rituals()
        local_ferveo_key = self.ritual_power.public_key()
        onchain_ferveo_key = self.coordinator_agent.get_provider_public_key(
            ritual_id=latest_ritual_id, provider=self.staking_provider_address
        )

        if bytes(local_ferveo_key) != bytes(onchain_ferveo_key):
            message = render_ferveo_key_mismatch_warning(
                local_key=local_ferveo_key,
                onchain_key=onchain_ferveo_key,
            )
            self.log.critical(message)
            raise FerveoKeyMismatch(message)


class PolicyAuthor(NucypherTokenActor):
    """Alice base class for blockchain operations, mocking up new policies!"""

    def __init__(self, eth_endpoint: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application_agent = ContractAgency.get_agent(
            TACoApplicationAgent,
            registry=self.registry,
            blockchain_endpoint=eth_endpoint,
        )

    def create_policy(self, *args, **kwargs):
        """Hence the name, a BlockchainPolicyAuthor can create a BlockchainPolicy with themself as the author."""
        from nucypher.policy.policies import Policy

        blockchain_policy = Policy(publisher=self, *args, **kwargs)
        return blockchain_policy
