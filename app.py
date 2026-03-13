from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

# Safely load college data
DATA_FILE = os.path.join(BASE_DIR, 'college_data.json')
college_data = {}

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        college_data = json.load(f)
else:
    print(f"Warning: {DATA_FILE} not found. Knowledge base is empty.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'response': 'Please type a message! 😊'})
        
    try:
        response = get_response(user_message, college_data)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({'response': '⚠️ Internal server error. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
