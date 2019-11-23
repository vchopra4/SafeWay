from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder='app')
CORS(app)


@app.route("/direction", methods=['POST', 'GET'])
def direction():
    error = None
    
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        # Here is where the Google Maps Direction API should exist

        # Here is where the model of processing should go

    return jsonify(start, end) # jsonify(Array of values to go in Map.js)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("../../Frontend/safeway/src/index.html")

