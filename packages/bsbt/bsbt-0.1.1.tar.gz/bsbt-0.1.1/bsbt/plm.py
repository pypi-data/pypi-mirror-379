# bsbt/plm.py

from .mock_data import get_mock_response


def predict_antigen(antibody_sequence: str) -> str:
    """
    Predicts antigen sequence for a given antibody sequence.

    Phase 1: Returns mock data from hardcoded dictionary.
    Phase 2: Replace this with PLM/LLM inference (API call, fine-tuned model, etc.)
    """
    return get_mock_response(antibody_sequence)
