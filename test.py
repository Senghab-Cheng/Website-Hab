from PIL import Image
import numpy as np

# Load the image
img_path = ''
img = Image.open(img_path)

# Convert image to grayscale
img_gray = img.convert('L')

# Convert grayscale image to binary (threshold = 128)
img_binary = img_gray.point(lambda x: 0 if x < 128 else 255, '1')

# Convert the binary image to a numpy array and display the array
binary_array = np.array(img_binary)
binary_array
