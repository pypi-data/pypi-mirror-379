#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for the Communication Protocol package comm.modbus_tcp.
"""

import pytest

from hvl_ccb.comm.modbus_tcp import (
    ModbusTcpCommunication,
    ModbusTcpCommunicationConfig,
    ModbusTcpConnectionFailedError,
)


@pytest.fixture(scope="module")
def testconfig():
    return ModbusTcpCommunicationConfig(
        host="127.0.0.1",
        unit=0,
    )


def test_modbus_tcp_conifg() -> None:
    with pytest.raises(ValueError):
        ModbusTcpCommunicationConfig(host="127..1", unit=0)


def test_modbus_tcp_connect(testconfig) -> None:
    mbtcp = ModbusTcpCommunication(testconfig)

    assert mbtcp is not None

    with pytest.raises(ModbusTcpConnectionFailedError):
        mbtcp.open()

    # test write
    with pytest.raises(ModbusTcpConnectionFailedError):
        mbtcp.write_registers(address=1234, values=5678)

    # test read holding registers
    with pytest.raises(ModbusTcpConnectionFailedError):
        mbtcp.read_holding_registers(address=9012, count=2)

    # test read input registers
    with pytest.raises(ModbusTcpConnectionFailedError):
        mbtcp.read_input_registers(address=3456, count=2)

    mbtcp.close()
