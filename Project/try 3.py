import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

i = 1

image = Image.open('data98.jpeg')

width, height = image.size
pixels = image.load()

has_alpha = len(pixels[0,0]) == 4

fill = 1
array = [[fill for x in range(width)] for y in range(height)]

for y in range(height):
    for x in range( width):
        if has_alpha:
            r, g, b, a = pixels[x,y]
        else:
            r, g, b = pixels[x,y]
        lum = ((r+g+b)/3) 
        array[y][x] = lum/255 # Map values from range 0-255 to 0-1
        

def get_intensity(pixel):
    if len(pixel) == 4:
        r, g, b, a = pixel
    else:
        r, g, b = pixel
    return (r + g + b) / 3
# print(image)
# print(array)

intensity_array = np.zeros((height,width))



    
        
    
