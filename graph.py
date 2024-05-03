import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the image
image = Image.open('2.jpg')  # Replace 'your_image.jpg' with your image file

# Convert the image to a NumPy array
img_array = np.array(image)

# Separate the RGB channels
red_channel = img_array[:, :, 0]
green_channel = img_array[:, :, 1]
blue_channel = img_array[:, :, 2]

# Create histograms for each channel
plt.figure(figsize=(12, 4))

# Red channel histogram
plt.subplot(131)
plt.hist(red_channel.ravel(), bins=256, color='red', alpha=0.5)
plt.xlabel('Red Intensity')
plt.ylabel('Frequency')
plt.title('Red Channel')

# Green channel histogram
plt.subplot(132)
plt.hist(green_channel.ravel(), bins=256, color='green', alpha=0.5)
plt.xlabel('Green Intensity')
plt.ylabel('Frequency')
plt.title('Green Channel')

# Blue channel histogram
plt.subplot(133)
plt.hist(blue_channel.ravel(), bins=256, color='blue', alpha=0.5)
plt.xlabel('Blue Intensity')
plt.ylabel('Frequency')
plt.title('Blue Channel')

plt.tight_layout()
plt.show()
