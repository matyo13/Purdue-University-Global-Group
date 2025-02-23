# Purdue Boilermake XII Project

## Repository Structure
- `Anti-Phish AI/`: Contains the Chrome extension files.
- `model-training/`: Contains the model training files.
- `server/`: Contains the Flask application for serving the model.

## Setup Instructions

### Chrome Extension
1. Navigate to `Anti-Phish AI/`.
2. Open Chrome and go to `chrome://extensions/`.
3. Enable "Developer mode" using the toggle switch in the top right corner.
4. Click "Load unpacked" and select the `Anti-Phish AI/` folder.

### Model Training
1. Navigate to `model-training/`.
2. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
3. Setup Kaggle API:
    - Go to your Kaggle account settings and create a new API token. This will download a kaggle.json file.
    - On Windows, place the kaggle.json file in the 'C:\Users\YourUsername\.kaggle directory'
4. Download and unzip the dataset from Kaggle
    ```sh
    python script/download_dataset.py
5. Train the model
    ```sh
    python script/training_model.py
6. Run the predict script to test the model
    ```sh
    python script/predict.py
    
### Flask Server
1. Navigate to `server/`
2. Install the necessary dependencies
    ```sh
    pip install -r requirements.txt
3. Run the flask server
    ```sh
    python app.py

## Using the Chrome Extension with the Flask Server
1. Ensure the flask server is running.
2. Use the Chrome extension to extract email content from Gmail.
3. The extension will send the extracted email content to the Flask server for prediction.
4. The prediction result (Phishing or Legitimate) will be displayed in the extension popup.

## File Descriptions

### Chrome Extension Files
- `Anti-Phish AI/manifest.json`: Configuration file for the Chrome extension.
- `Anti-Phish AI/styles.css`: Styles for the extension popup.
- `Anti-Phish AI/popup.html`: HTML for the extension popup.
- `Anti-Phish AI/popup.js`: JavaScript for handling user interactions in the popup.
- `Anti-Phish AI/content.js`: JavaScript for extracting email content from Gmail.

### Model Training Files
- `model-training/data/test_data/test_data.csv`: Test data for model evaluation.
- `model-training/models/trained_model.pkl`: Trained machine learning model.
- `model-training/models/vectorizer.pkl`: Vectorizer used for text transformation.
- `model-training/requirements.txt`: Dependencies for model training.
- `model-training/scripts/download_dataset.py`: Script to download and unzip the dataset from Kaggle.
- `model-training/scripts/predict.py`: Script to make predictions using the trained model.
- `model-training/scripts/training_model.py`: Script to train the machine learning model.

### Flask Server Files
- `server/app.py`: Flask application to serve the model and handle prediction requests.
- `server/requirements.txt`: Dependencies for the Flask server.