from .trgen import TrgenPort
from .trgen_pin import TrgenPin, TrgenLevel, GPIODirection
from .instruction import active_for_us, unactive_for_us, repeat, end, not_admissible
import socket
import time

CMD_PACKET_PROGRAM = 0x01
CMD_PACKET_START   = 0x02
CMD_SET_GPIO       = 0x03
CMD_REQ_IMPL       = 0x04
CMD_REQ_STATUS     = 0x05
CMD_SET_LEVEL      = 0x06
CMD_REQ_GPIO       = 0x07
CMD_REQ_LEVEL      = 0x08
CMD_STOP_TRGEN     = 0x09

class LevelConfig:
    """
    Class to configure trigger levels.
    Usage:
        code
        config = LevelConfig().high(TrgenPin.NS0, TrgenPin.SA1).low(TrgenPin.GPIO0).build()
        client.set_level(config)
    """
    def __init__(self):
        self.levels = {}

    def high(self, *pins):
        for p in pins:
            self.levels[p] = TrgenLevel.HIGH
        return self

    def low(self, *pins):
        for p in pins:
            self.levels[p] = TrgenLevel.LOW
        return self

    def build(self):
        return self.encode_levels(self.levels)
    
    def encode_levels(levels: dict[TrgenPin, TrgenLevel]) -> int:
        """
        levels: dizionario {pin: TrgenLevel.HIGH/LOW}
        ritorna: bitmask da passare a client.set_level()
        """
        mask = 0
        for pin, level in levels.items():
            if level == TrgenLevel.HIGH:
                mask |= (1 << pin)
        return mask

class DirectionConfig:
    """
    Class to configure GPIO directions.
    Usage:
        code
        config = DirectionConfig().output(TrgenPin.GPIO0, TrgenPin.GPIO1).input(TrgenPin.GPIO2).build()
        client.set_gpio_direction(config)
    """
    def __init__(self):
        self.levels = {}

    def output(self, *pins):
        self._check_gpio(pins)
        for p in pins:
            self.levels[p] = GPIODirection.OUT
        return self

    def input(self, *pins):
        self._check_gpio(pins)
        for p in pins:
            self.levels[p] = GPIODirection.IN
        return self

    def build(self):
        return self.encode_direction(self.levels)
    
    def encode_direction(levels: dict[TrgenPin, GPIODirection]) -> int:
        """
        levels: dizionario {pin: GPIODirection.IN/OUT}
        ritorna: bitmask da passare a client.set_gpio_directionl()
        """
        mask = 0
        for pin, level in levels.items():
            if level == GPIODirection.OUT:
                mask |= (1 << pin)
        return mask

    @staticmethod
    def _check_gpio(pins):
        valid_gpio = {TrgenPin.GPIO0, TrgenPin.GPIO1, TrgenPin.GPIO2, TrgenPin.GPIO3,
                      TrgenPin.GPIO4, TrgenPin.GPIO5, TrgenPin.GPIO6, TrgenPin.GPIO7}
        for pin in pins:
            if pin not in valid_gpio:
                raise InvalidPinError(f"Pin {pin} is not a GPIO pin. Allowed: GPIO0-GPIO7")

class InvalidPinError(Exception):
    """Raised when a non-GPIO pin is used for GPIO configuration."""
    pass

class InvalidAckError(Exception):
    """Raised when an invalid ACK response is received from the Trgen."""
    def __init__(self, expected, received):
        super().__init__(f"Expected ACK{expected}, got '{received}'")

class AckFormatError(Exception):
    """Raised when the ACK response format is incorrect."""
    def __init__(self, ack_str):
        super().__init__(f"Malformed ACK string: '{ack_str}'")

class TrgenClient:
    """
    Client used to communicate with TrgenPort Devices via TCP/IP sockets.
    """

    def __init__(self, ip='192.168.123.1', port=4242, timeout=2.0):
        """
        Initialize the client for the Trgen.

        Args:
            ip (str): IP address of the device.
            port (int): Communication port.
            timeout (float): Timeout for the connection in seconds.
        """
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self._impl = None
        self._memory_length = 32
    
    def create_trgen(self, trigger_id):
        """
        Create a TrgenPort object for the specified trigger ID.
        Args:
            trigger_id (TrgenPin): ID of the trigger to create.
        """
        #if self._impl is None:
        #    raise RuntimeError("Call connect() before creating triggers")
        return TrgenPort(trigger_id, self._memory_length)

    # Connect to Trgen and get the TrgenPort Implementation
    def connect(self):
        """
        Connect to the Trgen and retrieve its implementation details.

        Raises:
            InvalidAckError: If the ACK response is invalid.
            AckFormatError: If the ACK response is malformed.
            TimeoutError: If the connection times out.
        """
        try:
            self._impl = self.get_implementation()
            self._memory_length = self._impl.memory_length
        except InvalidAckError as e:
            print(f"⚠️ ACK sbagliato: {e}")
        except AckFormatError as e:
            print(f"⚠️ ACK malformato: {e}")
        except TimeoutError as e:
            print(f"⏱️ Timeout: {e}")

    # Get Device Availability
    def is_available(self):
        """
        Verifica se il dispositivo TrgenPort è raggiungibile.

        Returns:
            bool: True se il dispositivo risponde, False altrimenti.
        """
        try:
            with socket.create_connection((self.ip, self.port), timeout=self.timeout) as sock:
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

    def disable_trigger(self, trgenport):
        """
        Disable a specific trgenport by sending a default program that ends immediately.
        """
        packet_id = CMD_PACKET_PROGRAM | (trgenport.id << 24)
        payload = [0] * self._memory_length  # Default program (no-op)
        return self.__send_packet(packet_id, payload)

    # Start all triggers activities
    def start(self):
        """
        Start the execution of triggers on the device.
        """
        # Invia CMD_START (0x02) senza payload
        return self.__send_packet(CMD_PACKET_START)

    # Stop   all triggers activities
    def stop(self):
        """
        Stop the execution of triggers on the device.
        """
        # Invia CMD_STOP (0x09) senza payload
        return self.__send_packet(CMD_STOP_TRGEN)

    # Send program command for single trgenport
    def set_trgen_memory(self, trgenport):
        """
        Send the memory bank of one pre-programmed trigger Pin to the TrgenPort device.

        Args:
            trgenport (TrgenPort): Object to send.
        """
        packet_id = CMD_PACKET_PROGRAM | (trgenport.id << 24)
        return self.__send_packet(packet_id, trgenport.memory)

    # Set the Polarity Level for single TrgenPort
    def set_level(self, level_mask):
        """
        Set the trigger polarity (bitmask: 1 = active high, 0 = active low)
        Example:
            client.set_level(0b00000011)  # NS0 and NS1 HIGH, others LOW
        Args:
            level_mask (int): Bitmask representing the desired levels for each trigger pin.
        Raises:
            ValueError: If level_mask is not in the range 0-0x03FFFFFF  (26 bits).
        Raises:
            ValueError: If level_mask is not in the range 0-0x03FFFFFF (26 bits).

        """
        packet_id = CMD_SET_LEVEL
        payload = [level_mask]
        return self.__send_packet(packet_id, payload)

    def get_level(self):
        """
        Get the trigger active polarity
        """
        ack = self.__send_packet(CMD_REQ_LEVEL)
        return self.__parse_ack_value(ack, expected_id=CMD_REQ_LEVEL)
    
    # Get Trgen status
    def get_status(self):
        """
        Get current State for all triggers
        """
        ack = self.__send_packet(CMD_REQ_STATUS)
        return self.__parse_ack_value(ack, expected_id=CMD_REQ_STATUS)

    
    def set_gpio_direction(self, gpio_mask):
        """
        Set the direction (bitmask da 0 a 7) for GPIO

        example:
        client.set_gpio_direction(0b00001111)  # GPIO0-3 ON, GPIO4-7 OFF
        Args:
            gpio_mask (int): Bitmask representing the desired GPIO directions (1=output, 0=input).
        Raises: 
            ValueError: If gpio_mask is not in the range 0-0xFF (8 bits).   
        Raises:
            ValueError: If gpio_mask is not in the range 0-0xFF (8 bits).
        """

        packet_id = CMD_SET_GPIO
        payload = [gpio_mask]
        return self.__send_packet(packet_id, payload)
    
    def get_gpio_direction(self):
        """
        Get current direction for GPIO
        """
        ack = self.__send_packet(CMD_REQ_GPIO)
        return self.__parse_ack_value(ack, expected_id=CMD_REQ_GPIO)
    
    def get_implementation(self):
        """
        Get current implementation for Trgen
        Returns:
            TrgenImplementation: Implementation details of the connected Trgen.
        Raises:
            InvalidAckError: If the ACK response is invalid.
            AckFormatError: If the ACK response is malformed.
            TimeoutError: If the connection times out.
        """
        ack = self.__send_packet(CMD_REQ_IMPL)  # 
        value = self.__parse_ack_value(ack, expected_id=0x04)

        from .implementation import TrgenImplementation
        impl = TrgenImplementation.from_packed_value(value)
        print(f"[TRGEN] Config: ns={impl.ns_num}, sa={impl.sa_num}, "
            f"tmso={impl.tmso_num}, tmsi={impl.tmsi_num}, "
            f"gpio={impl.gpio_num}, mtml={impl.mtml} → memory_length={impl.memory_length}")
        return impl

    def __send_packet(self, packet_id, payload=None):
        """
        Send a packet to the TrgenPort device.

        Args:
            packet_id (int): The ID of the packet to send.
            payload (list, optional): The payload data to include in the packet.

        Raises:
            ConnectionError: If the connection to the TrgenPort device fails.
            TimeoutError: If the request times out.
        """
        try:
            if payload is None:
                payload_bytes = b''
            else:
                from struct import pack
                payload_bytes = b''.join(pack('<I', w) for w in payload)

            from struct import pack
            from .crc import compute_crc32

            header = pack('<I', packet_id)
            raw = header + payload_bytes
            crc = pack('<I', compute_crc32(raw))
            packet = raw + crc

            with socket.create_connection((self.ip, self.port), timeout=self.timeout) as sock:
                sock.sendall(packet)
                try:
                    response = sock.recv(64)
                    return response.decode(errors='ignore')
                except socket.timeout:
                    raise TimeoutError(f"No ACK received for packet 0x{packet_id:02X}")
        except socket.timeout:
            raise TimeoutError(f"⏱️ Connection timed out towards Trgen [{self.ip}:{self.port}]")
        except OSError as e:
            raise ConnectionError(f"🔌 Connection failed towards Trgen [{self.ip}:{self.port}] – {e.strerror or str(e)}")

    def __parse_ack_value(self, ack_str, expected_id):
        """
        Parse the ACK response from the TrgenPort device.

        Args:
            ack_str (str): The ACK response string.
            expected_id (int): The expected packet ID.

        Raises:
            InvalidAckError: If the ACK response is invalid.
            AckFormatError: If the ACK response is malformed.
        """
        if not ack_str.startswith(f"ACK{expected_id}"):
            raise InvalidAckError(f"Unexpected ACK: '{ack_str}'")
        parts = ack_str.strip().split(".")
        if len(parts) != 2:
            raise AckFormatError(f"ACK format invalid: '{ack_str}'")
        return int(parts[1])

    def __reset_trigger(self, trgenport):
        """
        Reset a specific trigger to a safe state.
        """
        trgenport.set_instruction(0, end())
        for i in range(1, 31):
            trgenport.set_instruction(i,not_admissible())
        self.set_trgen_memory(trgenport)


    def __reset_all_gpio(self):
        """
        Reset all GPIO triggers to a safe state.
        """
        gpioPinoutMap = [
            TrgenPin.GPIO0,
            TrgenPin.GPIO1,
            TrgenPin.GPIO2,
            TrgenPin.GPIO3,
            TrgenPin.GPIO4,
            TrgenPin.GPIO5,
            TrgenPin.GPIO6,
            TrgenPin.GPIO7
        ]
        for id in gpioPinoutMap:
            gpio = self.create_trgen(id)
            gpio.set_instruction(0, end())
            for i in range(1, 31):
                gpio.set_instruction(i,not_admissible())
            self.set_trgen_memory(gpio)

    def __reset_all_sa(self):
        """
        Reset all Synamps triggers to a safe state.
        """
        synampsPinoutMap = [
            TrgenPin.SA0,
            TrgenPin.SA1,
            TrgenPin.SA2,
            TrgenPin.SA3,
            TrgenPin.SA4,
            TrgenPin.SA5,
            TrgenPin.SA6,
            TrgenPin.SA7
        ]
        for id in synampsPinoutMap:
            sa = self.create_trgen(id)
            sa.set_instruction(0, end())
            for i in range(1, 31):
                sa.set_instruction(i,not_admissible())
            self.set_trgen_memory(sa)

    def __reset_all_ns(self):
        """
        Reset all NeuroScan triggers to a safe state.
        """
        neuroscanPinoutMap = [
            TrgenPin.NS0,
            TrgenPin.NS1,
            TrgenPin.NS2,
            TrgenPin.NS3,
            TrgenPin.NS4,
            TrgenPin.NS5,
            TrgenPin.NS6,
            TrgenPin.NS7
        ]
        for id in neuroscanPinoutMap:
            ns = self.create_trgen(id)
            ns.set_instruction(0, end())
            for i in range(1, 31):
                ns.set_instruction(i,not_admissible())
            self.set_trgen_memory(ns)
    
    def __reset_all_tmso(self):
        """
        Reset all TMSO triggers to a safe state.
        """
        tmsoPinoutMap = [
            TrgenPin.TMSO,
        ]
        for id in tmsoPinoutMap:
            tmso = self.create_trgen(id)
            tmso.set_instruction(0, end())
            for i in range(1, 31):
                tmso.set_instruction(i,not_admissible())
            self.set_trgen_memory(tmso)

    # Prende in input un oggetto TrgenPort e lo programma
    # con un impulso di default di durata 20µs
    def program_default_trigger(self, trgenport, us=20):
        """
        Program one trigger (by Id) with a default pulse of 20µs

        Args:
            trigger (TrgenId): id of the trigger to program.
            us (int): duration of the pulse in microseconds (default 20).
        """
        # TODO check if not Only Input (TMSI or GPIO Inputs)
        trgenport.set_instruction(0, active_for_us(us))
        trgenport.set_instruction(1, unactive_for_us(3))
        trgenport.set_instruction(2, end())
        for i in range(3, 31):
            trgenport.set_instruction(i, not_admissible())
        # Invio del trigger
        self.set_trgen_memory(trgenport)

    # decode and send out a marker to all ports
    # You can also choose to send individually to:
    # - NeuroScan 25Pin Serial connector
    # - Synamps 15Pin Serial connector
    # - GPIO 8Pin DIN connector
    #
    # 
    def sendMarker(self, markerNS=0, markerSA=0, markerGPIO=0, LSB=False,stop=False):
        """
        Send a marker to NS, SA and/or GPIO connectors.

        Args:
            markerNS (int, optional): Marker for NeuroScan.
            markerSA (int, optional): Marker for Synamps.
            markerGPIO (int, optional): Marker for GPIO.
            LSB (bool, optional): If True, use the least significant bit first.
            stop (bool, optional): If True, stop the trigger sequence after sending.
        """
        
        if markerNS and markerSA and markerGPIO == None:
            return
        
        neuroscanMap = [
            TrgenPin.NS0,
            TrgenPin.NS1,
            TrgenPin.NS2,
            TrgenPin.NS3,
            TrgenPin.NS4,
            TrgenPin.NS5,
            TrgenPin.NS6,
            TrgenPin.NS7
        ]

        synampsMap = [
            TrgenPin.SA0,
            TrgenPin.SA1,
            TrgenPin.SA2,
            TrgenPin.SA3,
            TrgenPin.SA4,
            TrgenPin.SA5,
            TrgenPin.SA6,
            TrgenPin.SA7
        ]

        gpioMap = [
            TrgenPin.GPIO0,
            TrgenPin.GPIO1,
            TrgenPin.GPIO2,
            TrgenPin.GPIO3,
            TrgenPin.GPIO4,
            TrgenPin.GPIO5,
            TrgenPin.GPIO6,
            TrgenPin.GPIO7,
        ]

        self.__reset_all_ns()
        self.__reset_all_sa()
        self.__reset_all_gpio()
        self.__reset_all_tmso()

        maskNS = list(format(markerNS, 'b').zfill(8))
        maskSA = list(format(markerSA, 'b').zfill(8))
        maskGPIO = list(format(markerGPIO, 'b').zfill(8))

        if LSB == False:
            maskNS = maskNS[::-1]
            maskSA = maskSA[::-1]
            maskGPIO = maskGPIO[::-1]

        for idx, i in enumerate(maskNS):
            if maskNS[idx] == '1':
                if(markerNS != None):
                    nsx = self.create_trgen(neuroscanMap[idx])
                    self.program_default_trigger(nsx)
        
        for idx, i in enumerate(maskGPIO):
            if maskGPIO[idx] == '1':
                if(markerGPIO != None):
                    sax = self.create_trgen(gpioMap[idx])
                    self.program_default_trigger(sax)
                
        for idx, i in enumerate(maskSA):
            if maskSA[idx] == '1':
                if(markerSA != None):
                    sax = self.create_trgen(synampsMap[idx])
                    self.program_default_trigger(sax)

        # Avvio sequenza
        self.start()

        if stop == True:
            # Stop alla sequenza del trigger
            self.stop()

    # Send Trigger signal out of the BNC (TMSO)
    def sendTrigger(self):
        """
        Send a trigger signal out of the BNC (TMSO).
        """

        # create trigger
        tr = self.create_trgen(TrgenPin.TMSO)
        
        # reset all triggers
        self.__reset_all_gpio()
        self.__reset_all_sa()
        self.__reset_all_ns()
        self.__reset_all_tmso()

        self.program_default_trigger(tr)
        
        # start
        self.start()

    def sendCustomTrigger(self,trgenPinList):
        """
        Send a custom trigger signal out of the BNC (TMSO).
        Args:
            triggerList (list of TrgenPin): List of :class:`TrgenPin` to be triggered.
        """
        if not isinstance(trgenPinList, list):
            raise ValueError("triggerList must be a list of TrgenPin")
        if len(trgenPinList) == 0:
            raise ValueError("triggerList cannot be empty")
        for tid in trgenPinList:
            if not isinstance(tid, TrgenPin):
                raise ValueError("triggerList must contain only TrgenPin values")
        if TrgenPin.TMSI in trgenPinList:
            raise ValueError("TMSI is input only and cannot be used in triggerList")
        
        # reset all triggers
        self.__reset_all_gpio()
        self.__reset_all_sa()
        self.__reset_all_ns()
        self.__reset_all_tmso()

        for tid in trgenPinList:
            # create trigger
            tr = self.create_trgen(tid)
            # set default program for each one
            self.program_default_trigger(tr)
        
        # start
        self.start()

