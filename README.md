<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0d1117&customColor=true&height=200&section=header&text=Exam%20Anxiety%20&%20Proctoring%20AI&fontSize=32&fontColor=00FFFF&animation=fadeIn&stroke=30363d" width="100%"/>

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://exam-anxiety-detector-su.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Face%20Detection-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
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

## ⚙️ Core System Workflow & Detection Metrics

The application follows a structured, multi-stage processing pipeline to transform raw video into actionable behavioral insights:

1. **Video Ingestion & Downscaling:**
   * The user uploads an exam recording (`mp4`, `avi`, `mov`, `mkv`).
   * Frames are dynamically read and downscaled to a standardized width ($420\text{px}$) to optimize processing speed and eliminate UI lag.

2. **Facial Bounding & Centroid Mapping (`src/tracker.py`):**
   * YOLOv8 detects the candidate's face, returning bounding box coordinates ($x_1, y_1, x_2, y_2$).
   * The geometric center point of the face is calculated for every frame.

3. **Fidget Velocity Calculation:**
   * Movement is quantified by measuring the **Euclidean distance** between the face's center point in consecutive frames:
     $$\text{Movement} = \sqrt{(x_t - x_{t-1})^2 + (y_t - y_{t-1})^2}$$
   * High displacement spikes indicate restlessness or fidgeting.

4. **Emotion & Anxiety Indexing (`src/analyzer.py`):**
   * Facial expressions are categorized, and movement metrics are weighted cumulatively.
   * The system outputs a dynamic **Exam Anxiety Score out of 100** and generates trend graphs using Matplotlib/Seaborn.

---

## 🛠️ Comprehensive Tech Stack

| Category | Technologies & Libraries | Purpose |
| :--- | :--- | :--- |
| **AI & Computer Vision** | `Ultralytics YOLOv8`, `PyTorch`, `OpenCV` | High-precision face bounding, spatial tracking, and inference execution. |
| **Web Framework** | `Streamlit Community Cloud` | Interactive, responsive web interface and cloud deployment. |
| **Data Processing** | `Pandas`, `NumPy` | Handling telemetry, tracking logs, and calculating statistical scores. |
| **Data Visualization** | `Matplotlib`, `Seaborn` | Generating time-series analytical graphs and session summary reports. |
| **Utilities** | `Python Standard Libraries (os, tempfile)` | Handling temporary video storage and local path management. |

---

## 📂 Repository Structure

```text
Exam-Anxiety-Detector/
│
├── src/
│   ├── __init__.py
│   ├── tracker.py       # YOLOv8 face tracking, fallbacks & coordinate mapping
│   ├── emotion.py     # Facial expression recognition pipeline
│   ├── analyzer.py    # Temporal anxiety scoring and CSV logging engine
│   └── visualizer.py  # Graph plotting & analytical trend generation
│
├── app.py             # Main Streamlit web app (Video upload, throttling & UI loop)
├── requirements.txt   # Pinned production dependencies
└── README.md          # Project Documentation
