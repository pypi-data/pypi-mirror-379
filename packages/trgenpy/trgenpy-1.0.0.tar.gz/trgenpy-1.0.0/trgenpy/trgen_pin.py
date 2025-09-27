from enum import IntEnum

class TrgenPin(IntEnum):
    """
    Enum for the trigger pins.
    """
    NS0 = 0
    NS1 = 1
    NS2 = 2
    NS3 = 3
    NS4 = 4
    NS5 = 5
    NS6 = 6
    NS7 = 7
    SA0 = 8
    SA1 = 9
    SA2 = 10
    SA3 = 11
    SA4 = 12
    SA5 = 13
    SA6 = 14
    SA7 = 15
    TMSO = 16
    TMSI = 17
    GPIO0 = 18
    GPIO1 = 19
    GPIO2 = 20
    GPIO3 = 21
    GPIO4 = 22
    GPIO5 = 23
    GPIO6 = 24
    GPIO7 = 25

class TrgenLevel(IntEnum):
    """
    Enum for the trigger levels.
    A trigger can be set to HIGH or LOW level.
    """
    LOW = 0
    HIGH = 1

class GPIODirection(IntEnum):
    """
    Enum for the GPIO directions.
    GPIO can be configured as input or output.
    """
    IN = 0
    OUT = 1
