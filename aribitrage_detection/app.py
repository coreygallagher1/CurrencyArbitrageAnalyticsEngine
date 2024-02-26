from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PROFIT_CALCULATION_SERVICE_URL = 'http://localhost:5003/calculate-profit'

@app.route('/detect-arbitrage', methods=['POST'])
def detect_arbitrage():
    data = request.json
    # Placeholder for arbitrage detection logic
    opportunities = [{'currency_pair': 'EUR/USD', 'profit': 0.01}]

    # Send opportunities to the Profit Calculation Service
    profit_responses = [requests.post(PROFIT_CALCULATION_SERVICE_URL, json=opportunity) for opportunity in opportunities]
    profits = [response.json() for response in profit_responses]

    return jsonify(profits)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
