from trgenpy.instruction import (
    unactive_for_us, active_for_us, wait_pe, wait_ne,
    repeat, end, not_admissible, decode_instruction
)

def test_unactive_for_us():
    assert unactive_for_us(10) == (10 << 3) | 0

def test_active_for_us():
    assert active_for_us(5) == (5 << 3) | 1

def test_wait_pe():
    assert wait_pe(2) == (2 << 3) | 2

def test_wait_ne():
    assert wait_ne(3) == (3 << 3) | 3

def test_repeat():
    assert repeat(1, 2) == (2 << 8) | (1 << 3) | 7

def test_end():
    assert end() == 4

def test_not_admissible():
    assert not_admissible() == 5

def test_decode_instruction_active():
    word = active_for_us(7)
    assert decode_instruction(word) == ('ACTIVE', 7)