# bsbt/pipeline.py

from .plm import predict_antigen


def findAntigen(antibody_sequence: str) -> str:
    """
    Entry point for antibody→antigen prediction.

    Phase 1: Calls mock PLM (returns hardcoded values).
    Phase 2: Will call real PLM/LLM model.
    """
    if not antibody_sequence.strip():
        raise ValueError("Input must be a non-empty string.")

    return predict_antigen(antibody_sequence)
