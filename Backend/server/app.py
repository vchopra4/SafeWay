from flask import Flask, jsonify, request
from flask_cors import CORS
import googlemaps
from datetime import datetime
import json
import HandleGeoData as hgd

app = Flask(__name__, static_folder='app')
CORS(app)
hd = hgd.HandleData()


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
                                     departure_time=now,
                                     region="ca")


        directions_result_temp = json.dumps(directions_result)
        directions_result_dict = json.loads(directions_result_temp)
        route = directions_result_dict[0]["legs"][0]["steps"]
        output = []

        for i in range(len(route) - 1):
            r_dict = {}
            r_dict['lat1'] = route[i]['start_location']
            r_dict['lng1'] = route[i]['end_location']
            output.append(r_dict)
        # Here is where the model of processing should go

    
    extras = hd.run_thread(output)

    print(len(extras), len(output))

    for i in range(len(output)):
        r_dict = output[i]
        r_dict['DgScr'] = extras[i]

    return jsonify(output)# final results


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("../../Frontend/safeway/src/index.html")

