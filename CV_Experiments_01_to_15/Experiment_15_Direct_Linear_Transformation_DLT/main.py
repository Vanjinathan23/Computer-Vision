from pathlib import Path
import cv2
import numpy as np

def compute_homography_dlt(src, dst):
    """Compute a 3x3 homography from at least four matching point pairs."""
    rows = []
    for (x, y), (u, v) in zip(src, dst):
        rows.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
        rows.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])
    A = np.asarray(rows, dtype=np.float64)
    _, _, vt = np.linalg.svd(A)
    H = vt[-1].reshape(3, 3)
    if abs(H[2, 2]) > 1e-12:
        H /= H[2, 2]
    return H

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
src = np.float32([[50, 40], [width - 50, 40], [width - 40, height - 40], [40, height - 40]])
dst = np.float32([[20, 20], [width - 30, 60], [width - 60, height - 20], [60, height - 60]])
H = compute_homography_dlt(src, dst)
result = cv2.warpPerspective(image, H, (width, height))
cv2.imwrite(str(ROOT / "output_dlt.png"), result)
print("DLT homography matrix:")
print(H)
cv2.imshow("Original", image)
cv2.imshow("DLT Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
