from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
source = np.float32([[50, 40], [width - 50, 40], [width - 40, height - 40], [40, height - 40]])
destination = np.float32([[20, 20], [width - 30, 60], [width - 60, height - 20], [60, height - 60]])
homography, _ = cv2.findHomography(source, destination)
transformed = cv2.warpPerspective(image, homography, (width, height))
cv2.imwrite(str(ROOT / "output_homography.png"), transformed)
cv2.imshow("Original", image)
cv2.imshow("Homography Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
