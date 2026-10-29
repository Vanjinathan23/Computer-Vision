from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
video_path = ROOT.parent / "sample_video.mp4"
cap = cv2.VideoCapture(str(video_path))
if not cap.isOpened():
    raise FileNotFoundError(f"Could not open video: {video_path}")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
source = np.float32([[80, 50], [width - 80, 50], [width - 30, height - 50], [30, height - 50]])
destination = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
matrix = cv2.getPerspectiveTransform(source, destination)

while True:
    ok, frame = cap.read()
    if not ok:
        break
    transformed = cv2.warpPerspective(frame, matrix, (width, height))
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
