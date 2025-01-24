# Serwer (Flask - HTTP RPC)
from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []  # Przykładowa wspólna baza danych dla klientów

@app.route("/add", methods=["POST"])
def add_item():
    """Dodawanie elementu do wspólnej bazy danych."""
    item = request.json.get("item")
    if not item:
        return jsonify({"error": "No item provided"}), 400

    data_store.append(item)
    return jsonify({"message": "Item added", "data": data_store}), 200

@app.route("/list", methods=["GET"])
def list_items():
    """Pobieranie wszystkich elementów."""
    return jsonify({"data": data_store}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
