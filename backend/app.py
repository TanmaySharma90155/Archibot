from flask import Flask, render_template, request
from services.gemini import get_gemini_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.get('user_input', '')
    ai_response = get_gemini_response(user_input)
    return ai_response

if __name__ == '__main__':
    app.run(debug=True)