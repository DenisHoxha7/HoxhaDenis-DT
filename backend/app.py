from flask import Flask, request, jsonify
from flask_cors import CORS
from DatabaseWrapper import DatabaseWrapper

app = Flask(__name__)
# Abilitiamo CORS per far parlare Angular e Flask
CORS(app)

db = DatabaseWrapper()

@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    """Endpoint per leggere le consegne dal Wrapper"""
    try:
        data = db.get_all_deliveries()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deliveries', methods=['POST'])
def add_delivery():
    """Endpoint per inserire una consegna tramite il Wrapper"""
    data = request.json
    if not data or not data.get('tracking_code'):
        return jsonify({"error": "Dati obbligatori mancanti"}), 400
    
    try:
        db.add_delivery(data)
        return jsonify({"message": "Consegna inserita"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Inizializza la tabella all'avvio
    db.init_database()
    app.run(debug=True, port=5000)