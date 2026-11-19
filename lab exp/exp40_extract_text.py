import cv2

# Note: For full OCR you need: pip install pytesseract
# and install Tesseract-OCR software

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Simple threshold to highlight possible text regions
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Original", image)
cv2.imshow("Possible Text Regions", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("For actual text extraction, install pytesseract and Tesseract-OCR.")
