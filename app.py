from flask import Flask, render_template, request
from flask import Blueprint
# Import kode chatbot
from chatAI import get_best_answer



static_bp = Blueprint('static', __name__, static_folder='static', static_url_path='/static')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_best_answer(user_input)  # fungsi chatbot Yang ada di dalam chatAI
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
