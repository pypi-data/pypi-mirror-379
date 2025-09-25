"""QRGB - Multi-color QR codes with 3x capacity."""

__version__ = "0.1.0"

from .qrgb import (
    app,
    encode,
    decode,
    encode_file,
    get_max_qr_capacity,
    calculate_file_capacity,
    # Export key functions for API use
)

__all__ = [
    "encode", 
    "decode", 
    "encode_file",
    "get_max_qr_capacity",
    "calculate_file_capacity",
]
