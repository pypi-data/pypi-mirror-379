import pytest
from trgenpy.crc import compute_crc32

def test_crc32_empty():
    assert compute_crc32(b"") == 0

