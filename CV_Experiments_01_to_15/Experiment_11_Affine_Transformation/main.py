from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
source = np.float32([[50, 50], [width - 50, 50], [50, height - 50]])
destination = np.float32([[80, 80], [width - 100, 60], [100, height - 80]])
matrix = cv2.getAffineTransform(source, destination)
transformed = cv2.warpAffine(image, matrix, (width, height))
cv2.imwrite(str(ROOT / "output_affine.png"), transformed)
cv2.imshow("Original", image)
cv2.imshow("Affine Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
