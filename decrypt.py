from PIL import Image
import numpy as np
import hashlib

# Function to generate control points based on a key
def generate_control_points(key):
    # Hash the key to obtain a consistent set of control points
    hash_obj = hashlib.sha256(key.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Convert the hash into a list of integers
    control_points = [int(hash_hex[i:i+2], 16) for i in range(0, len(hash_hex), 2)]
    
    return control_points

# Define a Bezier curve decryption function
def bezier_decrypt(encrypted_img, control_points):
    width, height, _ = encrypted_img.shape
    decrypted_img = np.zeros((width, height, 3), dtype=np.uint8)

    for channel in range(3):
        for x in range(width):
            for y in range(height):
                control_point = control_points[channel % len(control_points)]
                decrypted_value = (encrypted_img[x, y, channel] - control_point) % 256
                decrypted_img[x, y, channel] = decrypted_value

    return decrypted_img

# Get the encryption key from the user (replace with your key input mechanism)
encryption_key = input("Enter your encryption key: ")

# Generate control points based on the key
control_points = generate_control_points(encryption_key)

# Load the encrypted image
encrypted_image = Image.open('temp.png')

# Convert the image to a NumPy array
encrypted_img_array = np.array(encrypted_image)

# Decrypt the encrypted image
decrypted_img = bezier_decrypt(encrypted_img_array, control_points)

# Save the decrypted image
decrypted_image = Image.fromarray(decrypted_img)
decrypted_image.save('decrypted_image.png')

print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")
