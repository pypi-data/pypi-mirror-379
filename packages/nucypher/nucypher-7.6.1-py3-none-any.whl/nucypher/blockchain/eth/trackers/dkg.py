import datetime
import os
import time
from typing import Callable, List, Optional, Tuple

import maya
from prometheus_client import REGISTRY, Gauge
from twisted.internet import threads
from web3.datastructures import AttributeDict

from nucypher.blockchain.eth.models import Coordinator
from nucypher.config.constants import NUCYPHER_ENVVAR_MIN_RITUAL_EVENTS_CHUNK_NUM_BLOCKS
from nucypher.policy.conditions.utils import camel_case_to_snake
from nucypher.utilities.cache import TTLCache
from nucypher.utilities.events import EventScanner, JSONifiedState
from nucypher.utilities.logging import Logger
from nucypher.utilities.task import SimpleTask


class EventActuator(EventScanner):
    """Act on events that are found by the scanner."""

    def __init__(
        self,
        hooks: List[Callable],
        clear: bool = True,
        *args,
        **kwargs,
    ):
        self.log = Logger("EventActuator")
        if clear and os.path.exists(JSONifiedState.STATE_FILENAME):
            os.remove(JSONifiedState.STATE_FILENAME)
        self.hooks = hooks
        super().__init__(*args, **kwargs)

    def process_event(
        self, event: AttributeDict, get_block_when: Callable[[int], datetime.datetime]
    ):
        for hook in self.hooks:
            try:
                hook(event, get_block_when)
            except Exception as e:
                self.log.warn("Error during event hook: {}".format(e))
                raise
        super().process_event(event, get_block_when)


class EventScannerTask(SimpleTask):
    """Task that runs the event scanner in a looping call."""

    INTERVAL = 120  # seconds

    def __init__(self, scanner: Callable):
        self.scanner = scanner
        super().__init__()

    def run(self) -> None:
        self.scanner()

    def handle_errors(self, *args, **kwargs) -> None:
        self.log.warn(
            "Error during ritual event scanning: {}".format(args[0].getTraceback())
        )
        if not self._task.running:
            self.log.warn("Restarting event scanner task!")
            self.start(now=False)  # take a breather


class ActiveRitualTracker:

    CHAIN_REORG_SCAN_WINDOW = 20

    MIN_RITUAL_EVENTS_CHUNK_SIZE = int(
        os.environ.get(NUCYPHER_ENVVAR_MIN_RITUAL_EVENTS_CHUNK_NUM_BLOCKS, 60)
    )  # default 60 blocks @ 2s per block on Polygon = 120s of blocks (somewhat related to interval)

    # how often to check/purge for expired cached values - 8hrs?
    _PARTICIPATION_STATES_PURGE_INTERVAL = 60 * 60 * 8

    # what's the buffer for potentially receiving repeated events - 10mins?
    _RITUAL_TIMEOUT_ADDITIONAL_TTL_BUFFER = 60 * 10

    _LAST_SCANNED_BLOCK_METRIC = Gauge(
        "ritual_events_last_scanned_block_number",
        "Last scanned block number for ritual events",
        registry=REGISTRY,
    )

    class ParticipationState:
        def __init__(
            self,
            participating=False,
            already_posted_transcript=False,
            already_posted_aggregate=False,
        ):
            self.participating = participating
            self.already_posted_transcript = already_posted_transcript
            self.already_posted_aggregate = already_posted_aggregate

    def __init__(
        self,
        operator,
        persistent: bool = False,  # TODO: use persistent storage?
    ):
        self.log = Logger("RitualTracker")

        self.operator = operator
        self.coordinator_agent = operator.coordinator_agent

        # Restore/create persistent event scanner state
        self.persistent = persistent
        self.state = JSONifiedState(persistent=persistent)
        self.state.restore()

        # Map events to handlers
        self.actions = {
            self.contract.events.StartRitual: self.operator.perform_round_1,
            self.contract.events.StartAggregationRound: self.operator.perform_round_2,
            self.contract.events.HandoverRequest: self.operator.perform_handover_transcript_phase,
            self.contract.events.HandoverTranscriptPosted: self.operator.perform_handover_blinded_share_phase,
        }

        self.events = [
            self.contract.events.StartRitual,
            self.contract.events.StartAggregationRound,
            self.contract.events.EndRitual,
            self.contract.events.HandoverRequest,
            self.contract.events.HandoverTranscriptPosted,
            self.contract.events.HandoverFinalized,
        ]

        # TODO: Remove the default JSON-RPC retry middleware
        # as it correctly cannot handle eth_getLogs block range throttle down.
        # self.web3.middleware_onion.remove(http_retry_request_middleware)

        self.scanner = EventActuator(
            hooks=[self._handle_ritual_event],
            web3=self.web3,
            state=self.state,
            contract=self.contract,
            events=self.events,
            min_chunk_scan_size=self.MIN_RITUAL_EVENTS_CHUNK_SIZE,
            chain_reorg_rescan_window=self.CHAIN_REORG_SCAN_WINDOW,
        )

        self.task = EventScannerTask(scanner=self.scan)

        cache_ttl = (
            self.coordinator_agent.get_dkg_timeout()
            + self._RITUAL_TIMEOUT_ADDITIONAL_TTL_BUFFER
        )
        self._participation_states = TTLCache(
            ttl=cache_ttl
        )  # { ritual_id -> ParticipationState }
        self._participation_states_next_purge_timestamp = maya.now().add(
            seconds=self._PARTICIPATION_STATES_PURGE_INTERVAL
        )

    @property
    def provider(self):
        return self.web3.provider

    @property
    def web3(self):
        return self.coordinator_agent.blockchain.w3

    @property
    def contract(self):
        return self.coordinator_agent.contract

    # TODO: should sample_window_size be additionally configurable/chain-dependent?
    def _get_first_scan_start_block_number(self, sample_window_size: int = 100) -> int:
        """
        Returns the block number to start scanning for events from.
        """
        w3 = self.web3
        timeout = self.coordinator_agent.get_dkg_timeout()

        latest_block = w3.eth.get_block("latest")
        if latest_block.number == 0:
            return 0

        # get average block time
        sample_block_number = latest_block.number - sample_window_size
        if sample_block_number <= 0:
            return 0
        base_block = w3.eth.get_block(sample_block_number)
        average_block_time = (
            latest_block.timestamp - base_block.timestamp
        ) / sample_window_size

        number_of_blocks_in_the_past = int(timeout / average_block_time)

        expected_start_block = w3.eth.get_block(
            max(0, latest_block.number - number_of_blocks_in_the_past)
        )
        target_timestamp = latest_block.timestamp - timeout

        # Keep looking back until we find the last block before the target timestamp
        while (
            expected_start_block.number > 0
            and expected_start_block.timestamp > target_timestamp
        ):
            expected_start_block = w3.eth.get_block(expected_start_block.number - 1)

        # if non-zero block found - return the block before
        return expected_start_block.number - 1 if expected_start_block.number > 0 else 0

    def start(self) -> None:
        """Start the event scanner task."""
        self.task.start()

    def stop(self) -> None:
        """Stop the event scanner task."""
        self.task.stop()

    def _action_required(self, ritual_event: AttributeDict) -> bool:
        """Check if an action is required for a given ritual event."""

        # Let's handle separately handover events and non-handover events
        handover_events = [
            self.contract.events.HandoverTranscriptPosted,
            self.contract.events.HandoverRequest,
            self.contract.events.HandoverFinalized,
        ]
        event_type = getattr(self.contract.events, ritual_event.event)
        if event_type in handover_events:
            # handover modifies existing ritual metadata; so we need to proactively prune it
            # during handover process and at the end to avoid having any stale metadata
            # in the cache
            self.operator.prune_ritual_metadata_due_to_handover(
                ritual_event.args.ritualId
            )

            if event_type == self.contract.events.HandoverFinalized:
                # pruning metadata is sufficient when Handover is finalized;
                # no further action required
                return False

            is_departing_participant_in_handover = (
                event_type == self.contract.events.HandoverTranscriptPosted
                and ritual_event.args.departingParticipant
                == self.operator.checksum_address
            )
            is_incoming_participant_in_handover = (
                event_type == self.contract.events.HandoverRequest
                and ritual_event.args.incomingParticipant
                == self.operator.checksum_address
            )
            # for handover events we need to act only if the operator is the departing or incoming participant
            return (
                is_departing_participant_in_handover
                or is_incoming_participant_in_handover
            )

        # Non-handover events (for the moment, DKG events)

        # establish participation state first
        participation_state = self._get_participation_state(ritual_event)
        if not participation_state.participating:
            return False

        # does event have an associated action
        event_has_associated_action = event_type in self.actions
        already_posted_transcript = (
            event_type == self.contract.events.StartRitual
            and participation_state.already_posted_transcript
        )
        already_posted_aggregate = (
            event_type == self.contract.events.StartAggregationRound
            and participation_state.already_posted_aggregate
        )
        if any(
            [
                not event_has_associated_action,
                already_posted_transcript,
                already_posted_aggregate,
            ]
        ):
            return False

        return True

    def _get_ritual_participant_info(
        self, ritual_id: int
    ) -> Optional[Coordinator.Participant]:
        """
        Returns node's participant information for the provided
        ritual id; None if node is not participating in the ritual
        """
        is_participant = self.coordinator_agent.is_participant(
            ritual_id=ritual_id, provider=self.operator.checksum_address
        )
        if is_participant:
            participant = self.coordinator_agent.get_participant(
                ritual_id=ritual_id,
                provider=self.operator.checksum_address,
                transcript=True,
            )
            return participant

        return None

    def _purge_expired_participation_states_as_needed(self):
        # let's check whether we should purge participation states before returning
        now = maya.now()
        if now > self._participation_states_next_purge_timestamp:
            self._participation_states.purge_expired()
            self._participation_states_next_purge_timestamp = now.add(
                seconds=self._PARTICIPATION_STATES_PURGE_INTERVAL
            )

    def _get_participation_state_values_from_contract(
        self, ritual_id: int
    ) -> Tuple[bool, bool, bool]:
        """
        Obtains values for ParticipationState from the Coordinator contract.
        """
        participating = False
        already_posted_transcript = False
        already_posted_aggregate = False

        participant_info = self._get_ritual_participant_info(ritual_id=ritual_id)
        if participant_info:
            # actually participating in this ritual; get latest information
            participating = True
            # populate information since we already hit the contract
            already_posted_transcript = bool(participant_info.transcript)
            already_posted_aggregate = participant_info.aggregated

        return participating, already_posted_transcript, already_posted_aggregate

    def _get_participation_state(self, event: AttributeDict) -> ParticipationState:
        """
        Returns the current participation state of the Operator as it pertains to
        the ritual associated with the provided event.
        """
        self._purge_expired_participation_states_as_needed()

        event_type = getattr(self.contract.events, event.event)
        if event_type not in self.events:
            # should never happen since we specify the list of events we
            # want to receive (1st level of filtering)
            raise RuntimeError(f"Unexpected event type: {event_type}")

        args = event.args

        try:
            ritual_id = args.ritualId
        except AttributeError:
            # no ritualId arg
            raise RuntimeError(
                f"Unexpected event type: '{event_type}' has no ritual id as argument"
            )

        participation_state = self._participation_states[ritual_id]
        if not participation_state:
            # not previously tracked; get current state and return
            # need to determine if participating in this ritual or not
            if event_type == self.contract.events.StartRitual:
                participation_state = self.ParticipationState(
                    participating=(self.operator.checksum_address in args.participants)
                )
                self._participation_states[ritual_id] = participation_state
                return participation_state

            # obtain information from contract
            (
                participating,
                posted_transcript,
                posted_aggregate,
            ) = self._get_participation_state_values_from_contract(ritual_id=ritual_id)
            participation_state = self.ParticipationState(
                participating=participating,
                already_posted_transcript=posted_transcript,
                already_posted_aggregate=posted_aggregate,
            )
            self._participation_states[ritual_id] = participation_state
            return participation_state

        # already tracked but not participating
        if not participation_state.participating:
            return participation_state

        #
        # already tracked and participating in ritual - populate other values
        #
        if event_type == self.contract.events.StartAggregationRound:
            participation_state.already_posted_transcript = True
        elif event_type == self.contract.events.EndRitual:
            # while `EndRitual` signals the end of the ritual, and there is no
            # *current* node action for EndRitual, perhaps there will
            # be one in the future. So to be complete, and adhere to
            # the expectations of this function we still update
            # the participation state
            if args.successful:
                # since successful we know these values are true
                participation_state.already_posted_transcript = True
                participation_state.already_posted_aggregate = True
            elif (
                not participation_state.already_posted_transcript
                or not participation_state.already_posted_aggregate
            ):
                # not successful - and unsure of state values
                # obtain information from contract
                (
                    _,  # participating ignored - we know we are participating
                    posted_transcript,
                    posted_aggregate,
                ) = self._get_participation_state_values_from_contract(
                    ritual_id=ritual_id
                )
                participation_state.already_posted_transcript = posted_transcript
                participation_state.already_posted_aggregate = posted_aggregate

        return participation_state

    def __execute_action(
        self,
        ritual_event: AttributeDict,
        timestamp: int,
        defer: bool = False,
    ):
        """Execute a round of a ritual asynchronously."""
        # NOTE: this format splits on *capital letters* and converts to snake case
        #  so "StartConfirmationRound" becomes "start_confirmation_round"
        #  do not use abbreviations in event names (e.g. "DKG" -> "d_k_g")
        formatted_kwargs = {
            camel_case_to_snake(k): v for k, v in ritual_event.args.items()
        }
        event_type = getattr(self.contract.events, ritual_event.event)

        def task():
            self.actions[event_type](timestamp=timestamp, **formatted_kwargs)

        if defer:
            d = threads.deferToThread(task)
            d.addErrback(self.task.handle_errors)
            return d
        else:
            return task()

    def _handle_ritual_event(
        self,
        ritual_event: AttributeDict,
        get_block_when: Callable[[int], datetime.datetime],
    ):
        # is event actionable
        if not self._action_required(ritual_event):
            self.log.debug(
                f"Event '{ritual_event.event}', does not require further action either: not participating in ritual, no corresponding action or previously handled; skipping"
            )
            return

        timestamp = int(get_block_when(ritual_event.blockNumber).timestamp())
        d = self.__execute_action(ritual_event=ritual_event, timestamp=timestamp)
        return d

    def __scan(self, start_block, end_block, account):
        # Run the scan
        self.log.debug(
            f"({account[:8]}) Scanning events in block range {start_block} - {end_block}"
        )
        start = time.time()
        result, total_chunks_scanned = self.scanner.scan(start_block, end_block)
        if self.persistent:
            self.state.save()
        duration = time.time() - start
        self.log.debug(
            f"Scanned total of {len(result)} events, in {duration} seconds, "
            f"total {total_chunks_scanned} chunk scans performed"
        )

    def scan(self):
        """
        Assume we might have scanned the blocks all the way to the last Ethereum block
        that mined a few seconds before the previous scan run ended.
        Because there might have been a minor Ethereum chain reorganisations since the last scan ended,
        we need to discard the last few blocks from the previous scan results.
        """
        last_scanned_block = self.scanner.get_last_scanned_block()
        self._LAST_SCANNED_BLOCK_METRIC.set(last_scanned_block)

        if last_scanned_block == 0:
            # first run so calculate starting block number based on dkg timeout
            suggested_start_block = self._get_first_scan_start_block_number()
        else:
            self.scanner.delete_potentially_forked_block_data(
                last_scanned_block - self.scanner.chain_reorg_rescan_window
            )
            suggested_start_block = self.scanner.get_suggested_scan_start_block()

        end_block = self.scanner.get_suggested_scan_end_block()
        self.__scan(
            suggested_start_block, end_block, self.operator.transacting_power.account
        )
