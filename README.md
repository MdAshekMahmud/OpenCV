# OpenCV Learning Journey

A comprehensive collection of Computer Vision tutorials, examples, and projects using OpenCV and Python. This repository is structured as a progressive learning path from fundamentals to advanced applications.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Topics & Modules](#topics--modules)
- [Projects](#projects)
- [Tech Stack](#tech-stack)
- [Learning Path](#learning-path)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Resources](#resources)

## 🚀 Quick Start

```bash
# Clone or navigate to the repository
cd OpenCV

# Install dependencies
pip install -r requirements.txt

# Run a basic example
python 01_Basics/01_read_image.py
```

## 📁 Repository Structure

```
OpenCV/
├── 01_Basics/                          # Fundamental OpenCV operations
├── 02_Image_Processing/                # Image manipulation techniques
├── 03_Drawing_and_Annotation/          # Drawing shapes and text
├── 04_Color_Spaces/                    # Color space conversions
├── 05_Image_Enhancement/               # Image quality improvement
├── 06_Image_Thresholding/              # Binary image creation
├── 07_Morphological_Operations/        # Image shape manipulation
├── 08_Edge_and_Feature_Detection/      # Edge and corner detection
├── 09_Video_Processing/                # Video file and webcam handling
├── 10_Object_Detection/                # Object detection techniques
├── 11_Deep_Learning_with_OpenCV/       # DNN module and YOLO
├── projects/                           # Real-world application projects
├── notebooks/                          # Jupyter notebooks for experimentation
├── images/                             # Sample images for testing
│   ├── input/                          # Input images
│   └── output/                         # Output images
├── videos/                             # Sample videos for testing
└── requirements.txt                    # Python dependencies
```

## 📚 Topics & Modules

### Core Learning Modules

| #   | Topic                        | Description                                                               | Files     |
| --- | ---------------------------- | ------------------------------------------------------------------------- | --------- |
| 01  | **Image Basics**             | Read, display, save, and analyze images                                   | 5 scripts |
| 02  | **Image Processing**         | Resize, crop, rotate, flip, and transform images                          | 6 scripts |
| 03  | **Drawing & Annotation**     | Draw shapes, text, and handle mouse events                                | 5 scripts |
| 04  | **Color Spaces**             | Convert and work with different color models (BGR, RGB, HSV)              | 4 scripts |
| 05  | **Image Enhancement**        | Improve image quality with brightness, contrast, blurring, and sharpening | 7 scripts |
| 06  | **Image Thresholding**       | Create binary images using various threshold methods                      | 8 scripts |
| 07  | **Morphological Operations** | Apply erosion, dilation, opening, closing                                 | 7 scripts |
| 08  | **Edge & Feature Detection** | Detect edges and corners (Sobel, Laplacian, Canny, Harris)                | 5 scripts |
| 09  | **Video Processing**         | Capture, process, and save video streams                                  | 5 scripts |
| 10  | **Object Detection**         | Detect and track objects using contours                                   | 2 scripts |
| 11  | **Deep Learning**            | Use DNN module for AI-powered detection                                   | 3 scripts |

### See individual module READMEs for detailed documentation:

- [01_Basics](./01_Basics/README.md)
- [02_Image_Processing](./02_Image_Processing/README.md)
- [03_Drawing_and_Annotation](./03_Drawing_and_Annotation/README.md)
- [04_Color_Spaces](./04_Color_Spaces/README.md)
- [05_Image_Enhancement](./05_Image_Enhancement/README.md)
- [06_Image_Thresholding](./06_Image_Thresholding/README.md)
- [07_Morphological_Operations](./07_Morphological_Operations/README.md)
- [08_Edge_and_Feature_Detection](./08_Edge_and_Feature_Detection/README.md)
- [09_Video_Processing](./09_Video_Processing/README.md)
- [10_Object_Detection](./10_Object_Detection/README.md)
- [11_Deep_Learning_with_OpenCV](./11_Deep_Learning_with_OpenCV/README.md)

## 🎯 Projects

Real-world applications demonstrating complete workflows:

| Project                   | Description                                                           | Key Concepts                                            | Location                                                                 |
| ------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Document Scanner**      | Scan documents using contour detection and perspective transformation | Contours, Perspective Transform, Image Processing       | [projects/01_Document_Scanner](./projects/01_Document_Scanner)           |
| **Face Detection**        | Detect faces in images and videos using Haar Cascade classifiers      | Cascade Classifiers, Face Detection, Video Processing   | [projects/02_Face_Detection](./projects/02_Face_Detection)               |
| **Lane Detection**        | Detect road lanes in driving videos                                   | Canny Edge Detection, Hough Transform, Video Processing | [projects/03_Lane_Detection](./projects/03_Lane_Detection)               |
| **YOLO Object Detection** | Real-time object detection using YOLO deep learning model             | YOLO, DNN Module, Real-time Detection                   | [projects/04_Object_Detection_YOLO](./projects/04_Object_Detection_YOLO) |

## 🛠 Tech Stack

| Technology           | Purpose                     |
| -------------------- | --------------------------- |
| **Python 3.x**       | Programming language        |
| **OpenCV (cv2)**     | Computer Vision library     |
| **NumPy**            | Numerical computing         |
| **Matplotlib**       | Data visualization          |
| **Jupyter Notebook** | Interactive experimentation |

## 📖 Learning Path

### Beginner Level ✅

1. Start with [01_Basics](./01_Basics/README.md) - Understand image fundamentals
2. Progress to [02_Image_Processing](./02_Image_Processing/README.md) - Learn transformation techniques
3. Explore [03_Drawing_and_Annotation](./03_Drawing_and_Annotation/README.md) - Create visual content

### Intermediate Level ⏳

4. Study [04_Color_Spaces](./04_Color_Spaces/README.md) - Master color models
5. Learn [05_Image_Enhancement](./05_Image_Enhancement/README.md) - Improve image quality
6. Practice [06_Image_Thresholding](./06_Image_Thresholding/README.md) - Binary image techniques

### Advanced Level 🚀

7. Implement [07_Morphological_Operations](./07_Morphological_Operations/README.md) - Shape analysis
8. Explore [08_Edge_and_Feature_Detection](./08_Edge_and_Feature_Detection/README.md) - Feature extraction
9. Work with [09_Video_Processing](./09_Video_Processing/README.md) - Video analysis

### Expert Level 🔬

10. Master [10_Object_Detection](./10_Object_Detection/README.md) - Detect and track objects
11. Dive into [11_Deep_Learning_with_OpenCV](./11_Deep_Learning_with_OpenCV/README.md) - AI-powered vision

## ⚙️ Prerequisites

- **Python 3.7+** - [Download](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Basic Python knowledge** - Variables, functions, loops
- **Webcam (optional)** - For video processing examples

## 📦 Installation

### 1. Clone or Download Repository

```bash
# If cloning from git
git clone <repository-url>
cd OpenCV

# Or navigate to your OpenCV folder
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import cv2; print(f'OpenCV version: {cv2.__version__}')"
```

## 💻 Usage

### Running Individual Scripts

```bash
# Navigate to any module and run scripts
python 01_Basics/01_read_image.py
python 02_Image_Processing/01_resize.py
python 09_Video_Processing/03_webcam.py
```

### Running Jupyter Notebooks

```bash
# Start Jupyter
jupyter notebook

# Navigate to notebooks/ folder and open any .ipynb file
```

### Running Projects

```bash
# Navigate to project folder
cd projects/01_Document_Scanner
python main.py
```

## 📚 Resources

### Official Documentation

- [OpenCV Documentation](https://docs.opencv.org/)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [NumPy Documentation](https://numpy.org/doc/)

### Learning Resources

- [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [Computer Vision Basics](https://en.wikipedia.org/wiki/Computer_vision)
- [Image Processing Fundamentals](https://en.wikipedia.org/wiki/Digital_image_processing)

### Community

- [OpenCV Q&A Forum](https://answers.opencv.org/)
- [Stack Overflow - OpenCV Tag](https://stackoverflow.com/questions/tagged/opencv)

## 🚀 Progress Tracking

| Module                        | Status         | Completion |
| ----------------------------- | -------------- | ---------- |
| 01 - Image Basics             | ✅ Completed   | 100%       |
| 02 - Image Processing         | ✅ Completed   | 100%       |
| 03 - Drawing & Annotation     | ✅ Completed   | 100%       |
| 04 - Color Spaces             | ✅ Completed   | 100%       |
| 05 - Image Enhancement        | ✅ Completed   | 100%       |
| 06 - Image Thresholding       | ✅ Completed   | 100%       |
| 07 - Morphological Operations | ✅ Completed   | 100%       |
| 08 - Edge & Feature Detection | ✅ Completed   | 100%       |
| 09 - Video Processing         | ✅ Completed   | 100%       |
| 10 - Object Detection         | ⏳ In Progress | 40%        |
| 11 - Deep Learning            | ⏳ In Progress | 30%        |
| Projects                      | ⏳ In Progress | 50%        |

## 📝 Notes

- Ensure sample images are present in `images/input/` before running examples
- Some scripts require webcam access - allow permissions when prompted
- Adjust file paths in scripts if running from different directories
- Use virtual environment to avoid package conflicts

## 🤝 Contributing

To add more examples or improve documentation:

1. Follow the existing folder structure and naming conventions
2. Add clear comments explaining the code
3. Update relevant README files with new content
4. Test scripts before submitting

## 📄 License

This repository is created for educational purposes.

---

**Last Updated:** August 2026  
**Python Version:** 3.7+  
**OpenCV Version:** 4.x
