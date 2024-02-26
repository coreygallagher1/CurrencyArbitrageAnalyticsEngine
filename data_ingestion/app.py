from flask import Flask, jsonify
import requests

app = Flask(__name__)

ARBITRAGE_DETECTION_SERVICE_URL = 'http://localhost:5002/detect-arbitrage'

@app.route('/fetch-and-send-data', methods=['GET'])
def fetch_and_send_data():
    # Fetch currency data from an external API
    response = requests.get('https://api.exchangeratesapi.io/latest')
    currency_data = response.json()

    # Send the fetched data to the Arbitrage Detection Service
    arbitrage_response = requests.post(ARBITRAGE_DETECTION_SERVICE_URL, json=currency_data)
    arbitrage_opportunities = arbitrage_response.json()

    return jsonify(arbitrage_opportunities)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
