from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
inventory = [
    {"id": 1, "name": "Organic Almond Milk", "brand": "Silk", "price": 3.99, "stock": 50},
    {"id": 2, "name": "Whole Wheat Bread", "brand": "Nature's Own", "price": 2.49, "stock": 30},
    {"id": 3, "name": "Orange Juice", "brand": "Tropicana", "price": 4.99, "stock": 20}
]

if __name__ == '__main__':
    app.run(debug=True)