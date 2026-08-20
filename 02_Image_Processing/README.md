# 02 - Image Processing

Master geometric transformations and image manipulation techniques.

## Overview

This module covers essential image processing operations for resizing, transforming, and manipulating images:

- Resizing images to different dimensions
- Cropping regions of interest
- Rotating images at various angles
- Flipping images horizontally and vertically
- Translating images across space
- Applying affine and perspective transformations

## 📚 Topics

### 1. Resizing Images (`01_resize.py`)

Change image dimensions while preserving or modifying aspect ratio.

**Key Concepts:**

- `cv2.resize()` function
- Interpolation methods
- Aspect ratio preservation
- Output dimensions

**Methods:**

- `cv2.INTER_LINEAR` - Linear interpolation (default)
- `cv2.INTER_AREA` - Area-based (best for shrinking)
- `cv2.INTER_CUBIC` - Cubic interpolation (slower but better quality)
- `cv2.INTER_NEAREST` - Nearest neighbor (fast)

**Use Cases:**

- Prepare images for model input
- Reduce image size for storage
- Standardize image dimensions

### 2. Cropping Images (`02_crop.py`)

Extract regions of interest from larger images.

**Key Concepts:**

- Array slicing in OpenCV
- Region of Interest (ROI)
- Coordinate systems
- Cropping syntax: `image[y1:y2, x1:x2]`

**Use Cases:**

- Focus on specific areas
- Remove unwanted parts
- Create image patches

### 3. Rotating Images (`03_rotate.py`)

Rotate images around a center point by specified angles.

**Key Concepts:**

- `cv2.getRotationMatrix2D()` function
- `cv2.warpAffine()` transformation
- Rotation matrices
- Center point and angle parameters

**Use Cases:**

- Correct image orientation
- Data augmentation
- Align objects

### 4. Flipping Images (`04_flip.py`)

Mirror images horizontally, vertically, or both ways.

**Key Concepts:**

- `cv2.flip()` function
- Flip codes:
  - `0` = Vertical flip (along x-axis)
  - `1` = Horizontal flip (along y-axis)
  - `-1` = Both directions

**Use Cases:**

- Create symmetric effects
- Data augmentation
- Mirror images

### 5. Image Translation (`05_translation.py`)

Move images across the image plane.

**Key Concepts:**

- `cv2.warpAffine()` function
- Translation matrices
- X and Y displacement values
- Border handling

**Use Cases:**

- Shift image position
- Data augmentation
- Align images

### 6. Affine Transformation (`06_affine_transformation.py`)

Apply linear transformations preserving parallel lines.

**Key Concepts:**

- `cv2.getAffineTransform()` function
- `cv2.warpAffine()` application
- Transformation matrices
- Source and destination points
- 2x3 transformation matrix

**Use Cases:**

- Apply custom linear transformations
- Correct image skew
- Advanced geometric corrections

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- ✅ Resize images with various interpolation methods
- ✅ Crop specific regions from images
- ✅ Rotate images by arbitrary angles
- ✅ Flip images in different directions
- ✅ Translate images across the plane
- ✅ Apply affine transformations
- ✅ Understand transformation matrices
- ✅ Handle image boundaries during transformations

## 💡 Quick Examples

### Resizing an Image

```python
import cv2

image = cv2.imread("image.jpg")

# Resize to specific dimensions
resized = cv2.resize(image, (300, 400))

# Resize by scale factor
resized = cv2.resize(image, None, fx=0.5, fy=0.5)

# Resize with interpolation
resized = cv2.resize(image, (300, 400), interpolation=cv2.INTER_CUBIC)
```

### Cropping an Image

```python
import cv2

image = cv2.imread("image.jpg")

# Crop region [y1:y2, x1:x2]
cropped = image[50:200, 100:300]
```

### Rotating an Image

```python
import cv2

image = cv2.imread("image.jpg")
height, width = image.shape[:2]
center = (width // 2, height // 2)

# Create rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle=45, scale=1.0)

# Apply rotation
rotated = cv2.warpAffine(image, rotation_matrix, (width, height))
```

### Flipping an Image

```python
import cv2

image = cv2.imread("image.jpg")

# Horizontal flip
flipped_h = cv2.flip(image, 1)

# Vertical flip
flipped_v = cv2.flip(image, 0)

# Both directions
flipped_both = cv2.flip(image, -1)
```

## 🔧 Common Issues & Solutions

| Issue                           | Solution                                                |
| ------------------------------- | ------------------------------------------------------- |
| Resized image looks blurry      | Use better interpolation: `cv2.INTER_CUBIC`             |
| Rotated image has black corners | Image size increases with rotation. Adjust output size. |
| Cropped region is all black     | Check coordinate order (y before x) and array bounds    |
| Transformed image is cut off    | Increase output image dimensions                        |

## 📋 File Descriptions

| File                          | Purpose                                 |
| ----------------------------- | --------------------------------------- |
| `01_resize.py`                | Demonstrate various resizing techniques |
| `02_crop.py`                  | Extract specific image regions          |
| `03_rotate.py`                | Rotate images at different angles       |
| `04_flip.py`                  | Flip images in different directions     |
| `05_translation.py`           | Translate images across the plane       |
| `06_affine_transformation.py` | Apply affine transformations            |

## 🎨 Interpolation Methods Comparison

| Method           | Speed     | Quality   | Best For               |
| ---------------- | --------- | --------- | ---------------------- |
| `INTER_NEAREST`  | ⚡⚡⚡    | Low       | Real-time applications |
| `INTER_LINEAR`   | ⚡⚡      | Medium    | General use            |
| `INTER_AREA`     | ⚡⚡      | High      | Shrinking images       |
| `INTER_CUBIC`    | ⚡        | High      | Enlarging images       |
| `INTER_LANCZOS4` | Very Slow | Very High | Professional output    |

## 🚀 Next Steps

After mastering image processing:

1. Move to [03_Drawing_and_Annotation](../03_Drawing_and_Annotation/README.md) to add visual elements
2. Explore [05_Image_Enhancement](../05_Image_Enhancement/README.md) to improve image quality

## 📖 Additional Resources

- [OpenCV Geometric Transformations](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html)
- [Affine Transformations Tutorial](https://docs.opencv.org/master/d4/d61/tutorial_warp_affine.html)
- [Perspective Transformations](https://docs.opencv.org/master/d4/d61/tutorial_warp_affine.html)

## 💻 Running the Scripts

```bash
# From the repository root
python 02_Image_Processing/01_resize.py
python 02_Image_Processing/02_crop.py
# ... and so on
```

**Prerequisites:**

- OpenCV installed
- Python 3.7+
- Understanding of basic image concepts from Module 01
- Sample images in `images/input/` directory
