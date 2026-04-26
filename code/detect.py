
from ultralytics import YOLO
import cv2
import torch

print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

model = YOLO("yolov8n.pt")
model.to("cuda")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, device=0)
    annotated = results[0].plot()

    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
