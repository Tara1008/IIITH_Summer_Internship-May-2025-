from ultralytics import YOLO

# Load the YOLOv8n model
model = YOLO("yolov8n.pt")

# Predict on your local image
results = model("path/to/your/image")

# Show results
results[0].show()       # Optional: Display window with results
results[0].save()       # Saves output in 'runs/detect/predict'