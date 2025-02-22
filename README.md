# Purdue University Global Group Project

## Overview
This project includes a Chrome extension that scans emails for potential phishing attempts using a trained machine learning model. The model is served via a Flask application hosted on an AWS server.

## Repository Structure
- `chrome-extension/`: Contains the Chrome extension files.
- `model-training/`: Contains the model training files.
- `server/`: Contains the Flask application for serving the model.

## Setup Instructions

### Chrome Extension
1. Navigate to `chrome-extension/`.
2. Open Chrome and go to `chrome://extensions/`.
3. Enable "Developer mode" using the toggle switch in the top right corner.
4. Click "Load unpacked" and select the `chrome-extension/` folder.

### Model Training
1. Navigate to `model-training/`.

2. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt

3. Setup Kaggle API:
    - Go to your Kaggle account settings and create a new API token. This will download a kaggle.json file.
    - On Windows, place the kaggle.json file in the C:\Users\YourUsername\.kaggle directory

4. Download and unzip the dataset from Kaggle
    ```sh
    python script/download_dataset.py

5. Train the model
    ```sh
    python script/training_model.py

6. Run the predict script to test the model
    ```sh
    python script/predict.py