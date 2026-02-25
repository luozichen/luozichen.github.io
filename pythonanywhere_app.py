from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
# Enable CORS restricted to the GitHub Pages domain
CORS(app, resources={r"/api/*": {"origins": "https://luozichen.github.io"}})

# We will store the count in a simple JSON file
COUNTER_FILE = os.path.join(os.path.dirname(__file__), 'counter.json')

def get_count():
    if not os.path.exists(COUNTER_FILE):
        return 0
    try:
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
            return data.get('count', 0)
    except Exception as e:
        print(f"Error reading count: {e}")
        return 0

def save_count(count):
    try:
        with open(COUNTER_FILE, 'w') as f:
            json.dump({'count': count}, f)
    except Exception as e:
        print(f"Error saving count: {e}")

@app.route('/api/counter', methods=['GET'])
def counter():
    count = get_count()
    count += 1
    save_count(count)
    return jsonify({"count": count})

# Add a simple health check route
@app.route('/', methods=['GET'])
def home():
    return "Visitor Counter API is running!"

if __name__ == '__main__':
    app.run(debug=True)
