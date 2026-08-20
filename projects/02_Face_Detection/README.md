# 02 - Face Detection

Detect faces in images and videos using trained classifiers.

## Overview

This project demonstrates real-time face detection using Haar Cascade classifiers and modern deep learning approaches.

## 🎯 Features

- ✅ Face detection in static images
- ✅ Real-time face detection from webcam
- ✅ Face detection in video files
- ✅ Multiple face handling
- ✅ Face bounding box visualization

## 🔧 How It Works

### Haar Cascade Method

1. **Load Classifier** - Pre-trained Haar Cascade model
2. **Scale Space Analysis** - Multi-scale face detection
3. **Feature Matching** - Identify face characteristics
4. **Bounding Box** - Rectangle around detected face

### Deep Learning Alternative

Uses pre-trained models (DNN module) for:

- Better accuracy
- Fewer false positives
- Handle variations

## 📋 Requirements

```
Python 3.7+
OpenCV 4.5+
NumPy
```

## 🚀 Usage

### Basic Face Detection

```bash
python main.py --input image.jpg --output detected.jpg
```

### Webcam Detection

```bash
python main.py --webcam True
```

### Video Processing

```bash
python main.py --video path/to/video.mp4 --output output.mp4
```

## 💡 Code Example

```python
import cv2

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
```

## 🔧 Parameters

### detectMultiScale() Parameters

- **scaleFactor** - Scale reduction (1.05-1.4)
- **minNeighbors** - Detection confidence (3-10)
- **flags** - Detection algorithms
- **minSize** - Minimum face size
- **maxSize** - Maximum face size

## 📚 Related Modules

- [03_Drawing_and_Annotation](../../03_Drawing_and_Annotation/README.md) - Draw detection results
- [09_Video_Processing](../../09_Video_Processing/README.md) - Video handling
- [11_Deep_Learning_with_OpenCV](../../11_Deep_Learning_with_OpenCV/README.md) - Advanced detection

## 🚀 Enhancements

- Facial landmark detection
- Face recognition
- Emotion detection
- Age estimation
- Face alignment

---

**Status:** Ready to use  
**Complexity:** Beginner to Intermediate
