
# 🍽️ Plate Monitor – YOLOv8 + Flask Demo

This project is an upgraded version of a Smart India Hackathon prototype.  
It uses **YOLOv8 (Ultralytics)** for object detection combined with a **Flask backend** and a **simple frontend**  
to analyze plate images, estimate food coverage, and assign a "fine" based on leftovers.

---

## 🚀 Features
- Upload an image of a plate via web UI
- YOLOv8-powered object detection for food & plates
- Calculates coverage % (food area / plate area)
- Assigns plate status (empty, half-full, etc.) with fines 💸
- Results displayed with processed image & detected items list
- JSON API available (for programmatic access)

---

## 📂 Project Structure
```
├── app.py                 # Flask backend (routes & upload handling)
├── plate_detection.py     # YOLOv8 + CV logic for analyzing plates
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html         # Frontend template (Jinja2)
├── static/
│   ├── style.css          # Styling for UI
│   └── outputs/           # Processed images (auto-created)
├── uploads/               # Uploaded images (auto-created)
└── README.md              # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/ohnogaurav/plate-monitor.git
cd plate-monitor
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Flask App
```bash
python app.py
```

By default, app runs at: **http://127.0.0.1:5000/**

### Upload Plate Image
- Go to web UI in browser  
- Upload `.jpg` / `.jpeg` / `.png` file  
- View processed result with detected items + coverage

### API Usage (JSON)
Send `POST` request with image file:
```bash
curl -X POST -F file=@yourimage.jpg http://127.0.0.1:5000/upload -H "Accept: application/json"
```

Response example:
```json
{
  "status": "Plate is half full",
  "fine": 35,
  "coverage_percent": 47.5,
  "detected_items": [
    {"label": "plate", "conf": 0.92},
    {"label": "spoon", "conf": 0.88}
  ],
  "output_image_url": "/static/outputs/processed_1692628234_test.jpg"
}
```

---

## 📊 Tech Stack
- **Backend:** Flask (Python)
- **Computer Vision:** YOLOv8 (Ultralytics), OpenCV
- **Frontend:** HTML, CSS (Jinja2 templating)
- **Others:** Werkzeug for uploads, REST-style JSON API

---

## 📌 Future Improvements
- Fine-tune YOLO model on food datasets for better accuracy
- Add user authentication & history of uploads
- Deploy on cloud (Heroku/AWS/GCP) with Docker
- Add real-time video support

---

## 👨‍💻 Author
Project developed & upgraded by **Gaurav Kumar**  
Originally built during **Smart India Hackathon**

