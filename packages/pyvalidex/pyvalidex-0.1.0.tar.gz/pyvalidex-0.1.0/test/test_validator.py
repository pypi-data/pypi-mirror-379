import pytest
from pyvalidex import validator

def test_pan():
    assert validator.is_pan("ABCDE1234F")
    assert not validator.is_pan("abcde1234f")

def test_aadhaar():
    assert validator.is_aadhaar("123412341234")
    assert not validator.is_aadhaar("1234")

def test_gstin():
    assert validator.is_gstin("22AAAAA0000A1Z5")
    assert not validator.is_gstin("INVALIDGST")

def test_ifsc():
    assert validator.is_ifsc("SBIN0001234")
    assert not validator.is_ifsc("1234567890")
