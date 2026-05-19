from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite site-ului sa acceseze serverul

# Variabila globala unde tinem ultimele date primite
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
    # Ruleaza pe IP-ul local al Raspberry Pi pe portul 5000
    app.run(host='0.0.0.0', port=5000)