import cv2

cap = cv2.VideoCapture(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.mp4")

print("Press 'q' to stop each mode")

# Normal
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Normal Speed", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Slow
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(80) & 0xFF == ord('q'):
        break

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Fast
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
