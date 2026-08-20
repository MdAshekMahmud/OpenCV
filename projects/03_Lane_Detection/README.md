# 03 - Lane Detection

Detect road lanes in driving scenarios for autonomous vehicle applications.

## Overview

This project detects lane markings in road images and videos using computer vision techniques.

## 🎯 Features

- ✅ Lane boundary detection
- ✅ Lane line visualization
- ✅ Video processing support
- ✅ Configurable detection parameters
- ✅ Real-time processing

## 🔧 How It Works

### Processing Pipeline

1. **Preprocessing** - Convert to grayscale, apply blur
2. **Edge Detection** - Canny edge detection
3. **ROI Selection** - Focus on road area
4. **Hough Transform** - Detect lines
5. **Line Filtering** - Select lane lines
6. **Visualization** - Draw detected lanes

### Key Algorithms

- **Canny Edge Detection** - Find lane boundaries
- **Hough Line Transform** - Detect straight lines
- **ROI Masking** - Focus processing area
- **Line Fitting** - Refine lane boundaries

## 📋 Requirements

```
Python 3.7+
OpenCV 4.5+
NumPy
```

## 🚀 Usage

```bash
# Detect lanes in image
python main.py --input road_image.jpg --output lanes_detected.jpg

# Process video
python main.py --video road_video.mp4 --output lanes_video.mp4

# Webcam real-time
python main.py --webcam True
```

## 💡 Code Example

```python
import cv2
import numpy as np

def detect_lanes(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Define ROI (region of interest)
    height, width = image.shape[:2]
    roi = np.zeros_like(edges)
    pts = np.array([[[0, height],
                     [width//2, height//2],
                     [width, height]]], np.int32)
    cv2.fillPoly(roi, pts, 255)
    masked_edges = cv2.bitwise_and(edges, roi)

    # Hough line transform
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 50,
                            minLineLength=50, maxLineGap=20)

    # Draw lines
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image
```

## 🔧 Parameters

### Hough Transform

- **Rho** - Distance resolution (pixels)
- **Theta** - Angle resolution (radians)
- **Threshold** - Detection threshold
- **minLineLength** - Minimum line length
- **maxLineGap** - Maximum gap tolerance

## 📚 Related Modules

- [08_Edge_and_Feature_Detection](../../08_Edge_and_Feature_Detection/README.md) - Edge detection
- [09_Video_Processing](../../09_Video_Processing/README.md) - Video handling
- [10_Object_Detection](../../10_Object_Detection/README.md) - Contour analysis

## 🚀 Enhancements

- Curved lane detection
- Multi-lane detection
- Lane departure warnings
- Real-time dashboard overlay
- Machine learning-based detection

---

**Status:** Ready to use  
**Complexity:** Intermediate
