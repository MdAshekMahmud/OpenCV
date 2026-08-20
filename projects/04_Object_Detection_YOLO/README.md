# 04 - YOLO Object Detection

Real-time object detection using YOLO (You Only Look Once) deep learning model.

## Overview

This project implements state-of-the-art object detection using the YOLO v3/v4 model with OpenCV's DNN module.

## 🎯 Features

- ✅ Real-time object detection
- ✅ Multiple object class detection
- ✅ Confidence-based filtering
- ✅ Bounding box with labels
- ✅ Support for images and videos
- ✅ Webcam processing

## 🔧 How It Works

### YOLO Detection Pipeline

1. **Load Pre-trained Model** - YOLOv3/v4 weights and config
2. **Input Processing** - Resize to network input size
3. **Forward Pass** - Run through neural network
4. **Output Parsing** - Extract detections
5. **Post-Processing** - NMS (Non-Maximum Suppression)
6. **Visualization** - Draw boxes and labels

### Architecture

- **Backbone** - Feature extraction
- **Neck** - Multi-scale feature fusion
- **Head** - Object detection
- **80 Classes** - Common objects (COCO dataset)

## 📋 Requirements

```
Python 3.7+
OpenCV 4.5+
NumPy
Pre-trained YOLO weights (~245 MB)
```

### Download Models

```bash
# YOLOv3 weights
wget https://pjreddie.com/media/files/yolov3.weights

# Config file
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg

# Class names
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

## 🚀 Usage

```bash
# Detect objects in image
python main.py --input image.jpg --output detected.jpg

# Process video
python main.py --video video.mp4 --output output.mp4

# Webcam real-time detection
python main.py --webcam True

# Custom confidence threshold
python main.py --input image.jpg --confidence 0.5
```

## 💡 Code Example

```python
import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Prepare image
image = cv2.imread("image.jpg")
height, width, _ = image.shape

# Create blob
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0))
net.setInput(blob)

# Detect
outs = net.forward(net.getUnconnectedOutLayersNames())

# Process detections
confidences = []
boxes = []
class_ids = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            # Coordinates
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# NMS
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw boxes
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("YOLO Detection", image)
cv2.waitKey(0)
```

## 🔧 Parameters

### Detection Parameters

- **confidence** - Detection threshold (0.0-1.0)
- **nms_threshold** - Non-maximum suppression threshold
- **input_size** - Network input size (usually 416 or 608)

### Performance Trade-offs

| Parameter    | Speed     | Accuracy           |
| ------------ | --------- | ------------------ |
| Confidence ↑ | ⚡ Faster | 📉 Lower           |
| Input Size ↓ | ⚡ Faster | 📉 Lower           |
| NMS ↓        | ⚡ Faster | 📈 More detections |

## 🎯 COCO Classes

80 object classes including:

- Person, car, dog, cat
- Bicycle, motorcycle, bus
- Traffic light, stop sign
- And 70+ more...

## 📚 Related Modules

- [08_Edge_and_Feature_Detection](../../08_Edge_and_Feature_Detection/README.md) - Feature detection basics
- [09_Video_Processing](../../09_Video_Processing/README.md) - Video handling
- [11_Deep_Learning_with_OpenCV](../../11_Deep_Learning_with_OpenCV/README.md) - DNN module

## 🚀 Enhancements

- YOLOv5/v6/v7 support
- Custom dataset training
- Real-time tracking
- GPU acceleration (CUDA)
- Model optimization

## ⚡ Performance Tips

1. **Reduce Image Size** - Process smaller images faster
2. **Skip Frames** - Process every 2nd/3rd frame in video
3. **GPU Support** - Use CUDA for acceleration
4. **Smaller Model** - YOLOv3-tiny for fast inference
5. **Batch Processing** - Process multiple images together

## 🔗 Resources

- [YOLOv3 Paper](https://arxiv.org/abs/1804.02767)
- [Darknet Framework](https://pjreddie.com/darknet/)
- [COCO Dataset](https://cocodataset.org/)

---

**Status:** Ready to use  
**Complexity:** Advanced  
**Requires:** GPU recommended for real-time processing
