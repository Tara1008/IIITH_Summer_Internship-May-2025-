from ultralytics import YOLO

# Load a model
model = YOLO("D:\IIITH_internship\yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="african-wildlife.yaml", epochs=20, imgsz=640)