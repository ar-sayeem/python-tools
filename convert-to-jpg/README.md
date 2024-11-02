
# Any Image to JPG Converter

This Python tool converts images of various formats (e.g., PNG, BMP, TIFF, GIF) to JPG format in batch. Simply place your images in an input folder, and the tool will process and save the converted JPG images in a specified output folder. This tool uses the `Pillow` library for efficient image processing and format conversion.

## Features
- **Batch Processing**: Converts multiple images of various formats (PNG, BMP, TIFF, GIF) to JPG in a single run.
- **Customizable Folders**: Allows you to specify both the input folder for source images and the output folder for converted JPG images.
- **Image Quality**: Ensures quality is maintained during the conversion with the powerful `Pillow` library.

## Required Modules
- **Pillow** (Python Imaging Library)

## Installation
Make sure you have Python installed, then install the required `Pillow` library:

```bash
pip install pillow
```

## Usage

1. **Prepare Folders**: Place the images you want to convert in the input folder and specify an output folder for the converted JPG images.
2. **Run the Code**: Use the following code structure to start the conversion process:

   ```python
   import os
   from PIL import Image

   def convert_to_jpg(input_folder, output_folder):
       # Create output folder if it doesn't exist
       if not os.path.exists(output_folder):
           os.makedirs(output_folder)

       # Loop through all files in the input folder
       for filename in os.listdir(input_folder):
           # Check if the file is an image
           if filename.lower().endswith(('.png', '.bmp', '.tiff', '.gif', '.jpeg', '.jpg')):
               # Construct the full file path
               img_path = os.path.join(input_folder, filename)
               # Open the image and convert it to JPG format
               img = Image.open(img_path).convert('RGB')
               # Save the converted image to the output folder
               jpg_filename = os.path.splitext(filename)[0] + '.jpg'
               img.save(os.path.join(output_folder, jpg_filename), 'JPEG')
               print(f"Converted {filename} to {jpg_filename}")

   # Example usage
   input_folder = r'path/to/your/input_folder'      # Replace with your input folder path
   output_folder = r'path/to/your/output_folder'    # Replace with your output folder path
   convert_to_jpg(input_folder, output_folder)
   ```

3. **Check Output**: The converted JPG images will be saved in the specified output folder.

---

Happy converting!
