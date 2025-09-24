# Embody File

[![PyPI](https://img.shields.io/pypi/v/embody-file.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/embody-file.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/embody-file)][python version]
[![License](https://img.shields.io/pypi/l/embody-file)][license]

[![Tests](https://github.com/aidee-health/embody-file/workflows/Tests/badge.svg)][tests]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/embody-file/
[status]: https://pypi.org/project/embody-file/
[python version]: https://pypi.org/project/embody-file
[tests]: https://github.com/aidee-health/embody-file/actions?workflow=Tests
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

This is a Python based implementation for parsing binary files from the Aidee EmBody device.

## Features

- Converts binary embody files to HDF, CSV, etc
- Integrates with [the EmBody Protocol Codec](https://github.com/aidee-health/embody-protocol-codec) project
- CLI (command line interface)
- Can be used as package in other projects
- Type safe code using [mypy](https://mypy.readthedocs.io/) for type checking

## Requirements

- Python 3.11+

## Installation

You can install _Embody File_ via [pip]:

```console
$ pip install embody-file
```

## Usage

To use the command line, first install this library either globally or using venv:

```console
$ pip install embody-file
```

When this library has been installed, a new command is available, `embody-file` which can be used according to the examples below:

### Get help

To get an updated overview of all command line options:

```bash
embody-file --help
```

### Print version number

```bash
embody-file --version
```

### Convert binary embody file to HDF

To convert to a [HDF 5 (hierarcical data format)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) format, run the following:

```bash
embody-file testfiles/v5_0_0_test_file.log --output-format HDF
```

The file will be named the same as the input file, with the `.hdf` extension at the end of the file name.

**Performance Note**: HDF exports now use optimized batched writes for improved performance when exporting multiple datasets.

#### Reading HDF Metadata

The HDF files store sampling frequency as metadata attributes rather than on the DataFrame index. This approach handles real-world sensor data that may have timing variations or gaps.

To access the sampling frequency from HDF files:

```python
import pandas as pd

# Read the data
df = pd.read_hdf('your_file.hdf', key='multidata')

# Access sampling frequency metadata
with pd.HDFStore('your_file.hdf', mode='r') as store:
    attrs = store.get_storer('multidata').attrs
    if hasattr(attrs, 'sample_frequency_hz'):
        print(f"Sampling frequency: {attrs.sample_frequency_hz} Hz")
        print(f"Sample period: {attrs.sample_period_ms} ms")
```

Available metadata attributes:
- `sample_frequency_hz`: The sampling frequency in Hertz
- `sample_period_ms`: The sampling period in milliseconds

### Convert binary embody file to CSV

To convert to CSV format, run the following:

```bash
embody-file testfiles/v5_0_0_test_file.log --output-format CSV
```

The file will be named the same as the input file, with the `.csv` extension at the end of the file name.

### Convert to multiple formats at once

It is possible to convert to multiple formats at once. For example, to convert to both HDF and CSV, run the following:

```bash
embody-file testfiles/v5_0_0_test_file.log --output-format HDF CSV
```

### Print statistics for binary embody file

To print stats without conversion:

```bash
embody-file testfiles/v5_0_0_test_file.log --print-stats
```

### Fail on parse errors

The parser is lenient by default, accepting errors in the input file. If you want to the parsing to fail on any errors, use the `--strict` flag:

```bash
embody-file testfiles/v5_0_0_test_file.log --strict
```

## Logging

This library uses Python's standard logging module and follows best practices for libraries:

### For Library Users

The library is **silent by default** - it won't produce any output unless you configure logging. To enable logging from the library:

```python
import logging

# Enable INFO level logging for embodyfile
logging.getLogger('embodyfile').setLevel(logging.INFO)
logging.getLogger('embodyfile').addHandler(logging.StreamHandler())

# Or configure specific modules
logging.getLogger('embodyfile.parser').setLevel(logging.DEBUG)
```

### For CLI Users

The CLI configures logging automatically. Use `--log-level` to control verbosity:

```bash
embody-file input.log --log-level DEBUG
```

Available levels: CRITICAL, WARNING, INFO, DEBUG

### Sample Rate Handling

The parser automatically detects the sample rate from the data, with ECG and PPG synchronized:

- Both ECG and PPG run at the same rate (typically 500Hz or 1000Hz)
- PPG blocks are preferred for rate estimation (more samples per block = more reliable)
- Use `--samplerate` to override the detected rate for both sensors
- Rates are automatically snapped to standard values (100, 125, 250, 500, 1000, 2000 Hz) when within 1% tolerance
- Common rates: 250Hz, 500Hz, 1000Hz

**Why Rate Snapping Matters**: Due to integer millisecond timestamp resolution, non-standard rates (e.g., 501.96 Hz) would cause irregular sample spacing when expanded. For example, 501.96 Hz (1.992ms intervals) would create alternating 1ms/2ms gaps instead of consistent 2ms spacing, potentially misaligning ECG and PPG data. Snapping to 500 Hz ensures uniform 2ms intervals and proper sensor alignment.

**Note**: Hardware clock variations (±0.5%) are normal and handled transparently.

## Troubleshooting

### I get an error in the middle of the file - how do I start finding the root cause?

To get the best overview, start by running the parser in strict mode and with debug logging, so it stops at the first error:

```bash
embody-file troublesomefile.log --strict --log-level DEBUG
```

This provides positional information per message so it's easier to continue searching for errors.

If this doesn't give us enough information, look at the protocol documentation and start looking and the problematic areas in the input file.

There are several command line tools you can use. On MAC and Linux, one good example is to use the `hexdump` tool:

```bash
hexdump -C -n 70 -s 0 troublesomefile.log
```

Here, `-n 70` is the amount of bytes to print in hex format, and `-s 0` tells hexdump to start at position 0 in the file. Adjust these parameters according to your needs.

Make a note from the parser's error output of what position the first error started from, and based on that:

- Look at the preceding bytes to see whether there were any errors in the previous protocol message
- Look at the bytes from the reported (error) position to see if there are just a few bytes before a new, plausible protocol message starts

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

[file an issue]: https://github.com/aidee-health/embody-file/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/aidee-health/embody-file/blob/main/LICENSE
[contributor guide]: https://github.com/aidee-health/embody-file/blob/main/CONTRIBUTING.md
[command-line reference]: https://embody-file.readthedocs.io/en/latest/usage.html
