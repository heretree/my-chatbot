from flask import Flask, render_template, request, jsonify

from chatbot import MyChatBot


app = Flask(__name__)
chat = MyChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    # Replace the following line with your code to get a response from langchain
    response = chat.ask(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()