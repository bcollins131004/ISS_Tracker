from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/iss")
def iss_position():
    try:
        response = requests.get(ISS_API, timeout=5)
        response.raise_for_status()
        data = response.json()

        return jsonify({
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "altitude": data["altitude"],
            "velocity": data["velocity"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    app.run(debug=True)
