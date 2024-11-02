# 3:4 Aspect Ratio Image Resizer

This Python tool resizes images to a specified 3:4 aspect ratio by detecting and centering the main subject within the image, then resizing and padding to fit the target dimensions. Place your images in an input folder, and the tool will process them to create standardized 3:4 aspect ratio images in the output folder.

## Features
- **Automatic Subject Detection**: Uses contour detection to identify and crop the main subject.
- **Batch Processing**: Processes multiple images at once, automatically resizing each image to the desired 3:4 aspect ratio.
- **Customizable Output Size**: Set your desired target dimensions (default is 300x400 pixels).
- **Flexible Input Formats**: Supports common image formats like PNG, JPG, and JPEG.

## Required Modules
- **OpenCV** (`cv2`) for image processing and contour detection
- **Pillow** (`PIL`) for saving the processed images in the desired format
- **NumPy** (`numpy`) for efficient array manipulation

## Installation
Make sure you have Python installed, then install the required libraries:

```bash
pip install opencv-python pillow numpy
