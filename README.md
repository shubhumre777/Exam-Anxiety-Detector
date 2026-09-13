<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:172554,100:0D1117&height=210&section=header&text=EXAM%20ANXIETY%20%26%20PROCTORING%20AI&fontSize=32&fontColor=00FFFF&animation=twinkling&stroke=00FFFF&strokeWidth=1&desc=Computer%20Vision%20%7C%20Behavioral%20Analytics%20%7C%20Exam%20Monitoring&descSize=15&descColor=A0A0A0&descAlignY=65" width="100%"/>

[![🚀 Live App](https://img.shields.io/badge/🚀_LIVE_APP-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://exam-anxiety-detector-su.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Face_Detection-00FFFF?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![MIT](https://img.shields.io/badge/License-MIT-F5C542?style=for-the-badge)](LICENSE)

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=16&duration=2800&pause=900&color=00FFFF&center=true&vCenter=true&width=700&lines=Video+Analytics;YOLOv8+Face+Detection;Movement+%26+Expression+Analysis;Temporal+Anxiety+Scoring" alt="Typing Animation"/>

</div>

---

## 🎯 Overview

**Exam Anxiety & Proctoring AI** analyzes recorded exam videos using computer vision to estimate an **Anxiety Index (0–100)** from observable movement, facial-expression signals, and spatial changes over time.

> **Note:** The score is an experimental behavioral indicator, not a medical or psychological diagnosis.

## ⚙️ How It Works

```text
🎥 Video
   ↓
Frame Sampling & Resize
   ↓
👁️ YOLOv8 Face Detection
   ↓
📍 Centroid / Movement Tracking
   ↓
🙂 Facial Expression Analysis
   ↓
🧮 Anxiety Scoring
   ↓
📊 Trends & Session Report
```

### Core Metric

Face movement is calculated using centroid displacement:

```text
Movement = √((xₜ - xₜ₋₁)² + (yₜ - yₜ₋₁)²)
```

The movement and expression signals are aggregated over time to produce the final **Anxiety Index**.

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Computer Vision | YOLOv8, OpenCV |
| Deep Learning | PyTorch |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Deployment | Streamlit Community Cloud |

## 📂 Structure

```text
Exam-Anxiety-Detector/
├── src/
│   ├── tracker.py       # Face detection & movement tracking
│   ├── emotion.py       # Facial-expression analysis
│   ├── analyzer.py      # Anxiety scoring & telemetry
│   └── visualizer.py    # Analytical plots
├── app.py               # Streamlit application
├── requirements.txt     # Dependencies
└── README.md
```

## 🚀 Run Locally

```bash
git clone https://github.com/shubhumre777/Exam-Anxiety-Detector.git
cd Exam-Anxiety-Detector

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```
## 👨‍💻 Developer

**Shubh Umre**  
AI Developer • Computer Vision Engineer • AIML Student

Building practical applications in **AI, Machine Learning, Generative AI and Computer Vision**.

[![GitHub](https://img.shields.io/badge/GitHub-shubhumre777-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shubhumre777)

## 🤝 Contributions

Open to **contributions, ideas, bug fixes and improvements** in AI and Computer Vision.

If you find the project useful, consider ⭐ **starring the repository**.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:172554,100:0D1117&height=100&section=footer&animation=twinkling" width="100%"/>

</div>
