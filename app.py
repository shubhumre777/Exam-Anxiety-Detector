import streamlit as st
import cv2
import tempfile
import os
import numpy as np
from src.tracker import FaceTracker
from src.emotion import EmotionDetector
from src.analyzer import AnxietyAnalyzer
from src.visualizer import generate_report

st.set_page_config(page_title="Exam Anxiety Detector", page_icon="🧠", layout="centered")

st.title("🧠 Exam Anxiety & Proctoring Detector")
st.write("Upload an exam video for smooth, lag-free asynchronous analysis.")

uploaded_file = st.file_uploader("Choose an exam video...", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    st.video(video_path)
    
    if st.button("🚀 Start Optimized Video Analysis", type="primary"):
        tracker = FaceTracker()
        emotion_detector = EmotionDetector()
        analyzer = AnxietyAnalyzer()
        last_center = None

        cap = cv2.VideoCapture(video_path)
        
        st_frame = st.empty()
        metrics_container = st.container()
        
        with metrics_container:
            col1, col2, col3 = st.columns(3)
            m_score = col1.empty()
            m_emotion = col2.empty()
            m_fidget = col3.empty()
        
        progress_bar = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame_idx = 0
        skip_counter = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            current_frame_idx += 1
            skip_counter += 1
            
            # Performance optimization: Resize frame for fast processing
            h, w, _ = frame.shape
            if w > 420:
                scale = 420 / w
                frame = cv2.resize(frame, (int(w * scale), int(h * scale)))

            # AI Processing Pipeline
            annotated_frame, face_crop, current_center = tracker.process_frame(frame)
            
            movement = 0
            if current_center and last_center:
                dx, dy = current_center[0] - last_center[0], current_center[1] - last_center[1]
                movement = int(np.sqrt(dx**2 + dy**2))
            last_center = current_center
            
            emotion = emotion_detector.detect(face_crop)
            analyzer.log_data(movement, emotion)
            anxiety_score = analyzer.calculate_anxiety_score()
            
            # Frame skipping for UI rendering to completely eliminate lag (update UI every 2 frames)
            if skip_counter % 2 == 0 or current_frame_idx == 1:
                m_score.metric("Anxiety Score", f"{anxiety_score}/100")
                m_emotion.metric("Emotion", emotion)
                m_fidget.metric("Fidget Speed", movement)
                
                annotated_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                st_frame.image(annotated_rgb, channels="RGB")
            
            if total_frames > 0:
                progress_bar.progress(min(current_frame_idx / total_frames, 1.0))

        cap.release()
        st.success("✅ Analysis Completed Smoothly!")

        with st.spinner("Generating analytical session report..."):
            saved_file_path = analyzer.save_log()
            generate_report(saved_file_path)
            graph_path = saved_file_path.replace('.csv', '.png')
            
            st.subheader("📊 Final Session Report")
            if os.path.exists(graph_path):
                st.image(graph_path, caption="Anxiety & Fidget Trends Over Time")
            
            final_score = analyzer.calculate_anxiety_score()
            st.info(f"🎯 **Final Exam Anxiety Score:** {final_score} / 100")
if final_score == 0 :
    st.error("Please Upload the file again and Try Analyzing again") 
