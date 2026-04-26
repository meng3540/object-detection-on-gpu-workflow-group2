from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

# FORCE CPU
model.to("cpu")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # FORCE CPU inference
    results = model(frame, device="cpu")

    annotated = results[0].plot()

    cv2.imshow("CPU Detection", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
