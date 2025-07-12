from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/checkout', methods=['POST'])
def checkout():
    """
    API endpoint to process a checkout.
    Expects a JSON payload with a list of items.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    items = data.get('items')

    if not items or not isinstance(items, list):
        return jsonify({"error": "Missing or invalid 'items' list in payload"}), 400

    print("--- CHECKOUT RECEIVED ---")
    print(f"Processing checkout for {len(items)} item(s).")
    # In a real application, you would process payment, update inventory, etc.
    # For this demo, we just print the items.
    print(json.dumps(items, indent=2))
    print("-------------------------")

    return jsonify({"message": "Purchase successful! Thank you for your order."})

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000