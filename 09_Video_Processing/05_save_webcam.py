import cv2

# Initialize webcam (0 is usually the default built-in camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get default frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# Use 'mp4v' for .mp4 files or 'XVID' for .avi files
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    filename=r".\videos\web_output.mp4",
    fourcc=fourcc,
    fps=20.0,
    frameSize=(frame_width, frame_height),
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame.")
        break

    # Write the captured frame
    out.write(frame)

    # Display the resulting frame
    cv2.imshow("Webcam Recording", frame)

    # Press 'q' to exit the loop and stop recording
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything when job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
