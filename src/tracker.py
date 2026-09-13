import os
import cv2
from ultralytics import YOLO

class FaceTracker:
    def __init__(self):
        # Fallback mechanism for cloud deployment (Streamlit Cloud)
        model_path = 'yolov8n-face.pt'
        if not os.path.exists(model_path):
            model_path = 'yolov8n.pt'  # Standard ultralytics model that auto-downloads on cloud
            
        # Load the model
        self.model = YOLO(model_path) 

    def process_frame(self, frame):
        # Ask YOLO to find objects in the camera frame
        results = self.model(frame, verbose=False) # verbose = False means : Does not print extra YOLO details/logs in the terminal.
        
        # Draw the YOLO boxes on the frame
        annotated_frame = results[0].plot()  # This need to be returned
        
        # Get the raw coordinates of the boxes
        boxes = results[0].boxes.xyxy.cpu().numpy()  # .cpu() is used because NumPy can only work with CPU tensors.
        
        face_crop = None
        center_pt = None
        
        # If YOLO found at least one person/face
        if len(boxes) > 0:
            # Get coordinates for the first box
            x1, y1, x2, y2 = map(int, boxes[0][:4])
            
            # Calculate the exact middle of the box (for movement tracking)
            center_pt = ((x1 + x2) // 2, (y1 + y2) // 2)  # This need to be returned
            
            # Crop just the face/body from the original frame
            face_crop = frame[y1:y2, x1:x2]  # This need to be returned
            
        return annotated_frame, face_crop, center_pt
