from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/customer', methods=['GET'])
def get_customer_details():
    customer_data = {
        "id": "CUST-98765",
        "name": "Karthik",
        "email": "karthik@g.com",
        "membership": "premium",
        "status": "Active"
    }
    return jsonify(customer_data), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)