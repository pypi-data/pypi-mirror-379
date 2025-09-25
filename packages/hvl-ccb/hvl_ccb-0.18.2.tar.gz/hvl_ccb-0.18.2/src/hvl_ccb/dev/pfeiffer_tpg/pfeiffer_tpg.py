#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Device class for Pfeiffer TPG controllers.

The Pfeiffer TPG control units are used to control Pfeiffer Compact Gauges.
Models: TPG 251 A, TPG 252 A, TPG 256A, TPG 261, TPG 262, TPG 361, TPG 362 and TPG 366.

Manufacturer homepage:
https://www.pfeiffer-vacuum.com/en/products/measurement-analysis/
measurement/activeline/controllers/
"""

import logging
from enum import Enum, IntEnum
from typing import cast

from hvl_ccb.comm.serial import (
    SerialCommunication,
    SerialCommunicationBytesize,
    SerialCommunicationConfig,
    SerialCommunicationParity,
    SerialCommunicationStopbits,
)
from hvl_ccb.configuration import configdataclass
from hvl_ccb.dev.base import DeviceError, SingleCommDevice
from hvl_ccb.utils.enum import NameEnum
from hvl_ccb.utils.typing import Number

logger = logging.getLogger(__name__)


class PfeifferTPGError(DeviceError):
    """
    Error with the Pfeiffer TPG Controller.
    """


@configdataclass
class PfeifferTPGSerialCommunicationConfig(SerialCommunicationConfig):
    #: Baudrate for Pfeiffer TPG controllers is 9600 baud
    baudrate: int = 9600

    #: Pfeiffer TPG controllers do not use parity
    parity: str | SerialCommunicationParity = SerialCommunicationParity.NONE

    #: Pfeiffer TPG controllers use one stop bit
    stopbits: int | SerialCommunicationStopbits = SerialCommunicationStopbits.ONE

    #: One byte is eight bits long
    bytesize: int | SerialCommunicationBytesize = SerialCommunicationBytesize.EIGHTBITS

    #: The terminator is <CR><LF>
    terminator: bytes = b"\r\n"

    #: use 3 seconds timeout as default
    timeout: Number = 3


class PfeifferTPGSerialCommunication(SerialCommunication):
    """
    Specific communication protocol implementation for Pfeiffer TPG controllers.
    Already predefines device-specific protocol parameters in config.
    """

    def __init__(self, configuration) -> None:
        super().__init__(configuration)

    @staticmethod
    def config_cls():
        return PfeifferTPGSerialCommunicationConfig

    def send_command(self, cmd: str) -> None:
        """
        Send a command to the device and check for acknowledgement.

        :param cmd: command to send to the device
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if the answer from the device differs from the
            expected acknowledgement character 'chr(6)'.
        """

        with self.access_lock:
            # send the command
            self.write_text(cmd)
            # check for acknowledgment char (ASCII 6)
            answer = self.read_text()
            if len(answer) == 0 or ord(answer[0]) != 6:
                message = f"Pfeiffer TPG not acknowledging command {cmd}"
                logger.error(message)
                if len(answer) > 0:
                    logger.debug(f"Pfeiffer TPG: {answer}")
                raise PfeifferTPGError(message)

    def query(self, cmd: str) -> str:
        """
        Send a query, then read and returns the first line from the com port.

        :param cmd: query message to send to the device
        :return: first line read on the com
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if the device does not acknowledge the command or if
            the answer from the device is empty
        """

        with self.access_lock:
            # send the command
            self.write_text(cmd)
            # check for acknowledgment char (ASCII 6)
            answer = self.read_text()
            if len(answer) == 0 or ord(answer[0]) != 6:
                message = f"Pfeiffer TPG not acknowledging command {cmd}"
                logger.error(message)
                if len(answer) > 0:
                    logger.debug(f"Pfeiffer TPG: {answer}")
                raise PfeifferTPGError(message)
            # send enquiry
            self.write_text(chr(5))
            # read answer
            answer = self.read_text().strip()
            if len(answer) == 0:
                message = f"Pfeiffer TPG not answering to command {cmd}"
                logger.error(message)
                raise PfeifferTPGError(message)
            return answer


@configdataclass
class PfeifferTPGConfig:
    """
    Device configuration dataclass for Pfeiffer TPG controllers.
    """

    class Model(NameEnum, init="full_scale_ranges"):  # type: ignore[call-arg]
        TPG25xA = {  # noqa: RUF012
            1: 0,
            10: 1,
            100: 2,
            1000: 3,
            2000: 4,
            5000: 5,
            10000: 6,
            50000: 7,
            0.1: 8,
        }
        TPGx6x = {  # noqa: RUF012
            0.01: 0,
            0.1: 1,
            1: 2,
            10: 3,
            100: 4,
            1000: 5,
            2000: 6,
            5000: 7,
            10000: 8,
            50000: 9,
        }

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.full_scale_ranges_reversed: dict[int, int] = {
                v: k for k, v in self.full_scale_ranges.items()
            }

        def is_valid_scale_range_reversed_str(self, v: str) -> bool:
            """
            Check if given string represents a valid reversed scale range of a model.

            :param v: Reversed scale range string.
            :return: `True` if valid, `False` otherwise.
            """
            # Explicit check because otherwise we get `True` for instance for `float`
            if not isinstance(v, str):
                msg = f"Expected `str`, got `{type(v)}` instead."
                raise TypeError(msg)
            try:
                return int(v) in self.full_scale_ranges_reversed
            except ValueError as e:
                logger.exception("Given string is not a valid scale range", exc_info=e)
                return False

    # model of the TPG (determines which lookup table to use for the
    # full scale range)
    model: str | Model = Model.TPG25xA  # type: ignore[assignment]

    def clean_values(self) -> None:
        if not isinstance(self.model, self.Model):
            self.force_value("model", self.Model(self.model))  # type: ignore[attr-defined]


class PfeifferTPG(SingleCommDevice):
    """
    Pfeiffer TPG control unit device class
    """

    SensorTypes = Enum(
        value="SensorTypes",
        names=[
            ("TPR/PCR Pirani Gauge", 1),
            ("TPR", 1),
            ("TPR/PCR", 1),
            ("IKR Cold Cathode Gauge", 2),
            ("IKR", 2),
            ("IKR9", 2),
            ("IKR11", 2),
            ("PKR Full range CC", 3),
            ("PKR", 3),
            ("APR/CMR Linear Gauge", 4),
            ("CMR", 4),
            ("APR/CMR", 4),
            ("CMR/APR", 4),
            ("Pirani / High Pressure Gauge", 5),
            ("IMR", 5),
            ("Fullrange BA Gauge", 6),
            ("PBR", 6),
            ("None", 7),
            ("no Sensor", 7),
            ("noSen", 7),
            ("noSENSOR", 7),
        ],
    )

    class SensorStatus(IntEnum):
        Ok = 0
        Underrange = 1
        Overrange = 2
        Sensor_error = 3
        Sensor_off = 4
        No_sensor = 5
        Identification_error = 6

    def __init__(self, com, dev_config=None) -> None:
        # Call superclass constructor
        super().__init__(com, dev_config)

        # list of sensors connected to the TPG
        self.sensors: list[str] = []

    def __repr__(self) -> str:
        return f"Pfeiffer TPG with {self.number_of_sensors} sensors: {self.sensors}"

    @property
    def number_of_sensors(self) -> int:
        return len(self.sensors)

    @property
    def unit(self) -> str:
        """
        The pressure unit of readings is always mbar, regardless of the display unit.
        """
        return "mbar"

    @staticmethod
    def default_com_cls():
        return PfeifferTPGSerialCommunication

    @staticmethod
    def config_cls():
        return PfeifferTPGConfig

    def start(self) -> None:
        """
        Start this device. Opens the communication protocol,
        and identify the sensors.

        :raises SerialCommunicationIOError: when communication port cannot be opened
        """

        logger.info("Starting Pfeiffer TPG")
        super().start()

        # identify the sensors connected to the TPG
        # and also find out the number of channels
        self.identify_sensors()

    def stop(self) -> None:
        """
        Stop the device. Closes also the communication protocol.
        """

        logger.info(f"Stopping device {self}")
        super().stop()

    def identify_sensors(self) -> None:
        """
        Send identification request TID to sensors on all channels.

        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """

        try:
            answer = self.com.query("TID")
        except PfeifferTPGError:
            logger.exception("Pressure sensor identification failed.")
            raise

        # try matching the sensors:
        sensors = []
        for s in answer.split(","):
            try:
                sensors.append(self.SensorTypes[s].name)
            except KeyError:  # noqa: PERF203 Continue loop after exception
                logger.exception("Unknown sensor")
                sensors.append("Unknown")
        self.sensors = sensors
        # identification successful:
        logger.info(f"Identified {self}")

    def measure(self, channel: int) -> tuple[str, float]:
        """
        Get the status and measurement of one sensor

        :param channel: int channel on which the sensor is connected, with
            1 <= channel <= number_of_sensors
        :return: measured value as float if measurement successful,
            sensor status as string if not
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """

        if not 1 <= channel <= self.number_of_sensors:
            message = (
                f"{channel} is not a valid channel number, it should be between "
                f"1 and {self.number_of_sensors}"
            )
            logger.error(message)
            raise ValueError(message)

        try:
            answer = self.com.query(f"PR{channel}")
        except PfeifferTPGError as e:
            logger.exception(f"Reading sensor {channel} failed.", exc_info=e)
            raise

        status, measurement = answer.split(",")
        s = self.SensorStatus(int(status))
        if s == self.SensorStatus.Ok:
            logger.info(
                f"Channel {channel} successful reading of pressure: {measurement} mbar."
            )
        else:
            logger.info(
                f"Channel {channel} no reading of pressure, sensor status is "
                f"{self.SensorStatus(s).name}."
            )
        return s.name, float(measurement)

    def measure_all(self) -> list[tuple[str, float]]:
        """
        Get the status and measurement of all sensors (this command is
        not available on all models)

        :return: list of measured values as float if measurements successful,
            and or sensor status as strings if not
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """

        try:
            answer = self.com.query("PRX")
        except PfeifferTPGError as e:
            logger.exception(
                "Getting pressure reading from all sensors failed "
                "(this command is not available on all TGP models).",
                exc_info=e,
            )
            raise

        ans = answer.split(",")
        ret = [
            (self.SensorStatus(int(ans[2 * i])).name, float(ans[2 * i + 1]))
            for i in range(self.number_of_sensors)
        ]
        logger.info(f"Reading all sensors with result: {ret}.")
        return ret

    def _set_full_scale(self, fsr: list[Number], unitless: bool) -> None:
        """
        Set the full scale range of the attached sensors. See lookup table between
        command and corresponding pressure in the device user manual.

        :param fsr: list of full scale range values, like `[0, 1, 3, 3, 2, 0]` for
            `unitless = True` scale or `[0.01, 1000]` otherwise (mbar units scale)
        :param unitless: flag to indicate scale of range values; if `False` then mbar
            units scale
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """
        if len(fsr) != self.number_of_sensors:
            msg = (
                f"Argument fsr should be of length {self.number_of_sensors}. "
                f"Received length {len(fsr)}."
            )
            raise ValueError(msg)

        possible_values_map = (
            self.config.model.full_scale_ranges_reversed
            if unitless
            else self.config.model.full_scale_ranges
        )
        wrong_values = [v for v in fsr if v not in possible_values_map]
        if wrong_values:
            msg = (
                f"Argument fsr contains invalid values: {wrong_values}. Accepted "
                f"values are {list(possible_values_map.items())}"
                f"{'' if unitless else ' mbar'}."
            )
            raise ValueError(msg)

        str_fsr = ",".join(
            [str(f if unitless else possible_values_map[f]) for f in fsr]
        )
        try:
            self.com.send_command(f"FSR,{str_fsr}")
            logger.info(f"Set sensors full scale to {fsr} (unitless) respectively.")
        except PfeifferTPGError as e:
            logger.exception("Setting sensors full scale failed.", exc_info=e)
            raise

    def _get_full_scale(self, unitless: bool) -> list[Number]:
        """
        Get the full scale range of the attached sensors. See lookup table between
        command and corresponding pressure in the device user manual.

        :param unitless: flag to indicate scale of range values; if `False` then mbar
            units scale
        :return: list of full scale range values, like `[0, 1, 3, 3, 2, 0]` for
            `unitless = True` scale or `[0.01, 1000]` otherwise (mbar units scale)
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """

        try:
            answer = self.com.query("FSR")
        except PfeifferTPGError as e:
            logger.exception(
                "Query full scale range of all sensors failed.", exc_info=e
            )
            raise

        answer_values = answer.split(",")
        wrong_values = [
            v
            for v in answer_values
            if not self.config.model.is_valid_scale_range_reversed_str(v)
        ]
        if wrong_values:
            msg = (
                "The controller returned the full unitless scale range values: "
                f"{answer}. The values {wrong_values} are invalid. Accepted values are "
                f"{list(self.config.model.full_scale_ranges_reversed.keys())}."
            )
            raise PfeifferTPGError(msg)

        fsr = [
            int(v) if unitless else self.config.model.full_scale_ranges_reversed[int(v)]
            for v in answer_values
        ]
        logger.info(
            f"Obtained full scale range of all sensors as {fsr}"
            f"{'' if unitless else ' mbar'}."
        )
        return fsr

    def set_full_scale_unitless(self, fsr: list[int]) -> None:
        """
        Set the full scale range of the attached sensors. See lookup table between
        command and corresponding pressure in the device user manual.

        :param fsr: list of full scale range values, like `[0, 1, 3, 3, 2, 0]`
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """
        self._set_full_scale(cast("list[Number]", fsr), True)

    def get_full_scale_unitless(self) -> list[int]:
        """
        Get the full scale range of the attached sensors. See lookup table between
        command and corresponding pressure in the device user manual.

        :return: list of full scale range values, like `[0, 1, 3, 3, 2, 0]`
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """
        return cast("list[int]", self._get_full_scale(True))

    def set_full_scale_mbar(self, fsr: list[Number]) -> None:
        """
        Set the full scale range of the attached sensors (in unit mbar)

        :param fsr: full scale range values in mbar, for example `[0.01, 1000]`
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """
        self._set_full_scale(fsr, False)

    def get_full_scale_mbar(self) -> list[Number]:
        """
        Get the full scale range of the attached sensors

        :return: full scale range values in mbar, like `[0.01, 1, 0.1, 1000, 50000, 10]`
        :raises SerialCommunicationIOError: when communication port is not opened
        :raises PfeifferTPGError: if command fails
        """

        return self._get_full_scale(False)
