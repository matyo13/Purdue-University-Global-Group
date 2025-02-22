import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Ensure necessary downloads
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# File paths
files = [
    "data/Phishing_Email_Dataset/CEAS_08.csv",
    "data/Phishing_Email_Dataset/Enron.csv",
    "data/Phishing_Email_Dataset/Ling.csv",
    "data/Phishing_Email_Dataset/Nazario.csv",
    "data/Phishing_Email_Dataset/Nigerian_Fraud.csv"
]

# Load datasets
dfs = [pd.read_csv(file, encoding="latin1", on_bad_lines='skip') for file in files]

# Merge all datasets
df = pd.concat(dfs, ignore_index=True)

# Keep relevant columns and drop NaN values
df = df[['subject', 'body', 'label']].dropna()

# Ensure label is numeric (convert string labels if needed)
df['label'] = df['label'].astype(int)

# Preprocessing function
def preprocess_text(text):
    if pd.isna(text):  # Handle missing values
        return ''
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)  # Tokenize
    stop_words = set(stopwords.words('english'))  # Convert stopwords to set for efficiency
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing
df['clean_text'] = df['subject'].fillna('') + ' ' + df['body'].fillna('')
df['clean_text'] = df['clean_text'].apply(preprocess_text)

# Feature extraction
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text']).toarray()
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Feature extraction complete!")

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model saved!")

# Prediction function
def predict_email(email_subject, email_body):
    email_text = preprocess_text(email_subject + " " + email_body)
    email_features = vectorizer.transform([email_text]).toarray()
    prediction = model.predict(email_features)
    return "Phishing Email" if prediction[0] == 1 else "Legitimate Email"

email1 = """ 
Dear Ben

Thank you for shopping with TechGear! We’re happy to confirm that your order has been successfully placed. Below are your order details:

Order Summary:

Order Number: TG123456
Item(s): Wireless Bluetooth Headphones
Total Amount: $79.99
Shipping Address: 123 Main Street, City, State, ZIP
Estimated Delivery: March 2, 2025
You can track your order or make any changes by visiting your account:

🔗 Track My Order

If you have any questions, feel free to reply to this email or contact our support team at support@techgear.com.

Thank you for choosing TechGear!

Best regards,
TechGear Customer Support
📧 support@techgear.com | 📞 (555) 123-4567
🔗 www.techgear.com"""

email2 = """
Dear Ben,

We received a request to reset your password for your SecureBank account. If you made this request, please click the link below to reset your password:

🔗 Reset My Password

For security reasons, this link will expire in 30 minutes. If you did not request a password reset, you can safely ignore this email.

If you need further assistance, please contact our support team at support@securebank.com or call us at (800) 555-6789.

Best regards,
SecureBank Customer Support
📧 support@securebank.com | 📞 (800) 555-6789
🔗 www.securebank.com

"""

email3 = """
Subject: 📦 Order Confirmation - Your Package is on the Way!

Hello Ben,

Thank you for your purchase! Your order has been successfully processed and will be shipped soon.

Order Details:

Order ID: #A239812390
Amount: $899.99
Shipping Address: 594N Meridian St, Indianapolis 46028
If you did not authorize this transaction, please cancel your order immediately:

🔗 Cancel Order Now

Thank you for shopping with us!

Amazon Support Team"""

email4 = """
Dear Ben,

We hope you’re enjoying your Premium Membership with StreamFlix! Your subscription is set to renew on March 15, 2025, for $9.99/month.

No action is required if you wish to continue enjoying unlimited streaming. However, if you’d like to update your payment details or manage your subscription, please visit:

🔗 Manage Subscription

If you have any questions, feel free to contact our support team at support@streamflix.com.

Thank you for being a valued member of StreamFlix!

Best regards,
StreamFlix Support Team
📧 support@streamflix.com | 🔗 www.streamflix.com
"""
# Test with an example
print(predict_email("Your Recent Purchase from TechGear – Order #TG123456", email1))
print(predict_email("Password Reset Request for Your Account", email2))
print(predict_email("Order Confirmation - Your Package is on the Way!", email3))
print(predict_email("Your Premium Subscription is Renewing Soon", email4))

