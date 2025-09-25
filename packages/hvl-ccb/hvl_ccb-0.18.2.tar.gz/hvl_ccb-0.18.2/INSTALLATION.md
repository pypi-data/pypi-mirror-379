(installation)=
# Installation

## Stable release

To install HVL Common Code Base (hvl_ccb), we recommend to use [`uv`](https://docs.astral.sh/uv/):

```console
uv pip install hvl_ccb
```

To install HVL Common Code Base with optional Python libraries that require manual installations of additional system libraries, you need to specify on installation extra requirements corresponding to these controllers. For instance, to install Python requirements for LabJack and TiePie devices, run:

```console
uv pip install "hvl_ccb[tiepie,labjack]"
```

See below for the info about additional system libraries and the corresponding extra requirements.

To install all extra requirements run:

```console
uv pip install "hvl_ccb[all]"
```

This is the preferred method to install HVL Common Code Base, as it will always install the most recent stable release.

## From sources

The sources for HVL Common Code Base can be downloaded from the [GitLab repo](https://gitlab.com/ethz_hvl/hvl_ccb).

You can either clone the repository:

```console
git clone git@gitlab.com:ethz_hvl/hvl_ccb.git
```

Or download the [tarball](https://gitlab.com/ethz_hvl/hvl_ccb/-/archive/master/hvl_ccb.tar.gz):

```console
curl  -OL https://gitlab.com/ethz_hvl/hvl_ccb/-/archive/master/hvl_ccb.tar.gz
```

Once you have a copy of the source, you can install it with:

```console
uv pip install .
```

## Additional system libraries

If you have installed `hvl_ccb` with any of the extra features corresponding to
device controllers, you must additionally install respective system library; these are:

| Extra feature           | Additional system library                                  |
|-------------------------|------------------------------------------------------------|
| `labjack`         | [LJM Library](https://labjack.com/ljm)                                             |
| `picotech`        | [PicoSDK](https://www.picotech.com/downloads)(Windows) / [libusbpt104](https://labs.picotech.com/debian/pool/main/libu/libusbpt104/) (Ubuntu/Debian)      |

For more details on installation of the libraries see docstrings of the corresponding `hvl_ccb` modules.
