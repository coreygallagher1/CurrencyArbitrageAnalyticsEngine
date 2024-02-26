from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect-arbitrage', methods=['POST'])
def detect_arbitrage():
    data = request.json
    opportunities = []

    # Example arbitrage detection logic
    if 'EUR' in data['rates'] and 'USD' in data['rates']:
        eur_to_usd = data['rates']['USD']
        usd_to_eur = 1 / data['rates']['EUR']

        # Simulating a condition where converting EUR to USD and back to EUR results in a profit
        if eur_to_usd * usd_to_eur > 1.05:
            opportunities.append({
                'currency_pair': 'EUR/USD',
                'profit': eur_to_usd * usd_to_eur - 1
            })

    return jsonify(opportunities)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
