from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("weather_viz.html")

@app.route("/api/weather_data")
def weather_data():
    json_path = os.path.join("data", "weather_cleaned_20250709_151718.json")  # Adjust this name if needed
    with open(json_path, "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
