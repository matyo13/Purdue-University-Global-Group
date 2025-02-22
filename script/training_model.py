import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(data_file):
    # Load the dataset
    data = pd.read_csv(data_file)
    
    # Separate features and target variable
    X = data['text_combined']
    y = data['label']
    
    # Text vectorization
    vectorizer = TfidfVectorizer(max_features=10000)
    X_vectorized = vectorizer.fit_transform(X)
    
    # Split the data
    X_train, X_val_test, y_train, y_val_test = train_test_split(X_vectorized, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Validate model
    y_val_pred = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, y_val_pred)
    print(f'Validation Accuracy: {val_accuracy}')
    print(classification_report(y_val, y_val_pred))

    # Test model
    y_test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f'Test Accuracy: {test_accuracy}')
    print(classification_report(y_test, y_test_pred))

    # Save the model
    joblib.dump(model, '../Purdue-University-Global-Group/models/trained_model.pkl')
    joblib.dump(vectorizer, '../Purdue-University-Global-Group/models/vectorizer.pkl')

if __name__ == '__main__':
    train_model('../Purdue-University-Global-Group/data/raw/phishing_email.csv')

