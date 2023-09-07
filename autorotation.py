import pytesseract
import cv2

def autorotation(image):

    extracted_text = pytesseract.image_to_osd(image)

    # Check for orientation hints in the extracted text
    if 'Rotate' in extracted_text:
        angle = int(extracted_text.split('Rotate: ')[-1])
        # Correct the rotation angle (if needed)
        if angle != 0:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return image