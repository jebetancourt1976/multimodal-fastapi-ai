from ultralytics import YOLO
import cv2
import tempfile

model = YOLO("yolov8n.pt")

def analyze(video_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(video_file.file.read())
        video_path = tmp.name

    cap = cv2.VideoCapture(video_path)
    detected_objects = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        for r in results:
            for cls in r.boxes.cls:
                detected_objects.add(model.names[int(cls)])

    cap.release()
    return {
        "objects_detected": list(detected_objects)
    }
