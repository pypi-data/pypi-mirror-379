INST_MSK       = 0x7
INST_UNACTIVE  = 0x0
INST_ACTIVE    = 0x1
INST_WAITPE    = 0x2
INST_WAITNE    = 0x3
INST_REPEAT    = 0x7
INST_END       = 0x4
INST_NOT_ADMISSIBLE = 0x5

def unactive_for_us(x):
    """
    Encodes an 'unactive' instruction for a given number of microseconds.

    Args:
        x (int): Duration in microseconds.

    Returns:
        int: Encoded instruction word.
    """
    return (x << 3) | INST_UNACTIVE

def active_for_us(x):
    """
    Encodes an 'active' instruction for a given number of microseconds.

    Args:
        x (int): Duration in microseconds.

    Returns:
        int: Encoded instruction word.
    """
    return (x << 3) | INST_ACTIVE

def wait_pe(tr):
    """
    Encodes a 'wait for positive edge' instruction on a trigger pin.

    Args:
        tr (int): TrgenPort pin identifier.

    Returns:
        int: Encoded instruction word.
    """
    return (tr << 3) | INST_WAITPE

def wait_ne(tr):
    """
    Encodes a 'wait for negative edge' instruction on a trigger pin.

    Args:
        tr (int): TrgenPort pin identifier.

    Returns:
        int: Encoded instruction word.
    """
    return (tr << 3) | INST_WAITNE

def repeat(addr, times):
    """
    Encodes a 'repeat' instruction to repeat a sequence.

    Args:
        addr (int): Address to repeat from.
        times (int): Number of repetitions.

    Returns:
        int: Encoded instruction word.
    """
    return (times << 8) | (addr << 3) | INST_REPEAT

def end():
    """
    Encodes an 'end' instruction.

    Returns:
        int: Encoded instruction word.
    """
    return INST_END

def not_admissible():
    """
    Encodes a 'not admissible' instruction.

    Returns:
        int: Encoded instruction word.
    """
    return INST_NOT_ADMISSIBLE

def decode_instruction(word):
    """
    Decodes an instruction word into its type and parameters.

    Args:
        word (int): Encoded instruction word.

    Returns:
        tuple: (instruction_type (str), parameters (any))
            - For 'UNACTIVE' and 'ACTIVE': (type, duration)
            - For 'WAIT_PE' and 'WAIT_NE': (type, trigger pin)
            - For 'REPEAT': (type, {'addr': addr, 'times': times})
            - For 'END': (type, None)
            - For unknown: ('UNKNOWN', None)
    """
    opcode = word & INST_MSK
    if opcode == INST_UNACTIVE:
        return ('UNACTIVE', word >> 3)
    elif opcode == INST_ACTIVE:
        return ('ACTIVE', word >> 3)
    elif opcode == INST_WAITPE:
        return ('WAIT_PE', word >> 3)
    elif opcode == INST_WAITNE:
        return ('WAIT_NE', word >> 3)
    elif opcode == INST_REPEAT:
        addr = (word >> 3) & 0x1F
        times = word >> 8
        return ('REPEAT', {'addr': addr, 'times': times})
    elif opcode == INST_END:
        return ('END', None)
    else:
        return ('UNKNOWN', None)
