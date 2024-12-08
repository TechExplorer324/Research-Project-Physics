import numpy as np
from PIL import Image

# Function to calculate intensity of a pixel
def calculate_intensity(pixel):
    if len(pixel) == 4:
        r, g, b, a = pixel
    else:
        r, g, b = pixel
    return (r + g + b) / 3

# Open the image
image = Image.open('data_sum_of_all.jpeg')

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

        # Sum of intensities of the pixel and its 4 neighbors (if within bounds)
        intensity_sum = current_intensity
        count = 1

        # Top neighbor
        if y > 0:
            intensity_sum += calculate_intensity(pixels[x, y - 1])

        
            
            count += 1

        # Bottom neighbor
        if y < height - 1:
            intensity_sum += calculate_intensity(pixels[x, y + 1])
            count += 1

        # Left neighbor
        if x > 0:
            intensity_sum += calculate_intensity(pixels[x - 1, y])
            count += 1

        # Right neighbor
        if x < width - 1:
            intensity_sum += calculate_intensity(pixels[x + 1, y])
            count += 1

        # Average intensity of the pixel and its neighbors
        average_intensity = intensity_sum / count

        # Store average intensity in the array
        intensity_array[y, x] = average_intensity

# Display the resulting intensity array
print(intensity_array)

np.savetxt('intensity_array_data_sum_of_all.txt', intensity_array, fmt='%.2f')

