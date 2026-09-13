<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D1117&height=220&section=header&text=EXAM%20ANXIETY%20%26%20PROCTORING%20AI&fontSize=32&fontColor=00E5FF&animation=fadeIn&fontAlignY=40&desc=Computer%20Vision%20Behavioral%20Analytics%20Engine&descSize=16&descColor=9CA3AF&descAlignY=65" width="100%" />

<br />

<a href="https://exam-anxiety-detector-su.streamlit.app/">
<img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-00A8E8?style=for-the-badge&logo=streamlit&logoColor=white" alt="Open Live Application" />
</a>

<br /><br />

<a href="https://github.com/shubhumre777/Exam-Anxiety-Detector">
<img src="https://img.shields.io/badge/VIEW%20SOURCE%20CODE%20ON%20GITHUB-161B22?style=for-the-badge&logo=github&logoColor=white" alt="View Source Code" />
</a>

<br /><br />

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/YOLOv8-Face%20Detection-00E5FF?style=for-the-badge" alt="YOLOv8" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
<img src="https://img.shields.io/badge/License-MIT-F5C542?style=for-the-badge" alt="MIT License" />

</div>

---

## Overview

**Exam Anxiety & Proctoring AI** analyzes recorded examination videos using computer vision to estimate an **Anxiety Index (0–100)** from observable movement, facial-expression signals and spatial changes over time.

> The score is an experimental behavioral indicator, not a medical or psychological diagnosis.

## Pipeline

```text
Exam Video
    ↓
Frame Sampling & Resize
    ↓
YOLOv8 Face Detection
    ↓
Centroid & Movement Tracking
    ↓
Facial Expression Analysis
    ↓
Temporal Feature Aggregation
    ↓
Anxiety Index + Visual Report
```

### Movement Metric

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

## Contributing

Contributions are welcome. Bug fixes, documentation improvements and new computer vision features are encouraged.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D1117&height=90&section=footer&animation=fadeIn" width="100%" />

</div>
