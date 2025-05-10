# radius_filter_api.py

import os
import json
import math
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Restrict origins in production

# Load zones once at startup
data_path = os.getenv('ZONES_JSON_PATH', 'zones.json')
with open(data_path, 'r') as f:
    zones_data = json.load(f)
    if isinstance(zones_data, dict) and 'features' in zones_data:
        features = zones_data['features']
    elif isinstance(zones_data, list):
        features = zones_data
    else:
        raise ValueError('zones.json must be a FeatureCollection or list of features')

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 3958.8  # miles
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/api/zones', methods=['GET'])
@app.route('/api/zones', methods=['GET'])
def get_zones():
    return jsonify({
        'type': 'FeatureCollection',
        'features': features
    })

