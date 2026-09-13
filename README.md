<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&amp;color=0D1117&amp;height=200&amp;section=header&amp;text=EXAM%20ANXIETY%20%26%20PROCTORING%20AI&amp;fontSize=32&amp;fontColor=00E5FF&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=Computer%20Vision%20Behavioral%20Analytics%20Engine&amp;descSize=16&amp;descColor=9CA3AF&amp;descAlignY=68&amp;stroke=00E5FF&amp;strokeWidth=1" width="100%"/>

</div>

<a href="https://exam-anxiety-detector-su.streamlit.app/">
<img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-00A8E8?style=for-the-badge&amp;logo=streamlit&amp;logoColor=white" alt="Open Live Application"/>
</a>

<br><br>

<a href="https://github.com/shubhumre777/Exam-Anxiety-Detector">
<img src="https://img.shields.io/badge/VIEW%20SOURCE%20CODE%20ON%20GITHUB-161B22?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="View Source Code"/>
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/YOLOv8-Face%20Detection-00E5FF?style=for-the-badge" alt="YOLOv8"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&amp;logo=pytorch&amp;logoColor=white" alt="PyTorch"/>
<img src="https://img.shields.io/badge/License-MIT-F5C542?style=for-the-badge" alt="MIT License"/>

<br><br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&amp;weight=500&amp;size=15&amp;duration=3000&amp;pause=1000&amp;color=00E5FF&amp;center=true&amp;vCenter=true&amp;width=720&amp;lines=YOLOv8+Face+Detection;Temporal+Movement+Analysis;Facial+Expression+Signals;Anxiety+Index+%7C+0%E2%80%93100" alt="Project capabilities"/>

</div>

---

## Overview

**Exam Anxiety &amp; Proctoring AI** is a computer vision application for analyzing recorded examination videos. It combines face detection, spatial movement tracking and facial-expression signals to generate an experimental **Anxiety Index (0–100)**.

The score is intended for technical experimentation and behavioral analysis. It is **not a medical or psychological diagnosis**.

## Pipeline

```text
Exam Video
    │
    ▼
Frame Sampling &amp; Resize
    │
    ▼
YOLOv8 Face Detection
    │
    ▼
Centroid &amp; Movement Tracking
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

## Contributing

Contributions are welcome. Bug fixes, documentation improvements and new computer vision features are encouraged.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:0D1117,50:172554,100:0D1117&amp;height=90&amp;section=footer&amp;animation=fadeIn" width="100%"/>

</div>
