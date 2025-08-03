from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from services.gemini import get_gemini_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('user_input', '') if data else ''
    ai_response = get_gemini_response(user_input)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)