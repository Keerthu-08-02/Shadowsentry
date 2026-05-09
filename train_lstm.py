import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split

import tensorflow as tf

Sequential = tf.keras.models.Sequential
LSTM = tf.keras.layers.LSTM
Dense = tf.keras.layers.Dense

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/app_logs.csv")

X = df[["hour", "camera", "mic", "screen", "screen_on"]].values
y = df["anomaly"].values

# Reshape for LSTM [samples, timesteps, features]
X = X.reshape((X.shape[0], 1, X.shape[1]))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Sequential([
    LSTM(32, input_shape=(1, 5)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=5, batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"\n✅ LSTM Accuracy: {accuracy:.4f}")

model.save("models/lstm_model.h5")
print("✅ LSTM Model saved!")