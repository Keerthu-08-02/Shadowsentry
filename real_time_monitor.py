import joblib
import numpy as np
import random
import time
import pandas as pd
import tensorflow as tf

print("🔐 Starting ShadowSentry Real-Time Monitoring...")

# Load models
rf_model = joblib.load("models/rf_model.pkl")
lstm_model = tf.keras.models.load_model("models/lstm_model.h5")

def generate_live_log():
    hour = random.randint(0, 23)
    camera = random.choice([0, 1])
    mic = random.choice([0, 1])
    screen = random.choice([0, 1])
    screen_on = random.choice([0, 1])

    return np.array([[hour, camera, mic, screen, screen_on]])

try:
    while True:
        log = generate_live_log()

        # Convert to DataFrame (fixes sklearn warning)
        log_df = pd.DataFrame(
            log,
            columns=["hour", "camera", "mic", "screen", "screen_on"]
        )

        rf_prediction = rf_model.predict(log_df)
        lstm_prediction = lstm_model.predict(log.reshape(1, 1, 5), verbose=0)

        if rf_prediction[0] == 1 or lstm_prediction[0][0] > 0.5:
            print("🚨 ALERT: Suspicious App Behavior Detected!")
        else:
            print("✅ Normal Activity")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")