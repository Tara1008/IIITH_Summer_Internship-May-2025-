from ultralytics import YOLO
import cv2
import os

# Load YOLOv8n segmentation model
model = YOLO("yolov8n-seg.pt")

# Input/output
frames_dir = "D:\\IIITH_internship\\Assignment_2\\frames"            # folder of extracted video frames
processed_dir = "processed"      # folder to save overlayed frames
os.makedirs(processed_dir, exist_ok=True)

# Loop over each frame
for file in sorted(os.listdir(frames_dir)):
    if not file.lower().endswith(('.png', '.jpg')):
        continue

    path = os.path.join(frames_dir, file)
    result = model(path)[0]  # get prediction for single image

    # Save overlayed frame
    out_path = os.path.join(processed_dir, file)
    result.save(filename=out_path)
