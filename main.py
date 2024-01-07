import cv2
import numpy as np

def process_mammogram(image_path, output_path):
    # Read the original grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    normalized_image = cv2.normalize(gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Applying Gaussian Blur
    blurred_image = cv2.GaussianBlur(normalized_image , (7,7), cv2.BORDER_DEFAULT)

    # Lower the brightness by reducing the pixel values of the denoised image
    lowered_brightness_nlm_image = cv2.subtract(blurred_image, 60)

    # Apply global thresholding after lowering the brightness
    _, thresholded_nlm_image = cv2.threshold(lowered_brightness_nlm_image, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    final_img = cv2.add(normalized_image, thresholded_nlm_image)

    # Save the final image
    cv2.imwrite(output_path, final_img)


# Process the image
process_mammogram('breast2.jpeg', 'gpt1.png')