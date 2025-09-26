import re

def is_pan(value: str) -> bool:
    """Validate Indian PAN number format (ABCDE1234F)"""
    return bool(re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", value))

def is_aadhaar(value: str) -> bool:
    """Validate Aadhaar number (12 digits)"""
    return bool(re.fullmatch(r"\d{12}", value))

def is_gstin(value: str) -> bool:
    """Validate GSTIN format"""
    return bool(re.fullmatch(r"\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}", value))

def is_ifsc(value: str) -> bool:
    """Validate IFSC code (BANKXXXXXXX)"""
    return bool(re.fullmatch(r"[A-Z]{4}0[A-Z0-9]{6}", value))
