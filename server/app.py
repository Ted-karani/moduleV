from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
inventory = [
    {"id": 1, "name": "Organic Almond Milk", "brand": "Silk", "price": 3.99, "stock": 50},
    {"id": 2, "name": "Whole Wheat Bread", "brand": "Nature's Own", "price": 2.49, "stock": 30},
    {"id": 3, "name": "Orange Juice", "brand": "Tropicana", "price": 4.99, "stock": 20}
]


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):
    item = next((i for i in inventory if i["id"] == id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item isnt found"}), 404


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()
    new_id = len(inventory) + 1
    new_item = {
        "id": new_id,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
    }
    inventory.append(new_item)
    return jsonify(new_item), 201


@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):
    item = next((i for i in inventory if i["id"] == id), None)
    if item:
        data = request.get_json()
        if "name" in data:
            item["name"] = data["name"]
        if "brand" in data:
            item["brand"] = data["brand"]
        if "price" in data:
            item["price"] = data["price"]
        if "stock" in data:
            item["stock"] = data["stock"]
        return jsonify(item), 200
    return jsonify({"error": "Item isnt found"}), 404


@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = next((i for i in inventory if i["id"] == id), None)
    if item:
        inventory.remove(item)
        return jsonify({"message": "Item its deleted"}), 200
    return jsonify({"error": "Item isnt found"}), 404

#supposed to use barcode from the api, this is lowkey hard lemme chack canvas.

@app.route("/fetch/<string:barcode>", methods=["GET"])
def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"
    response = requests.get(url,headers={"User-Agent": "InventoryApp/1.0"})
    data = response.json()

    if data["status"] == "failure":
        return jsonify({"error": "Product not found"}), 404

    product = data["product"]

    result = {
         "name": product["product_name"],
         "brand": product["brands"],
         "ingredients": product["ingredients_text"]
    }

    return jsonify(result), 200


@app.route("/fetch/<string:barcode>/add", methods=["POST"])
def fetch_and_add(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"
    response = requests.get(url,headers={"User-Agent": "InventoryApp/1.0"})
    data = response.json()

    if data["status"] == "failure":
        return jsonify({"error": "Product not found"}), 404

    product = data["product"]

    new_id = len(inventory) + 1
    new_item = {
         "id": new_id,
         "name": product["product_name"],
         "brand": product["brands"],
         "price": 0.00,
         "stock": 0
    }

    inventory.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)