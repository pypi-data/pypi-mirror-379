from trgenpy.implementation import TrgenImplementation

def test_implementation_from_packed_value():
    packed = (
        (1 << 0)  |  # ns_num = 1
        (2 << 5)  |  # sa_num = 2
        (3 << 10) |  # tmso_num = 3
        (4 << 13) |  # tmsi_num = 4
        (5 << 16) |  # gpio_num = 5
        (6 << 26)    # mtml = 6
    )
    impl = TrgenImplementation.from_packed_value(packed)
    assert impl.ns_num == 1
    assert impl.sa_num == 2
    assert impl.tmso_num == 3
    assert impl.tmsi_num == 4
    assert impl.gpio_num == 5
    assert impl.mtml == 6