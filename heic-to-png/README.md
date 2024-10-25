
# HEIC to PNG Converter

This Python tool automates the conversion of images from HEIC format to PNG format, allowing for seamless processing of batches of images stored in a specified input folder, with outputs saved to a designated output folder.

## Features
- Converts HEIC images to PNG format.
- Supports batch processing for converting multiple images at once.
- Ensures high-quality output suitable for e-commerce, media, and personal projects.
- Uses `pillow_heif` for Windows-compatible HEIC handling and `Pillow` for reliable image processing.

## Required Modules
- `pillow_heif`: For handling HEIC images on Windows.
- `Pillow`: For image processing and saving in PNG format.

## Installation
To install the required modules, run the following command:

```bash
pip install pillow pillow_heif
```

## Usage
1. Place your HEIC images in the designated input folder.
2. Update the input and output folder paths in the script.
3. Run the script to convert images to PNG format and save them in the output folder.
