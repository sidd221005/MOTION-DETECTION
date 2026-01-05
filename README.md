# MOTION-DETECTION
Real-time motion detection security system using Python and OpenCV
# 🔔 Motion Detection Security System

A real-time motion detection security system built using **Python and OpenCV**.
The system monitors a live camera feed and triggers an alarm when continuous motion is detected.



## 🚀 Features
- Real-time motion detection
- Noise reduction using Gaussian Blur
- Smart alarm triggering (avoids false positives)
- Alarm stops automatically when motion disappears
- Multithreaded alarm system
- Keyboard-controlled alarm mode



## 🛠️ Problems It Solves
- Unauthorized entry detection (home, hostel, office)
- After-hours monitoring for rooms, labs, or shops
- Basic CCTV automation without expensive hardware
- Avoids false alarms caused by light flicker
- Detects continuous motion rather than single-frame noise



## 🧠 How It Works
1. Captures live video using webcam
2. Converts frames to grayscale and applies Gaussian Blur
3. Compares current frame with background frame
4. Counts changed pixels to detect motion
5. Triggers alarm if motion persists across multiple frames


