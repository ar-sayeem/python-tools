import os
import cv2
import numpy as np
from PIL import Image
 
def center_and_resize(image_path, output_path, target_size=(300, 400)):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
 
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Use a simple thresholding method to create a binary image
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
 
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
    # If contours are found, proceed
    if contours:
        # Get the largest contour (assumed to be the main subject)
        largest_contour = max(contours, key=cv2.contourArea)
 
        # Get bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
 
        # Crop the image to the bounding box
        cropped_image = image[y:y+h, x:x+w]
 
        # Calculate the aspect ratio of the cropped image
        crop_height, crop_width = cropped_image.shape[:2]
        crop_aspect_ratio = crop_width / crop_height
 
        # Calculate new dimensions to maintain 3:4 aspect ratio
        if crop_aspect_ratio < (3/4):  # Wider than 3:4
            new_height = target_size[1]
            new_width = int(new_height * (3 / 4))
        else:  # Taller than or equal to 3:4
            new_width = target_size[0]
            new_height = int(new_width * (4 / 3))
 
        # Resize the cropped image to the new dimensions
        resized_image = cv2.resize(cropped_image, (new_width, new_height))
 
        # Create a blank 3:4 image and place the resized image in the center
        final_image = np.zeros((target_size[1], target_size[0], 3), dtype=np.uint8)
        start_x = (target_size[0] - new_width) // 2
        start_y = (target_size[1] - new_height) // 2
        final_image[start_y:start_y+new_height, start_x:start_x+new_width] = resized_image
 
        # Save the output image using Pillow
        output_image = Image.fromarray(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
        output_image.save(output_path)
    else:
        # If no contours are found, save a blank image of the target size
        blank_image = np.zeros((target_size[1], target_size[0], 3), dtype=np.uint8)
        output_image = Image.fromarray(blank_image)
        output_image.save(output_path)
 
def process_images(input_folder, output_folder, target_size=(300, 400)):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
 
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            center_and_resize(input_image_path, output_image_path, target_size)
            print(f'Processed: {filename}')
 
# Define input and output folder paths
input_folder = r'path\input_folder'  # Replace with your actual input folder path
output_folder = r'path\output_folder'  # Replace with your desired output folder path
 
# Run the process
process_images(input_folder, output_folder, target_size=(300, 400))  # Set the output size to 3:4
