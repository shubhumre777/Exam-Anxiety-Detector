# import os
# import cv2
# from ultralytics import YOLO

# class FaceTracker:
#     def __init__(self):
#         try:
#             self.model = YOLO('yolov8n-face.pt')
#         except Exception as e:
#             print(f"Error loading YOLO face model: {e}")
#             self.model = None

#     def process_frame(self, frame):
#         if self.model is None:
#             return frame, None, None
            
#         results = self.model(frame, verbose=False)
#         annotated_frame = results[0].plot()
#         boxes = results[0].boxes.xyxy.cpu().numpy()
        
#         face_crop = None
#         center_pt = None
        
#         if len(boxes) > 0:
#             x1, y1, x2, y2 = map(int, boxes[0][:4])
#             center_pt = ((x1 + x2) // 2, (y1 + y2) // 2)
#             face_crop = frame[y1:y2, x1:x2]
            
#         return annotated_frame, face_crop, center_pt



import cv2

class FaceTracker:
    def __init__(self):
        # Load OpenCV's built-in robust face detector (No external file downloads or cloud locks needed)
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def process_frame(self, frame):
        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=6, 
            minSize=(30, 30)
        )
        
        annotated_frame = frame.copy()
        face_crop = None
        center_pt = None
        
        if len(faces) >  0:
            # Get coordinates of the first detected face
            x, y, w, h = faces[0]
            x1, y1, x2, y2 = x, y, x + w, y + h
            
            # Calculate center point for fidget movement tracking
            center_pt = ((x1 + x2) // 2, (y1 + y2) // 2)
            
            # Crop the exact face region for emotion analysis
            face_crop = frame[y1:y2, x1:x2]
            
            # Draw a clean visual bounding box around the face on the video
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 128), 2)
            cv2.putText(
                annotated_frame, 
                "Exam Candidate", 
                (x1, y1 - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, 
                (0, 255, 128), 
                2
            )
            
        return annotated_frame, face_crop, center_pt
