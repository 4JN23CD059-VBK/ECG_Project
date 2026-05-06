import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow # Special Colab function for images


def process_my_ecg(image_path):
    # 1. Load the image
    img = cv2.imread(image_path)
    # Check if image was loaded successfully
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None # Return None if image loading fails
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
