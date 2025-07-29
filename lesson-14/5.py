from PIL import Image
import numpy as np
import random

# Load image
img = Image.open("images/birds.jpg")
img_np = np.array(img)

def flip_image(image):
    flipped_h = np.flip(image, axis=1)  # Horizontal
    flipped_v = np.flip(flipped_h, axis=0)  # Then vertical
    return flipped_v

def add_noise(image):
    noise = np.random.randint(0, 50, image.shape, dtype='uint8')
    noisy_img = np.clip(image + noise, 0, 255)
    return noisy_img

def brighten_channels(image, value=40):
    brightened = np.clip(image + value, 0, 255)
    return brightened.astype(np.uint8)

def apply_mask(image, mask_size=(100, 100)):
    h, w = image.shape[:2]
    y1 = h // 2 - mask_size[0] // 2
    y2 = y1 + mask_size[0]
    x1 = w // 2 - mask_size[1] // 2
    x2 = x1 + mask_size[1]
    
    image_copy = image.copy()
    image_copy[y1:y2, x1:x2] = [0, 0, 0]
    return image_copy

# Apply all manipulations
flipped = flip_image(img_np)
noisy = add_noise(img_np)
bright = brighten_channels(img_np)
masked = apply_mask(img_np)

# Save outputs using PIL
Image.fromarray(flipped).save("output/flipped.jpg")
Image.fromarray(noisy).save("output/noisy.jpg")
Image.fromarray(bright).save("output/bright.jpg")
Image.fromarray(masked).save("output/masked.jpg")
