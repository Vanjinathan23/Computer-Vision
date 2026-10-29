from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
tx, ty = 80, 40
matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(image, matrix, (width, height))
cv2.imwrite(str(ROOT / "output_translated.png"), translated)
cv2.imshow("Original", image)
cv2.imshow("Translated", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
