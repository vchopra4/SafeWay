from flask import Flask, jsonify, request
from flask_cors import CORS
import googlemaps
from datetime import datetime
app = Flask(__name__, static_folder='app')
CORS(app)


@app.route("/direction", methods=['POST', 'GET'])
def direction():
    error = None
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        # Here is where the Google Maps Direction API should exist
        
        gmaps = googlemaps.Client(key='AIzaSyA05IZP-_GDgylMrM22XBYZ9qUxiTXjq-w')
        now = datetime.now()
        directions_result = gmaps.directions(start,
                                     end,
                                     mode="driving",
                                     departure_time=now)
        
        # Here is where the model of processing should go

    return # jsonify(Array of values to go in Map.js)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("../../Frontend/safeway/src/index.html")

