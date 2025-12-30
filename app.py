from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = pd.read_csv("alerts.csv")

    # ✅ Convert to Python int explicitly
    attack_count = int(data[data["prediction"] == "attack"].shape[0])
    normal_count = int(data[data["prediction"] == "normal"].shape[0])

    # ✅ Severity counts (force Python int)
    severity_counts_raw = data["severity"].value_counts()
    severity_counts = {
        "LOW": int(severity_counts_raw.get("LOW", 0)),
        "MEDIUM": int(severity_counts_raw.get("MEDIUM", 0)),
        "HIGH": int(severity_counts_raw.get("HIGH", 0)),
    }

    recent_alerts = data.tail(20).to_dict(orient="records")

    return render_template(
        "index.html",
        attack_count=attack_count,
        normal_count=normal_count,
        severity_counts=severity_counts,
        tables=recent_alerts
    )

if __name__ == "__main__":
    app.run(debug=True)
