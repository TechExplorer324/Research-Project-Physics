import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

my_img = cv2.imread('data0.jpeg')

plt.imshow(my_img)
plt.show()

print(my_img.shape)

