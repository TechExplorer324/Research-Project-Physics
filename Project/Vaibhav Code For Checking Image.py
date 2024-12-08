import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def calculate_center_of_mass(image):

    y_coords, x_coords = np.mgrid[0:image.shape[0], 0:image.shape[1]]

    total_intensity = np.sum(image)

    centroid_x = np.sum(x_coords * image) / total_intensity
    centroid_y = np.sum(y_coords * image) / total_intensity

    return centroid_x, centroid_y

image = np.array([ [0, 0, 0, 0],
                   [0, 1, 1, 0],
                   [0, 1, 1, 0],
                   [0, 0, 0, 0]])

centroid_x, centroid_y = calculate_center_of_mass(image)
print(f"Center of mass: ({centroid_x}, {centroid_y})")