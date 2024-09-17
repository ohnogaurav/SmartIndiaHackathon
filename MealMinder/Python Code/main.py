import cv2
import numpy as np

# Open the camera (Irium Webcam)
cap = cv2.VideoCapture(0)  # Change index if needed

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert the frame to HSV (hue, saturation, value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for detecting white (or near-white) plate color in HSV
    lower_white = np.array([0, 0, 168])   # Adjust based on actual plate color
    upper_white = np.array([172, 111, 255])

    # Create a mask to isolate white areas (the plate)
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Apply the mask to get the plate region
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours on the masked image (white regions)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Calculate the total area of the contours (food area)
    total_area = sum(cv2.contourArea(contour) for contour in contours)

    # Get the total area of the frame (or the masked region)
    frame_area = frame.shape[0] * frame.shape[1]

    # Calculate the percentage of the frame occupied by the contours
    coverage = (total_area / frame_area) * 100

    # Determine plate status and fines based on the coverage percentage
    if coverage < 5:
        plate_status = "Plate is empty"
        fine = 0
    elif 5 <= coverage < 20:
        plate_status = "Plate is nearly empty"
        fine = 10
    elif 20 <= coverage < 40:
        plate_status = "Plate is 1/4 full"
        fine = 20
    elif 40 <= coverage < 60:
        plate_status = "Plate is half full"
        fine = 35
    elif 60 <= coverage < 80:
        plate_status = "Plate is 3/4 full"
        fine = 50
    else:
        plate_status = "Plate is full"
        fine = 70

    # Display the plate status and fine on the frame
    cv2.putText(frame, plate_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    fine_message = f"You have been fined Rs {fine}"
    cv2.putText(frame, fine_message, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the original frame and the masked result
    cv2.imshow('Plate Scan', frame)
    cv2.imshow('Plate Detection (Masked)', result)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and close the window
cap.release()
cv2.destroyAllWindows()
