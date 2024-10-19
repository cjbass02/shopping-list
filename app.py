from flask import Flask, request, jsonify, render_template
from service import ShoppingListService
from models import Schema

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def home():
    return render_template('index.html')  # Serve the front-end web page

@app.route("/shopping-list", methods=["GET"])
def list_items():
    return jsonify(ShoppingListService().list())

@app.route("/shopping-list", methods=["POST"])
def create_item():
    return jsonify(ShoppingListService().create(request.get_json()))

@app.route("/shopping-list/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ShoppingListService().update(item_id, request.get_json()))

@app.route("/shopping-list/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify(ShoppingListService().get_by_id(item_id))

@app.route("/shopping-list/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ShoppingListService().delete(item_id))

if __name__ == "__main__":
    Schema()  # Initialize the database schema
    app.run(debug=True, host="0.0.0.0", port=5000)
