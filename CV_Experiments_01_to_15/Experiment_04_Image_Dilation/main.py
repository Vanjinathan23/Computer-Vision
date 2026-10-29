from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

_, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(binary, kernel, iterations=1)
cv2.imwrite(str(ROOT / "output_dilation.png"), dilated)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
