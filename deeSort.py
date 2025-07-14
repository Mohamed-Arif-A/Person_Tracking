from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=60)

# Start webcam
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("video.mp4")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Detect objects using YOLO
    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = box.conf[0].item()
        cls = int(box.cls[0].item())
        label = model.names[cls]

        if label == "person" and conf > 0.5:
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf, label))

    # Step 2: Track using DeepSORT
    tracks = tracker.update_tracks(detections, frame=frame)

    # Step 3: Draw bounding boxes with IDs
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()  # left, top, right, bottom
        x1, y1, x2, y2 = map(int, ltrb)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("YOLO + DeepSORT", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()