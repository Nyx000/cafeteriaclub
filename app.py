# Standard library imports
import logging
from datetime import datetime

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

def log_visit():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.remote_addr
    user_agent_string = request.user_agent.string
    user_agent = parse(user_agent_string)
    
    visit_data = {
        "timestamp": current_time,
        "ip_address": ip_address,
        "path": request.path,
        "method": request.method,
        "user_agent": {
            "browser": user_agent.browser.family,
            "browser_version": user_agent.browser.version_string,
            "os": user_agent.os.family,
            "device": user_agent.device.family,
            "is_mobile": user_agent.is_mobile,
            "is_tablet": user_agent.is_tablet,
            "is_pc": user_agent.is_pc,
            "is_bot": user_agent.is_bot
        },
        "referrer": request.referrer
    }
    
    log_message = json.dumps(visit_data)
    logging.info(log_message)

@app.route('/')
def home():
    log_visit()
    return render_template('index.html')

@app.route('/api/menu')
def get_menu():
    menu = get_menu_data()
    return jsonify(menu)

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(filename='visits.log', level=logging.INFO)
    app.run(debug=True)