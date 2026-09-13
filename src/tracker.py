import os
import cv2
from ultralytics import YOLO

class FaceTracker:
    def __init__(self):
        # Build an absolute path pointing to the root directory from src/tracker.py
        current_dir = os.path.dirname(os.path.abspath(__file__)) # points to src/
        root_dir = os.path.dirname(current_dir) # points to project root
        model_path = os.path.join(root_dir, 'yolov8n-face.pt')
        
        # Fallback check if file is in current working directory
        if not os.path.exists(model_path):
            model_path = 'yolov8n-face.pt'

        # Load the custom face model
        self.model = YOLO(model_path) 

    def process_frame(self, frame):
        results = self.model(frame, verbose=False)
        annotated_frame = results[0].plot()
        boxes = results[0].boxes.xyxy.cpu().numpy()
        
        face_crop = None
        center_pt = None
        
        if len(boxes) > 0:
            x1, y1, x2, y2 = map(int, boxes[0][:4])
            center_pt = ((x1 + x2) // 2, (y1 + y2) // 2)
            face_crop = frame[y1:y2, x1:x2]
            
        return annotated_frame, face_crop, center_pt
