from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

blurred = cv2.GaussianBlur(image, (21, 21), 0)
cv2.imwrite(str(ROOT / "output_gaussian_blur.png"), blurred)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
