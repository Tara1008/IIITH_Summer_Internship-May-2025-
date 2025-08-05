from ultralytics import YOLO

# Load the YOLOv8n model
model = YOLO("yolov8n.pt")

# Predict on your local image
results = model("D:\\IIITH_internship\\Assignment_1\\bus.jpg")

# Show results
results[0].show()       # Optional: Display window with results
results[0].save()       # Saves output in 'runs/detect/predict'