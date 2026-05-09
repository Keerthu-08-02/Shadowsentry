import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

apps = ["WhatsApp", "Instagram", "Zoom", "YouTube"]
data = []

for _ in range(2000):
    app = random.choice(apps)
    hour = random.randint(0, 23)
    camera = random.choice([0, 1])
    mic = random.choice([0, 1])
    screen = random.choice([0, 1])
    screen_on = random.choice([0, 1])

    # Anomaly rules
    anomaly = 0
    if camera == 1 and screen_on == 0:
        anomaly = 1
    if mic == 1 and hour < 5:
        anomaly = 1

    data.append([app, hour, camera, mic, screen, screen_on, anomaly])

df = pd.DataFrame(data, columns=[
    "app", "hour", "camera", "mic",
    "screen", "screen_on", "anomaly"
])

df.to_csv("data/app_logs.csv", index=False)
print("✅ Log file generated successfully!")