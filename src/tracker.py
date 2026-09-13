import os
import cv2
import urllib.request
from ultralytics import YOLO

class FaceTracker:
    def __init__(self):
        model_path = 'yolov8n-face.pt'
        
        # Agar file nahi hai ya GitHub ka LFS pointer file hai (size bahut chota hai), toh direct download kar lo
        if not os.path.exists(model_path) or os.path.getsize(model_path) < 1024 * 1024:
            print("Downloading yolov8n-face.pt model...")
            # Public direct download URL for yolov8n-face.pt
            url = "https://github.com/DerronQi/yolov8-face/releases/download/v1.0/yolov8n-face.pt"
            try:
                urllib.request.urlretrieve(url, model_path)
            except Exception as e:
                print(f"Download failed: {e}, falling back to standard yolov8n.pt")
                model_path = 'yolov8n.pt'

        # Load the model safely
        try:
            self.model = YOLO(model_path)
        except Exception as e:
            print(f"Error loading model, falling back to yolov8n.pt: {e}")
            self.model = YOLO('yolov8n.pt')

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
