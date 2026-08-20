# 01 - Image Basics

Learn fundamental OpenCV operations for working with images.

## Overview

This module covers the essential skills for image handling in OpenCV:

- Reading images from files
- Displaying images on screen
- Saving images to disk
- Accessing and analyzing image properties
- Understanding image matrices and pixel values

## 📚 Topics

### 1. Reading Images (`01_read_image.py`)

Learn how to load images from file paths and store them as NumPy arrays.

**Key Concepts:**

- `cv2.imread()` function
- Image path handling
- Image data structure

**Use Cases:**

- Load photos for processing
- Access image data

### 2. Image Properties (`02_image_properties.py`)

Understand the structure and characteristics of images.

**Key Concepts:**

- Image shape (height, width, channels)
- Image data type
- Color channels
- Image size in bytes

**Use Cases:**

- Validate image dimensions
- Check image format
- Memory usage calculation

### 3. Image Matrix (`03_image_matrix.py`)

Access and manipulate individual pixel values and regions.

**Key Concepts:**

- NumPy array indexing
- Pixel access patterns
- Region of Interest (ROI)
- Array slicing

**Use Cases:**

- Modify specific pixels
- Extract image regions
- Analyze pixel values

### 4. Display Images (`04_display_image.py`)

Show images in windows for visualization.

**Key Concepts:**

- `cv2.imshow()` function
- `cv2.waitKey()` for user input
- `cv2.destroyAllWindows()` cleanup
- Window management

**Use Cases:**

- Preview images
- Debugging visual output
- Interactive displays

### 5. Save Images (`05_save_image.py`)

Store processed images to disk.

**Key Concepts:**

- `cv2.imwrite()` function
- File format selection
- Quality/compression settings
- Path management

**Use Cases:**

- Export results
- Save processed images
- Create image sequences

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- ✅ Read images from various file formats
- ✅ Access image properties (size, channels, type)
- ✅ Navigate image matrices and access pixels
- ✅ Display images in windows
- ✅ Save images in different formats
- ✅ Handle image file paths correctly

## 💡 Quick Examples

### Reading an Image

```python
import cv2

# Read image
image = cv2.imread("path/to/image.jpg")

# Check if image was loaded
if image is None:
    print("Error loading image")
else:
    print("Image loaded successfully")
```

### Displaying an Image

```python
import cv2

image = cv2.imread("image.jpg")
cv2.imshow("My Image", image)
cv2.waitKey(0)  # Wait for key press
cv2.destroyAllWindows()
```

### Saving an Image

```python
import cv2

image = cv2.imread("image.jpg")
# Save image
cv2.imwrite("output.jpg", image)
```

### Accessing Image Properties

```python
import cv2

image = cv2.imread("image.jpg")
height, width, channels = image.shape
print(f"Height: {height}, Width: {width}, Channels: {channels}")
```

## 🔧 Common Issues & Solutions

| Issue                               | Solution                                                         |
| ----------------------------------- | ---------------------------------------------------------------- |
| "NoneType has no attribute 'shape'" | Image path is incorrect or file doesn't exist. Verify file path. |
| Image display is too small/large    | Use `cv2.resize()` or adjust window size                         |
| Incorrect color display             | OpenCV uses BGR format, not RGB. Convert if needed.              |
| Cannot save image                   | Check write permissions in output directory                      |

## 📋 File Descriptions

| File                     | Purpose                              |
| ------------------------ | ------------------------------------ |
| `01_read_image.py`       | Demonstrate image loading            |
| `02_image_properties.py` | Show image dimensions and attributes |
| `03_image_matrix.py`     | Access individual pixels and regions |
| `04_display_image.py`    | Display images in windows            |
| `05_save_image.py`       | Save images to disk                  |

## 🚀 Next Steps

After mastering the basics:

1. Move to [02_Image_Processing](../02_Image_Processing/README.md) to learn transformation techniques
2. Explore [03_Drawing_and_Annotation](../03_Drawing_and_Annotation/README.md) to create visual content

## 📖 Additional Resources

- [OpenCV imread Documentation](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html)
- [NumPy Array Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)
- [Image File Formats](https://en.wikipedia.org/wiki/Image_file_format)

## 💻 Running the Scripts

```bash
# From the repository root
python 01_Basics/01_read_image.py
python 01_Basics/02_image_properties.py
# ... and so on
```

**Prerequisites:**

- OpenCV installed
- Python 3.7+
- Sample image files in `images/input/` directory
