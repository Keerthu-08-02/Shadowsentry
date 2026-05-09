import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/app_logs.csv")

X = df[["hour", "camera", "mic", "screen", "screen_on"]]
y = df["anomaly"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ RF Accuracy: {accuracy:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred := model.predict(X_test)))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(model, "models/rf_model.pkl")
print("✅ RF Model saved!")