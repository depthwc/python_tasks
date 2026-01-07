import numpy as np
from PIL import Image

# Task 1: Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
celsius_vectorized = np.vectorize(fahrenheit_to_celsius)
print("Celsius:", celsius_vectorized(temps_f))

# Task 2: Custom power function
def raise_to_power(x, y):
    return x ** y

base = np.array([2, 3, 4, 5])
power = np.array([1, 2, 3, 4])
power_vectorized = np.vectorize(raise_to_power)
print("Powers:", power_vectorized(base, power))

# Task 3: Solve system of equations
A1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b1 = np.array([7, 4, 5])
solution1 = np.linalg.solve(A1, b1)
print("x, y, z:", solution1)

# Task 4: Electrical circuit equations
A2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
b2 = np.array([12, -5, 15])
solution2 = np.linalg.solve(A2, b2)
print("I1, I2, I3:", solution2)

# Image Manipulation
def flip_image(img_array):
    return np.flipud(np.fliplr(img_array))

def add_noise(img_array):
    noise = np.random.randint(0, 50, img_array.shape, dtype='uint8')
    return np.clip(img_array + noise, 0, 255)

def brighten_channels(img_array, value=40):
    return np.clip(img_array + value, 0, 255)

def apply_mask(img_array):
    h, w = img_array.shape[:2]
    start_h, start_w = h//2 - 50, w//2 - 50
    img_array[start_h:start_h+100, start_w:start_w+100] = [0, 0, 0]
    return img_array

# Load and manipulate image
img = Image.open("images/birds.jpg")
img_array = np.array(img)

flipped = flip_image(img_array)
noised = add_noise(flipped)
brightened = brighten_channels(noised)
masked = apply_mask(brightened)

# Save final result
Image.fromarray(masked.astype('uint8')).save("images/birds_modified.jpg")
    