# Assignment 1 - YOLOv8 Object Detection

This assignment demonstrates how to use the YOLOv8 object detection model from the Ultralytics package on a local image using Python in a virtual environment.

---

## 🔧 Steps Followed

### 1. Virtual Environment Setup

- Created a folder named `Internship`
- Inside it, created another folder `Assignment_1`
- Opened `Assignment_1` in **VS Code**
- Opened the terminal and ran the following command to create a virtual environment:

```bash
python -m venv venv
```

---

### 2. Set Execution Policy (Windows PowerShell)

To allow the activation script to run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### 3. Activate the Virtual Environment

Run the following command inside PowerShell:

```powershell
.env\Scripts\Activate.ps1
```

---

### 4. Install Ultralytics

With the virtual environment active, install the `ultralytics` package:

```bash
pip install ultralytics
```

---

### 5. Save the Image

- Download and save the provided image as `bus.jpg` in the `Assignment_1` folder.

---

### 6. Run the Detection Script

Create a Python script with the following content and run it:

```python
from ultralytics import YOLO

# Load the YOLOv8n model
model = YOLO("yolov8n.pt")

# Predict on the local image
results = model("C:\Internship\Assignment_1\bus.jpg")

# Show and save results
results[0].show()        # Display the image with detections
results[0].save()        # Save the result in the same folder
```

- The output image (with bounding boxes) will be saved in the same folder as `result_bus.jpg`.

---

## 📝 Note

As an alternative to step 6, you can directly run the following YOLO CLI command:

```bash
yolo task=detect mode=predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

- This will download the image, run detection, and save the output in:
  
  ```
  runs/detect/predict
  ```

---

## ✅ Output

- The output image (`result_bus.png`) shows the detected objects.
- It is saved in the same directory as the input image (`Assignment_1`).

---
