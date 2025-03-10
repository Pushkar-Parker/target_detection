# Target Tracking Using MediaPipe Face Mesh

## Overview
This project leverages **MediaPipe's Face Mesh module** to track a specific facial point—the region between the eyes, just above the nose. By utilizing **real-time face landmark detection**, this implementation enables applications such as **head pose estimation, gesture-based interactions, augmented reality, and facial recognition enhancements**.

## Features
- Tracks a key facial point between the eyes using **MediaPipe Face Mesh**
- **Real-time facial landmark detection** with high accuracy
- Utilizes **468 facial landmarks** for precise tracking
- Lightweight and efficient, running on standard hardware
- Potential applications in **gaze tracking, AR filters, virtual avatars, and emotion analysis**

## Technologies Used
- **Python**
- **MediaPipe Face Mesh**
- **OpenCV** (for visualization and video processing)
- **NumPy** (for numerical computations)

## Installation
To run this project, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the script to start face tracking:

```bash
python target_tracking.py
```

## How It Works
1. **Capture video input** using OpenCV.
2. **Process each frame** using MediaPipe Face Mesh.
3. **Extract and track the landmark** located between the eyes.
4. **Visualize the tracking point** on the video feed.

## Potential Applications
- **Head pose estimation**
- **Augmented reality (AR) filters**
- **Virtual avatar control**
- **Gaze tracking and eye movement analysis**
- **Gesture-based interactions**

## Contribution
Contributions and suggestions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

## License
This project is licensed under the **MIT License**.

---
### Let's Connect
If you're working on similar projects or have ideas for improvement, feel free to reach out!
