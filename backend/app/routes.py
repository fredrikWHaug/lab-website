from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, world!"})

@api.route("/api/test", methods=["GET"])
def test_api():
    # Simulate JSON data
    data = {
        "name": "Test API",
        "status": "success",
        "items": ["item1", "item2", "item3"]
    }
    return jsonify(data)
