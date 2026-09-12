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

st.title("🧠 Exam Anxiety & Proctoring Detector (Video Upload)")
st.write("Upload a recorded exam video to analyze student movement, emotions, and calculate an overall anxiety score.")

# File uploader widget
uploaded_file = st.file_uploader("Choose an exam video...", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    # Save uploaded video to a temporary file so OpenCV can read it
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    st.video(video_path)
    
    if st.button("🚀 Start Video Analysis", type="primary"):
        # Initialize AI components fresh for this session
        tracker = FaceTracker()
        emotion_detector = EmotionDetector()
        analyzer = AnxietyAnalyzer()
        last_center = None

        cap = cv2.VideoCapture(video_path)
        
        # UI placeholders for live progress during processing
        st_frame = st.empty()
        st_score = st.empty()
        st_emotion = st.empty()
        st_fidget = st.empty()
        
        progress_bar = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame_idx = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            current_frame_idx += 1
            
            # Optional: Optimize resolution for speed
            h, w, _ = frame.shape
            if w > 480:
                scale = 480 / w
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
            
            # Update metrics on screen
            st_score.metric("Current Anxiety Score", f"{anxiety_score}/100")
            st_emotion.metric("Detected Emotion", emotion)
            st_fidget.metric("Fidget Speed", movement)
            
            # Convert OpenCV BGR to RGB for Streamlit display (width parameter removed to prevent version errors)
            annotated_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            st_frame.image(annotated_rgb, channels="RGB")
            
            # Update progress bar
            if total_frames > 0:
                progress_bar.progress(min(current_frame_idx / total_frames, 1.0))

        cap.release()
        st.success("✅ Video Analysis Complete!")

        # Generate and display final report graph
        with st.spinner("Generating final analytical report..."):
            saved_file_path = analyzer.save_log()
            generate_report(saved_file_path)
            graph_path = saved_file_path.replace('.csv', '.png')
            
            st.subheader("📊 Final Session Report")
            if os.path.exists(graph_path):
                st.image(graph_path, caption="Anxiety & Fidget Analysis Over Time")
            
            final_score = analyzer.calculate_anxiety_score()
            st.info(f"🎯 **Final Exam Anxiety Score:** {final_score} / 100")