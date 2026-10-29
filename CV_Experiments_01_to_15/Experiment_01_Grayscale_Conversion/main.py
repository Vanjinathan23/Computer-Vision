from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"

image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(ROOT / "output_grayscale.png"), gray)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
