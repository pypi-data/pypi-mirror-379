#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
The device class `Technix` and its corresponding configuration class
"""

import logging
from time import sleep
from typing import cast

from hvl_ccb import configdataclass
from hvl_ccb.dev import SingleCommDevice
from hvl_ccb.utils.poller import Poller
from hvl_ccb.utils.typing import Number
from hvl_ccb.utils.validation import validate_bool, validate_number

from .base import (
    TechnixError,
    TechnixFaultError,
    _GetRegisters,
    _SetRegisters,
    _Status,
    _TechnixCommunicationClasses,
)

logger = logging.getLogger(__name__)


@configdataclass
class TechnixConfig:
    #: communication channel between computer and Technix
    communication_channel: _TechnixCommunicationClasses

    #: Maximal Output voltage
    max_voltage: Number

    #: Maximal Output current
    max_current: Number

    #: Polling interval in s to maintain to watchdog of the device
    polling_interval_sec: Number = 4

    #: Time to wait after stopping the device
    post_stop_pause_sec: Number = 1

    #: Time for pulsing a register
    register_pulse_time: Number = 0.1

    #: Read output voltage and current within the polling event
    read_output_while_polling: bool = False


class Technix(SingleCommDevice):
    """
    Device class to control capacitor chargers from Technix
    """

    def __init__(self, com, dev_config) -> None:
        # Call superclass constructor
        super().__init__(com, dev_config)

        # maximum output current of the hardware
        self._max_current_hardware = self.config.max_current
        # maximum output voltage of the hardware
        self._max_voltage_hardware = self.config.max_voltage

        self._set_voltage: Number = 0
        self._set_current: Number = 0

        #: status of Technix
        self._status: _Status | None = None

        #: Status Poller to maintain the watchdog of the device
        self._status_poller: Poller = Poller(
            spoll_handler=self._spoll_handler,
            polling_interval_sec=self.config.polling_interval_sec,
        )

        logger.debug("Technix Power Supply initialised.")

    @staticmethod
    def config_cls():
        return TechnixConfig

    def default_com_cls(self) -> _TechnixCommunicationClasses:  # type: ignore[override]
        return self.config.communication_channel

    @property
    def is_started(self) -> bool:
        """
        Is the device started?
        """
        return self.status is not None

    def start(self) -> None:
        """
        Start the device and set it into the remote controllable mode. The high
        voltage is turn off, and the status poller is started.
        """

        if self.is_started:
            logger.debug("Technix device was already started.")
            return

        super().start()

        with self.com.access_lock:
            logger.debug("Starting Technix...")
            self.remote = True
            self.output = False
            self.inhibit = False
            self._status_poller.start_polling()

        logger.info("Started Technix")

    def stop(self) -> None:
        """
        Stop the device. The status poller is stopped and the high voltage output
        is turn off.
        """
        if not self.is_started:
            logger.debug("Technix device was not started.")
            return

        with self.com.access_lock:
            self._status_poller.stop_polling()
            self.output = False
            self.remote = False
            self._status = None
            sleep(self.config.post_stop_pause_sec)

        super().stop()

        logger.info("Stopped Technix")

    def _set_register(self, register: _SetRegisters, value: bool | int):
        """
        Function to set a value to a register
        """
        command = f"{register},{int(value)}"
        answer = self.com.query(command)
        if answer != command:
            msg = f"Expected '{command}', but answer was '{answer}'"
            logger.error(msg)
            raise TechnixError(msg)

    def _get_register(self, register: _GetRegisters) -> int:
        """
        Function to query a register
        """
        _register: str = str(register)
        answer = self.com.query(_register)
        if answer[: len(_register)] != _register:
            msg = f"Expected '{_register}', but answer was '{answer}'"
            logger.error(msg)
            raise TechnixError(msg)

        return int(answer[len(_register) :])

    def _spoll_handler(self):
        """
        Function to be called from the poller
        """
        with self.com.access_lock:
            """
            This method can be called manually and by the poller. In case of a
            fault the communication is stopped and subsequent calls of this function
            are skipped. Only one unique call of this function is allowed to be
            performed at the same time. cf. issue 161 on gitlab.com/ethz_hvl/hvl_ccb
            """
            try:
                self.query_status()
                logger.info(self.status)
            except TechnixError as e:
                self._status_poller.stop_polling()
                self._status = None
                msg = (
                    "An error occurred during the polling event and the connection "
                    "is closed"
                )
                logger.exception(msg)
                raise TechnixError(msg) from e

    @property
    def status(self) -> _Status | None:
        """
        The status of the device with the different states as sub-fields
        """
        return self._status if self.com.is_open else None

    @property
    def max_current(self) -> Number:
        """
        Maximal output current of the hardware in A
        """
        return self._max_current_hardware

    @property
    def max_voltage(self) -> Number:
        """
        Maximal output voltage of the hardware in V
        """
        return self._max_voltage_hardware

    def query_status(self, *, _retry: bool = False) -> None:
        """
        Query the status of the device.

        :return: This function returns nothing
        """
        with self.com.access_lock:
            """
            This method can be called manually and by the poller. In case of a
            fault the communication is stopped and subsequent calls of this function
            are skipped. Only one unique call of this function is allowed to be
            performed at the same time. cf. issue 161 on gitlab.com/ethz_hvl/hvl_ccb
            """
            try:
                status_byte = self._get_register(_GetRegisters.STATUS)  # type: ignore[arg-type]
                validate_number(
                    "Integer of status byte", status_byte, (0, 255), int, logger
                )
                status_bits = [bool(int(bit)) for bit in f"{status_byte:08b}"]
                status_bits[1] = not status_bits[1]

                if self.config.read_output_while_polling:
                    voltage: Number | None = self._measure_voltage()
                    current: Number | None = self._measure_current()
                else:
                    voltage, current = None, None

                self._status = _Status(*status_bits, voltage, current)  # type: ignore[call-arg]

                if self._status.fault and not self.open_interlock:
                    msg = (
                        "The fault flag was detected with closed interlock. There can"
                        "be a hardware problem with the device."
                    )
                    logger.error(msg)
                    raise TechnixFaultError(msg)  # noqa: TRY301

            except TechnixFaultError as e:
                if not _retry:
                    # When the interlock gets closed, the HV has to be turned off to
                    # remove the fault flag. This is achieved with this retry.
                    logger.info(
                        "Try to clear the fault. If it persists, there is a "
                        "real hardware problem."
                    )
                    self.output = False
                    self.query_status(_retry=True)
                else:
                    self._status = None
                    msg = "An error occurred during querying the status"
                    logger.exception(msg)
                    raise TechnixError(msg) from e

    def _measure_voltage(self) -> Number:
        """
        Internal function to measure the output voltage
        """
        return self._get_register(_GetRegisters.VOLTAGE) / 4095 * self.max_voltage  # type: ignore[arg-type]

    @property
    def voltage(self) -> Number:
        """
        Actual voltage at the output in V
        """
        if not self.is_started:
            return 0
        if self.config.read_output_while_polling:
            _voltage = cast("Number", cast("_Status", self.status).voltage)
            # Make mypy happy, `_voltage` is None when it is not queried during polling
        else:
            _voltage = self._measure_voltage()
        logger.info(f"Present Output Voltage: {_voltage:_.2f} V")
        return _voltage

    @voltage.setter
    def voltage(self, value: Number):
        """
        Set voltage of the high voltage output

        :param value: Voltage as a `Number` in V
        :raises ValueError: if the set voltage is below 0 V or higher than the
            maximal voltage of the device
        """
        validate_number("Set Voltage", value, (0, self.max_voltage), logger=logger)
        _voltage = int(4095 * value / self.max_voltage)
        validate_number(
            "Register value of set voltage", _voltage, (0, 4095), int, logger=logger
        )
        # Double-check the value if it is really within the limits

        self._set_voltage = value
        logger.info(f"Set Output Voltage: {value:_.2f} V")
        self._set_register(_SetRegisters.VOLTAGE, _voltage)  # type: ignore[arg-type]

    @property
    def set_voltage(self) -> Number:
        """Return the set voltage (may differ from actual value) in V"""
        return self._set_voltage

    @set_voltage.setter
    def set_voltage(self, value: Number) -> None:
        """Set the output voltage"""
        self.voltage = value

    def _measure_current(self) -> Number:
        """
        Internal function to measure the output current
        """
        return self._get_register(_GetRegisters.CURRENT) / 4095 * self.max_current  # type: ignore[arg-type]

    @property
    def current(self) -> Number:
        """
        Actual current of the output in A
        """
        if not self.is_started:
            return 0
        if self.config.read_output_while_polling:
            _current = cast("Number", cast("_Status", self.status).current)
            # Make mypy happy, `_current` is None when it is not queried during polling
        else:
            _current = self._measure_current()
        logger.info(f"Present Output Current: {_current:_.3f} A")
        return _current

    @current.setter
    def current(self, value: Number):
        """
        Set current of the output

        :param value: Current as a `Number` in A
        """
        validate_number("Set Current", value, (0, self.max_current), logger=logger)
        _current = int(4095 * value / self.max_current)
        validate_number(
            "Register value of set current", _current, (0, 4095), int, logger=logger
        )
        # Double-check the value if it is really within the limits

        self._set_current = value
        logger.info(f"Set Output Current: {value:_.3f} A")
        self._set_register(_SetRegisters.CURRENT, _current)  # type: ignore[arg-type]

    @property
    def set_current(self) -> Number:
        """Return the set current (may differ from actual value) in A"""
        return self._set_current

    @set_current.setter
    def set_current(self, value: Number) -> None:
        """Set the output current"""
        self.current = value

    @property
    def output(self) -> bool | None:
        """
        State of the high voltage output
        """
        if self.is_started:
            return cast("_Status", self.status).output
        return None

    @output.setter
    def output(self, value: bool):
        """
        Activates the output of the source

        :param value: `True` for activation, `False` for deactivation
        :raises TypeError: if value is not a `bool`
        """
        validate_bool("Enable HV-Output", value, logger)
        register = _SetRegisters.HVON if value else _SetRegisters.HVOFF

        self._set_register(register, True)  # type: ignore[arg-type]
        sleep(self.config.register_pulse_time)
        self._set_register(register, False)  # type: ignore[arg-type]

        logger.info(f"HV-Output is {'' if value else 'de'}activated")

    @property
    def remote(self) -> bool | None:
        """
        Is the device in remote control mode?
        """
        if self.is_started:
            return cast("_Status", self.status).remote
        return None

    @remote.setter
    def remote(self, value: bool):
        """
        (De-)Activate the remote control mode

        :param value: `True` to control the device with this remote control, `False` to
            control it with the hardware front panel
        """
        validate_bool("Remote control", value, logger)

        self._set_register(_SetRegisters.LOCAL, not value)  # type: ignore[arg-type]
        logger.info(f"Remote control is {'' if value else 'de'}activated")

    @property
    def inhibit(self) -> bool | None:
        """
        Is the output of the voltage inhibited?
        The output stage can still be active.
        """
        if self.is_started:
            return cast("_Status", self.status).inhibit
        return None

    @inhibit.setter
    def inhibit(self, value: bool):
        """
        Inhibit the output without deactivating the HV-output section. To generate
        high voltage this value must be `False`(!).

        :param value: `True` to turn off the output for a short time, `False` to re-turn
            it on
        :raises TypeError: if value is not a `bool`
        """
        validate_bool("Inhibit the output", value, logger)

        self._set_register(_SetRegisters.INHIBIT, value)  # type: ignore[arg-type]
        logger.info(f"Inhibit is {'' if value else 'de'}activated")

    @property
    def open_interlock(self) -> bool | None:
        """
        Is the interlock open? (in safe mode)
        """
        if self.is_started:
            return cast("_Status", self.status).open_interlock
        return None

    @property
    def voltage_regulation(self) -> bool | None:
        """
        Status if the output is in voltage regulation mode (or current regulation)
        """
        if self.is_started:
            return cast("_Status", self.status).voltage_regulation
        return None
