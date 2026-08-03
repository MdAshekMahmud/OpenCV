import cv2

# Read input video
cap = cv2.VideoCapture(r".\videos\race_car.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(r".\videos\output.avi", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    out.write(frame)
    cv2.imshow("Saving Video", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        print("Quitting...")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
