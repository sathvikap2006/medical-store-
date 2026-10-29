from flask import Flask, jsonify, request
app = Flask(__name__)
inventory = {}

@app.get("/")
def home():
    return jsonify({"application":"Medical Store","version":"v2","features":["Add Medicine","Update Quantity"]})

@app.get("/health")
def health():
    return jsonify({"status":"healthy","version":"v2"})

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

@app.put("/medicines/<name>")
def update_quantity(name):
    data = request.get_json(silent=True) or {}
    quantity = data.get("quantity")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
        return jsonify({"error":"Quantity must be a non-negative integer"}), 400
    key = name.lower()
    if key not in inventory:
        return jsonify({"error":"Medicine not found"}), 404
    inventory[key]["quantity"] = quantity
    return jsonify({"message":"Quantity updated","medicine":inventory[key]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
