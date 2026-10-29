from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent
image_path = ROOT.parent / "sample_image.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

height, width = image.shape[:2]
center = (width // 2, height // 2)
clockwise_matrix = cv2.getRotationMatrix2D(center, -30, 1.0)
counterclockwise_matrix = cv2.getRotationMatrix2D(center, 30, 1.0)
clockwise = cv2.warpAffine(image, clockwise_matrix, (width, height))
counterclockwise = cv2.warpAffine(image, counterclockwise_matrix, (width, height))
cv2.imwrite(str(ROOT / "output_clockwise.png"), clockwise)
cv2.imwrite(str(ROOT / "output_counterclockwise.png"), counterclockwise)
cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counterclockwise", counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
