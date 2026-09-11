import pandas as pd
import os
import datetime

class AnxietyAnalyzer:
    def __init__(self):
        self.history = pd.DataFrame(columns=['timestamp', 'fidget_speed', 'emotion', 'anxiety_score'])
        
        # Generate a unique filename using current timestamp
        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.csv_filename = f"data/exam_log_{timestamp_str}.csv"
        
    def log_data(self, fidget_speed, emotion):
        new_row = {
            'timestamp': pd.Timestamp.now(),
            'fidget_speed': fidget_speed,
            'emotion': emotion,
            'anxiety_score': 0
        }
        new_df = pd.DataFrame([new_row]) # [new_row] : Dictionary is stored in a list because want only single-single rows .
        self.history = pd.concat([self.history, new_df], ignore_index=True)
            
    def calculate_anxiety_score(self):
        recent_window = self.history.tail(150) # Look at last 5 seconds (150 frames)
        if len(recent_window) < 30:
            return 0
            
        avg_speed = recent_window['fidget_speed'].mean()
        speed_score = min((avg_speed / 40.0) * 50, 50)
        
        negative_emotions = ['Angry', 'Disgust', 'Fear', 'Sad']
        recent_emotions = recent_window['emotion'].tail(30)
        neg_count = recent_emotions.isin(negative_emotions).sum()
        emotion_score = (neg_count / 30.0) * 50
        
        total_score = int(speed_score + emotion_score)
        
        self.history.loc[self.history.index[-1], 'anxiety_score'] = total_score
        return total_score
        
    def save_log(self):
        # Ensure the data directory exists before saving
        os.makedirs(os.path.dirname(self.csv_filename), exist_ok=True)
        self.history.to_csv(self.csv_filename, index=False)
        print(f"\n[INFO] Exam finished. Data saved to {self.csv_filename}")
        return self.csv_filename