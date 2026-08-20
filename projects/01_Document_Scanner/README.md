# 01 - Document Scanner

Automatically scan and digitize documents using computer vision techniques.

## Overview

This project demonstrates how to detect documents in images and apply perspective transformation to create a scanned version. It's useful for:

- Document digitization
- Receipt scanning
- Book page capture
- Auto-correction of skewed documents

## 🎯 Features

- ✅ Automatic document boundary detection
- ✅ Contour analysis for edge finding
- ✅ Perspective transformation for flat view
- ✅ Adjustable processing for different lighting conditions
- ✅ Output high-quality scanned document

## 🔧 How It Works

### Step-by-Step Process

1. **Image Input** - Read image from file or camera
2. **Preprocessing** - Convert to grayscale, apply blur
3. **Edge Detection** - Find document edges using Canny
4. **Contour Detection** - Identify document boundary
5. **Perspective Transform** - Flatten document to rectangular view
6. **Output** - Save or display scanned result

### Key Algorithms

- **Canny Edge Detection** - Robust edge finding
- **Contour Detection** - Boundary identification
- **Perspective Transformation** - 3D to 2D conversion
- **Morphological Operations** - Shape refinement

## 📋 Requirements

```
Python 3.7+
OpenCV 4.5+
NumPy
```

Install dependencies:

```bash
pip install -r ../../requirements.txt
```

## 🚀 Usage

### Basic Usage

```bash
python main.py --input path/to/image.jpg --output scanned.jpg
```

### Command Line Arguments

```
--input, -i     Input image path (required)
--output, -o    Output image path (default: output_scanned.jpg)
--debug, -d     Show intermediate processing steps
--threshold     Edge detection threshold (default: 100)
```

### Example

```bash
# Scan a document
python main.py -i document.jpg -o scanned_document.jpg

# With debug output
python main.py -i receipt.jpg -o receipt_scanned.jpg --debug
```

## 💡 Code Example

```python
import cv2
import numpy as np

def scan_document(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Preprocessing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get largest contour
    largest = max(contours, key=cv2.contourArea)

    # Approximate to 4 corners
    epsilon = 0.02 * cv2.arcLength(largest, True)
    corners = cv2.approxPolyDP(largest, epsilon, True)

    # Perspective transform
    if len(corners) == 4:
        h, w = image.shape[:2]
        dst = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)
        M = cv2.getPerspectiveTransform(corners.astype(np.float32), dst)
        scanned = cv2.warpPerspective(image, M, (w, h))
        return scanned

    return image

# Usage
result = scan_document("document.jpg")
cv2.imwrite("scanned.jpg", result)
```

## 🎨 Processing Stages

### Original Image

Raw input image with document at angle

### Gray & Blurred

Preprocessing for edge detection

### Edge Detection

Identified document boundaries

### Contours

Document outline detected

### Final Result

Straightened, scanned document

## 🔧 Troubleshooting

### Issue: Document Not Detected

**Solutions:**

- Improve lighting conditions
- Adjust Canny threshold values
- Ensure document has clear edges
- Try different preprocessing methods

### Issue: Incorrect Perspective

**Solutions:**

- Verify 4 corners detected correctly
- Increase edge detection thresholds
- Use better quality input image

### Issue: Distorted Output

**Solutions:**

- Check perspective transformation points
- Verify input resolution matches expectations
- Try different interpolation methods

## 📚 Related Modules

- [02_Image_Processing](../../02_Image_Processing/README.md) - Transformation techniques
- [06_Image_Thresholding](../../06_Image_Thresholding/README.md) - Binary image creation
- [08_Edge_and_Feature_Detection](../../08_Edge_and_Feature_Detection/README.md) - Edge detection
- [10_Object_Detection](../../10_Object_Detection/README.md) - Contour analysis

## 🚀 Enhancements

Potential improvements:

1. **Multi-document scanning** - Detect multiple documents
2. **Adaptive thresholding** - Better for varying lighting
3. **Rotation correction** - Auto-detect and correct rotation
4. **Image enhancement** - Post-processing to improve scanned quality
5. **Real-time processing** - Webcam-based scanning
6. **Batch processing** - Process multiple files

## 💻 Output Example

**Input:** Tilted document photo  
**Output:** Straight, scanned document ready for OCR or archival

## 📖 Additional Resources

- [Perspective Transformation](https://docs.opencv.org/master/d4/d61/tutorial_warp_affine.html)
- [Contour Detection](https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html)
- [Canny Edge Detector](https://docs.opencv.org/master/da/d22/tutorial_py_canny.html)

## 🤝 Integration

Can be integrated with:

- OCR engines (Tesseract, Google Cloud Vision)
- PDF creation libraries
- Document management systems
- Mobile scanning apps

---

**Created:** August 2026  
**Status:** Ready to use  
**Complexity:** Intermediate
