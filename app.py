from flask import Flask, render_template, request
from flask import Blueprint
# Import kode chatbot yang telah Anda buat sebelumnya
from chatAI import get_best_answer
# Pastikan Anda memiliki kode chatbot dalam file yang sama atau import kode tersebut dengan benar.


static_bp = Blueprint('static', __name__, static_folder='static', static_url_path='/static')

app = Flask(__name__)
app.static_folder = 'static'  # Sesuaikan dengan nama folder tempat Anda menyimpan file CSS

@app.route('/test-css')
def test_css():
    return app.send_static_file('css/styles.css')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_best_answer(user_input)  # Gantilah dengan fungsi chatbot Anda sendiri
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
