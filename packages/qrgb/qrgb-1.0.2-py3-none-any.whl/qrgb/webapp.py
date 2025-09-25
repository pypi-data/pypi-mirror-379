# /// script
# requires-python = ">=3.8"
# dependencies = [
## VIBECODE OPSEC NOTICE  
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
from flask import Flask, render_template, request, jsonify, send_file
import io
import base64
import numpy as np
from PIL import Image
import tempfile
import os

# Import the QRGB functions
import qrgb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_text():
    try:
        data = request.json.get('text', '')
        if not data:
            return jsonify({'error': 'No text provided'}), 400
        
        # Create temporary file for output
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            temp_path = tmp.name
        
        try:
            # Use the qrgb encode function
            qrgb._encode_data(data, temp_path, False, False)
            
            # Read the generated image
            with open(temp_path, 'rb') as f:
                img_data = f.read()
            
            # Convert to base64 for web display
            img_b64 = base64.b64encode(img_data).decode('utf-8')
            
            return jsonify({
                'success': True,
                'image': img_b64,
                'message': f'Encoded {len(data)} characters'
            })
        
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decode', methods=['POST'])
def decode_image():
    try:
        # Get the uploaded image
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            temp_path = tmp.name
            file.save(temp_path)
        
        try:
            # Load image
            img = Image.open(temp_path).convert('RGB')
            img_array = np.array(img)
            
            # Define color channels - use exact colors from encoding
            red_colors = [qrgb.BLACK, qrgb.RED, qrgb.YELLOW, qrgb.MAGENTA]
            green_colors = [qrgb.BLACK, qrgb.GREEN, qrgb.YELLOW, qrgb.CYAN] 
            blue_colors = [qrgb.BLACK, qrgb.BLUE, qrgb.CYAN, qrgb.MAGENTA]
            
            # Decode each channel separately
            results = {}
            for channel_name, colors in [("Red", red_colors), ("Green", green_colors), ("Blue", blue_colors)]:
                try:
                    data = qrgb.decode_channel_as_qr(img_array, colors, channel_name)
                    results[channel_name] = data
                except ValueError as e:
                    return jsonify({'error': f'Failed to decode {channel_name} channel'}), 400
            
            # Combine the data
            combined_data = results["Red"] + results["Green"] + results["Blue"]
            decoded_text = combined_data.rstrip(qrgb.PAD_CHAR)
            
            return jsonify({
                'success': True,
                'text': decoded_text,
                'channels': {
                    'red': results["Red"],
                    'green': results["Green"], 
                    'blue': results["Blue"]
                }
            })
        
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
            # Clean up any debug files
            for channel in ["red", "green", "blue"]:
                debug_file = f"debug_{channel}_channel.png"
                if os.path.exists(debug_file):
                    os.unlink(debug_file)
                    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/capacity')
def get_capacity():
    max_capacity = qrgb.get_max_qr_capacity()
    return jsonify({
        'single_qr': qrgb.QR_CAPACITIES[40],
        'rgb_qr': max_capacity,
        'text_chars': max_capacity,
        'binary_bytes': int(max_capacity * 0.75)
    })

# Create templates directory and index.html
import os
if not os.path.exists('templates'):
    os.makedirs('templates')

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QRGB - Multicolor QR Codes</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .panel {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .legend {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            height: 120px;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            resize: vertical;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }
        button:hover {
            background: #0056b3;
        }
        button:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        .qr-display {
            text-align: center;
            margin-top: 20px;
        }
        .qr-display img {
            max-width: 100%;
            height: auto;
            border: 2px solid #ddd;
            border-radius: 5px;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .success {
            background: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        #cameraInput {
            margin: 10px 0;
        }
        .camera-section {
            border: 2px dashed #ddd;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin: 10px 0;
        }
        .color-box {
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border: 1px solid #ccc;
        }
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 5px;
            font-family: monospace;
        }
        .capacity-info {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌈 QRGB - Multicolor QR Codes</h1>
        <p>Encode 3x more data using RGB color channels</p>
    </div>

    <div class="legend">
        <h3>Color Legend</h3>
        <div class="legend-grid">
            <div><span class="color-box" style="background: white; border: 2px solid black;"></span> 0 = White</div>
            <div><span class="color-box" style="background: red;"></span> 1 = Red</div>
            <div><span class="color-box" style="background: green;"></span> 2 = Green</div>
            <div><span class="color-box" style="background: yellow;"></span> 3 = Yellow (R+G)</div>
            <div><span class="color-box" style="background: blue;"></span> 4 = Blue</div>
            <div><span class="color-box" style="background: magenta;"></span> 5 = Magenta (R+B)</div>
            <div><span class="color-box" style="background: cyan;"></span> 6 = Cyan (G+B)</div>
            <div><span class="color-box" style="background: black;"></span> 7 = Black (R+G+B)</div>
        </div>
    </div>

    <div class="capacity-info" id="capacityInfo">
        Loading capacity information...
    </div>

    <div class="container">
        <div class="panel">
            <h2>📝 Encode Text</h2>
            <textarea id="inputText" placeholder="Enter text to encode into QRGB code..."></textarea>
            <button onclick="encodeText()">Generate QRGB Code</button>
            <div id="encodeResult"></div>
        </div>

        <div class="panel">
            <h2>📷 Decode QRGB</h2>
            <div class="camera-section">
                <p>Take a photo or upload an image of a QRGB code</p>
                <input type="file" id="cameraInput" accept="image/*" capture="camera">
                <button onclick="decodeImage()">Decode Image</button>
            </div>
            <div id="decodeResult"></div>
        </div>
    </div>

    <script>
        // Load capacity information on page load
        fetch('/capacity')
            .then(response => response.json())
            .then(data => {
                document.getElementById('capacityInfo').innerHTML = `
                    <strong>Capacity Information:</strong><br>
                    • Single QR Code: ${data.single_qr.toLocaleString()} bytes<br>
                    • QRGB Code: ${data.rgb_qr.toLocaleString()} bytes (3x capacity!)<br>
                    • Text: ~${data.text_chars.toLocaleString()} characters<br>
                    • Binary files: ~${data.binary_bytes.toLocaleString()} bytes
                `;
            });

        function encodeText() {
            const text = document.getElementById('inputText').value;
            const resultDiv = document.getElementById('encodeResult');
            
            if (!text.trim()) {
                resultDiv.innerHTML = '<div class="error">Please enter some text to encode</div>';
                return;
            }

            resultDiv.innerHTML = '<p>Generating QRGB code...</p>';

            fetch('/encode', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultDiv.innerHTML = `
                        <div class="success">${data.message}</div>
                        <div class="qr-display">
                            <img src="data:image/png;base64,${data.image}" alt="QRGB Code">
                            <p>Right-click to save image</p>
                        </div>
                    `;
                } else {
                    resultDiv.innerHTML = `<div class="error">Error: ${data.error}</div>`;
                }
            })
            .catch(error => {
                resultDiv.innerHTML = `<div class="error">Network error: ${error}</div>`;
            });
        }

        function decodeImage() {
            const fileInput = document.getElementById('cameraInput');
            const resultDiv = document.getElementById('decodeResult');
            
            if (!fileInput.files[0]) {
                resultDiv.innerHTML = '<div class="error">Please select an image first</div>';
                return;
            }

            resultDiv.innerHTML = '<p>Decoding QRGB code...</p>';

            const formData = new FormData();
            formData.append('image', fileInput.files[0]);

            fetch('/decode', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultDiv.innerHTML = `
                        <div class="success">Successfully decoded QRGB code!</div>
                        <div style="background: #f8f9fa; padding: 10px; border-radius: 5px; margin: 10px 0;">
                            <strong>Decoded Text:</strong><br>
                            <textarea readonly style="width: 100%; height: 100px;">${data.text}</textarea>
                        </div>
                        <details>
                            <summary>Channel Details</summary>
                            <div style="font-family: monospace; font-size: 12px; margin: 10px 0;">
                                <div style="color: red;">Red: "${data.channels.red}"</div>
                                <div style="color: green;">Green: "${data.channels.green}"</div>
                                <div style="color: blue;">Blue: "${data.channels.blue}"</div>
                            </div>
                        </details>
                    `;
                } else {
                    resultDiv.innerHTML = `<div class="error">Decoding failed: ${data.error}</div>`;
                }
            })
            .catch(error => {
                resultDiv.innerHTML = `<div class="error">Network error: ${error}</div>`;
            });
        }

        // Allow enter key to encode
        document.getElementById('inputText').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                encodeText();
            }
        });
    </script>
</body>
</html>
"""

with open('templates/index.html', 'w') as f:
    f.write(html_content)

if __name__ == '__main__':
    print("Starting QRGB Flask App...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
