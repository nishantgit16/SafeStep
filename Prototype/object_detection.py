import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load YOLO model

def detect_objects_live():
    cap = cv2.VideoCapture(0)  # Open webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)  # Detect objects
        for result in results:
            for obj in result.boxes.data:
                x1, y1, x2, y2, conf, cls = obj
                label = result.names[int(cls)]

                if conf > 0.5:  # Confidence threshold
                    print(f"Detected: {label}")
                    cap.release()
                    return label  # Return first detected object

        cv2.imshow("SafeStep Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None
