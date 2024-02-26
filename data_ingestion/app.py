from flask import Flask
import requests

app = Flask(__name__)

@app.route('/fetch-data')
def fetch_data():
    # Example API call to fetch currency data
    response = requests.get('https://api.exchangeratesapi.io/latest')
    return response.json()

if __name__ == '__main__':
    app.run(port=5001, debug=True)
