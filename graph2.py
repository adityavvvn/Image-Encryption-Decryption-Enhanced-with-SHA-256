import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the image
image = Image.open('medical.jpg')  # Replace with the path to your image

# Convert the image to a NumPy array
img_array = np.array(image)

# Calculate the color distribution by channel
hist_red = np.histogram(img_array[:, :, 0], bins=256, range=(0, 256))
hist_green = np.histogram(img_array[:, :, 1], bins=256, range=(0, 256))
hist_blue = np.histogram(img_array[:, :, 2], bins=256, range=(0, 256))

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Plot the histograms for each channel
ax.plot(hist_red[1][:-1], hist_red[0], color='red', label='Red', alpha=0.7)
ax.plot(hist_green[1][:-1], hist_green[0], color='green', label='Green', alpha=0.7)
ax.plot(hist_blue[1][:-1], hist_blue[0], color='blue', label='Blue', alpha=0.7)

# Set labels and title
ax.set_xlabel('Color Value')
ax.set_ylabel('Frequency')
ax.set_title('Color Distribution Histogram')

# Add a legend
ax.legend()

# Show the plot
plt.show()
