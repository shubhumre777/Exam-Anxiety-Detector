<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0D1117&height=180&section=header&text=EXAM%20ANXIETY%20%26%20PROCTORING%20AI&fontSize=31&fontColor=00E5FF&animation=fadeIn&stroke=00E5FF&strokeWidth=1&desc=Computer%20Vision%20Behavioral%20Analytics&descSize=16&descColor=9CA3AF&descAlignY=68" width="100%"/>

<br>

[![Live App](https://img.shields.io/badge/LIVE%20APP-Streamlit-00A8E8?style=for-the-badge&logo=streamlit&logoColor=white)](https://exam-anxiety-detector-su.streamlit.app/)
[![Repository](https://img.shields.io/badge/SOURCE-GitHub-161B22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shubhumre777/Exam-Anxiety-Detector)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Face%20Detection-00E5FF?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-F5C542?style=for-the-badge)](LICENSE)

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=15&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=720&lines=YOLOv8+Face+Detection;Temporal+Movement+Analysis;Facial+Expression+Signals;Anxiety+Index+%7C+0%E2%80%93100" alt="Project capabilities"/>

</div>

---

## Overview

**Exam Anxiety & Proctoring AI** is a computer vision application for analyzing recorded examination videos. It combines face detection, spatial movement tracking and facial-expression signals to generate an experimental **Anxiety Index (0–100)**.

The system is intended for technical experimentation and behavioral analysis. The score is **not a medical or psychological diagnosis**.

## Pipeline

```text
Exam Video
    │
    ▼
Frame Sampling & Resize
    │
    ▼
YOLOv8 Face Detection
    │
    ▼
Centroid & Movement Tracking
    │
    ▼
Facial Expression Analysis
    │
    ▼
Temporal Feature Aggregation
    │
    ▼
Anxiety Index + Visual Report
```

### Movement Metric

Face movement is estimated from the displacement of the detected face centroid between consecutive frames:

```text
Movement = √((xₜ - xₜ₋₁)² + (yₜ - yₜ₋₁)²)
```

Movement and expression signals are aggregated over time to calculate the session-level index.

## Tech Stack

| Component | Technology |
|---|---|
| Computer Vision | YOLOv8, OpenCV |
| Deep Learning | PyTorch |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Application | Streamlit |
| Deployment | Streamlit Community Cloud |

## Project Structure

```text
Exam-Anxiety-Detector/
├── src/
│   ├── tracker.py       # Face detection and movement tracking
│   ├── emotion.py       # Facial-expression analysis
│   ├── analyzer.py      # Anxiety scoring and telemetry
│   └── visualizer.py    # Analytical visualization
├── app.py               # Streamlit application
├── requirements.txt     # Project dependencies
└── README.md
```

## Run Locally

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

## Developer

**Shubh Umre**  
AI Developer · Computer Vision Engineer · AIML Student

Focused on building practical systems in **AI, Machine Learning, Generative AI and Computer Vision**.

[![GitHub](https://img.shields.io/badge/GitHub-shubhumre777-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shubhumre777)

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request for improvements, bug fixes, documentation or new computer vision features.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:172554,100:0D1117&height=90&section=footer&animation=fadeIn" width="100%"/>

</div>
