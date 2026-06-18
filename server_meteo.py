from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

date_senzori = {
    "temp": 0,
    "hum": 0,
    "co2": 0
}

@app.route('/update', methods=['POST'])
def update():
    global date_senzori
    date_senzori = request.json
    print(f"Date noi primite: {date_senzori}")
    return jsonify({"status": "succes"})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(date_senzori)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
