# SHA256-Python

[![Build Status](https://travis-ci.com/trevortomlin/SHA256-Python.svg?branch=main)](https://travis-ci.com/trevortomlin/SHA256-Python)[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\
\
Implements the SHA256 hashing algorithm in Python.

## Description

This project recreates the SHA256 algorithm in Python similar to the Python module hashlib. It can take in any string and outputs a 256 bit hash that is not reversible.

## Installation

`
git clone https://github.com/trevortomlin/SHA256-Python.git
`

## Usage

```python
from SHA256Hash import Sha256

string = "abc"

sha = Sha256()
sha.hash(string)

print(sha.hexDigest())
```

Output:
`
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
`

## Technologies Used

Python, hashlib, unittest, Travis CI

## Improvements

- Implement a bitstring class that uses operator overloading to make code more readable.
- Rename variable and function names to fit PEP-8 standard.

## References

[Wikipedia](https://en.wikipedia.org/wiki/SHA-2)

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details
