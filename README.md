<div align="center">

<!-- HERO -->

<img src="https://capsule-render.vercel.app/api?type=waving&height=230&section=header&text=EXAM%20ANXIETY%20%26%20PROCTORING%20AI&fontSize=34&fontColor=FFFFFF&fontAlignY=40&desc=Computer%20Vision%20%7C%20Behavioral%20Analytics%20%7C%20AI&descSize=17&descColor=E0F2FE&descAlignY=62&gradient=true&animation=fadeIn" width="100%"/>

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=00E5FF&center=true&vCenter=true&width=750&lines=AI-powered+Exam+Behavior+Analysis;Computer+Vision+%2B+Deep+Learning;Movement+%2B+Facial+Expression+Analytics;Turning+Video+Signals+into+Behavioral+Insights" alt="Typing animation"/>

<br><br>

<a href="https://exam-anxiety-detector-su.streamlit.app/">
<img src="https://img.shields.io/badge/%E2%96%B6%20LIVE%20APPLICATION-00C2FF?style=for-the-badge&logo=streamlit&logoColor=white" />
</a>

<a href="https://github.com/shubhumre777/Exam-Anxiety-Detector">
<img src="https://img.shields.io/badge/%E2%98%85%20SOURCE%20CODE-18181B?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/YOLOv8-Face%20Detection-FF6B35?style=flat-square"/>
<img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>

<br><br>

<img src="https://komarev.com/ghpvc/?username=shubhumre777&repo=Exam-Anxiety-Detector&color=00E5FF&style=flat-square&label=PROJECT+VIEWS"/>

</div>

---

## 🧠 What is Exam Anxiety & Proctoring AI?

**Exam Anxiety & Proctoring AI** is an experimental computer-vision system that analyzes examination videos and extracts observable behavioral signals such as:

* 👤 Face movement
* 🔄 Fidgeting / movement intensity
* 🙂 Facial-expression signals
* 📈 Temporal behavioral patterns
* 🎯 Session-level behavioral score

These signals are combined into an experimental **Anxiety Index (0–100)**.

> ⚠️ **Important:** The Anxiety Index is an experimental behavioral indicator. It is **not a medical, psychological, or diagnostic measurement**.

---

## ⚡ AI Pipeline

<div align="center">

```text
                    🎥 EXAM VIDEO
                      │
                      ▼
              ┌─────────────────────┐
              │ Frame Sampling      │
              │ Resize & Preprocess │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   YOLOv8 Face       │
              │     Detection       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Centroid Tracking   │
              │ Movement Analysis   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Facial Expression   │
              │     Analysis        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Temporal Feature    │
              │    Aggregation      │
              └──────────┬──────────┘
                         │
                         ▼
                ┌────────────────┐
                │ ANXIETY INDEX  │
                │      0–100     │
                └────────┬───────┘
                         │
                         ▼
                📊 VISUAL REPORT
```

</div>

---

## 🔬 How Movement is Measured

The system tracks changes in the detected face position between consecutive frames.

```text
Movement =
√((xₜ - xₜ₋₁)² + (yₜ - yₜ₋₁)²)
```

Movement signals are aggregated over time and combined with expression-related features to produce the session-level behavioral index.

---

## 🎯 Core Features

<table>
<tr>
<td align="center" width="25%">

### 👁️

**Face Detection**

YOLOv8-based face localization

</td>

<td align="center" width="25%">

### 🏃

**Movement Tracking**

Centroid-based temporal tracking

</td>

<td align="center" width="25%">

### 🙂

**Expression Analysis**

Facial-expression signals

</td>

<td align="center" width="25%">

### 📊

**Analytics**

Behavioral trends & reports

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

<div align="center">

| Layer                   | Technology                |
| ----------------------- | ------------------------- |
| 👁️ Computer Vision     | YOLOv8 · OpenCV           |
| 🧠 Deep Learning        | PyTorch · Torchvision     |
| 📐 Numerical Processing | NumPy                     |
| 🗃️ Data Processing     | Pandas                    |
| 📊 Visualization        | Matplotlib · Seaborn      |
| 🌐 Application          | Streamlit                 |
| ☁️ Deployment           | Streamlit Community Cloud |

</div>

---

## 📁 Project Architecture

```text
Exam-Anxiety-Detector/
│
├── src/
│   ├── tracker.py
│   │   └── Face detection + movement tracking
│   │
│   ├── emotion.py
│   │   └── Facial-expression analysis
│   │
│   ├── analyzer.py
│   │   └── Anxiety scoring + telemetry
│   │
│   └── visualizer.py
│       └── Analytics + visualization
│
├── app.py
│   └── Streamlit application
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/shubhumre777/Exam-Anxiety-Detector.git

cd Exam-Anxiety-Detector

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
streamlit run app.py
```

---

## 🌐 Try the Live Application

<div align="center">

<a href="https://exam-anxiety-detector-su.streamlit.app/">

<img src="https://img.shields.io/badge/🚀%20LAUNCH%20EXAM%20ANXIETY%20AI-00C2FF?style=for-the-badge&labelColor=111827"/>

</a>

<br><br>

**Upload → Analyze → Track → Visualize**

</div>

---

## 📊 System Output

The application transforms raw examination video into interpretable behavioral analytics:

```text
Video
  ↓
Face Detection
  ↓
Movement Signals
  ↓
Expression Signals
  ↓
Temporal Analysis
  ↓
Behavioral Features
  ↓
Anxiety Index
  ↓
Visual Analytics
```


---

## ⚠️ Limitations

The system should be treated as a **research / experimental computer-vision project**.

Behavioral signals can be affected by lighting, camera position, individual behavior, facial expressions, video quality and other environmental factors.

Therefore, the generated score should **not** be used as a standalone measure of a student's psychological state.

---

## 🤝 Contributing

Contributions are welcome.

You can contribute through:

* 🐛 Bug fixes
* 📚 Documentation
* ⚡ Performance improvements
* 👁️ New computer-vision features
* 🧠 Better behavioral models

```text
Fork → Improve → Test → Pull Request
```

---

## 👨‍💻 Developer

<div align="center">

### Shubh Umre

**AI Developer · Computer Vision Engineer · AIML Student**

Building practical systems across:

`Artificial Intelligence` · `Machine Learning` · `Generative AI` · `Computer Vision`

<br>

<a href="https://github.com/shubhumre777">
<img src="https://img.shields.io/badge/GitHub-Shubh%20Umre-18181B?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<br><br>

**Open to collaboration, contributions and interesting AI projects.**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&text=BUILD%20%7C%20EXPERIMENT%20%7C%20IMPROVE&fontSize=22&fontColor=FFFFFF&gradient=true&animation=fadeIn" width="100%"/>

</div>
