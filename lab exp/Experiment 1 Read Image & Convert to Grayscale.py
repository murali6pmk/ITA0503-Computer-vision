import cv2

# Your full image path
image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")

if image is None:
    print("Image still not found. Please check the path.")
else:
    print("Image loaded successfully!")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Display both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
