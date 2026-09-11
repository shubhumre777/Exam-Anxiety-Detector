import cv2
import math
from src.tracker import FaceTracker
from src.emotion import EmotionDetector
from src.analyzer import AnxietyAnalyzer
from src.visualizer import generate_report 

def main():
    cap = cv2.VideoCapture(0)
    tracker = FaceTracker()
    emotion_detector = EmotionDetector()
    analyzer = AnxietyAnalyzer()
    
    last_center = None
    print("Starting camera... Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        annotated_frame, face_crop, current_center = tracker.process_frame(frame)
        
        movement = 0
        if current_center and last_center:
            dx = current_center[0] - last_center[0]
            dy = current_center[1] - last_center[1]
            movement = math.sqrt(dx**2 + dy**2) 
        last_center = current_center
        
        emotion = emotion_detector.detect(face_crop)
        
        analyzer.log_data(movement, emotion)
        anxiety_score = analyzer.calculate_anxiety_score()
        
        cv2.putText(annotated_frame, f"Emotion: {emotion}", (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.putText(annotated_frame, f"Fidget Speed: {int(movement)}", (10, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        color = (0, 0, 255) if anxiety_score > 40 else (0, 255, 0)
        cv2.putText(annotated_frame, f"ANXIETY SCORE: {anxiety_score}/100", (10, 130), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        
        cv2.imshow("Exam Anxiety Detector", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # 1. Save data and get unique filename
    saved_file_path = analyzer.save_log()
    
    cap.release()
    cv2.destroyAllWindows()
    
    # 2. Generate the report for this exact session
    generate_report(saved_file_path)

if __name__ == "__main__":
    main()