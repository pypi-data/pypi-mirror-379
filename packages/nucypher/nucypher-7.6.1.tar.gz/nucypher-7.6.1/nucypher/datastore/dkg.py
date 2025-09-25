from collections import defaultdict
from typing import List, Optional

from atxm.tx import AsyncTx
from nucypher_core.ferveo import (
    Validator,
)

from nucypher.blockchain.eth.models import (
    HANDOVER_AWAITING_BLINDED_SHARE,
    HANDOVER_AWAITING_TRANSCRIPT,
    PHASE1,
    PHASE2,
    Coordinator,
)
from nucypher.types import PhaseId


class DKGStorage:
    """A simple in-memory storage for DKG data"""

    # round 1
    _KEY_PHASE_1_TXS = "phase_1_txs"
    _KEY_VALIDATORS = "validators"
    # round 2
    _KEY_PHASE_2_TXS = "phase_2_txs"
    # handover phases
    _KEY_PHASE_AWAITING_TRANSCRIPT_TXS = "handover_transcript_txs"
    _KEY_PHASE_AWAITING_BLINDED_SHARE_TXS = "handover_blinded_share_txs"
    # active rituals
    _KEY_ACTIVE_RITUAL = "active_rituals"

    _KEYS = [
        _KEY_PHASE_1_TXS,
        _KEY_VALIDATORS,
        _KEY_PHASE_2_TXS,
        _KEY_ACTIVE_RITUAL,
        _KEY_PHASE_AWAITING_TRANSCRIPT_TXS,
        _KEY_PHASE_AWAITING_BLINDED_SHARE_TXS,
    ]

    def __init__(self):
        self._data = defaultdict(dict)

    def clear(self, ritual_id):
        for key in self._KEYS:
            try:
                del self._data[key][ritual_id]
            except KeyError:
                continue

    #
    # DKG Phases
    #
    @classmethod
    def __get_phase_key(cls, phase: int):
        if phase == PHASE1:
            return cls._KEY_PHASE_1_TXS
        elif phase == PHASE2:
            return cls._KEY_PHASE_2_TXS
        elif phase == HANDOVER_AWAITING_TRANSCRIPT:
            return cls._KEY_PHASE_AWAITING_TRANSCRIPT_TXS
        elif phase == HANDOVER_AWAITING_BLINDED_SHARE:
            return cls._KEY_PHASE_AWAITING_BLINDED_SHARE_TXS
        else:
            raise ValueError(f"Unknown phase: {phase}")

    def store_ritual_phase_async_tx(self, phase_id: PhaseId, async_tx: AsyncTx):
        key = self.__get_phase_key(phase_id.phase)
        self._data[key][phase_id.ritual_id] = async_tx

    def clear_ritual_phase_async_tx(self, phase_id: PhaseId, async_tx: AsyncTx) -> bool:
        key = self.__get_phase_key(phase_id.phase)
        if self._data[key].get(phase_id.ritual_id) is async_tx:
            try:
                del self._data[key][phase_id.ritual_id]
                return True
            except KeyError:
                pass
        return False

    def get_ritual_phase_async_tx(self, phase_id: PhaseId) -> Optional[AsyncTx]:
        key = self.__get_phase_key(phase_id.phase)
        return self._data[key].get(phase_id.ritual_id)

    # Validators for rituals
    def store_validators(self, ritual_id: int, validators: List[Validator]) -> None:
        self._data[self._KEY_VALIDATORS][ritual_id] = list(validators)

    def get_validators(self, ritual_id: int) -> Optional[List[Validator]]:
        validators = self._data[self._KEY_VALIDATORS].get(ritual_id)
        if not validators:
            return None

        return list(validators)

    def clear_validators(self, ritual_id: int) -> bool:
        try:
            del self._data[self._KEY_VALIDATORS][ritual_id]
            return True
        except KeyError:
            return False

    #
    # Active Rituals
    #
    def store_active_ritual(self, active_ritual: Coordinator.Ritual) -> None:
        if active_ritual.total_aggregations != active_ritual.dkg_size:
            # safeguard against a non-active ritual being cached
            raise ValueError("Only active rituals can be cached")
        self._data[self._KEY_ACTIVE_RITUAL][active_ritual.id] = active_ritual

    def get_active_ritual(self, ritual_id: int) -> Optional[Coordinator.Ritual]:
        return self._data[self._KEY_ACTIVE_RITUAL].get(ritual_id)

    def clear_active_ritual_object(self, ritual_id: int) -> bool:
        try:
            del self._data[self._KEY_ACTIVE_RITUAL][ritual_id]
            return True
        except KeyError:
            return False
