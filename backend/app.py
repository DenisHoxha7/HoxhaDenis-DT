from flask import Flask, request, jsonify
from flask_cors import CORS
from DatabaseWrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app) # Fondamentale per la velocità di comunicazione
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
    try:
        data = request.json
        db.add_delivery(data)
        return jsonify({"status": "created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deliveries/<int:delivery_id>/status', methods=['PUT'])
def update_status(delivery_id):
    try:
        nuovo_stato = request.json.get('stato')
        db.update_status(delivery_id, nuovo_stato)
        return jsonify({"status": "updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    db.init_database()
    app.run(debug=True, port=5000)