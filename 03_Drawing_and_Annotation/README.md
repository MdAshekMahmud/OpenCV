# 03 - Drawing and Annotation

Learn to create visual elements and handle user interactions.

## Overview

This module covers techniques for drawing shapes, adding text, and handling user input events:

- Drawing lines, rectangles, and circles
- Adding text annotations to images
- Responding to mouse events
- Creating interactive applications

## 📚 Topics

### 1. Drawing Lines (`01_line.py`)

Create line segments on images.

**Key Concepts:**

- `cv2.line()` function
- Starting and ending points
- Color specification (BGR format)
- Line thickness
- Line types (solid, dashed)

**Use Cases:**

- Connect points
- Create wireframes
- Draw trajectories

### 2. Drawing Rectangles (`02_rectangle.py`)

Draw rectangular shapes on images.

**Key Concepts:**

- `cv2.rectangle()` function
- Top-left and bottom-right corners
- Fill vs outline rectangles
- Thickness parameter

**Use Cases:**

- Mark regions of interest
- Draw bounding boxes
- Highlight objects

### 3. Drawing Circles (`03_circle.py`)

Create circular shapes on images.

**Key Concepts:**

- `cv2.circle()` function
- Center point and radius
- Fill circles
- Outline circles

**Use Cases:**

- Mark point locations
- Highlight features
- Create visual markers

### 4. Adding Text (`04_put_text.py`)

Place text labels on images.

**Key Concepts:**

- `cv2.putText()` function
- Font selection
- Text size and thickness
- Position coordinates
- Text color

**Supported Fonts:**

- `cv2.FONT_HERSHEY_SIMPLEX`
- `cv2.FONT_HERSHEY_COMPLEX`
- `cv2.FONT_ITALIC`

**Use Cases:**

- Label objects
- Add annotations
- Display information

### 5. Mouse Events (`05_mouse_events.py`)

Handle mouse interactions with images.

**Key Concepts:**

- `cv2.setMouseCallback()` function
- Mouse event types
- Event coordinates
- Interactive drawing

**Mouse Events:**

- `cv2.EVENT_MOUSEMOVE` - Mouse movement
- `cv2.EVENT_LBUTTONDOWN` - Left button press
- `cv2.EVENT_LBUTTONUP` - Left button release
- `cv2.EVENT_RBUTTONDOWN` - Right button press
- `cv2.EVENT_MOUSEWHEEL` - Scroll wheel

**Use Cases:**

- Interactive drawing applications
- Point selection
- Region selection

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- ✅ Draw lines, rectangles, and circles
- ✅ Add text to images
- ✅ Use different colors and styles
- ✅ Handle mouse events
- ✅ Create interactive applications
- ✅ Annotate results

## 💡 Quick Examples

### Drawing a Line

```python
import cv2

image = cv2.imread("image.jpg")

# Draw line from (100, 100) to (200, 200)
cv2.line(image, (100, 100), (200, 200), (0, 255, 0), 2)

cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Drawing a Rectangle

```python
import cv2

image = cv2.imread("image.jpg")

# Draw filled rectangle
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), -1)

# Draw rectangle outline
cv2.rectangle(image, (200, 50), (300, 150), (0, 255, 0), 2)

cv2.imshow("Rectangles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Drawing a Circle

```python
import cv2

image = cv2.imread("image.jpg")

# Draw filled circle
cv2.circle(image, (200, 200), 50, (0, 0, 255), -1)

# Draw circle outline
cv2.circle(image, (300, 200), 50, (255, 255, 0), 2)

cv2.imshow("Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Adding Text

```python
import cv2

image = cv2.imread("image.jpg")

# Add text
text = "OpenCV Text"
font = cv2.FONT_HERSHEY_SIMPLEX
position = (50, 50)
font_scale = 1
color = (255, 255, 255)  # White
thickness = 2

cv2.putText(image, text, position, font, font_scale, color, thickness)

cv2.imshow("Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Mouse Event Handling

```python
import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")

image = cv2.imread("image.jpg").copy()
cv2.imshow("Mouse Events", image)
cv2.setMouseCallback("Mouse Events", mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 🎨 Color Format

OpenCV uses BGR (Blue, Green, Red) format for colors:

```python
# BGR color format (not RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)
```

## 📋 Shape Parameters

| Shape     | Function          | Parameters                                          |
| --------- | ----------------- | --------------------------------------------------- |
| Line      | `cv2.line()`      | image, pt1, pt2, color, thickness                   |
| Rectangle | `cv2.rectangle()` | image, pt1, pt2, color, thickness (-1 for fill)     |
| Circle    | `cv2.circle()`    | image, center, radius, color, thickness             |
| Text      | `cv2.putText()`   | image, text, org, font, fontScale, color, thickness |

## 🔧 Common Issues & Solutions

| Issue                        | Solution                                      |
| ---------------------------- | --------------------------------------------- |
| Text appears too small/large | Adjust `fontScale` parameter                  |
| Colors appear wrong          | Remember OpenCV uses BGR, not RGB             |
| Mouse events not working     | Ensure window is active; call `cv2.waitKey()` |
| Text is cut off              | Adjust text position; use `cv2.getTextSize()` |
| Shapes not visible           | Check if coordinates are within image bounds  |

## 📋 File Descriptions

| File                 | Purpose                             |
| -------------------- | ----------------------------------- |
| `01_line.py`         | Demonstrate line drawing            |
| `02_rectangle.py`    | Draw rectangles with various styles |
| `03_circle.py`       | Draw circles and filled shapes      |
| `04_put_text.py`     | Add text annotations                |
| `05_mouse_events.py` | Handle user mouse interactions      |

## 🚀 Advanced Techniques

### Ellipses

```python
cv2.ellipse(image, (200, 200), (100, 50), 0, 0, 360, (0, 255, 0), 2)
```

### Polygons

```python
pts = [[10, 5], [20, 30], [70, 20], [50, 10]]
pts = np.array(pts, np.int32)
cv2.polylines(image, [pts], True, (0, 255, 0), 2)
```

### Filled Polygons

```python
pts = [[10, 5], [20, 30], [70, 20], [50, 10]]
pts = np.array(pts, np.int32)
cv2.fillPoly(image, [pts], (0, 255, 0))
```

## 🚀 Next Steps

After mastering drawing and annotation:

1. Move to [04_Color_Spaces](../04_Color_Spaces/README.md) to work with colors
2. Explore [05_Image_Enhancement](../05_Image_Enhancement/README.md) for quality improvements

## 📖 Additional Resources

- [OpenCV Drawing Functions](https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html)
- [Mouse Events Tutorial](https://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling_zh.html)

## 💻 Running the Scripts

```bash
# From the repository root
python 03_Drawing_and_Annotation/01_line.py
python 03_Drawing_and_Annotation/05_mouse_events.py
# ... and so on
```

**Prerequisites:**

- OpenCV installed
- Python 3.7+
- Understanding from Module 01-02
- Sample images (optional for some examples)
