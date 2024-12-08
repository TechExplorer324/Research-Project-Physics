import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to calculate intensity of a pixel
def calculate_intensity(pixel):
    if len(pixel) == 4:
        r, g, b, a = pixel
    else:
        r, g, b = pixel
    return (r + g + b) / 3

# Open the image
image = Image.open('data98new2.jpg')

# Get image size
width, height = image.size

# Load pixel values
pixels = image.load()

# Initialize an empty array to store intensities
intensity_array = np.zeros((height, width))

# Iterate over each pixel
for y in range(height):
    for x in range(width):
        # Calculate intensity of the current pixel
        current_intensity = calculate_intensity(pixels[x, y])

        # Sum of intensities of the pixel and its neighbors (if within bounds)
        intensity_sum = current_intensity
        count = 1

        # Define neighboring pixels
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]

        # Iterate over neighboring pixels
        for neighbor_x, neighbor_y in neighbors:
            if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                intensity_sum += calculate_intensity(pixels[neighbor_x, neighbor_y])
                count += 1
                

        # Average intensity of the pixel and its neighbors
        average_intensity = intensity_sum / count

        # Store average intensity in the array
        intensity_array[y, x] = average_intensity

# Display the resulting intensity array
print(intensity_array)

# Save the intensity array to a text file
np.savetxt('pic98.2.txt', intensity_array, fmt='%.2f')
