# 06 - Image Thresholding

Master binary image creation and segmentation techniques.

## Overview

This module covers converting grayscale images to binary (black and white) images:

- Simple binary thresholding
- Adaptive thresholding
- Otsu's method
- Various threshold techniques
- Image segmentation

## 📚 Topics

### 1. Binary Threshold (`01_binary_threshold.py`)

Convert images to black and white with a fixed threshold.

**Key Concepts:**

- Fixed threshold value
- Binary conversion
- `cv2.threshold()` function
- Threshold selection

**Use Cases:**

- Simple binarization
- Quick segmentation
- Preprocessing

### 2. Binary Inverse (`02_binary_inv.py`)

Invert binary image values (black ↔ white).

**Key Concepts:**

- `cv2.THRESH_BINARY_INV` mode
- Inverted thresholding
- Value inversion

**Use Cases:**

- Switch foreground/background
- Correct inverted images

### 3. Truncated Threshold (`03_truncated_thresh.py`)

Truncate pixel values above threshold.

**Key Concepts:**

- `cv2.THRESH_TRUNC` mode
- Value clipping
- Partial binarization

**Use Cases:**

- Cap maximum values
- Brightness limiting

### 4. To Zero Threshold (`04_to_zero_thresh.py`)

Set values below threshold to zero.

**Key Concepts:**

- `cv2.THRESH_TOZERO` mode
- Value suppression
- Zero masking

**Use Cases:**

- Remove dark areas
- Suppress background

### 5. To Zero Inverted (`05_to_zero_inverted.py`)

Set values above threshold to zero.

**Key Concepts:**

- `cv2.THRESH_TOZERO_INV` mode
- Inverse suppression

**Use Cases:**

- Remove bright areas
- Isolate dark regions

### 6. Adaptive Threshold (`06_adaptive_threshold.py`)

Threshold based on local neighborhood.

**Key Concepts:**

- `cv2.adaptiveThreshold()` function
- Local vs global thresholding
- Adaptive methods
- Better for varying lighting

**Methods:**

- Mean - Average of neighborhood
- Gaussian - Weighted average

**Use Cases:**

- Uneven lighting
- Variable backgrounds
- Better edge preservation

### 7. Otsu's Method (`07_otsu_threshold.py`)

Automatic optimal threshold calculation.

**Key Concepts:**

- `cv2.THRESH_OTSU` flag
- Automatic threshold selection
- Histogram analysis
- Bimodal distribution

**Use Cases:**

- Unknown optimal threshold
- Automatic binarization
- Robust segmentation

### 8. Image Segmentation with Morphology (`08_image_seg_morph.py`)

Combine thresholding with morphological operations.

**Key Concepts:**

- Threshold + morphology
- Contour cleanup
- Shape refinement
- Connected components

**Use Cases:**

- Object isolation
- Noise removal
- Shape analysis

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- ✅ Apply simple binary thresholding
- ✅ Use different threshold modes
- ✅ Implement adaptive thresholding
- ✅ Apply Otsu's method
- ✅ Combine thresholding with morphology
- ✅ Choose appropriate threshold method
- ✅ Segment images into regions

## 💡 Quick Examples

### Simple Binary Threshold

```python
import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Apply threshold (pixels > 127 become white, rest black)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", binary)
```

### Binary Inverse

```python
import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Invert binary result
_, binary_inv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Inverted", binary_inv)
```

### Adaptive Threshold

```python
import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Adaptive thresholding
adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Adaptive", adaptive)
```

### Otsu's Method

```python
import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Otsu's method
_, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Otsu", otsu)
```

### Thresholding + Morphology

```python
import cv2
import numpy as np

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Threshold
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Morphological operations to clean up
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
cleaned = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Cleaned", cleaned)
```

## 📊 Threshold Method Comparison

| Method     | Speed  | Best For          | Automatic |
| ---------- | ------ | ----------------- | --------- |
| BINARY     | ⚡⚡⚡ | Simple objects    | ❌        |
| BINARY_INV | ⚡⚡⚡ | Inverted objects  | ❌        |
| TRUNC      | ⚡⚡⚡ | Value capping     | ❌        |
| TOZERO     | ⚡⚡⚡ | Suppression       | ❌        |
| ADAPTIVE   | ⚡⚡   | Variable lighting | ✅        |
| OTSU       | ⚡⚡   | Unknown threshold | ✅        |

## 🔧 Common Issues & Solutions

| Issue                             | Solution                         |
| --------------------------------- | -------------------------------- |
| Threshold loses important details | Use adaptive threshold           |
| Binary too dark/light             | Adjust threshold value           |
| Morphology makes image worse      | Reduce kernel size               |
| Otsu's fails with poor contrast   | Use histogram equalization first |

## 📋 File Descriptions

| File                       | Purpose                      |
| -------------------------- | ---------------------------- |
| `01_binary_threshold.py`   | Simple binary thresholding   |
| `02_binary_inv.py`         | Inverted threshold           |
| `03_truncated_thresh.py`   | Truncate mode                |
| `04_to_zero_thresh.py`     | To zero mode                 |
| `05_to_zero_inverted.py`   | To zero inverted mode        |
| `06_adaptive_threshold.py` | Local adaptive thresholding  |
| `07_otsu_threshold.py`     | Automatic Otsu's method      |
| `08_image_seg_morph.py`    | Segmentation with morphology |

## 🎨 Threshold Selection Guide

```
┌─ Image has uniform background?
│  ├─ YES → Use BINARY or OTSU
│  └─ NO  → Use ADAPTIVE
│
└─ Object darker or lighter than background?
   ├─ Darker → BINARY (foreground black)
   ├─ Lighter → BINARY_INV (foreground white)
   └─ Uncertain → OTSU (automatic)
```

## 🚀 Next Steps

After mastering thresholding:

1. Move to [07_Morphological_Operations](../07_Morphological_Operations/README.md) for shape refinement
2. Explore [08_Edge_and_Feature_Detection](../08_Edge_and_Feature_Detection/README.md) for feature extraction

## 📖 Additional Resources

- [OpenCV Thresholding](https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html)
- [Otsu's Method](https://en.wikipedia.org/wiki/Otsu%27s_method)
- [Image Segmentation](https://en.wikipedia.org/wiki/Image_segmentation)

## 💻 Running the Scripts

```bash
# From the repository root
python 06_Image_Thresholding/01_binary_threshold.py
python 06_Image_Thresholding/07_otsu_threshold.py
# ... and so on
```

**Prerequisites:**

- OpenCV installed
- Python 3.7+
- Understanding from Module 01-05
- Sample images in `images/input/` directory
