# spikesafe-python

The official Python driver supporting Vektrex SpikeSafe products:
- [SpikeSafe PSMU](https://www.vektrex.com/products/spikesafe-source-measure-unit/)
- [SpikeSafe Performance Series ("PRF")](https://www.vektrex.com/products/spikesafe-performance-series-precision-pulsed-current-sources/)

Vektrex SpikeSafe Python API used for automation of custom instrument control sequences for testing LED, laser, and electronic equipment.

The Vektrex SpikeSafe Python API powers the Python examples published on Github.

GitHub Repository: [SpikeSafe Python Samples](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples)

Library help documentation: [spikesafe_python_lib_docs](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples/tree/master/spikesafe_python_lib_docs)

Release notes: [spikesafe_python_lib_docs/_releases](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples/tree/master/spikesafe_python_lib_docs/_releases)

## About

The **spikesafe-python** package provides light-weight access Python helper classes and functions to easily communicate with to your SpikeSafe and parse data into easy to use objects.

**spikesafe-python** supports all operating systems that support the free [Python](https://www.python.org/) interpreter.

**spikesafe-python** follows [Python Software Foundation](https://devguide.python.org/#status-of-python-branches) for supporting different versions.

## Installation

Install the latest stable version of **spikesafe-python** by using instructions in [Installing spikesafe-python Package](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples?tab=readme-ov-file#installing-spikesafe-python-package).

## Usage

To learn how to use this package, it is best to do the [Getting Started](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples/tree/master/getting_started) samples listed in order.

Then continue through the remainder of the samples listed in the order of the [Directory](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples?tab=readme-ov-file#directory).

### FAQ
How does Python handle locale?  
The [locale](https://docs.python.org/3/library/locale.html#module-locale) module is implemented on top of the _locale module, which in turn uses an ANSI [C locale](https://docs.oracle.com/cd/E19253-01/817-2521/overview-1002/index.html) (also called the "POSIX locale") implementation if available. The C locale is often described as "culture-neutral" because it doesn't apply any regional or language-specific rules for formatting data. It is a basic, system-independent locale that follows standardized rules for formatting data such as numbers, dates, and currency. The C locale uses U.S.-style conventions by default, such as:
- Period (.) as the decimal point for numbers
- Simple ASCII character classification and sorting
- English-style date and time formats

## Support / Feedback

For further assistance with **spikesafe-python** please contact Vektrex support at support@vektrex.com. This page is regularly monitored and maintained by Vektrex engineers.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python for Windows](https://www.python.org/downloads/windows/)

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Bill Thompson** - [BillThomp](https://github.com/BillThomp)
* **Eljay Gemoto** - [eljayg](https://github.com/eljayg)

## License

**spikesafe-python** is licensed under the MIT license, which allows for non-commercial and commercial use.