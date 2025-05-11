import os
import json
import math
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Restrict origins in production

@app.route("/")
def index():
    return jsonify({"message": "Radius Filter API is running."})

@app.route("/api/zones", methods=["GET"])
def filter_zones():
    try:
        lat = float(request.args.get("lat"))
        lon = float(request.args.get("lon"))
        radius = float(request.args.get("radius"))

        # ✅ Use the correct path to the zones.json file
        data_path = os.path.join(os.path.dirname(__file__), "zones.json")
        with open(data_path, "r") as f:
            zones = json.load(f)

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # Earth radius in kilometers
            phi1 = math.radians(lat1)
            phi2 = math.radians(lat2)
            dphi = math.radians(lat2 - lat1)
            dlambda = math.radians(lon2 - lon1)

            a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
            return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        nearby = [
            zone for zone in zones
            if haversine(lat, lon, zone["lat"], zone["lon"]) <= radius
        ]

        return jsonify(nearby)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
