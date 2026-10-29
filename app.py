from flask import Flask, jsonify, request
app = Flask(__name__)
inventory = {}
@app.get("/")
def home():
    return jsonify({"application":"Medical Store","version":"v1","feature":"Add Medicine"})
@app.get("/health")
def health():
    return jsonify({"status":"healthy","version":"v1"})
@app.post("/medicines")
def add_medicine():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    quantity = data.get("quantity")
    if not name or not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
        return jsonify({"error":"Provide a name and a non-negative integer quantity"}), 400
    key = name.lower()
    if key in inventory:
        return jsonify({"error":"Medicine already exists"}), 409
    inventory[key] = {"name":name,"quantity":quantity}
    return jsonify({"message":"Medicine added","medicine":inventory[key]}), 201
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)