from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
source = np.float32([[80, 60], [width - 80, 60], [width - 50, height - 60], [50, height - 60]])
destination = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
matrix = cv2.getPerspectiveTransform(source, destination)
transformed = cv2.warpPerspective(image, matrix, (width, height))
cv2.imwrite(str(ROOT / "output_perspective.png"), transformed)
cv2.imshow("Original", image)
cv2.imshow("Perspective Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
