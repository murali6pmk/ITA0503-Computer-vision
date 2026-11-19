import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255
box_h, box_w = height // 10, width // 10

image[:box_h, :box_w] = [0, 0, 0]          # Black
image[:box_h, -box_w:] = [255, 0, 0]       # Blue
image[-box_h:, :box_w] = [0, 255, 0]       # Green
image[-box_h:, -box_w:] = [0, 0, 255]      # Red

cv2.imshow("Colored Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
