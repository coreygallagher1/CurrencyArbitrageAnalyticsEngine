from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-profit', methods=['POST'])
def calculate_profit():
    opportunity = request.json
    transaction_fee_percentage = 0.01  # Example transaction fee: 1%

    gross_profit = opportunity['profit']
    # Calculating net profit after subtracting transaction fees
    net_profit = gross_profit - (gross_profit * transaction_fee_percentage)

    return jsonify({'currency_pair': opportunity['currency_pair'], 'net_profit': net_profit})

if __name__ == '__main__':
    app.run(port=5003, debug=True)
