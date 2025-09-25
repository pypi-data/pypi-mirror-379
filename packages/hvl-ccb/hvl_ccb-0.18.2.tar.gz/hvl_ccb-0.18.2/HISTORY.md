# History

## 0.18.2 (2025-09-24)

* Fix ReadTheDocs
* Update to be compatible with `0.13.0` of `ruff`

## 0.18.1 (2025-08-19)

* Hot-fix to be compatible with the newly released version `3.10.0` of `pymodbus` (removal of `BinaryPayloadBuilder` and `BinaryPayloadDecoder`)
* Update `CONTRIBUTING.md`, fix typos and grammar
* Add "Coding Style" in `CONTRIBUTING.md`

## 0.18.0 (2025-06-23)

* New device: PFA-2 filter
* `RangeEnum` supports now also reverse range
* Update on `README.md` and `INSTALLATION.md` include `uv`

## 0.17.1 (2025-05-14)

* Update to be compatible with `0.11.0` of `ruff`
* Change `AUTHOR.rst`, `CONTRIBUTING.rst`, `INSTALLATION.rst`, `README.rst`, and `HISTORY.rst` to `*.md` format
* Update `CONTRIBUTING.md` include `uv` usage and test guideline
* Update `pyproject.toml`: add dependency-groups dev and lint

## 0.17.0 (2025-01-17)

* New devices: FPCSCube and SynthCube
* Drop support for Python 3.9
* Add support for Python 3.13
* Drop TelnetCommunication and use TCP for our devices
* Update code style (e.g. `ruff>=0.9.2`)
* Use `pytest-profiling>=1.8.1` for development

## 0.16.0 (2024-10-18)

* New device: Korad laboratory bench DC power supply KA3000p-series
* Fix `pytest-profiling` to `1.7.0` as new release has a bug
* Use `datetime.now()` with timezone

## 0.15.1 (2024-09-25)

* Update to be compatible with `0.6.0` of `ruff`
* Remove wrong kwarg from `ModbusTcpClient`
* Small fix of logging in `tcp`-communication
* Change logging behaviour when checking the status of a `labjack` connection
* Report test results in CI as jUnit-data

## 0.15.0 (2024-05-14)

* Support of Python 3.11 and 3.12 (Older Python versions will not be supported with future release)
* Code formatting and linting is performed with `Ruff` (`black`, `isort`, `pylint` are not used anymore)
* Minor rework of VISA communication
* Minor rework of `fug`-package
* Bugfixes in `tiepie`
* New feature in `lauda`: Read temperature from external sensor

## 0.14.4 (2023-12-22)

* Hot-fix to be compatible with the newly released version `23.12.0` of `black`
* Switch to src-layout
* In `tiepie`:
  * implementation property `generator_is_running` to check, whether the generator is running
  * properties `probe_offset` and `probe_gain` are not implemented and raise NotImplementedError

## 0.14.3 (2023-11-17)

* Fix Heinzinger conversion from mA to A and fix wrong docstrings
* Hot-fix to be compatible with the newly released version `23.11.0` of `black`
* Fix `bumpver` tag messages
* Implementation of Technix to fulfil `protocols.Source`

## 0.14.2 (2023-09-07)

* Change dependency to `libtiepie` with linux binaries using forked version `python-libtiepie-bi`
* Adapt `makefile` after removing `setup.py`
* Fix commit messages and tag with `bumpver`
* Hot-fix to be compatible with the newly released version `3.5.0` of `pymodbus`

## 0.14.1 (2023-08-21)

* Remove `setup.cfg`, `setup.py`, `mypy.ini`, `pytest.ini`, `requirements_dev.txt` and change to `pyproject.toml`
* Replace `bump2version` with `bumpver`
* Change dependency to `libtiepie` with linux binaries
* Hot-fix to be compatible with the newly released version `6.1.0` of `flake8`

## 0.14.0 (2023-07-28)

* Rework of Heinzinger high voltage source control
  * validation of input values (e.g. `voltage`-property)
  * merge `HeinzingerPNC` and `HeinzingerDI` to `Heinzinger`
  * always return values as V for voltage and A for current
  * RangeEnum for `number_of_recordings`
  * fulfil `protocols.Source`
  * raise Error for getter and setter (e.g. set_current, get_current ...), use property instead
* Hot-fix to be compatible with the newly released version `23.7.0` of `black`
* Hot-fix to be compatible with the newly released version `3.4.0` of `pymodbus`
* Hot-fix to be compatible with the newly released version `1.1.6` of `libtiepie`
  * drop support for I2C
* Remove default import from `hvl_ccb.comm` and `hvl_ccb.dev` for specific communication protocols and devices

## 0.13.3 (2023-03-31)

* Introduce common protocol for voltage and current sources `hvl_ccb.dev.protocols.sources`
* Update code style to `black` 23.3.0 and `isort` 5.12.0
* An `_EarthingStick` of `BaseCube` is implemented as a `_Switch`
* Code improvements for device `Heinzinger`
  * use property-based instead of getter and setter
  * DeprecationWarning for getter and setter (e.g. set_current, get_current ...)

## 0.13.2 (2023-03-17)

* Hot-fix to be compatible with the newly released version `3.0.0` of `typeguard`

## 0.13.1 (2023-03-03)

* Repository maintenance
  * add the option to manually set `n_attempts_max` and `attempt_interval_sec` in `query` of the `SyncCommunicationProtocol`
  * fix links in description for `Heinzinger` digital interface and universal high voltage power supplies
  * keep copyright year information only in `docs/conf.py` and `README.rst`
  * remove copyright year information from the files
  * fix readthedocs build failed issue
  * update code style to `black` 23.1.0

## 0.13.0 (2023-01-27)

* Drop support for Python 3.7 and 3.8:
  * remove version dependent implementations
  * changed typing acc. to PEP 585
* Un-freeze version number of dependencies and upgrade to most recent versions

## 0.12.3 (2022-12-27)

* Code improvements for device `cube`:
  * split `alarms` from `constants`
  * split `errors` from `constants`
  * split `earthing_stick` from `constants`
  * split `support` from `constants`
* Update code style to `black` 22.12.0
* Smaller change of device `tiepie`:
  * change hard coded trigger time out value for no time out/infinite (-1) to `ltp.const.TO_INFINITY`

## 0.12.2 (2022-11-29)

* Move the device modules into packages
* Bugfix in `validate_number` to check the order of the limits
* Repository maintenance:
  * imports are sorted with `isort`
  * some `mypy` fixing and additional typing

## 0.12.1 (2022-10-31)

* Fix `numpy` version requirement problem
  * for Python 3.7: 1.21.6
  * for Python 3.8 and onwards: 1.23.4

## 0.12.0 (2022-10-17)

* Last release for Python 3.7 and 3.8
* Repository maintenance
  * update Labjack LJM software installer link in the pipeline
  * fix dependencies to the fixed version
  * fix `asyncua` to 0.9.95 and `pymodbus` to 2.5.3 (newer versions break the code)
  * fix PICube checker for slope as it is always positive

## 0.11.1 (2022-09-15)

* Repository maintenance
  * fix issue with `mypy` and Python 3.10.7
  * update code style to `black` 22.8.0
  * project configurations merged into `setup.cfg`
  * fix coverage indicator

## 0.11.0 (2022-06-22)

* New device: Fluke 884X Bench 6.5 Digit Precision Multimeter
* `RangeEnum` is a new enum for e.g. measurement ranges which also finds a suitable range object
* smaller changes of device `tiepie`:
  * introduce status method `is_measurement_running()` to check if the device is armed
  * introduce `stop_measurement()` to disarm the trigger of the device
  * fix bug with docs due to change of `libtiepie`
* `NameEnum` and inherited enums can only have unique entries

## 0.10.3 (2022-03-21)

* fix bug in the Labjack pulse feature that occurred when the start time was set to 0s
* new conversion utility to map two ranges on each other
* update CONTRIBUTING.RST
* update makefile and make.sh
* improve the mockup telnet test server

## 0.10.2 (2022-02-28)

* introduction of `black` as code formatter
* increase the required version of the package `aenum`
* remove device `supercube2015` - as it is no longer used
* remove unused package `openpyxl` requirement
* fix bug in highland logging
* improve handling for communication error with picotech

## 0.10.1 (2022-01-24)

* several improvements and fixes for device `cube`:
  * privatize `Alarms` and `AlarmsOverview`
  * fix list of cube alarms
  * improve docs
  * fix bugs with earthing sticks
  * fix bug in config dataclass of cube
* introduction of BoolEnum
* introduction of RangeEnum
* bumpversion -> bump2version

## 0.10.0 (2022-01-17)

* Reimplementation of the Cube (before known as Supercube)
* new names:
  * Supercube Typ B -> BaseCube
  * Supercube Typ A -> PICube (power inverter Cube)
* new import:
  * `from hvl_ccb.dev.supercube import SupercubeB` ->
    `from hvl_ccb.dev.cube import BaseCube`
* new programming style:
  * getter / setter methods -> properties
  * e.g. get: `cube.get_support_output(port=1, contact=1)` ->
    `cube.support_1.output_1`
  * e.g. set: `cube.get_support_output(port=1, contact=1,
    state=True)` -> `cube.support_1.output_1 = True`
* unify Exceptions of Cube
* implement Fast Switch-Off of Cube
* remove method `support_output_impulse`
* all active alarms can now be queried `cube.active_alarms()`
* alarms will now result in different logging levels depending on the
  seriousness of the alarm.
* introduction of limits for slope and safety limit for RedReady
* during the startup the CCB will update the time of the cube.
* verification of inputs
* polarity of DC voltage
* Switch from `python-opcua` to `opcua-asyncio`
  (former package is no longer maintained)

## 0.9.0 (2022-01-07)

* New device: Highland T560 digital delay and pulse generator over Telnet.
* Rework of the Technix Capacitor Charger.
  * Moved into a separate sub-package
  * NEW import over `import hvl_ccb.dev.technix as XXX`
  * Slightly adapted behaviour
* Add `validate_tcp_port` to validate port number.
* Add `validate_and_resolve_host` to validate and resolve host names and IPs.
  * Remove requirement `IPy`
* Add a unified CCB Exception schema for all devices and communication protocols.
* Add data conversion functions to README.
* Update CI and devel images from Debian 10 buster to Debian 11 bullseye.
* Fix typing due to `numpy` update.
* Fix incorrect overloading of `clean_values()` in classes of
  type `XCommunicationConfig`.

## 0.8.5 (2021-11-05)

* Added arbitrary waveform for TiePie signal generation, configurable via
  `dev.tiepie.generator.TiePieGeneratorConfig.waveform` property.
* In `utils.conversion_sensor`: improvements for class constants; removed SciPy
  dependency.
* Added Python 3.10 support.

## 0.8.4 (2021-10-22)

* `utils.validation.validate_number` extension to handle NumPy arrays and
  array-like objects.
* `utils.conversion_unit` utility classes handle correctly `NamedTuple`
  instances.
* `utils.conversion_sensor` and `utils.conversion_unit` code
  simplification (no `transfer_function_order` attribute) and cleanups.
* Fixed incorrect error logging in `configuration.configdataclass`.
* `comm.telnet.TelnetCommunication` tests fixes for local run errors.

## 0.8.3 (2021-09-27)

* New data conversion functions in `utils.conversion_sensor` and
  `utils.conversion_unit` modules. Note: to use these functions you must install
  `hvl_ccb` with extra requirement, either `hvl_ccb[conversion]` or
  `hvl_ccb[all]`.
* Improved documentation with respect to installation of external libraries.

## 0.8.2 (2021-08-27)

* New functionality in `dev.labjack.LabJack`:
  * configure clock and send timed pulse sequences
  * set DAC/analog output voltage
* Bugfix: ignore random bits sent by to `dev.newport.NewportSMC100PP`
  controller during start-up/powering-up.

## 0.8.1 (2021-08-13)

* Add Python version check (min version error; max version warning).
* Daily checks for upstream dependencies compatibility and devel environment
  improvements.

## 0.8.0 (2021-07-02)

* TCP communication protocol.
* Lauda PRO RP 245 E circulation thermostat device over TCP.
* Pico Technology PT-104 Platinum Resistance Data Logger device as a wrapper of the
  Python bindings for the PicoSDK.
* In `com.visa.VisaCommunication`: periodic status polling when VISA/TCP keep
  alive connection is not supported by a host.

## 0.7.1 (2021-06-04)

* New `utils.validation` submodule with `validate_bool` and
  `validate_number` utilities extracted from internal use within a
  `dev.tiepie` subpackage.
* In `comm.serial.SerialCommunication`:
  * strict encoding errors handling strategy for subclasses,
  * user warning for a low communication timeout value.

## 0.7.0 (2021-05-25)

* The `dev.tiepie` module was splitted into a subpackage with, in particular,
  submodules for each of the device types -- `oscilloscope`, `generator`,
  and `i2c` -- and with backward-incompatible direct imports from the submodules.
* In `dev.technix`:
  * fixed communication crash on nested status byte query;
  * added enums for GET and SET register commands.
* Further minor logging improvements: added missing module level logger and removed some
  error logs in `except` blocks used for a flow control.
* In `examples/` folder renamed consistently all the examples.
* In API documentation: fix incorrect links mapping on inheritance diagrams.

## 0.6.1 (2021-05-08)

* In `dev.tiepie`:
  * dynamically set oscilloscope's channel limits in
    `OscilloscopeChannelParameterLimits`: `input_range` and
    `trigger_level_abs`, incl. update of latter on each change of
    `input_range` value of a `TiePieOscilloscopeChannelConfig`
    instances;
  * quick fix for opening of combined instruments by disabling
    `OscilloscopeParameterLimits.trigger_delay` (an advanced feature);
  * enable automatic devices detection to be able to find network devices with
    `TiePieOscilloscope.list_devices()`.
* Fix `examples/example_labjack.py`.
* Improved logging: consistently use module level loggers, and always log exception
  tracebacks.
* Improve API documentation: separate pages per modules, each with an inheritance
  diagram as an overview.

## 0.6.0 (2021-04-23)

* Technix capacitor charger using either serial connection or Telnet protocol.
* Extensions, improvements and fixes in existing devices:
  * In `dev.tiepie.TiePieOscilloscope`:
    * redesigned measurement start and data collection API, incl. time out
         argument, with no/infinite time out option;
    * trigger allows now a no/infinite time out;
    * record length and trigger level were fixed to accept, respectively, floating
         point and integer numbers;
    * fixed resolution validation bug;
  * `dev.heinzinger.HeinzingerDI` and `dev.rs_rto1024.RTO1024` instances are now
     resilient to multiple `stop()` calls.
  * In `dev.crylas.CryLasLaser`: default configuration timeout and
     polling period were adjusted;
  * Fixed PSI9080 example script.
* Package and source code improvements:
  * Update to backward-incompatible `pyvisa-py>=0.5.2`. Developers, do update
     your local development environments!
  * External libraries, like LibTiePie SDK or LJM Library, are now not installed by
     default; they are now extra installation options.
  * Added Python 3.9 support.
  * Improved number formatting in logs.
  * Typing improvements and fixes for `mypy>=0.800`.

## 0.5.0 (2020-11-11)

* TiePie USB oscilloscope, generator and I2C host devices, as a wrapper of the Python
  bindings for the LibTiePie SDK.
* a FuG Elektronik Power Supply (e.g. Capacitor Charger HCK) using the built-in ADDAT
  controller with the Probus V protocol over a serial connection
* All devices poling status or measurements use now a `dev.utils.Poller` utility
  class.
* Extensions and improvements in existing devices:
  * In `dev.rs_rto1024.RTO1024`: added Channel state, scale, range,
      position and offset accessors, and measurements activation and read methods.
  * In `dev.sst_luminox.Luminox`: added querying for all measurements
      in polling mode, and made output mode activation more robust.
  * In `dev.newport.NewportSMC100PP`: an error-prone
      `wait_until_move_finished` method of replaced by a fixed waiting time,
      device operations are now robust to a power supply cut, and device restart is not
      required to apply a start configuration.
* Other minor improvements:
  * Single failure-safe starting and stopping of devices sequenced via
      `dev.base.DeviceSequenceMixin`.
  * Moved `read_text_nonempty` up to `comm.serial.SerialCommunication`.
  * Added development Dockerfile.
  * Updated package and development dependencies: `pymodbus`,
      `pytest-mock`.

## 0.4.0 (2020-07-16)

* Significantly improved new Supercube device controller:
  * more robust error-handling,
  * status polling with generic `Poller` helper,
  * messages and status boards.
  * tested with a physical device,
* Improved OPC UA client wrapper, with better error handling, incl. re-tries on
  `concurrent.futures.TimeoutError`.
* SST Luminox Oxygen sensor device controller.
* Backward-incompatible changes:
  * `CommunicationProtocol.access_lock` has changed type from
    `threading.Lock` to `threading.RLock`.
  * `ILS2T.relative_step` and `ILS2T.absolute_position` are now called,
    respectively, `ILS2T.write_relative_step` and
    `ILS2T.write_absolute_position`.
* Minor bugfixes and improvements:
  * fix use of max resolution in `Labjack.set_ain_resolution()`,
  * resolve ILS2T devices relative and absolute position setters race condition,
  * added acoustic horn function in the 2015 Supercube.
* Toolchain changes:
  * add Python 3.8 support,
  * drop pytest-runner support,
  * ensure compatibility with `labjack_ljm` 2019 version library.

## 0.3.5 (2020-02-18)

* Fix issue with reading integers from LabJack LJM Library (device's product ID, serial
  number etc.)
* Fix development requirements specification (tox version).

## 0.3.4 (2019-12-20)

* New devices using serial connection:
  * Heinzinger Digital Interface I/II and a Heinzinger PNC power supply
  * Q-switched Pulsed Laser and a laser attenuator from CryLas
  * Newport SMC100PP single axis motion controller for 2-phase stepper motors
  * Pfeiffer TPG controller (TPG 25x, TPG 26x and TPG 36x) for Compact pressure Gauges
* PEP 561 compatibility and related corrections for static type checking (now in CI)
* Refactorings:
  * Protected non-thread safe read and write in communication protocols
  * Device sequence mixin: start/stop, add/rm and lookup
  * `.format()` to f-strings
  * more enumerations and a quite some improvements of existing code
* Improved error docstrings (`:raises:` annotations) and extended tests for
  errors.

## 0.3.3 (2019-05-08)

* Use PyPI labjack-ljm (no external dependencies)

## 0.3.2 (2019-05-08)

* INSTALLATION.rst with LJMPython prerequisite info

## 0.3.1 (2019-05-02)

* readthedocs.org support

## 0.3 (2019-05-02)

* Prevent an automatic close of VISA connection when not used.
* Rhode & Schwarz RTO 1024 oscilloscope using VISA interface over TCP::INSTR.
* Extended tests incl. messages sent to devices.
* Added Supercube device using an OPC UA client
* Added Supercube 2015 device using an OPC UA client (for interfacing with old system
  version)

## 0.2.1 (2019-04-01)

* Fix issue with LJMPython not being installed automatically with setuptools.

## 0.2.0 (2019-03-31)

* LabJack LJM Library communication wrapper and LabJack device.
* Modbus TCP communication protocol.
* Schneider Electric ILS2T stepper motor drive device.
* Elektro-Automatik PSI9000 current source device and VISA communication wrapper.
* Separate configuration classes for communication protocols and devices.
* Simple experiment manager class.

## 0.1.0 (2019-02-06)

* Communication protocol base and serial communication implementation.
* Device base and MBW973 implementation.
