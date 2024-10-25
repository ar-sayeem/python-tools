import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(input_folder, output_folder):
    # Register HEIF format with Pillow
    pillow_heif.register_heif_opener()

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Open HEIC file and convert to PNG
            with Image.open(heic_path) as image:
                image.save(png_path, "PNG")
                print(f"Converted: {filename} to {png_filename}")

# Define the input and output folder paths
input_folder = r"F:\python-tools\heic-to-png\folder_in"
output_folder = r"F:\python-tools\heic-to-png\folder_out"


# Run the conversion
convert_heic_to_png(input_folder, output_folder)
