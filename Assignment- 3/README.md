# YOLOv8 African Wildlife Detection

## 1) Dataset Installation
Using the link:  
[Download African Wildlife Dataset](https://github.com/ultralytics/assets/releases/download/v0.0.0/african-wildlife.zip)  
The dataset was downloaded and unzipped in the working directory.

## 2) Model Training
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo8n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="african-wildlife.yaml", epochs=20, imgsz=640)
```

## 3) Training Results
After 20 epochs:
```
20 epochs completed in 2.302 hours.
Optimizer stripped from runs\detect\train\weights\last.pt, 6.2MB
Optimizer stripped from runs\detect\train\weights\best.pt, 6.2MB

Validating runs\detect\train\weights\best.pt...
Ultralytics 8.3.151  Python-3.11.9 torch-2.7.1+cpu CPU (12th Gen Intel Core(TM) i7-1260P)
Model summary (fused): 72 layers, 3,006,428 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 8/8 [00:11<00
                   all        225        379      0.936      0.878      0.946      0.777
               buffalo         62         89      0.963      0.874      0.954      0.802
              elephant         53         91      0.884      0.835      0.915      0.737
                 rhino         55         85      0.962      0.918      0.959      0.818
                 zebra         59        114      0.935      0.884      0.957       0.75
Speed: 0.7ms preprocess, 46.0ms inference, 0.0ms loss, 0.4ms postprocess per image
Results saved to runs\detect\train
```

## 4) Output Graphs Analysis

### Confusion Matrix
- Strong diagonal dominance → high classification accuracy.
- Buffalo and elephant show some mutual confusion → similar visual features.
- Some background misclassification → detection failures in cluttered scenes.

### F1-Confidence Curve
- Peak **F1 = 0.91** at **0.575 confidence** → optimal balance point.
- Sharp drop after 0.8 → overly conservative at high thresholds.
- Rhino best performance, elephant weakest.

### Precision-Confidence Curve
- Precision reaches **1.0** at **0.97 confidence** → excellent calibration.
- Gradual slope indicates some mid-range confident-but-wrong predictions.

### Precision-Recall Curve
- High AUC values (**0.946–0.959**) → strong performance across operating points.
- Rectangular shape → consistent precision and recall.

### Recall-Confidence Curve
- Starts at **98% recall** at low thresholds.
- Sharp drop after 0.8 → misses valid detections at high thresholds.

### Training Curves
- Smooth convergence without overfitting.
- Parallel train/validation curves → strong generalization.

### Data Distribution
- Balanced classes (**400–575 samples each**).
- No dominant species → consistent cross-class performance.
