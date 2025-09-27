from trgenpy.trgen_pin import TrgenPin

def test_trigger_pin_members():
    # Verifica che i membri esistano
    assert hasattr(TrgenPin, "NS0")
    assert hasattr(TrgenPin, "SA0")
    assert hasattr(TrgenPin, "GPIO0")

def test_trigger_pin_values():
    # Sostituisci con i nomi e valori reali dei tuoi pin
    assert TrgenPin.NS0.value == 0
    assert TrgenPin.SA0.value == 8
    assert TrgenPin.GPIO0.value == 18

def test_trigger_pin_enum_type():
    # Verifica che sia effettivamente una Enum
    from enum import Enum
    assert issubclass(TrgenPin, Enum)