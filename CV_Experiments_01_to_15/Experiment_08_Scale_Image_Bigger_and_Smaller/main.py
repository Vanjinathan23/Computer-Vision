from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

bigger = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imwrite(str(ROOT / "output_bigger.png"), bigger)
cv2.imwrite(str(ROOT / "output_smaller.png"), smaller)
cv2.imshow("Original", image)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
