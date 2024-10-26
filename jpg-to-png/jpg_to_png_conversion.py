import os
from PIL import Image

def convert_jpg_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            # Construct the full file path
            img_path = os.path.join(input_folder, filename)
            # Open the image and convert it to PNG format
            img = Image.open(img_path).convert('RGB')
            # Save the converted image to the output folder
            png_filename = os.path.splitext(filename)[0] + '.png'
            img.save(os.path.join(output_folder, png_filename), 'PNG')
            print(f"Converted {filename} to {png_filename}")

# Example usage
input_folder = 'F:\python-tools\jpg-to-png\input_folder'        # Replace with your actual input folder path
output_folder = 'F:\python-tools\jpg-to-png\output_folder'      # Replace with your actual input folder path
convert_jpg_to_png(input_folder, output_folder)
