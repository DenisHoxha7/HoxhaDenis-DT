from flask import Flask, request, jsonify
from flask_cors import CORS
from DatabaseWrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)
db = DatabaseWrapper()

@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    try:
        data = db.get_all_deliveries()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deliveries', methods=['POST'])
def add_delivery():
    data = request.json
    # Validazione base
    if not data.get('tracking_code') or not data.get('destinatario'):
        return jsonify({"error": "Dati mancanti"}), 400
    try:
        db.add_delivery(data)
        return jsonify({"message": "Successo"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    db.init_table()
    app.run(debug=True, port=5000)