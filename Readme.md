# 🔐 AI-Powered Cyber Threat Intelligence Platform

An AI-based Cyber Threat Intelligence (CTI) system that detects malicious network activities using Machine Learning combined with rule-based logic, visualizes threats on a web dashboard, and logs alerts for analysis.

---

## 📌 Project Overview

Cyber attacks are increasing rapidly, and traditional rule-based security systems are not enough to detect new or unknown threats.  
This project uses a **hybrid approach (Machine Learning + Rule-Based Detection)** to identify cyber threats, assign severity levels, calculate risk scores, and visualize the results in real time.

---

## 🎯 Objectives

- Detect normal and malicious network traffic
- Reduce false negatives using hybrid detection
- Assign severity levels (LOW / MEDIUM / HIGH)
- Calculate threat risk score (0–100)
- Log alerts for analysis
- Visualize threats using a web dashboard

---

## ⚙️ Technologies Used

- **Python**
- **Machine Learning (Random Forest)**
- **Pandas, NumPy**
- **Flask (Web Framework)**
- **Chart.js (Data Visualization)**
- **CSV-based Logging**

---

## 🧠 System Architecture


# Network Data
#      ↓
# Machine Learning Model
#      ↓
# Rule-Based Override
#      ↓
# Severity & Risk Score
#      ↓
# Alert Logging (CSV)
#      ↓
# Flask Dashboard


---

## 🚀 How It Works

1. Network traffic data is given as input
2. ML model predicts Normal / Attack
3. Rule-based logic overrides ML if threat indicators are strong
4. Severity and risk score are calculated
5. Alerts are logged into `alerts.csv`
6. Dashboard displays alerts and charts

---

## 📊 Dashboard Features

- Attack vs Normal Pie Chart
- Severity Distribution Bar Chart
- Recent Alerts Table
- Auto-updating visualization

---

## ▶️ How to Run the Project

### 1️⃣ Activate virtual environment
source env/bin/activate

### 2️⃣ Run threat detection
python detect_threat.py

### 3️⃣ Start dashboard
python app.py

### 4️⃣ Open browser
http://127.0.0.1:5000

### 🧪 Sample Output
🚨 ALERT: Cyber Attack Detected | Severity: HIGH | Risk Score: 100
Threat Intelligence System Running...

### 🎓 Why Hybrid Detection?

ML alone may miss rare attacks

Rules alone may cause false alarms

Hybrid approach improves reliability

### 🔮 Future Scope

Use real-time network logs

Improve ML model with larger datasets

Add anomaly detection models

Deploy dashboard on cloud

Integrate with SIEM/SOC tools


### 📜 License

This project is for educational purposes only.


---

