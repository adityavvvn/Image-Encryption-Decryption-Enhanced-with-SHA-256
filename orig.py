import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the original image (not the encrypted image)
original_image = Image.open('1.jpg')
original_img_array = np.array(original_image)

# Create a histogram for each color channel (R, G, B)
for channel in range(3):
    channel_values = original_img_array[:, :, channel]
    
    plt.figure()
    plt.hist(channel_values.flatten(), bins=256, range=(0, 256), color=f'C{channel}', alpha=0.7, label=f'Channel {channel}')

plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()
