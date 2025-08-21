
# Plate Monitor (Flask + OpenCV)

A simple, intermediate-level web app that estimates plate coverage from an uploaded image.
It demonstrates a clean Flask backend, a minimal HTML/CSS frontend, and classic CV logic.

## Features
- Upload an image (JPG/PNG) via web UI
- Backend runs OpenCV-based analysis (HSV threshold + contours)
- Returns status (empty / nearly empty / quarter / half / three-quarter / full), fine, and coverage %
- Saves and displays a processed image with overlays in `static/outputs/`

## Tech Stack
- Backend: Flask (Python)
- CV: OpenCV + NumPy (traditional image processing)
- Frontend: Jinja2 templating + minimal CSS

## Project Structure
```
plate-monitor/
├── app.py
├── plate_detection.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── outputs/
├── uploads/
├── requirements.txt
└── README.md
```

## Setup & Run (Local)
1. **Create venv & install deps**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Run the server**
   ```bash
   python app.py
   ```
3. **Open in browser**
   - Navigate to: http://localhost:5000
   - Upload a `.jpg` or `.png` image of a plate

## API (JSON)
You can also call the API directly and get JSON by sending `Accept: application/json`:
```bash
curl -H "Accept: application/json" -F "file=@examples/plate.jpg" http://localhost:5000/upload
```
Response:
```json
{
  "status": "Plate is half full",
  "fine": 35,
  "coverage_percent": 48.23,
  "output_image_url": "/static/outputs/processed_1712345678_plate.jpg"
}
```


