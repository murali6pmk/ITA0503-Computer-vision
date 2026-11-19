import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(image, (x+sx, y+sy), (x+sx+sw, y+sy+sh), (0, 255, 0), 2)

cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
