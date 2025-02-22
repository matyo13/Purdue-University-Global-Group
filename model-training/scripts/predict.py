import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_model_and_vectorizer(model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict_emails(model, vectorizer, emails):
    # Vectorize the input emails
    emails_vectorized = vectorizer.transform(emails)
    # Make predictions
    predictions = model.predict(emails_vectorized)
    return predictions

if __name__ == '__main__':
    # Get the absolute paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, '../models/trained_model.pkl')
    vectorizer_path = os.path.join(base_dir, '../models/vectorizer.pkl')
    test_data_path = os.path.join(base_dir, '../data/test_data/test_data.csv')

    # Load the model and vectorizer
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)

    # Load the synthetic test data
    test_df = pd.read_csv(test_data_path)

    # Predict whether the emails are phishing or not
    predictions = predict_emails(model, vectorizer, test_df['text_combined'])
    for email, prediction in zip(test_df['text_combined'], predictions):
        print(f"Email: {email}\nPrediction: {'Phishing' if prediction == 1 else 'Legitimate'}\n")