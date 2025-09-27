# Ethernet CRC32 (polynomial 0xEDB88320)
import zlib

def compute_crc32(data: bytes) -> int:
    """
    Compute the CRC32 checksum of the given data.
    Args:
        data (bytes): Input data to compute the CRC32 checksum for.
    Returns:
        int: The computed CRC32 checksum as an unsigned 32-bit integer.
    """
    return zlib.crc32(data) & 0xFFFFFFFF
