# pyvalidex

**pyvalidex** is a Python library for validating Indian identifiers. It provides simple functions to validate **PAN, Aadhaar, GSTIN, and IFSC codes**. Designed to be lightweight, easy to use, and Pythonic, it’s perfect for projects that require Indian ID validations.

---

## Features

- Validate **PAN** numbers (`ABCDE1234F`)  
- Validate **Aadhaar** numbers (12-digit numeric)  
- Validate **GSTIN** numbers (`22AAAAA0000A1Z5`)  
- Validate **IFSC** codes (`BANKXXXXXXX`)  
- Lightweight, dependency-free

---

## Installation

```bash
pip install pyvalidex
```


## Usage
from pyvalidex import validator

# PAN
print(validator.is_pan("ABCDE1234F"))  # True
print(validator.is_pan("abcde1234f"))  # False

# Aadhaar
print(validator.is_aadhaar("123412341234"))  # True
print(validator.is_aadhaar("1234"))          # False

# GSTIN
print(validator.is_gstin("22AAAAA0000A1Z5"))  # True
print(validator.is_gstin("INVALIDGST"))       # False

# IFSC
print(validator.is_ifsc("SBIN0001234"))  # True
print(validator.is_ifsc("1234567890"))   # False

