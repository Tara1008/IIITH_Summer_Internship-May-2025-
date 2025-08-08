from ultralytics import YOLO

# Load a model
model = YOLO("/path/to/your/model")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="african-wildlife.yaml", epochs=20, imgsz=640)