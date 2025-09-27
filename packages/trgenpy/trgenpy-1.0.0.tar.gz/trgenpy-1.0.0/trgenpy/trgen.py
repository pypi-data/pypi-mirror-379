class TrgenPort:
    def __init__(self, id, memory_length=5):
        """
        Initialize a Trgen instance.

        Args:
            id (int): The ID of the trigger (0-25).
            memory_length (int): The length of the trigger memory (1-64).
            default is 5, which means 2^5 = 32 instructions.

        Raises:
            TypeError: If id or memory_length is not an integer.
            ValueError: If id or memory_length is out of allowed range.
        Raises:
        """

        if id is None or memory_length is None:
            raise ValueError("Both 'id' and 'memory_length' must be provided.")
        
        if memory_length < 1 or memory_length > 64:
            raise ValueError("'memory_length' must be between 1 and 64.")   
        
        if memory_length != int(memory_length):
            raise TypeError("'memory_length' must be an integer.")

        if not isinstance(id, int) or not isinstance(memory_length, int):
            raise TypeError("'id' and 'memory_length' must be integers.")

        if not (0 <= id <= 25):
            raise ValueError(f"ID {id} out of allowed range (0-25)")
        if not (1 <= memory_length <= 64):
            raise ValueError(f"Memory length {memory_length} out of allowed range (1-64)")

        # Set ID
        self._id = id
        
        # Set type label
        self.type = ""
        if 0 <= id < 7:
            self.type = "NeuroScan"
        elif 8 <= id < 15:
            self.type = "Synamps"
        elif id == 16:
            self.type = "TMSO"
        elif id == 17:
            self.type = "TMSI"
        elif 18 <= id < 26:
            self.type = "GPIO"
        
        # set max trigger memory length (mtml)
        self._memory_length = memory_length
        self.memory = [0] * memory_length

    @property
    def id(self):
        """Get the ID of the trgen."""
        return self._id

    def __repr__(self):
        return f"<Trgen id={self.id} instructions={len(self.memory)}>"

    def set_instruction(self, index, instruction):
        """
        Set an instruction at a specific index in the trigger memory.
        Args:
            index (int): The index in the trigger memory to set the instruction.
            instruction (int): The instruction to set.
        Raises:
            IndexError: If the index is out of bounds.
        """

        if not (0 <= index < self._memory_length):
            raise IndexError(f"Indice {index} fuori limiti (max {self._memory_length - 1})")
        self.memory[index] = instruction