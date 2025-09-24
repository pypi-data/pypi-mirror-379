# SmallDog

## Introduction

This is a Python package currently under testing, temporarily named "smalldog".
There was another package named "bigdog" under testing that handles uncertainty by a theoretical approach.
We will develop/update the simulation implementation version, "smalldog", which will be the main package.
It contains ValueU and QuantityU, which are designed to handle numerical values with asymmetric uncertainty and physical units.
This package provides a robust framework for managing uncertainties in scientific computations, extending traditional numerical representations with error propagation and unit management.

### Dependencies

- Python 3.6+
- `numpy`
- `scipy`
- `astropy`

### Key Features

- **ValueU**: Handles numerical values with asymmetric uncertainties.
- **QuantityU**: Extends `ValueU` by incorporating unit management
- Supports arithmetic operations with proper uncertainty propagation.
- Provides various comparison and formatting methods.
- Includes built-in documentation accessible via `.help()`.

## Installation

The package is currently in the alpha stage of development and is being tested on the test field named "smalldog".
To install the package, run the following command in your terminal:

```sh
pip install smalldog
```

Once installed, you can import the necessary modules in your Python script or interactive console:

```python
from smalldog import ValueU, QuantityU
```

To view the detailed descriptions for `ValueU` and `QuantityU`, use the built-in help function:

```python
ValueU().help()  # Displays detailed information on ValueU
QuantityU().help()  # Displays detailed information on QuantityU
```

These commands provide comprehensive details about generating instance objects, representation of the object, and handling object methods that contain operations, unit conversions, as well as additional functionalities.

## License & Disclaimer

- Unauthorized modification and redistribution of the source code are strictly prohibited.
- The authors bear no responsibility for any errors, malfunctions, or unintended consequences resulting from code modifications.
- This package assumes all variables are independent (zero covariance). Users should exercise caution when working with correlated data.
## Credits

**Main Developer**: DH.Koh ([donghyeok.koh.code@gmail.com](mailto\:donghyeok.koh.code@gmail.com))\
**Collaborating Developers**: JH.Kim, KM.Heo\
**Alpha Testers**: None

## Changelog

### v0.2510.14 (2025-03-07)

- Fixed operation method priority bug.
- Improved help message formatting.
- Minor path-related fixes.

## Contact & Contributions

Bug reports and contributions are welcome! Please contact the main developer for more information.

