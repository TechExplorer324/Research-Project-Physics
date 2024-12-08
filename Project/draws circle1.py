import numpy as np
from PIL import Image, ImageDraw

# Load intensity array from the saved text file
intensity_array = np.loadtxt('pic98.2.txt')

# Create a mask for points with intensity greater than 12
mask = intensity_array > 30

# Get the coordinates of points with intensity greater than 12
points = np.argwhere(mask)

# Open the original image
image = Image.open('data98new2.jpg')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw red circles around points with intensity greater than 12
for point in points:
    draw.ellipse((point[1]-1, point[0]-1, point[1]+1, point[0]+1), outline='red')

# Save the modified image
image.save('marked_image.png')

# Open the modified image using the default image viewer
image.show()
image2 = Image.open('marked_image.png')
