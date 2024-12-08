# Function to calculate intensity of a pixel

#!/usr/bin/env python3.11
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
image = Image.open('data98.jpeg')

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
np.savetxt('pic2.2.txt', intensity_array, fmt='%.2f')

#!/usr/bin/env python3.11
import numpy as np
from PIL import Image, ImageDraw

# Load intensity array from the saved text file
intensity_array = np.loadtxt('/Users/vaibhavdivakar/Desktop/research project/pic2.2.txt')

# Create a mask for points with intensity greater than 0
mask = intensity_array > 40

# Get the coordinates of points with intensity greater than 0
points = np.argwhere(mask)

# Open the original image
image = Image.open('/Users/vaibhavdivakar/Desktop/research project/pics/data2.jpeg')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define a function to check if the intensity of the center pixel is greater than the average intensity of the surrounding pixels
def check_intensity(center, window):
    avg_intensity = np.mean(window)
    return center > avg_intensity

# Define a function to calculate the distance between two points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Draw red circles around points with intensity greater than surrounding pixels
if len(points) > 0:
    drawn_centers = []  # List to store the centers of the drawn circles
    for point in points:
        y, x = point
        y_start, y_end = max(y-1, 0), min(y+2, intensity_array.shape[0])  # Avoid out of bounds
        x_start, x_end = max(x-1, 0), min(x+2, intensity_array.shape[1])  # Avoid out of bounds
        window = intensity_array[y_start:y_end, x_start:x_end]  # Get the intensity values of the surrounding pixels
        if window.size > 0:  # Check if window is not empty
            center_intensity = window[1, 1]  # Get the intensity of the center pixel
            if check_intensity(center_intensity, window):
                current_center = (x, y)
                # Check if the current center is at least 5 pixels away from any previously drawn centers
                if all(distance(current_center, center) >= 15 for center in drawn_centers):
                    draw.ellipse((x-7, y-7, x+7, y+7), outline='red')
                    drawn_centers.append(current_center)

# Save the modified image
image.save('marked_image.png')

# Open the modified image using the default image viewer
image.show()
