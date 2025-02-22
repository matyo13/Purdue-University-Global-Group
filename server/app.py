from flask import Flask, request, jsonify
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), '../model-training/models/trained_model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../model-training/models/vectorizer.pkl')
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email_content = data['email_content']
    email_vectorized = vectorizer.transform([email_content])
    prediction = model.predict(email_vectorized)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)