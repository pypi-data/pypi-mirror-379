from typing import List, Union

from nucypher_core.ferveo import (
    AggregatedTranscript,
    CiphertextHeader,
    DecryptionSharePrecomputed,
    DecryptionShareSimple,
    Dkg,
    DkgPublicKey,
    FerveoVariant,
    HandoverTranscript,
    Keypair,
    Transcript,
    Validator,
    ValidatorMessage,
)

from nucypher.utilities.logging import Logger

LOGGER = Logger('ferveo-dkg')


_VARIANTS = {
    FerveoVariant.Simple: AggregatedTranscript.create_decryption_share_simple,
    FerveoVariant.Precomputed: AggregatedTranscript.create_decryption_share_precomputed,
}


def _make_dkg(
    me: Validator,
    ritual_id: int,
    shares: int,
    threshold: int,
    nodes: List[Validator],
) -> Dkg:
    dkg = Dkg(
        tau=ritual_id,
        shares_num=shares,
        security_threshold=threshold,
        validators=nodes,
        me=me
    )
    LOGGER.debug(f"Initialized DKG backend for {threshold}/{shares} nodes: {', '.join(n.address[:6] for n in nodes)}")
    return dkg


def generate_transcript(
    me: Validator,
    ritual_id: int,
    shares: int,
    threshold: int,
    nodes: List[Validator],
) -> Transcript:
    dkg = _make_dkg(
        me=me, ritual_id=ritual_id, shares=shares, threshold=threshold, nodes=nodes
    )
    transcript = dkg.generate_transcript()
    return transcript


def derive_public_key(
    me: Validator, ritual_id: int, shares: int, threshold: int, nodes: List[Validator]
) -> DkgPublicKey:
    dkg = _make_dkg(
        me=me, ritual_id=ritual_id, shares=shares, threshold=threshold, nodes=nodes
    )
    return dkg.public_key


def aggregate_transcripts(
    me: Validator,
    ritual_id: int,
    shares: int,
    threshold: int,
    validator_messages: List[ValidatorMessage],
) -> AggregatedTranscript:
    nodes = [vm.validator for vm in validator_messages]
    dkg = _make_dkg(
        me=me, ritual_id=ritual_id, shares=shares, threshold=threshold, nodes=nodes
    )
    pvss_aggregated = dkg.aggregate_transcripts(validator_messages)
    verify_aggregate(pvss_aggregated, shares, validator_messages)
    LOGGER.debug(
        f"derived final DKG key {bytes(pvss_aggregated.public_key).hex()[:10]}"
    )
    return pvss_aggregated


def verify_aggregate(
    pvss_aggregated: AggregatedTranscript,
    shares: int,
    transcripts: List[ValidatorMessage],
):
    pvss_aggregated.verify(shares, transcripts)


def produce_decryption_share(
    nodes: List[Validator],
    aggregated_transcript: AggregatedTranscript,
    keypair: Keypair,
    ciphertext_header: CiphertextHeader,
    aad: bytes,
    variant: FerveoVariant,
    me: Validator,
    ritual_id: int,
    shares: int,
    threshold: int,
) -> Union[DecryptionShareSimple, DecryptionSharePrecomputed]:
    dkg = _make_dkg(
        me=me, ritual_id=ritual_id, shares=shares, threshold=threshold, nodes=nodes
    )
    if not all((nodes, aggregated_transcript, keypair, ciphertext_header, aad)):
        raise Exception("missing arguments")  # sanity check
    try:
        derive_share = _VARIANTS[variant]
    except KeyError:
        raise ValueError(f"Invalid variant {variant}")

    # TODO: #3636 - Precomputed variant now requires selected validators, which is not passed here
    #  However, we never use it in the codebase, so this is not a problem for now.
    share = derive_share(
        # first arg here is intended to be "self" since the method is unbound
        aggregated_transcript,
        dkg,
        ciphertext_header,
        aad,
        keypair
    )
    return share


def produce_handover_transcript(
    nodes: List[Validator],
    aggregated_transcript: AggregatedTranscript,
    handover_slot_index: int,
    keypair: Keypair,
    ritual_id: int,
    shares: int,
    threshold: int,
) -> HandoverTranscript:
    if not all((nodes, aggregated_transcript, keypair)):
        raise Exception("missing arguments")  # sanity check

    dkg = _make_dkg(
        # TODO: is fixed 0-index fine here? I don't believe it matters
        me=nodes[0],
        ritual_id=ritual_id,
        shares=shares,
        threshold=threshold,
        nodes=nodes,
    )
    handover_transcript = dkg.generate_handover_transcript(
        aggregated_transcript,
        handover_slot_index,
        keypair,
    )
    return handover_transcript


def finalize_handover(
    aggregated_transcript: AggregatedTranscript,
    handover_transcript: HandoverTranscript,
    keypair: Keypair,
) -> HandoverTranscript:
    if not all((aggregated_transcript, handover_transcript, keypair)):
        raise Exception("missing arguments")  # sanity check

    new_aggregate = aggregated_transcript.finalize_handover(
        handover_transcript, keypair
    )
    return new_aggregate
