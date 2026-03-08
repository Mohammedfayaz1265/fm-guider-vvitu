from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import json
import os

app = Flask(__name__, template_folder='.')

with open('college_data.json', 'r') as f:
    college_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html', college=college_data)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'response': 'Please type a message! 😊'})
    response = get_response(user_message, college_data)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
