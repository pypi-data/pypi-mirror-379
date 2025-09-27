import pytest
from trgenpy.trgen_pin import TrgenPin
from trgenpy.trgen import TrgenPort

def test_trgen_init_ok():
    trgen = TrgenPort(TrgenPin.SA0)
    assert isinstance(trgen, TrgenPort)

def test_trgen_init_default_enabled():
    trgen = TrgenPort(TrgenPin.NS0)
    assert isinstance(trgen, TrgenPort)

def test_trgen_init_invalid_port_type():
    with pytest.raises(TypeError):
        TrgenPort("a", True)

def test_trgen_init_invalid_memory_length():
    with pytest.raises(ValueError):
        TrgenPort(1, 0)
    with pytest.raises(ValueError):
        TrgenPort(1, -1)
    with pytest.raises(ValueError):
        TrgenPort(1, 256)

def test_trgen_init_none_port():
    with pytest.raises(ValueError):
        TrgenPort(None, True)

def test_trgen_init_invalid_memory_length_type():
    with pytest.raises(TypeError):
        TrgenPort(1, "a")
    with pytest.raises(TypeError):
        TrgenPort(1, 2.5)