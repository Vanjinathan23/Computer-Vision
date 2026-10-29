from pathlib import Path
import cv2
import time

ROOT = Path(__file__).resolve().parent
video_path = ROOT.parent / "sample_video.mp4"
if not video_path.exists():
    raise FileNotFoundError(f"Place a video named sample_video.mp4 at: {video_path}")

cap = cv2.VideoCapture(str(video_path))
if not cap.isOpened():
    raise RuntimeError(f"Could not open video: {video_path}")

fps = cap.get(cv2.CAP_PROP_FPS) or 20
mode = "slow"  # Change to "fast" to play fast motion
delay_ms = int(1000 / fps * (2 if mode == "slow" else 0.5))

while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow(f"Video ({mode} motion)", frame)
    if cv2.waitKey(max(1, delay_ms)) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Tip: set mode = 'slow' or mode = 'fast' and run again.")
