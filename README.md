<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0d1117&customColor=true&height=200&section=header&text=Exam%20Anxiety%20&%20Proctoring%20AI&fontSize=32&fontColor=00FFFF&animation=fadeIn&stroke=30363d" width="100%"/>

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://exam-anxiety-detector-su.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Face%20Detection-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%2C%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

*An advanced computer vision application engineered to quantify candidate stress levels, monitor head movement dynamics, and automate academic proctoring integrity checking.*

</div>

---

## 🌐 Live Application
Access the fully deployed cloud version here:
👉 **[Exam Anxiety & Proctoring Detector Live](https://exam-anxiety-detector-su.streamlit.app/)**

---

## 🎯 Project Overview & Objective
Traditional online exam proctoring relies heavily on intrusive live webcam feeds or binary tab-switching flags, which often fail to gauge a student's actual cognitive stress or subtle physical unease. 

This project bridges that gap by implementing an **AI-driven video analytics pipeline**. It processes recorded examination footage to compute a holistic **Anxiety Index (0–100)** based on physical fidget velocity, spatial positioning shifts, and facial emotion metrics over time.

---

## 🛠️ Technical Architecture & Approach

The application follows a modular, pipeline-based architecture designed for optimal performance under cloud resource constraints:

1. **Ingestion & Preprocessing (`app.py`):**
   * Accepts standard video formats (`mp4`, `avi`, `mov`, `mkv`) via Streamlit uploader.
   * Leverages temporary file caching (`tempfile`) and OpenCV (`cv2.VideoCapture`) for frame extraction.
   * **Performance Throttling:** Implements adaptive frame-skipping and resolution downscaling ($420\text{px}$ width) to prevent UI socket bottlenecks and eliminate playback lag on cloud hardware.

2. **Facial Tracking & Bounding (`src/tracker.py`):**
   * Powered by **YOLOv8 Face Detection** (`yolov8n-face.pt`).
   * Extracts precise bounding box coordinates (`xyxy`) to track the candidate's centroid displacement across consecutive frames (calculating Euclidean distance for fidget speed).

3. **Emotion Assessment (`src/emotion.py`):**
   * Analyzes cropped facial regions (`face_crop`) to categorize primary affective states indicating stress or distraction.

4. **Scoring & Statistical Logging (`src/analyzer.py` & `src/visualizer.py`):**
   * Continuously logs movement metrics and emotional weights into time-series data structures.
   * Generates mathematical anxiety scores and compiles trend charts using Matplotlib/Seaborn for post-session review.

---

## 🛑 Engineering Challenges & Solutions Faced

Developing and deploying a heavy computer vision pipeline to **Streamlit Community Cloud** presented several core engineering hurdles:

* **Challenge 1: Heavy Binary Model Files on Git**
  * *Issue:* Custom weights like `yolov8n-face.pt` exceed optimal storage limits or get converted into Git LFS pointer text files, causing PyTorch unpickling crashes on the cloud.
  * *Solution:* Built an automated **runtime fallback & dynamic download hook** inside `src/tracker.py`. If custom weights are missing or invalid, the app safely pulls lightweight weights or gracefully falls back to standard `yolov8n.pt`.

* **Challenge 2: Streamlit UI Rendering Lag (WebSocket Overload)**
  * *Issue:* Pushing high-res frame-by-frame updates (`st.image`) alongside real-time metrics caused severe UI freezing and frame drops.
  * *Solution:* Implemented frame-throttling logic (updating UI elements selectively every 2nd frame) and containerized metrics layout to optimize render cycles.

* **Challenge 3: Dependency and Environment Mismatches**
  * *Issue:* OpenCV GUI dependencies (`cv2.imshow`) crashing headless cloud Linux environments.
  * *Solution:* Migrated completely to `opencv-python-headless` and streamlined `requirements.txt` to align strictly with cloud container capabilities.

---

## 📂 Repository Structure

```text
Exam-Anxiety-Detector/
│
├── src/
│   ├── __init__.py
│   ├── tracker.py       # YOLOv8 face detection, fallback logic & movement geometry
│   ├── emotion.py     # Facial expression recognition pipeline
│   ├── analyzer.py    # Temporal anxiety scoring and CSV logging engine
│   └── visualizer.py  # Graph plotting & analytical trend generation
│
├── app.py             # Main Streamlit web app (Video upload, throttling & UI loop)
├── requirements.txt   # Pinned production dependencies
└── README.md          # Project Documentation
