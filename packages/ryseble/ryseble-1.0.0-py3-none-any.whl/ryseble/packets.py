def build_position_packet(pos: int) -> bytes:
    """Build a packet to set the shade position.

    Args:
        pos: Desired position (0–100).

    Returns:
        Bytes representing the command packet.
    """
    if not (0 <= pos <= 100):
        raise ValueError("Position must be between 0 and 100")

    # Example format: [0x01, pos]
    return bytes([0x01, pos])


def build_get_position_packet() -> bytes:
    """Build a packet to request the current shade position.

    Returns:
        Bytes representing the command packet.
    """
    # Example format: [0x02]
    return bytes([0x02])
