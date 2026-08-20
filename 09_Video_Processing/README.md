# 09 - Video Processing

Master video capture, processing, and storage techniques.

## Overview

This module covers working with video files and webcam streams:

- Capture video from files and webcams
- Process video frame-by-frame
- Save processed video to disk
- Real-time video analysis

## 📚 Topics

### 1. Video Capture (`01_video_capture.py`)

Read and process frames from video files.

**Key Concepts:**

- `cv2.VideoCapture()` class
- Video properties (FPS, resolution, codec)
- Frame-by-frame iteration
- Release resources

**Video Properties:**

- `cv2.CAP_PROP_FRAME_WIDTH` - Frame width
- `cv2.CAP_PROP_FRAME_HEIGHT` - Frame height
- `cv2.CAP_PROP_FPS` - Frames per second
- `cv2.CAP_PROP_FRAME_COUNT` - Total frames

**Use Cases:**

- Video analysis
- Extract frames
- Video preprocessing

### 2. Save Video (`02_save_video.py`)

Write processed frames to video files.

**Key Concepts:**

- `cv2.VideoWriter()` class
- Video codec selection (MP4V, MJPEG, etc.)
- Frame rate and resolution
- Writing frames sequentially

**Codecs:**

- `cv2.VideoWriter_fourcc(*'mp4v')` - MP4 format
- `cv2.VideoWriter_fourcc(*'MJPG')` - Motion JPEG
- `cv2.VideoWriter_fourcc(*'XVID')` - XVID format
- `cv2.VideoWriter_fourcc(*'WMV1')` - Windows Media

**Use Cases:**

- Save processed video
- Create video outputs
- Export results

### 3. Webcam Processing (`03_webcam.py`)

Real-time processing from webcam.

**Key Concepts:**

- Camera index (0, 1, 2, etc.)
- Real-time frame processing
- Live preview
- Recording webcam

**Camera Indices:**

- `0` - Default/primary camera
- `1` - Secondary camera (if available)
- `-1` - Auto-detect camera

**Use Cases:**

- Live video analysis
- Real-time object detection
- Interactive applications

### 4. Video Operations (`04_video_operations.py`)

Apply transformations to video frames.

**Key Concepts:**

- Resize frames
- Apply filters to video
- Frame annotation
- Performance optimization

**Use Cases:**

- Video stabilization
- Quality enhancement
- Feature extraction

### 5. Save Webcam (`05_save_webcam.py`)

Record and save webcam stream.

**Key Concepts:**

- Continuous frame capture
- Real-time saving
- File management
- Memory efficiency

**Use Cases:**

- Video recording
- Surveillance
- Activity logging

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- ✅ Read video files frame-by-frame
- ✅ Extract video properties
- ✅ Process each frame
- ✅ Write frames to output video
- ✅ Capture from webcam
- ✅ Apply real-time processing
- ✅ Save video recordings
- ✅ Handle video formats

## 💡 Quick Examples

### Reading Video Frames

```python
import cv2

# Open video file
video = cv2.VideoCapture("video.mp4")

# Get video properties
fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"FPS: {fps}, Resolution: {width}x{height}")

# Read frames
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Process frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display frame
    cv2.imshow("Video", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```

### Saving Video

```python
import cv2

# Define video properties
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
frame_size = (640, 480)

# Create VideoWriter object
output = cv2.VideoWriter("output.mp4", fourcc, fps, frame_size)

# Assume we're reading frames from somewhere
for frame in frames:
    output.write(frame)

output.release()
```

### Webcam Capture

```python
import cv2

# Open default camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display frame
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Real-time Processing

```python
import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply Canny edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Display result
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Recording Webcam

```python
import cv2

cap = cv2.VideoCapture(0)

# Get camera properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("webcam_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)
    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```

## 📊 Video Codec Comparison

| Codec  | Format | Quality   | Speed  | File Size |
| ------ | ------ | --------- | ------ | --------- |
| `mp4v` | MP4    | High      | Medium | Small     |
| `MJPG` | AVI    | Medium    | Fast   | Large     |
| `XVID` | AVI    | High      | Medium | Medium    |
| `H264` | MP4    | Very High | Slow   | Small     |

## 🔧 Common Issues & Solutions

| Issue                    | Solution                                                |
| ------------------------ | ------------------------------------------------------- |
| Webcam not recognized    | Check device ID (0, 1, 2); check permissions            |
| Video codec not found    | Install codec; try different fourcc code                |
| Video plays but is slow  | Reduce frame size; skip frames; optimize processing     |
| Audio not included       | OpenCV doesn't handle audio; use ffmpeg post-processing |
| Permission denied saving | Check output directory permissions                      |

## 📋 File Descriptions

| File                     | Purpose                         |
| ------------------------ | ------------------------------- |
| `01_video_capture.py`    | Read and process video files    |
| `02_save_video.py`       | Write processed frames to video |
| `03_webcam.py`           | Capture from webcam             |
| `04_video_operations.py` | Apply transformations to video  |
| `05_save_webcam.py`      | Record webcam stream            |

## ⚙️ Performance Tips

1. **Reduce Resolution:** Process smaller frames faster
2. **Skip Frames:** Process every nth frame for speed
3. **GPU Acceleration:** Use CUDA for processing
4. **Threading:** Process in separate thread
5. **Codec Selection:** Choose fast codec for real-time

```python
# Example: Skip frames
frame_count = 0
skip_frames = 2

while True:
    ret, frame = cap.read()
    frame_count += 1

    if frame_count % skip_frames != 0:
        continue

    # Process this frame
    processed = apply_processing(frame)
```

## 🚀 Next Steps

After mastering video processing:

1. Move to [10_Object_Detection](../10_Object_Detection/README.md) for object tracking
2. Explore [11_Deep_Learning_with_OpenCV](../11_Deep_Learning_with_OpenCV/README.md) for AI-powered analysis

## 📖 Additional Resources

- [OpenCV Video I/O](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html)
- [Video Codecs Reference](https://en.wikipedia.org/wiki/Video_codec)
- [FourCC Codes](https://fourcc.org/)

## 💻 Running the Scripts

```bash
# From the repository root
python 09_Video_Processing/01_video_capture.py
python 09_Video_Processing/03_webcam.py
# ... and so on
```

**Prerequisites:**

- OpenCV installed
- Python 3.7+
- Webcam (for webcam examples)
- Video files in `videos/` directory
- Understanding from previous modules
