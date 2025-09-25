# 🌈 QRGB - Multicolor QR Codes


## VIBECODE OPSEC NOTICE  
This code was largely produced by AI (Claude mainly) under my supervision. I work in infosec (pentesting and application security) and have reviewed it for glaring holes, but it's always possible to miss something. To my knowledge it's safe enough for general usage. Consider your own threat model and the sensitivity of your information when storing anything in any system. 

---

A Python library and CLI tool for creating and decoding multi-color QR codes that can store 3x more data than traditional QR codes by using RGB color channels.
Features

Triple Capacity: Store 3x more data than standard QR codes (up to 6,993 bytes)
8-Color Encoding: Uses black, white, red, green, blue, yellow, cyan, and magenta
CLI Interface: Full-featured command-line tool with rich terminal output
Web Interface: Flask web app with camera support for mobile scanning
File Support: Encode/decode both text and binary files
ASCII Art: Terminal-friendly visualization of color QR codes
Grid Output: Export as Python data structures
Docker Ready: Containerized with modern Python tooling

## Quick Start

### online demo https://qrgb.shyft.us

Installation
# Install from PyPI (when published)
uv pip install qrgb

# Or install from source
git clone <repo-url>
cd qrgb
uv pip install -e .
Basic Usage
# Encode text
qrgb encode "Hello, World!" --out hello.png

# Show ASCII art version
qrgb encode "Secret message" --ascii

# Encode a file
qrgb encode-file document.pdf --out qrcode.png

# Decode an image
qrgb decode qrcode.png

# Show capacity information
qrgb capacity
How It Works
QRGB splits your data into three equal parts and encodes each part into a separate QR code using different color channels (Red, Green, Blue). The final image combines all three channels using 8 colors:

Black (0): All channels active
Red (1): Red channel only
Green (2): Green channel only  
Yellow (3): Red + Green channels
Blue (4): Blue channel only
Magenta (5): Red + Blue channels
Cyan (6): Green + Blue channels
White (7): No channels active

Command Reference
Encoding Commands
Text Encoding:
qrgb encode "Your text here" --out output.png
qrgb encode --ascii  # Show ASCII art version
qrgb encode --grid   # Output as Python grid data
File Encoding:
qrgb encode-file image.jpg --out qr.png
qrgb encode-file document.pdf --ascii --code  # Show matrix representation
Decoding Commands
qrgb decode qrcode.png
qrgb decode qrcode.png --save  # Save decoded file
qrgb decode qrcode.png --tolerance 50  # Adjust color tolerance
Utility Commands
qrgb capacity  # Show capacity information
Web Interface
The package includes a Flask web application for browser-based encoding/decoding:
# Run web app
python -m qrgb.webapp

# Or with Docker
docker build -t qrgb .
docker run -p 5000:5000 qrgb
Features:

Camera integration for mobile QR scanning
Drag-and-drop file upload
Real-time capacity calculation
Responsive design

Python API
from qrgb import encode, decode, get_max_qr_capacity

# Encode text to image
encode("Hello World", "output.png", show_ascii=True)

# Get capacity info
max_capacity = get_max_qr_capacity()
print(f"Max capacity: {max_capacity} bytes")

# Decode from image
decoded_text = decode("qrcode.png")
Technical Specifications

Maximum Capacity: 6,993 bytes (3× QR Version 40)
Error Correction: Level M (15% recovery)
Color Tolerance: Adjustable (default: 30)
Supported Formats: PNG, JPEG, BMP, GIF
Python Version: 3.8+

File Format Support
Text Data:

UTF-8 encoded strings
Up to ~6,993 characters

Binary Files:

Any file type via Base64 encoding
Effective capacity: ~5,245 bytes after encoding overhead
Automatic filename preservation

Installation Options
Using uv (Recommended)
# Install globally
uv pip install qrgb

# Install in isolated environment
uv venv qrgb-env
source qrgb-env/bin/activate  # or qrgb-env\Scripts\activate on Windows
uv pip install qrgb
Using pip
pip install qrgb
From Source
git clone <repo-url>
cd qrgb
uv pip install -e .
Docker
# Build and run web interface
docker build -t qrgb .
docker run -p 5000:5000 qrgb

# Use CLI in Docker
docker run --rm -v $(pwd):/data qrgb qrgb encode "Hello" --out /data/output.png
Dependencies
Core dependencies:

pillow - Image processing
qrcode - QR code generation
pyzbar - QR code decoding
numpy - Array operations
typer - CLI interface
rich - Terminal formatting

Web interface:

flask - Web framework
werkzeug - WSGI utilities

Contributing

Fork the repository
Create a feature branch
Make your changes
Add tests
Submit a pull request

License
MIT License - see LICENSE file for details.
Troubleshooting
Decoding Issues:

Ensure good lighting and focus when capturing images
Try adjusting --tolerance parameter (10-100)
Check that image contains all 8 colors clearly

Capacity Exceeded:

Use qrgb capacity to check limits
Consider compressing files before encoding
Split large data across multiple QRGB codes

Installation Issues:

Ensure system has libzbar installed (apt install libzbar0 on Ubuntu)
For M1 Macs, may need brew install zbar

Examples
Encoding Examples
# Simple text
qrgb encode "Meet me at the secret location at midnight"

# File with custom output
qrgb encode-file confidential.pdf --out secure-qr.png

# View as ASCII art (terminal friendly)
echo "Testing QRGB" | qrgb encode --ascii

# Export as Python data
qrgb encode "API_KEY=abc123" --grid > qr_data.py
Decoding Examples
# Basic decode
qrgb decode photo.jpg

# Decode with higher tolerance for blurry images
qrgb decode screenshot.png --tolerance 50

# Save decoded file automatically
qrgb decode file-qr.png --save
Web Interface Screenshots
The web interface provides:

📱 Mobile-friendly camera capture
🖼️ Drag-and-drop image upload  
📊 Real-time capacity indicators
🎨 Color legend and preview
💾 Instant download of generated QR codes
