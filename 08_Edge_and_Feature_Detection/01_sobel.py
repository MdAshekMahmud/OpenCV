import time
import cv2
import numpy as np

# Setup Configuration Variables
VIDEO_PATH = r".\videos\race_car.mp4"
OUTPUT_PATH = r".\videos\edge_output.mp4"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480


# Create a Resize Helper Function
def resize_frame(frame, width, height):
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def to_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# Apply CLAHE Local Contrast Enhancement
def apply_clahe(gray):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray)


# Apply Edge-Preserving Bilateral Smoothing
def bilateral_smooth(gray):
    return cv2.bilateralFilter(gray, 9, 75, 75)


# Perform Dynamic Canny Edge Detection
def dynamic_canny(smooth):
    sigma = np.std(smooth)
    lower = max(20, int(0.66 * sigma))
    upper = min(200, int(1.33 * sigma))
    return cv2.Canny(smooth, lower, upper)


# Extract Sobel and Laplacian Gradients
def sobel_gradient(gray):
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    return cv2.convertScaleAbs(np.sqrt(sx**2 + sy**2))


def laplacian_edge(gray):
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return cv2.convertScaleAbs(lap)


# Fuse Multiple Edge Maps
def fuse_edges(canny, lap, sobel):
    fused = cv2.addWeighted(canny, 0.6, lap, 0.3, 0)
    return cv2.addWeighted(fused, 0.7, sobel, 0.3, 0)


# Apply Morphological Closing
def morphology_close(fused):
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(fused, cv2.MORPH_CLOSE, kernel)


# Apply Temporal Smoothing Across Frames
prev_fused = None


def temporal_smooth(fused):
    global prev_fused
    if prev_fused is None:
        prev_fused = fused.copy()
    fused = cv2.addWeighted(fused, 0.7, prev_fused, 0.3, 0)
    prev_fused = fused.copy()
    return fused


# Overlay Detected Edges on Original Frame
def overlay_edges(frame, fused):
    overlay = frame.copy()
    overlay[fused > 40] = [0, 0, 255]
    return overlay


# Combine All Stages into process_frame()
def process_frame(frame):
    gray = to_grayscale(frame)
    clahe_gray = apply_clahe(gray)
    smooth = bilateral_smooth(clahe_gray)
    canny = dynamic_canny(smooth)
    lap = laplacian_edge(smooth)
    sobel = sobel_gradient(smooth)
    fused = fuse_edges(canny, lap, sobel)
    fused = morphology_close(fused)
    fused = temporal_smooth(fused)
    output = overlay_edges(frame, fused)
    return output


# Open Video Stream and Create Writer
cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or np.isnan(fps):
    fps = 30

# FIXED: Use VideoWriter_fourcc instead of VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (FRAME_WIDTH, FRAME_HEIGHT))

# Frame Processing Loop
prev_time = time.time()
frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Finished processing video.")
        break

    frame = resize_frame(frame, FRAME_WIDTH, FRAME_HEIGHT)
    output = process_frame(frame)
    out.write(output)

    frame_counter += 1
    curr_time = time.time()

    if curr_time - prev_time >= 1.0:
        fps_live = frame_counter / (curr_time - prev_time)
        print(f"Live FPS: {fps_live:.2f}")
        prev_time = curr_time
        frame_counter = 0

# Cleanup Resources and Save Output
cap.release()
out.release()
print(f"Video saved at: {OUTPUT_PATH}")
