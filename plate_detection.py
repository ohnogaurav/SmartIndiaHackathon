from ultralytics import YOLO
import cv2, os

# Load pretrained YOLOv8 model (n = nano for speed, s = small for more accuracy)
model = YOLO("yolov8n.pt")

def analyze_plate(image_path: str, output_path: str):
    """
    Runs YOLOv8 detection to find plates and food items.
    Computes coverage as ratio of food area / plate area.
    Saves annotated image with results.

    Returns: (plate_status, fine, output_path_abs, coverage_percent, detected_items)
    """
    # Run YOLO inference
    results = model(image_path)
    r = results[0]

    detected_items = []
    food_area = 0
    plate_area = 0

    # Loop through detections
    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        area = (x2 - x1) * (y2 - y1)

        # If it's a plate (or bowl), treat as plate area
        if any(k in label.lower() for k in ["plate", "bowl", "dining table"]):
            plate_area += area
        else:
            food_area += area


        detected_items.append({"label": label, "conf": round(conf, 2)})

    # Compute coverage
    coverage = (food_area / plate_area * 100) if plate_area > 0 else 0

    # Assign status + fine (same thresholds as before)
    if coverage < 5:
        plate_status, fine = "Plate is empty", 0
    elif 5 <= coverage < 20:
        plate_status, fine = "Plate is nearly empty", 10
    elif 20 <= coverage < 40:
        plate_status, fine = "Plate is 1/4 full", 20
    elif 40 <= coverage < 60:
        plate_status, fine = "Plate is half full", 35
    elif 60 <= coverage < 80:
        plate_status, fine = "Plate is 3/4 full", 50
    else:
        plate_status, fine = "Plate is full", 70

    # Save YOLO’s annotated image
    r.save(filename=output_path)

    return plate_status, fine, output_path, round(coverage, 2), detected_items
