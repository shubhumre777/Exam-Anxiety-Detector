import cv2
import math
import streamlit as st
from src.tracker import FaceTracker
from src.emotion import EmotionDetector
from src.analyzer import AnxietyAnalyzer
from src.visualizer import generate_report 
import time

st.set_page_config(page_title="Anxiety Detector", layout="wide")
st.title("Real Time Anxiety Detector")

# Changed button name to make more sense
run_analysis = st.button("Start Camera")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Camera Feed")
    video_placeholder = st.empty() 
    report_placeholder = st.empty()

with col2:
    st.subheader("Live Analytics")
    score_placeholder = st.empty()
    emotion_placeholder = st.empty()
    fidget_placeholder = st.empty()

if run_analysis:
    cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    tracker = FaceTracker()
    emotion_detector = EmotionDetector()
    analyzer = AnxietyAnalyzer()
    
    last_center = None

    progress_bar = st.progress(0)
    status_text = st.empty()
    max_frames = 300
    # Run the camera for 1000 frames
    for frames_count in range(max_frames):
        ret, frame = cap.read()
        if not ret:
            st.error("Unable to capture the webcam !!")
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
        
        # Convert color for Streamlit and update UI
        frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)
        
        score_placeholder.metric("Anxiety Score", f"{anxiety_score}/100")
        emotion_placeholder.metric("Current Emotion", emotion)
        fidget_placeholder.metric("Fidget Speed", int(movement))

        # Update the progress bar
        progress_percentage = int(((frames_count + 1) / max_frames) * 100)
        progress_bar.progress((frames_count + 1) / max_frames)
        status_text.text(f"Analysis in progress... {progress_percentage}%")
            
    # VERY IMPORTANT: Release the webcam after the loop!
    cap.release()
    
    # Clear the video box
    video_placeholder.empty()

    status_text.text("Exam Complete! Processing data...")
    progress_bar.empty() # Progress bar ko screen se hata do
    
    # Show a 3-second countdown before showing the graph
    with st.spinner("Generating result in 3 seconds..."):
        time.sleep(3)
    
    # Save data and get unique filename
    saved_file_path = analyzer.save_log()
    st.success(f"Exam finished! Log saved to {saved_file_path}")

    # Generate and show the report graph
    generate_report(saved_file_path)
    graph_filename = saved_file_path.replace('.csv', '.png')
    report_placeholder.image(graph_filename, caption="Final Detected Report")