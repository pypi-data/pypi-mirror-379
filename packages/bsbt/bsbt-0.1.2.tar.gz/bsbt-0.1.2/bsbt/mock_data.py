# bsbt/mock_data.py

MOCK_RESPONSES = {
    # HIV gp120 (antigen) – b12 antibody
    "ARDYWGQGTLVTVSS": "NNTNNTNSSSGRM",
    # SARS-CoV-2 Spike RBD – CR3022 antibody
    "ARDRYYGSSYWYFDV": "FPNITNLCPFGEVFNATR",
    # Hen Egg Lysozyme (HEL) – HyHEL-10 antibody
    "ARGGYSSYWYFDV": "NAWVAWR",
    # Influenza Hemagglutinin (HA) – CR9114 antibody
    "ARVYYYGSSHWYFDV": "GLFGAIAGFIENGWEGMIDG",
    # Insulin (antigen) – Insulin Autoantibody (IAA)
    "ARDYGGGYYAMDY": "SHLVEALYLVCGERG"
}


def get_mock_response(key: str) -> str:
    return MOCK_RESPONSES.get(key, "Unknown antibody sequence")
