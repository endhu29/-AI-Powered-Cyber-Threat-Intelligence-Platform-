import joblib
import pandas as pd
import os
import csv
from datetime import datetime

# --------------------------------
# 1. Load trained ML model
# --------------------------------
model = joblib.load("model/threat_model.pkl")

# --------------------------------
# 2. Simulated input data (ATTACK)
# --------------------------------
new_data = pd.DataFrame(
    [[1, 90000, 100000, 8]],  # high bytes + failed logins
    columns=["duration", "src_bytes", "dst_bytes", "failed_logins"]
)

# --------------------------------
# 3. ML Prediction
# --------------------------------
ml_prediction = model.predict(new_data)[0]  # 0 = normal, 1 = attack

# Extract values
duration = int(new_data["duration"].iloc[0])
src_bytes = int(new_data["src_bytes"].iloc[0])
dst_bytes = int(new_data["dst_bytes"].iloc[0])
failed_logins = int(new_data["failed_logins"].iloc[0])

# --------------------------------
# 4. HYBRID DECISION (ML + RULE)
# --------------------------------
# Rule-based override (industry practice)
if failed_logins > 5 or src_bytes > 50000:
    prediction = 1   # force ATTACK
else:
    prediction = ml_prediction

# --------------------------------
# 5. Risk Score & Severity
# --------------------------------
if prediction == 1:
    risk_score = min(100, (failed_logins * 10) + (src_bytes / 1000))

    if failed_logins > 5 or src_bytes > 50000:
        severity = "HIGH"
    else:
        severity = "MEDIUM"
else:
    risk_score = 0
    severity = "LOW"

# --------------------------------
# 6. Output
# --------------------------------
if prediction == 1:
    print(f"🚨 ALERT: Cyber Attack Detected | Severity: {severity} | Risk Score: {int(risk_score)}")
else:
    print(f"✅ Normal Network Activity | Severity: {severity} | Risk Score: {int(risk_score)}")

print("Threat Intelligence System Running...")

# --------------------------------
# 7. Log Alert to CSV
# --------------------------------
file_name = "alerts.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "duration",
            "src_bytes",
            "dst_bytes",
            "failed_logins",
            "prediction",
            "severity",
            "risk_score"
        ])

    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        duration,
        src_bytes,
        dst_bytes,
        failed_logins,
        "attack" if prediction == 1 else "normal",
        severity,
        int(risk_score)
    ])
