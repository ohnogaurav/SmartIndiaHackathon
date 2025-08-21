import os
import time
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from werkzeug.utils import secure_filename
from plate_detection import analyze_plate

ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg'}

def allowed_file(filename: str) -> bool:
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret'  # replace in production
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['OUTPUT_FOLDER'] = os.path.join('static', 'outputs')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('index'))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('index'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ts = int(time.time())
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{ts}_{filename}")
            file.save(upload_path)

            output_filename = f"processed_{ts}_{filename}"
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

            # NEW: analyze_plate now returns (status, fine, output_path_abs, coverage, detected_items)
            result = analyze_plate(upload_path, output_path)

            payload = {
                'status': result[0],
                'fine': int(result[1]),
                'coverage_percent': result[3],
                'detected_items': result[4],   # ✅ new key
                'output_image_url': url_for('static', filename=f"outputs/{output_filename}")
            }

            # API clients get JSON
            if request.headers.get('Accept') == 'application/json':
                return jsonify(payload)

            # Web clients get template
            return render_template('index.html', result=payload)

        else:
            flash('Unsupported file type. Please upload .png, .jpg, or .jpeg')
            return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
