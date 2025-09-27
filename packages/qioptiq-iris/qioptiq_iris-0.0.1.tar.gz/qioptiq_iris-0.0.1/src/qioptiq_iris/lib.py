from typing import Optional, Self
import logging
import warnings
from enum import Enum
import serial


logger = logging.getLogger(__name__)


class Command(Enum):
    ENABLE = 2
    SET_POWER = 3
    SERIAL_NUMBER = 4
    FIRMWARE_VERSION = 6
    BASEPLATE_TEMPERATURE = 7
    WAVELENGTH = 8
    SET_ADDRESS = 12
    LASER_STATUS = 14
    DIODE_TEMPERATURE = 15
    INVERT_DIGITAL_MODULATION = 17
    INPUT_MODE_STATUS = 20
    OPERATING_TIME = 26
    SET_POWER_CONTROL_SOURCE = 28
    MANUFACTURE_DATE = 40
    MAX_LASER_CURRENT = 42
    MODEL = 43
    POWER = 44
    PART_NUMBER = 45
    NOMINAL_POWER = 47
    CURRENT = 56
    ADDRESS = 99


class CommandFrame:
    CMD_START = "#"
    CMD_END = "\r\n"
    ID_LEN = 2
    CMD_LEN = 2

    def __init__(self, address: int, command: Command, data: int = 0):
        """Create a new command frame.

        Args:
            address (int): Laser address.
            command (Command): Command.
            data (int, optional): Data. Defaults to 0.

        Raises:
            ValueError: If laser address is invalid.
        """
        if address < 1 or address > 99:
            raise ValueError(f"Unit address must be in [1, 99], found {address}")

        self.address = address
        self.command = command
        self.data = data

    def __repr__(self) -> str:
        """Converts the frame into a command string.

        Follows the format `[#|id|cmd|data|\\r\\n]`
        + `#` (1 byte): Literal `#` indicates the command start.
        + `id` (2 bytes): Laser id.
        + `cmd` (2 bytes): Command id.
        + `data` (0-16 bytes): Data associated with the command.
        + `\\r\\n` (2 bytes): Indicates command end.

        Returns:
            str: _description_
        """
        return f"#{self.address:02}{self.command.value:02}{self.data:04}\r\n"
    
    @classmethod
    def parse_str(cls, input: str) -> Self:
        offset = len(cls.CMD_START)
        expected_len = 11
        if input[0] != cls.CMD_START:
            offset = 0
            expected_len = 10
            # raise ValueError(f"Invalid command frame string. First character should be `#`, found `{input[0]}`")
        if input[-2:] != "\r\n":
            raise ValueError(f"Invalid command frame string. Frame should terminate with `\r\n`, found `{input[-2:]}`")
        if len(input) != expected_len:
            raise ValueError(f"Invalid command frame string. Frame should be 11 bytes, found {len(input)}")
        
        id = int(input[offset:(offset + cls.ID_LEN)])
        cmd = int(input[(offset + cls.ID_LEN):(offset + cls.ID_LEN + cls.CMD_LEN)])
        if not any(cmd == c.value for c in Command):
            raise ValueError(f"Invalid command value `{cmd}`")
            
        data = int(input[(offset + cls.ID_LEN + cls.CMD_LEN):-len(cls.CMD_END)])
        return CommandFrame(id, Command(cmd), data)

class Iris:
    BAUDRATE = 115200
    DATASIZE = 8  # in bits
    PARITY = serial.PARITY_NONE
    CMD_ENDING = b"\r\n"

    def __init__(
        self,
        port: str,
        address: int = 1,
        timeout: Optional[int] = None,
        write_timeout: Optional[int] = None,
    ):
        """Create a new Qioptiq iFLEX iRIS laser controller.

        Args:
            port (str): Port to connect to (e.g. "COM3").
            address (int): Laser's address. Defaults to 1.
            timeout (Optional[int], optional): Read timeout in seconds. Defaults to None.
            write_timeout (Optional[int], optional): Write timeout in seconds. Defaults to None.
        """
        self.__ser = serial.Serial(
            port,
            baudrate=self.BAUDRATE,
            parity=self.PARITY,
            timeout=timeout,
            write_timeout=write_timeout,
        )
        
        if address < 1 or address > 99:
            raise ValueError(f"Unit address must be in [1, 99], found {address}")
        self._address = address

    def __del__(self):
        if self.__ser.is_open:
            self.__ser.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__ser.is_open:
            self.__ser.close()

    def open(self):
        self.__ser.open()

    def close(self):
        self.__ser.close()

    def send(self, command: Command, data: int = 0):
        """Send a command.
        
        Args:
            command (Command): Command to send.
            data (int, optional): Data to send. Defaults to 0.
        """
        frame = CommandFrame(self._address, command, data)
        logger.info(f"sending {frame}")
        n_out = self.__ser.write(str(frame).encode())
        logger.debug(f"sent {n_out} bytes")

    def read(self) -> Optional[CommandFrame]:
        """Read a command response.

        Returns:
            Optional[CommandFrame]: Response. None if no data was read.
        """
        data = self.__ser.read_until(self.CMD_ENDING)
        logger.info(f"recieved {data}")
        if len(data) == 0:
            return None
        else:
            return CommandFrame.parse_str(data.decode())

    def query(self, command: Command, data: int = 0) -> Optional[CommandFrame]:
        """Query the device. Combines `send` and `read`.

        Args:
            command (Command): Command to send.
            data (int, optional): Data to send. Defaults to 0.

        Returns:
            Optional[CommandFrame]: Device response. None if no data was received.
        """
        self.send(command, data)
        return self.read()
        
    def on(self):
        self.query(Command.ENABLE, 1)

    def off(self):
        self.query(Command.ENABLE, 0)

    @property
    def power(self) -> float:
        """Query the laser's power.

        Returns:
            float: Laser's power.
        """
        resp = self.query(Command.POWER)
        return resp.data / 10
        
    @power.setter
    def power(self, power: float):
        """Set the laser's power.

        Args:
            power (float): Power setpoint in mW.
        """
        if power < 0 or power > 999.9:
            raise ValueError(f"Invalid power. Must be in [0, 999.9], found {power}")
        pwr = int(power * 10)
        if pwr != power * 10:
            warnings.warn(f"Power resolution too high. Highest resolution is 10ths, found {power}")
            
        self.query(Command.SET_POWER, pwr)
