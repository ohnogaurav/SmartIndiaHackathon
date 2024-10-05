## WORK IS ON HALT

# MealMinder

MealMinder is a Python-based application designed to track food wastage by scanning plates and imposing fines on users based on the amount of leftover food detected. The app automates the process of identifying food waste, analyzing the plate, and fining users accordingly.

## Features

- **Plate Scanning:** Automatically detects food items left on a plate using a camera and advanced image processing techniques.
- **Fining System:** Implements an automated fine system based on the amount of food left unconsumed.
- **Data Logging:** Logs the results of each scan, including the amount of waste detected and the fines applied.

## Installation

To use the app, you'll need Python 3 and the required libraries:

1. Clone this repository:

    ```bash
    git clone https://github.com/ohnogaurav/SmartIndiaHackathon.git
    cd SmartIndiaHackathon/MealMinder/PythonCode
    ```

2. Install the required libraries:

    ```bash
    pip install opencv-python numpy
    ```

## Usage

### Scanning Plates

1. Set up your camera to capture images of plates:

    ```bash
    python MealMinder.py scan
    ```

2. The app will process the image and detect leftover food. Based on the detected amount, it will calculate and display the fine.

### Data Logging

1. Results are saved automatically after each scan in a log file, which contains information such as the plate ID, timestamp, and fine amount.

## Handling Errors

The app includes error handling for:

- Missing or incorrect image files.
- Issues with the camera or image processing.
- Invalid input for fines or scanning processes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Gaurav

## Script Overview

The `MealMinder.py` script handles both the scanning of plates and the fining process based on leftover food detection.

### Script Workflow

- **Plate Scanning:**
  - Captures an image of the plate using a connected camera.
  - Processes the image to detect leftover food and calculates the amount of waste.
  
- **Fining System:**
  - Based on the waste detected, it automatically applies a fine.
  - Logs all fines and scan results in a structured log file.

## Additional Information

- Make sure to run the app in an environment where the required libraries can access your camera.
- The app is designed for use in food-serving environments, such as hostels or cafeterias, and may require adjustments based on specific setups or camera hardware.
