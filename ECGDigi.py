import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow # Special Colab function for images

#Function to process the images
def process_my_ecg(image_path):
    # 1. Load the image
    img = cv2.imread(image_path)
    # Check if image was loaded successfully
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None # Return None if image loading fails
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #2. Zoom in/Pre-process (Adaptive thresholding handles uneven lighting)
    #This is great for phone photos with shadows!
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, CV2.THRESH_BINARY_INV, 11, 2)


   #3. Clean up small noise (like paper texture)
   kernel = np.ones((2,2), np.uint8)
   clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, Kernel)

   #4. Extract the signal logic (as we discussed)
   height, width = clean.shape
   signal = []
   for x in range)width):
       black_pixels = np.where(clean[:, x] > 0) [0]
       if len(black_pixels) > 0:
           signal.append(np.mean(black_pixels))
       else:
           signal.append(signal[-1] if signal else height/2)
    #5. Show the "Before" and "After"
    print("---STEP 1: ISOLATING THE DARK PIXEL ---")
    cv2_imshow(cv2.resize(clean, (800, 400))) #Resizing so it fits your screen

    print("\n---STEP 2: CONVERTING PIXELS TO A DIGITAL WAVEFORM ---")
    plt.figure(figsize=(15, 5))
    plt.plot(signal, color='red', linewidth=1)
    plt.gca().invert_yaxis() # Important: Images count rows from top-down
    plt.title("Digitized Signal from your Gallery Photo")
    plt.grid(True, alpha=0.3)
    plt.show()
    return signal # Return the signal so it can be used globally

