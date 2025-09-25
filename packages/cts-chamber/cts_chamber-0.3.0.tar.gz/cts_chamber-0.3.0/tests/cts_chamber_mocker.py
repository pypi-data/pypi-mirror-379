"""
Mocker for the control of a CTS environmental chamber.

This mocker simulates the behavior of a CTS environmental chamber, allowing you to set and get
temperature and humidity setpoints, control the running state, and manage ramp rates for both
temperature and humidity. It is designed to be used in testing environments where you need to
simulate the chamber's behavior without requiring actual hardware.

The mocker can be accessed via PyVISA by using a resource manager with the mock library:

.. code-block:: python

    from pyvisa import ResourceManager
    from pyvisa_mock.base.register import register_resource
    from cts_chamber import CTSChamber

    from tests.cts_chamber_mocker import CTSChamberMocker

    resource_manager = ResourceManager(visa_library="@mock")

    mock_resource_path = "MOCK0::mock1::INSTR"
    cts_mocker = CTSChamberMocker()
    register_resource(mock_resource_path, cts_mocker)

    cts_chamber = CTSChamber(
        resource_path=mock_resource_path,
        resource_manager=resource_manager,
    )

"""

from typing import Any

from pyvisa_mock.base.base_mocker import BaseMocker, scpi_raw_regex

__author__ = "Leandro Lanzieri"
__copyright__ = "Deutsches Elektronen-Synchrotron, DESY"
__license__ = "LGPL-3.0"


class CTSChamberMocker(BaseMocker):
    """
    A mocker for a CTS environmental chamber.
    """

    _LINE_TERMINATION = None
    """The line termination character for the mocker."""

    def __init__(
        self,
        call_delay: float = 0.0,
    ):
        super().__init__(call_delay=call_delay)
        self.temperature_current: float = 25.0
        "The current temperature in degrees Celsius."

        self.temperature_setpoint: float = 25.0
        "The setpoint temperature in degrees Celsius."

        self.humidity_current: float = 50.0
        "The current humidity in percent."

        self.humidity_setpoint: float = 50.0
        "The setpoint humidity in percent."

        self.running: bool = False
        "Flag indicating if the chamber is running."

        self.paused: bool = False
        "Flag indicating if the chamber is paused."

        self.temperature_ramp_up: float = 0.0
        "The ramp-up rate for temperature in K/min."

        self.temperature_ramp_down: float = 0.0
        "The ramp-down rate for temperature in K/min."

        self.humidity_ramp_up: float = 0.0
        "The ramp-up rate for humidity in K/min."

        self.humidity_ramp_down: float = 0.0
        "The ramp-down rate for humidity in K/min."

        self.timeout_commands: int = 0
        "Number of commands to timeout. Each command will return an empty response."

    def _format_float(self, value: float) -> str:
        """
        Format a float value to a string with 5 characters, 1 decimal place.
        """
        return f"{value:05.1f}"

    @scpi_raw_regex(r"a0 (?P<value>.*)")
    def _set_temperature_setpoint(self, value: str) -> bytearray:
        """
        Set the temperature setpoint of the chamber.
        """
        _value = float(value)
        if _value < -40.0 or _value > 180.0:
            raise ValueError(f"Temperature setpoint {_value} out of range (-40 to 180 °C)")
        self.temperature_setpoint = _value

        response = "a"
        return self._create_frame(response)

    @scpi_raw_regex(r"a1 (?P<value>.*)")
    def _set_humidity_setpoint(self, value: str) -> bytearray:
        """
        Set the humidity setpoint of the chamber.
        """
        _value = float(value)
        if _value < 0.0 or _value > 100.0:
            raise ValueError(f"Humidity setpoint {_value} out of range (0 to 100 %)")
        self.humidity_setpoint = _value

        response = "a"
        return self._create_frame(response)

    @scpi_raw_regex(r"A0")
    def _get_temperature(self) -> bytearray:
        """
        Get the current temperature of the chamber.
        """
        response = "A0 "
        response += self._format_float(self.temperature_current) + " "
        response += self._format_float(self.temperature_setpoint)

        return self._create_frame(response)

    @scpi_raw_regex(r"A1")
    def _get_humidity(self) -> bytearray:
        """
        Get the current humidity of the chamber.
        """
        response = "A1 "
        response += self._format_float(self.humidity_current) + " "
        response += self._format_float(self.humidity_setpoint)

        return self._create_frame(response)

    @scpi_raw_regex(r"s1 (?P<value>.*)")
    def _set_running(self, value: str) -> bytearray:
        """
        Set the running state of the chamber.

        Args:
            value: The value to set the running state to (e.g., "1" for running, "0" for stopped).

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.running = value == "1"
        response = "s1"
        return self._create_frame(response)

    @scpi_raw_regex(r"s3 (?P<value>.*)")
    def _set_paused(self, value: str) -> bytearray:
        """
        Set the paused state of the chamber.

        Args:
            value: The value to set the paused state to (e.g., "1" for paused, "0" for stopped).

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.paused = value == "1"
        response = "s3"
        return self._create_frame(response)

    @scpi_raw_regex(r"u1 (?P<rate>.*)")
    def _set_temp_ramp_up(self, rate: str) -> bytearray:
        """
        Set the temperature ramp-up rate.

        Args:
            rate: The ramp-up rate in K/min.

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.temperature_ramp_up = float(rate)
        response = "u1"
        return self._create_frame(response)

    @scpi_raw_regex(r"d1 (?P<rate>.*)")
    def _set_temp_ramp_down(self, rate: str) -> bytearray:
        """
        Set the temperature ramp-down rate.

        Args:
            rate: The ramp-down rate in K/min.

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.temperature_ramp_down = float(rate)
        response = "d1"
        return self._create_frame(response)

    @scpi_raw_regex(r"u2 (?P<rate>.*)")
    def _set_humidity_ramp_up(self, rate: str) -> bytearray:
        """
        Set the humidity ramp-up rate.

        Args:
            rate: The ramp-up rate in K/min.

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.humidity_ramp_up = float(rate)
        response = "u2"
        return self._create_frame(response)

    @scpi_raw_regex(r"d2 (?P<rate>.*)")
    def _set_humidity_ramp_down(self, rate: str) -> bytearray:
        """
        Set the humidity ramp-down rate.

        Args:
            rate: The ramp-down rate in K/min.

        Returns:
            A bytearray response indicating the success of the operation.
        """
        self.humidity_ramp_down = float(rate)
        response = "d2"
        return self._create_frame(response)

    @scpi_raw_regex(r"R1")
    def _get_temp_ramp_info(self) -> bytearray:
        """
        Get the temperature ramp information.

        Returns:
            A bytearray response containing the temperature ramp information.
        """
        # Ramp is active if ramp rate is set and current != setpoint
        ramp_active = (self.temperature_ramp_up > 0 or self.temperature_ramp_down > 0) \
            and (self.temperature_current != self.temperature_setpoint)
        response = "R1 "
        response += ("1" if ramp_active else "0")  # ramp_active
        response += ("1" if ramp_active else "0")  # ramp_running
        response += f" {self.temperature_ramp_up:07.2f} {self.temperature_ramp_down:07.2f} "
        response += f"{self.temperature_setpoint:07.2f}"
        return self._create_frame(response)

    @scpi_raw_regex(r"R2")
    def _get_humidity_ramp_info(self) -> bytearray:
        """
        Get the humidity ramp information.

        Returns:
            A bytearray response containing the humidity ramp information.
        """
        ramp_active = (self.humidity_ramp_up > 0 or self.humidity_ramp_down > 0) \
            and (self.humidity_current != self.humidity_setpoint)
        response = "R2 "
        response += ("1" if ramp_active else "0")  # ramp_active
        response += ("1" if ramp_active else "0")  # ramp_running
        response += f" {self.humidity_ramp_up:07.2f} {self.humidity_ramp_down:07.2f} "
        response += f"{self.humidity_setpoint:07.2f}"
        return self._create_frame(response)

    def _humidity_active(self) -> bool:
        """
        Check if humidity control is active.

        Returns:
            True if humidity control is active, False otherwise.
        """
        return self.humidity_ramp_up > 0 or self.humidity_ramp_down > 0 or \
               self.humidity_current != self.humidity_setpoint

    @scpi_raw_regex(r"S")
    def _get_state(self) -> bytearray:
        """
        Get the current state of the chamber.

        Returns:
            A bytearray response containing the current state.
        """
        response = "S"
        response += "1" if self.running else "0"
        response += "0" #error
        response += "1" if not self.paused else "0"
        response += "1" if self._humidity_active() else "0"
        response += "0" # dew_gt_7
        response += "0" # dew_lt_7
        response += "0" # deep dehumidity
        response += "0" # reg supply air
        response += "0" # error number

        return self._create_frame(response)

    def _verify_frame_checksum(self, frame: bytearray):
        """
        Verify the checksum of the frame.

        Args:
            frame: The bytearray frame to verify.

        Raises:
            AssertionError: If the checksum does not match.
        """
        checksum = 0
        for byte in frame[:-1]:
            checksum ^= byte

        print(f"Calculated checksum: {checksum}, Frame checksum: {frame[-1]}")
        assert checksum == frame[-1], "Checksum verification failed"

    def _process_frame(self, frame: bytearray) -> str:
        """
        Process the received SCPI bytearray frame.

        Args:
            frame: The bytearray frame to process.

        Returns:
            The processed SCPI command as a string.

        Raises:
            AssertionError: If the frame does not start with the start character or end with the
                line termination character.
            ValueError: If the frame is malformed or does not contain a valid SCPI command.
        """
        assert frame.startswith(b"\x02"), "SCPI command must start with the start character"
        assert frame.endswith(b"\x03"), "SCPI command must end with the line termination character"

        # Remove start and end characters
        frame = frame[1:-1]

        # Unset MSB
        frame = bytearray(byte & 0x7F for byte in frame)

        self._verify_frame_checksum(frame)

        # Remove the checksum byte
        frame = frame[:-1]

        # Remove address
        frame = frame[1:]

        return frame.decode("ascii").strip()

    def _create_frame(self, scpi_string: str) -> bytearray:
        """
        Create a SCPI bytearray frame from a SCPI command string.

        Args:
            scpi_string: The SCPI command string to convert into a frame.

        Returns:
            A bytearray representing the SCPI command frame.

        Raises:
            ValueError: If the SCPI command string is empty.
        """
        if self.timeout_commands > 0:
            self.timeout_commands -= 1
            return bytearray()

        frame = bytearray(scpi_string.encode("ascii"))

        # Add address
        frame.insert(0, 0x01)

        # Add checksum byte
        checksum = 0
        for byte in frame:
            checksum ^= byte

        frame.append(checksum)

        # Set MSB
        frame = bytearray(byte | 0x80 for byte in frame)

        # Add start and end characters
        frame.insert(0, 0x02)
        frame.append(0x03)
        return frame


    def send(self, frame: bytearray) -> Any:
        """
        Parse received SCPI bytearray frame and pass the SCPI string to the base class.

        Args:
            frame: The bytearray frame to process.

        Returns:
            The response from the base class after processing the SCPI command.

        Raises:
            AssertionError: If the frame does not start with the start character or end with the
                line termination character.
            ValueError: If the frame is malformed or does not contain a valid SCPI command.
        """
        scpi_string = self._process_frame(frame)
        return super().send(scpi_string)
