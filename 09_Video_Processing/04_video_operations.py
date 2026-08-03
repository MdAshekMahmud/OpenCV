import cv2

# Open webcam
cap = cv2.VideoCapture(r".\videos\race_car.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # Resize
    frame = cv2.resize(frame, (640, 480))

    # Flip horizontally
    frame = cv2.flip(frame, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original", frame)
    cv2.imshow("Gray", gray)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
