# Purdue-University-Global-Group
Repository for BoilerMake XII

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/<yourusername>/Purdue-University-Global-Group.git
    cd Purdue-University-Global-Group

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

3. Setup Kaggle API:
    - Go to your Kaggle account settings and create a new API token. This will download a kaggle.json file.
    - On Windows, place the kaggle.json file in the C:\Users\YourUsername\.kaggle directory
    - Place the kaggle.json file in the root directory of this project.
        On Unix-based systems (macOS or Linux):
        ```bash
        mkdir ~/.kaggle
        mv ~/Downloads/kaggle.json ~/.kaggle/
        chmod 600 ~/.kaggle/kaggle.json

4. Download and unzip the dataset from Kaggle
    ```bash
    python script/download_dataset.py

5. Train the model
    ```bash
    python script/training_model.py

6. Run the predict script to test the model
    ```bash
    python script/predict.py