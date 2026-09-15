import os
import cv2
from ultralytics import YOLO

class FaceTracker:
    def __init__(self):
        # Use standard model and handle any serialization/loading issues gracefully
        try:
            self.model = YOLO('yolov8n-face.pt')
        except Exception as e:
            print(f"Error loading YOLO model: {e}")
            # Fallback to an alternative or handle it
            self.model = None

    def process_frame(self, frame):
        if self.model is None:
            return frame, None, None
            
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
