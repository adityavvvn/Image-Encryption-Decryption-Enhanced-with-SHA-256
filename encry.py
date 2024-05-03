import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the encrypted image
encrypted_image = Image.open('encrypted_image.png')
encrypted_img_array = np.array(encrypted_image)

# Create a histogram for each color channel (R, G, B)
for channel in range(3):
    channel_values = encrypted_img_array[:, :, channel]
    
    plt.figure()
    plt.hist(channel_values.flatten(), bins=256, range=(0, 256), color=f'C{channel}', alpha=0.7, label=f'Channel {channel}')

plt.title('Histogram of Encrypted Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()
