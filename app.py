from flask import Flask, jsonify, abort
import os

app = Flask(__name__)

# A simulated database of customers
CUSTOMERS = {
    1: {
        "id": "CUST-98765",
        "name": "Karthik",
        "email": "karthik@g.com",
        "membership": "premium",
        "status": "Active"
    },
    2: {
        "id": "CUST-11223",
        "name": "Raj",
        "email": "raj@example.com",
        "membership": "regular",
        "status": "Active"
    }
}

# 🟢 New Dynamic Endpoint: <int:customer_id> captures whatever number is in the URL
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    # Look up the customer ID in our simulated database
    customer = CUSTOMERS.get(customer_id)
    
    # SYSTEM DESIGN BEST PRACTICE: If it doesn't exist, return a proper 404 status code
    if not customer:
        return jsonify({"error": "Customer not found", "requested_id": customer_id}), 404
        
    return jsonify(customer), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
