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
input_folder = r'F:\python-tools\convert-to-jpg\input_folder'        # Replace with your actual input folder path
output_folder = r'F:\python-tools\convert-to-jpg\output_folder'      # Replace with your actual output folder path
convert_to_jpg(input_folder, output_folder)
