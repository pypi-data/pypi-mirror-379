import time

import pytest
from cts_chamber_mocker import CTSChamberMocker

from cts_chamber import CTSChamber


def test_temperature_setpoint(cts_chamber: CTSChamber):
    SETPOINT = 25.0

    cts_chamber.set_temperature(SETPOINT)

    _, setpoint = cts_chamber.get_temperature()

    assert isinstance(setpoint, float)
    assert setpoint == SETPOINT

@pytest.mark.skipif(
    "config.getvalue('hil')", reason="Not valid for hardware-in-the-loop"
)
def test_temperature(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    SETPOINT = 25.0
    CURRENT = 20.0

    cts_chamber.set_temperature(SETPOINT)
    mock_cts_chamber.temperature_current = CURRENT

    current, setpoint = cts_chamber.get_temperature()

    assert isinstance(current, float)
    assert isinstance(setpoint, float)
    assert current == CURRENT
    assert setpoint == SETPOINT

def test_start_stop(cts_chamber: CTSChamber):
    cts_chamber.start()
    state = cts_chamber.get_state()
    assert state.running

    time.sleep(2)

    cts_chamber.stop()
    state = cts_chamber.get_state()
    assert not state.running

def test_humidity_setpoint(cts_chamber: CTSChamber):
    SETPOINT = 55.0

    cts_chamber.set_humidity(SETPOINT)

    _, setpoint = cts_chamber.get_humidity()

    assert isinstance(setpoint, float)
    assert setpoint == SETPOINT

@pytest.mark.skipif(
    "config.getvalue('hil')", reason="Not valid for hardware-in-the-loop"
)
def test_humidity(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    SETPOINT = 60.0
    CURRENT = 45.0

    cts_chamber.set_humidity(SETPOINT)
    mock_cts_chamber.humidity_current = CURRENT

    current, setpoint = cts_chamber.get_humidity()

    assert isinstance(current, float)
    assert isinstance(setpoint, float)
    assert current == CURRENT
    assert setpoint == SETPOINT

def test_temperature_ramp_up(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    CURRENT = 20.0
    SETPOINT = 40.0
    RAMP_UP = 2.0
    RAMP_DOWN = 1.0

    # Set initial temperature below setpoint
    mock_cts_chamber.temperature_current = CURRENT

    cts_chamber.set_temperature(SETPOINT)
    cts_chamber.ramp_to_temperature(SETPOINT, ramp_up_rate=RAMP_UP, ramp_down_rate=RAMP_DOWN)

    ramp_info = cts_chamber.get_temperature_ramp_information()

    assert ramp_info.ramp_active
    assert ramp_info.ramp_running
    assert ramp_info.ramp_rate_up == RAMP_UP
    assert ramp_info.ramp_rate_down == RAMP_DOWN
    assert ramp_info.ramp_target == SETPOINT

def test_temperature_ramp_down(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    CURRENT = 30.0
    SETPOINT = 10.0
    RAMP_UP = 2.0
    RAMP_DOWN = 1.5

    # Set initial temperature above setpoint
    mock_cts_chamber.temperature_current = CURRENT

    cts_chamber.set_temperature(SETPOINT)
    cts_chamber.ramp_to_temperature(SETPOINT, ramp_up_rate=RAMP_UP, ramp_down_rate=RAMP_DOWN)

    ramp_info = cts_chamber.get_temperature_ramp_information()

    assert ramp_info.ramp_active
    assert ramp_info.ramp_running
    assert ramp_info.ramp_rate_up == RAMP_UP
    assert ramp_info.ramp_rate_down == RAMP_DOWN
    assert ramp_info.ramp_target == SETPOINT

def test_humidity_ramp_up(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    CURRENT = 40.0
    SETPOINT = 60.0
    RAMP_UP = 3.0
    RAMP_DOWN = 1.0

    # Set initial humidity below setpoint
    mock_cts_chamber.humidity_current = CURRENT

    cts_chamber.set_humidity(SETPOINT)
    cts_chamber.ramp_to_humidity(SETPOINT, ramp_up_rate=RAMP_UP, ramp_down_rate=RAMP_DOWN)

    ramp_info = cts_chamber.get_humidity_ramp_information()

    assert ramp_info.ramp_active
    assert ramp_info.ramp_running
    assert ramp_info.ramp_rate_up == RAMP_UP
    assert ramp_info.ramp_rate_down == RAMP_DOWN
    assert ramp_info.ramp_target == SETPOINT

def test_humidity_ramp_down(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    CURRENT = 70.0
    SETPOINT = 50.0
    RAMP_UP = 2.0
    RAMP_DOWN = 1.5

    # Set initial humidity above setpoint
    mock_cts_chamber.humidity_current = CURRENT

    cts_chamber.set_humidity(SETPOINT)
    cts_chamber.ramp_to_humidity(SETPOINT, ramp_up_rate=RAMP_UP, ramp_down_rate=RAMP_DOWN)

    ramp_info = cts_chamber.get_humidity_ramp_information()

    assert ramp_info.ramp_active
    assert ramp_info.ramp_running
    assert ramp_info.ramp_rate_up == RAMP_UP
    assert ramp_info.ramp_rate_down == RAMP_DOWN
    assert ramp_info.ramp_target == SETPOINT

def test_retry_failed_command(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    SETPOINT = 25.0

    # Configure the mocker to timeout the next 2 commands (default retries is 3)
    mock_cts_chamber.timeout_commands = 2

    cts_chamber.set_temperature(SETPOINT)

    _, setpoint = cts_chamber.get_temperature()

    assert isinstance(setpoint, float)
    assert setpoint == SETPOINT

def test_command_failure(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    SETPOINT = 25.0

    # Configure the mocker to timeout the next 4 commands (default retries is 3)
    mock_cts_chamber.timeout_commands = 4

    with pytest.raises(Exception):
        cts_chamber.set_temperature(SETPOINT)
        cts_chamber.get_temperature()
        # Should raise an exception due to command failure after retries

def test_no_retries(cts_chamber: CTSChamber, mock_cts_chamber: CTSChamberMocker):
    SETPOINT = 25.0

    # Configure the mocker to timeout the next command
    mock_cts_chamber.timeout_commands = 1

    # Set retries to 0
    cts_chamber._communication_retries = 0

    with pytest.raises(Exception):
        cts_chamber.set_temperature(SETPOINT)
        cts_chamber.get_temperature()
        # Should raise an exception due to no retries allowed
