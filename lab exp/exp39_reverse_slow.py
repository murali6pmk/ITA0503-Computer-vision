import cv2

cap = cv2.VideoCapture(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample.mp4")
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

print("Playing reverse slow motion... Press 'q' to stop")
for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
