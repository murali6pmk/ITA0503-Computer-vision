import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    
    if not frames:
        print("No frames found or video not available.")
        return
    
    height, width = frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
    
    for frame in reversed(frames):
        out.write(frame)
    
    out.release()
    print("Reversed video saved as:", output_path)

# Change the video path if needed
reverse_video(r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\sample 1.mp4",
              r"C:\Users\Chandini_Ramaiah\Desktop\cv exp 1\reversed.mp4")
