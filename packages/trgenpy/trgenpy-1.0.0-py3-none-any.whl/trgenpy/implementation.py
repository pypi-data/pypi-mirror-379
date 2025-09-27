class TrgenImplementation:
    """
    Class to represent the Trgen implementation details.
    """
    def __init__(self, ns_num, sa_num, tmso_num, tmsi_num, gpio_num, mtml):
        self.ns_num = ns_num
        self.sa_num = sa_num
        self.tmso_num = tmso_num
        self.tmsi_num = tmsi_num
        self.gpio_num = gpio_num
        self._mtmlmtml = mtml

    @property
    def total_triggers(self):
        """
        Returns the total number of triggers.
        """
        return self.ns_num + self.sa_num + self.tmso_num + self.tmsi_num + self.gpio_num

    @property
    def memory_length(self):
        """
        Returns the memory length required for the triggers.
        """
        return 1 << self.mtml
    
    @property
    def mtml(self):
        """Get the memory length exponent (mtml)."""
        return self._mtmlmtml

    @classmethod
    def from_packed_value(cls, value: int):
        """Create an instance from a packed integer value."""
        return cls(
            ns_num   = (value >> 0)  & 0x1F,
            sa_num   = (value >> 5)  & 0x1F,
            tmso_num = (value >> 10) & 0x7,
            tmsi_num = (value >> 13) & 0x7,
            gpio_num = (value >> 16) & 0x1F,
            mtml     = (value >> 26) & 0x3F,
        )

    def __repr__(self):
        """
        Returns a string representation of the TrgenImplementation instance.
        """
        return "<TrgenImplementation ns={} sa={} tmso={} tmsi={} gpio={} mtml={}>".format(
            self.ns_num, self.sa_num, self.tmso_num, self.tmsi_num, self.gpio_num, self.mtml
        )
