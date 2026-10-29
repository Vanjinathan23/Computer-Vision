# Computer Vision Lab — Experiments 01–15

This package contains one folder per experiment. Each folder includes `main.py` and a short README. Image-based experiments include example output images generated from the included sample image.

## Contents
- Experiment_01–05: grayscale, Gaussian blur, Canny, dilation, erosion
- Experiment_06–07: video slow/fast playback and webcam capture
- Experiment_08–12: scaling, rotation, translation, affine and perspective transformations
- Experiment_13: perspective transformation on video
- Experiment_14: homography transformation
- Experiment_15: Direct Linear Transformation (DLT)

## Setup
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install packages:
   `pip install -r requirements.txt`
4. Run an experiment:
   `python Experiment_01_Grayscale_Conversion/main.py`

## Notes
- A sample image and sample video are included in the root directory.
- Webcam access requires a connected camera and permission from your operating system.
- The saved output PNGs are example outputs. Run the code to regenerate them.
- Video and webcam experiments display windows rather than saving a still image, so no output image is included for those experiments.
- Press `q` to exit video loops.
