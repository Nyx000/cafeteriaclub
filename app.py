# Standard library imports
import logging
from datetime import datetime
import os

# Third-party library imports
from flask import Flask, render_template, jsonify, request
import json
from user_agents import parse

app = Flask(__name__)

def get_menu_data():
    return [
        {"id": 1, "name": "Burger", "price": 8.99},
        {"id": 2, "name": "Pizza", "price": 10.99},
        {"id": 3, "name": "Salad", "price": 6.99}
    ]

    
    log_message = json.dumps(visit_data)
    logging.info(log_message)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/menu')
def get_menu():
    menu = get_menu_data()
    return jsonify(menu)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
