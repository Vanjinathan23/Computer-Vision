from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent
# Set to 0 for the default webcam. Change delay_factor to 2 for slow
# playback or 0.5 for fast playback.
camera_index = 0
delay_factor = 1.0

cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    raise RuntimeError("Could not open webcam. Check camera permissions.")

while True:
    ok, frame = cap.read()
    if not ok:
        print("Could not read a frame from the webcam.")
        break
    cv2.imshow("Webcam - press q to quit", frame)
    if cv2.waitKey(max(1, int(30 * delay_factor))) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
