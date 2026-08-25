from pathlib import Path

import cv2
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

# Path to YOLO files
WEIGHTS_PATH = str(MODELS_DIR / "yolov3.weights")
CONFIG_PATH = str(MODELS_DIR / "yolov3.cfg")
NAMES_PATH = str(MODELS_DIR / "coco.names")

# Confidence threshold and NMS threshold
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4


def load_yolo():
    for file_path in (WEIGHTS_PATH, CONFIG_PATH, NAMES_PATH):
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Missing YOLO model file: {file_path}")

    with open(NAMES_PATH, "r") as f:
        classes = [line.strip() for line in f if line.strip()]

    net = cv2.dnn.readNetFromDarknet(CONFIG_PATH, WEIGHTS_PATH)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    return net, classes


def detect_objects(frame, net, classes):
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(
        frame,
        1 / 255.0,
        (416, 416),
        swapRB=True,
        crop=False,
    )
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_layers = [
        layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()
    ]
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > CONFIDENCE_THRESHOLD:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)

    if len(indices) == 0:
        return frame

    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        conf = confidences[i]

        color = (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(
            frame,
            f"{label} {conf:.2f}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2,
        )

    return frame


def main():
    net, classes = load_yolo()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_objects(frame, net, classes)
        cv2.imshow("YOLO Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
