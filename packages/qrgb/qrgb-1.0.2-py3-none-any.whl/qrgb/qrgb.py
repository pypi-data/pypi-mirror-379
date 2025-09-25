#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "gunicorn",
#     "flask",
#     "pillow",
#     "numpy",
#     "qrcode",
#     "pyzbar",
#     "typer",
#     "rich",
#     "werkzeug",
# ]
# ///
import math
import base64
import numpy as np
from PIL import Image, ImageOps
import qrcode
import typer
from rich.console import Console
from rich.text import Text
from pathlib import Path
from rich import print

# Constant definitions for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Added padding character to avoid QR conflicts
PAD_CHAR = '\u00b7'  # Middle dot · (U+00B7)

app = typer.Typer()
console = Console()

# QR Code capacity limits (bytes) for different versions with Error Correction M
QR_CAPACITIES = {
    1: 14, 2: 26, 3: 42, 4: 62, 5: 84, 6: 106, 7: 122, 8: 152, 9: 180, 10: 213,
    11: 251, 12: 287, 13: 331, 14: 362, 15: 412, 16: 450, 17: 504, 18: 560, 19: 624, 20: 666,
    21: 711, 22: 779, 23: 857, 24: 911, 25: 997, 26: 1059, 27: 1125, 28: 1190, 29: 1264, 30: 1370,
    31: 1452, 32: 1538, 33: 1628, 34: 1722, 35: 1809, 36: 1911, 37: 1989, 38: 2099, 39: 2213, 40: 2331
}

def get_max_qr_capacity() -> int:
    """Get maximum capacity for RGB QR (3x single QR capacity)"""
    return QR_CAPACITIES[40] * 3

def calculate_file_capacity(file_path: str) -> tuple[int, int, bool]:
    """Calculate if file fits in RGB QR and return size info"""
    file_size = Path(file_path).stat().st_size
    # Base64 encoding increases size by ~33%
    encoded_size = math.ceil(file_size * 4 / 3)
    max_capacity = get_max_qr_capacity()
    
    return file_size, encoded_size, encoded_size <= max_capacity

def ensure_multiple_of_3(data: str) -> str:
    """Add padding to make length divisible by 3"""
    pad_len = (3 - (len(data) % 3)) % 3
    return data + PAD_CHAR * pad_len

def split_data(data: str) -> tuple[str, str, str]:
    """Split padded data into equal parts"""
    chunk_size = len(data) // 3
    return (
        data[:chunk_size],
        data[chunk_size:2*chunk_size],
        data[2*chunk_size:]
    )

def get_max_version(texts: tuple[str, str, str]) -> int:
    """Determine the minimum QR version needed for the longest segment"""
    max_len = max(len(text.encode('utf-8')) for text in texts)
    
    for version, capacity in QR_CAPACITIES.items():
        if max_len <= capacity:
            return version
    
    raise ValueError("Data too large for QR code")

def make_mono(img: Image.Image) -> Image.Image:
    """Convert QR image to pure black and white"""
    img = img.convert('L')
    return img.point(lambda p: 0 if p < 128 else 255)

def generate_qr(data: str, version: int, box_size: int, border: int) -> Image.Image:
    """Generate QR code image"""
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    return make_mono(qr.make_image())

def render_color(r_val: int, g_val: int, b_val: int) -> tuple:
    """Determine pixel color based on layer inputs"""
    r_black = (r_val == 0)
    g_black = (g_val == 0)
    b_black = (b_val == 0)
    
    if r_black and g_black and b_black:
        return BLACK
    elif r_black and g_black:
        return YELLOW
    elif r_black and b_black:
        return MAGENTA
    elif g_black and b_black:
        return CYAN
    elif r_black:
        return RED
    elif g_black:
        return GREEN
    elif b_black:
        return BLUE
    else:
        return WHITE

def color_to_ascii_char(color: tuple) -> str:
    """Convert color tuple to ASCII character with color"""
    char_map = {
        BLACK: "██",
        WHITE: "  ",
        RED: "██", 
        GREEN: "██",
        BLUE: "██",
        YELLOW: "██",
        CYAN: "██",
        MAGENTA: "██"
    }
    return char_map.get(color, "  ")

def qr_to_matrix(r_img: Image.Image, 
                 g_img: Image.Image, 
                 b_img: Image.Image
                ) -> list[tuple[int, ...]]:
    """
    Given the three mono QR PIL images (0=black, 255=white), 
    return a matrix (list of row‐tuples) of ints in [0..7] where bits 
    encode channel‐presence: bit0=R, bit1=G, bit2=B.
    """
    # convert to numpy arrays of 0/255
    r_arr = np.array(r_img.convert('L'))
    g_arr = np.array(g_img.convert('L'))
    b_arr = np.array(b_img.convert('L'))
    
    h, w = r_arr.shape
    matrix: list[tuple[int, ...]] = []
    
    for y in range(h):
        row = []
        for x in range(w):
            r_bit = 1 if r_arr[y, x] == 0 else 0
            g_bit = 1 if g_arr[y, x] == 0 else 0
            b_bit = 1 if b_arr[y, x] == 0 else 0
            code = (r_bit << 0) | (g_bit << 1) | (b_bit << 2)
            row.append(code)
        matrix.append(tuple(row))
    
    return matrix

def print_legend():
    """Print the color legend for the QR code"""
    legend = """
QRGB: MuLtIcOlOr QRcOdEs
Legend:
0 = white
1 = red
2 = green
3 = yellow (red + green)
4 = blue
5 = magenta (red + blue)
6 = cyan (green + blue)
7 = black (red + green + blue)
    """
    print(legend)

def render_ascii_art(img_array: np.ndarray, scale_factor: int = 10, show_legend: bool = False) -> None:
    """Render ASCII art version of the RGB QR code"""
    height, width, _ = img_array.shape
    
    if show_legend:
        print_legend()
    
    console.print("\n[bold]ASCII Art RGB QR Code:[/bold]")
    console.print("=" * (width // scale_factor * 2))
    
    for y in range(0, height, scale_factor):
        line = Text()
        for x in range(0, width, scale_factor):
            color = tuple(img_array[y, x])
            
            # Use spaces with background colors to represent blocks
            char = "  "  # Two spaces for square-ish appearance
            
            # Map colors to rich background color styles using exact RGB values
            if color == BLACK:
                line.append(char, style="on rgb(0,0,0)")
            elif color == WHITE:
                line.append(char, style="on rgb(255,255,255)")
            elif color == RED:
                line.append(char, style="on rgb(255,0,0)")
            elif color == GREEN:
                line.append(char, style="on rgb(0,255,0)")
            elif color == BLUE:
                line.append(char, style="on rgb(0,0,255)")
            elif color == YELLOW:
                line.append(char, style="on rgb(255,255,0)")  # Pure yellow
            elif color == CYAN:
                line.append(char, style="on rgb(0,255,255)")
            elif color == MAGENTA:
                line.append(char, style="on rgb(255,0,255)")
            else:
                line.append(char, style="on rgb(255,255,255)")  # Default to white
        
        console.print(line)
    
    console.print("=" * (width // scale_factor * 2))


@app.command()
def encode(
    data: str = typer.Argument(None, help="Text data to encode"), 
    output: str = typer.Option("output.png", "--out", help="Save to file"),
    show_ascii: bool = typer.Option(False, "--ascii", help="Show ASCII art version"),
    output_grid: bool = typer.Option(False, "--grid", "--code", help="Output grid instead of image")
):
    """Encode text data into colored QR or output grid"""
    if not data:
        data = typer.prompt("Enter text to encode")
    
    if output_grid:
        grid = _encode_data(data, output, show_ascii, is_binary=False, output_grid=True)
        print_legend()
        print(grid)
    else:
        _encode_data(data, output, show_ascii, is_binary=False)

        
@app.command()
def encode_file(
    file_path: str = typer.Argument(..., help="Path to binary file to encode"),
    output: str = typer.Option("output.png", "--out", help="Save to file"),    show_ascii: bool = typer.Option(False, "--ascii", help="Show ASCII art version"),
    show_code:bool=typer.Option(False, "--code", help="Show python code. list of lists")
):
    """Encode a binary file into colored QR image"""
    if not Path(file_path).exists():
        console.print(f"[red]Error: File {file_path} not found[/red]")
        raise typer.Exit(1)
    
    # Check file capacity
    file_size, encoded_size, fits = calculate_file_capacity(file_path)
    max_capacity = get_max_qr_capacity()
    
    console.print(f"File size: {file_size:,} bytes")
    console.print(f"Base64 encoded size: {encoded_size:,} bytes")
    console.print(f"RGB QR capacity: {max_capacity:,} bytes")
    
    if not fits:
        console.print(f"[red]Error: File too large! Exceeds capacity by {encoded_size - max_capacity:,} bytes[/red]")
        raise typer.Exit(1)
    
    console.print("[green]✓ File fits in RGB QR code[/green]")
    
    # Read and encode file
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    # Encode as base64 and add file metadata
    b64_data = base64.b64encode(file_data).decode('utf-8')
    file_name = Path(file_path).name
    
    # Format: FILENAME|BASE64DATA
    encoded_data = f"{file_name}|{b64_data}"
    
    console.print(f"Encoding file: {file_name}")
    _encode_data(encoded_data, output, show_ascii, is_binary=True, show_matrix=show_code)

def _encode_data(data: str, output: str, show_ascii: bool, is_binary: bool = False, output_grid: bool = False, show_matrix: bool = False):
    """Internal function to encode data - now with grid output option"""
    padded = ensure_multiple_of_3(data)
    r_data, g_data, b_data = split_data(padded)
    
    version = get_max_version((r_data, g_data, b_data))
    box_size = 10
    border = 4
    
    if not output_grid:  # Only show these messages for image output
        console.print(f"Using QR version: {version}")
        console.print(f"Data split into {len(r_data)}, {len(g_data)}, {len(b_data)} chars per channel")
    
    # Generate base QR code images
    r_img = generate_qr(r_data, version, box_size, border)
    g_img = generate_qr(g_data, version, box_size, border)
    b_img = generate_qr(b_data, version, box_size, border)
    
    r_arr = np.array(r_img)
    g_arr = np.array(g_img)
    b_arr = np.array(b_img)
    
    height, width = r_arr.shape
    if g_arr.shape != (height, width) or b_arr.shape != (height, width):
        raise ValueError("QR code dimensions mismatch")

    if output_grid:
        # Calculate QR module dimensions (remove border and box_size scaling)
        module_size = (height - 2 * border * box_size) // box_size
        
        # Generate and return color grid representation
        color_grid = []
        for y in range(module_size):
            row = []
            for x in range(module_size):
                # Sample from the center of each module
                pixel_y = border * box_size + y * box_size + box_size // 2
                pixel_x = border * box_size + x * box_size + box_size // 2
                
                r_val = r_arr[pixel_y, pixel_x]
                g_val = g_arr[pixel_y, pixel_x]
                b_val = b_arr[pixel_y, pixel_x]
                
                # Map to numeric values
                r_black = (r_val == 0)
                g_black = (g_val == 0)
                b_black = (b_val == 0)
                
                if r_black and g_black and b_black:
                    row.append(7)  # black (R+G+B)
                elif r_black and g_black:
                    row.append(3)  # yellow (R+G)
                elif r_black and b_black:
                    row.append(5)  # magenta (R+B)
                elif g_black and b_black:
                    row.append(6)  # cyan (G+B)
                elif r_black:
                    row.append(1)  # red
                elif g_black:
                    row.append(2)  # green
                elif b_black:
                    row.append(4)  # blue
                else:
                    row.append(0)  # white
            color_grid.append(tuple(row))
        return color_grid
    else:
        # Create image output (original functionality)
        color_img = np.zeros((height, width, 3), dtype=np.uint8)
        
        for y in range(height):
            for x in range(width):
                r_val = r_arr[y, x]
                g_val = g_arr[y, x]
                b_val = b_arr[y, x]
                color_img[y, x] = render_color(r_val, g_val, b_val)
        
        final_img = Image.fromarray(color_img)
        final_img.save(output)
        
        data_type = "binary file" if is_binary else "text"
        console.print(f"[green]✓ Encoded {data_type} saved to {output}[/green]")
        
        if show_ascii:
            render_ascii_art(color_img, show_legend=True)


def is_color_in_channel(pixel, channel_colors, tolerance=30):
    """Check if pixel color belongs to any color in the channel"""
    for target_color in channel_colors:
        # Calculate Manhattan distance to avoid overflow
        distance = sum(abs(int(p) - int(t)) for p, t in zip(pixel[:3], target_color))
        if distance <= tolerance:
            return True
    return False

def decode_channel_as_qr(img_array: np.ndarray, channel_colors: list, channel_name: str):
    """Extract a single color channel and decode it as a regular QR code"""
    from pyzbar import pyzbar  # Add this import
    
    height, width = img_array.shape[:2]

    # Create binary image for this channel
    binary_img = np.full((height, width), 255, dtype=np.uint8)  # Start with white

    # Mark pixels that belong to this channel as black
    for y in range(height):
        for x in range(width):
            pixel = img_array[y, x][:3]  # RGB only

            if is_color_in_channel(pixel, channel_colors):
                binary_img[y, x] = 0

    # Convert to PIL Image and try to decode
    pil_img = Image.fromarray(binary_img, mode='L')

    # Save debug image to see what we're trying to decode
    pil_img.save(f"debug_{channel_name.lower()}_channel.png")

    # Try to decode using the same logic as your existing decode_qr function
    try:
        # Try multiple thresholds
        thresholds = [128, 100, 150, 70, 180, 50, 200]
        for threshold in thresholds:
            thresholded = pil_img.point(lambda p: 255 if p > threshold else 0)
            binary_version = thresholded.convert('1')
            
            results = pyzbar.decode(binary_version)
            if results:
                return results[0].data.decode('utf-8')
            
            # Try inverted too
            inverted = pil_img.point(lambda p: 0 if p > threshold else 255)
            inverted_binary = inverted.convert('1')
            
            results = pyzbar.decode(inverted_binary)
            if results:
                return results[0].data.decode('utf-8')

    except Exception as e:
        console.print(f"[yellow]Decode error for {channel_name}: {e}[/yellow]")

    raise ValueError(f"Unable to decode {channel_name} layer")

@app.command()
def decode(
    input_path: str,
    save_file: bool = typer.Option(False, "--save", help="Save decoded data as file"),
    tolerance: int = typer.Option(30, "--tolerance", "-t", help="Color matching tolerance")
):
    """Decode RGB QR code from image"""
    if not Path(input_path).exists():
        console.print(f"[red]Error: File {input_path} not found[/red]")
        raise typer.Exit(1)
    
    # Load image
    img = Image.open(input_path).convert('RGB')
    img_array = np.array(img)
    
    console.print(f"Image size: {img_array.shape}")
    console.print(f"Using color tolerance: {tolerance}")
    
    # Define color channels - use exact colors from encoding
    red_colors = [BLACK, RED, YELLOW, MAGENTA]      # Colors with red component
    green_colors = [BLACK, GREEN, YELLOW, CYAN]     # Colors with green component  
    blue_colors = [BLACK, BLUE, CYAN, MAGENTA]      # Colors with blue component
    
    console.print("Extracting and decoding RGB channels...")
    console.print("Debug images will be saved as debug_*_channel.png")
    
    # Decode each channel separately
    results = {}
    for channel_name, colors in [("Red", red_colors), ("Green", green_colors), ("Blue", blue_colors)]:
        try:
            data = decode_channel_as_qr(img_array, colors, channel_name)
            results[channel_name] = data
            console.print(f"✓ {channel_name} channel: '{data}' ({len(data)} chars)")
        except ValueError as e:
            console.print(f"[red]✗ {e}[/red]")
            console.print(f"[yellow]Check debug_{channel_name.lower()}_channel.png to see what was extracted[/yellow]")
            return
    
    # Combine the data
    combined_data = results["Red"] + results["Green"] + results["Blue"]
    padded_data = combined_data.rstrip(PAD_CHAR)
    
    console.print(f"\n[bold green]Successfully decoded RGB QR![/bold green]")
    console.print(f"Combined data: '{padded_data}'")
    
    # Clean up debug files
    for channel in ["red", "green", "blue"]:
        debug_file = Path(f"debug_{channel}_channel.png")
        if debug_file.exists():
            debug_file.unlink()


@app.command()
def capacity():
    """Show RGB QR capacity information"""
    max_capacity = get_max_qr_capacity()
    console.print(f"[bold]RGB QR Code Capacity Information[/bold]")
    console.print(f"Single QR (v40): {QR_CAPACITIES[40]:,} bytes")
    console.print(f"RGB QR (3x): {max_capacity:,} bytes")
    console.print(f"Approximate file sizes:")
    console.print(f"  • Plain text: ~{max_capacity:,} characters")
    console.print(f"  • Binary files: ~{int(max_capacity * 0.75):,} bytes (after base64 overhead)")

def decode_qr(image: Image.Image, layer_name: str = "") -> str:
    """Decode QR from mono image"""
    from pyzbar import pyzbar
    
    # Convert to grayscale first for better control
    gray_img = image.convert('L')
    
    preprocessing_methods = []
    
    # Try multiple thresholds with better range
    thresholds = [128, 100, 150, 70, 180, 50, 200, 30, 220, 85, 115, 160]
    for threshold in thresholds:
        thresholded = gray_img.point(lambda p: 255 if p > threshold else 0)
        binary_img = thresholded.convert('1')
        preprocessing_methods.append(binary_img)
        
        # Also try inverted
        inverted = gray_img.point(lambda p: 0 if p > threshold else 255)
        inverted_binary = inverted.convert('1')
        preprocessing_methods.append(inverted_binary)
    
    # Try different scales (important for screenshots)
    for scale in [0.5, 1.5, 2.0, 0.75]:
        original_size = gray_img.size
        new_size = (int(original_size[0] * scale), int(original_size[1] * scale))
        resized = gray_img.resize(new_size, Image.LANCZOS)
        resized_mono = resized.convert('1')
        preprocessing_methods.append(resized_mono)
    
    # Try all preprocessing methods
    for method_img in preprocessing_methods:
        try:
            results = pyzbar.decode(method_img)
            if results:
                data = results[0].data.decode('utf-8')
                if layer_name:
                    console.print(f"[dim]{layer_name} layer: {len(data)} chars[/dim]")
                return data
        except:
            continue
    
    raise ValueError(f"Unable to decode {layer_name} layer")


if __name__ == "__main__":
    app()
