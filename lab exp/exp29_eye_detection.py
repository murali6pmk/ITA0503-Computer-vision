import cv2

image = cv2.imread(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)

cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
