# ShadowSentry - Real-Time App Behavior Detection
ShadowSentry: AI-Powered Privacy Guardian
Overview

ShadowSentry is an AI-powered privacy monitoring system designed to detect unauthorized access to sensitive mobile device resources such as the camera, microphone, and screen. The project uses Machine Learning models like LSTM and Random Forest to analyze app behavior, identify anomalies, and alert users about suspicious activities in real time.

Features
Real-time monitoring of app activities
Detection of abnormal camera and microphone usage
Screen access and permission misuse detection
AI/ML-based anomaly detection
User alerts for suspicious behavior
Lightweight and efficient architecture
Works without requiring root access
Technologies Used
Python
Machine Learning
LSTM
Random Forest
VS Code
Android monitoring concepts
Project Workflow
Collect app behavior and permission usage data
Preprocess and extract activity features
Train ML models on normal behavior patterns
Detect anomalies in real time
Alert or block suspicious app activities

## Setup Instructions

1. Create virtual environment:
   python -m venv venv

2. Activate environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Generate logs:
   python generate_logs.py

5. Train Random Forest:
   python train_rf.py

6. Train LSTM:
   python train_lstm.py

7. Start real-time monitoring:
   python real_time_monitor.py

Project demonstrates AI-based anomaly detection for app permission misuse.
