from flask import Flask, jsonify, render_template, request
import yfinance as yf
import pandas as pd

app = Flask(__name__)

def get_index_data(index_symbol, days=30):
    try:
        index = yf.Ticker(index_symbol)
        data = index.history(period=f"{days}d")
        return data
    except Exception as e:
        print(f"Error fetching {index_symbol} data:", e)
        return None

@app.route('/get_sp500_data')
def get_sp500_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        try:
            sp500 = yf.Ticker("^GSPC")
            data = sp500.history(start=start_date, end=end_date)
            data_json = data.reset_index().to_json(orient='records')  # Convert DataFrame to JSON
            return data_json
        except Exception as e:
            print("Error fetching S&P 500 data:", e)
            return jsonify({'error': 'Failed to fetch data'})
    else:
        data = get_index_data("^GSPC")
        if data is not None:
            data_json = data.reset_index().to_json(orient='records')  # Convert DataFrame to JSON
            return data_json
        else:
            return jsonify({'error': 'Failed to fetch data'})

@app.route('/get_dowjones_data')
def get_dowjones_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        try:
            dowjones = yf.Ticker("^DJI")
            data = dowjones.history(start=start_date, end=end_date)
            data_json = data.reset_index().to_json(orient='records')
            return data_json
        except Exception as e:
            print("Error fetching Dow Jones data:", e)
            return jsonify({'error': 'Failed to fetch data'})
    else:
        data = get_index_data("^DJI")
        if data is not None:
            data_json = data.reset_index().to_json(orient='records')
            return data_json
        else:
            return jsonify({'error': 'Failed to fetch data'})

@app.route('/get_nasdaq_data')
def get_nasdaq_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        try:
            nasdaq = yf.Ticker("^IXIC")
            data = nasdaq.history(start=start_date, end=end_date)
            data_json = data.reset_index().to_json(orient='records')
            return data_json
        except Exception as e:
            print("Error fetching NASDAQ data:", e)
            return jsonify({'error': 'Failed to fetch data'})
    else:
        data = get_index_data("^IXIC")
        if data is not None:
            data_json = data.reset_index().to_json(orient='records')
            return data_json
        else:
            return jsonify({'error': 'Failed to fetch data'})

@app.route('/')
def index():
    return render_template('webpage.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
