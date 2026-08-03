import cv2

# Open webcam
cap = cv2.VideoCapture(r".\videos\race_car.mp4")

while True:
    # 'ret' is a boolean (True if frame read successfully), 'frame' is the image array
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # Apply image processing here (e.g., converting to grayscale)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", frame)
    # cv2.imshow("Capturing Webcam", gray) # for grayscale

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
