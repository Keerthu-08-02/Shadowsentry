# ShadowSentry - Real-Time App Behavior Detection

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
