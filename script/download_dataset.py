import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_unzip_dataset(dataset, download_path, unzip_path):
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download dataset
    api.dataset_download_files(dataset, path=download_path, unzip=True)

    # Unzip dataset
    for file in os.listdir(download_path):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(download_path, file), 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

if __name__ == '__main__':
    dataset = 'naserabdullahalam/phishing-email-dataset'
    download_path = 'data/raw/'
    unzip_path = 'data/raw/'
    download_and_unzip_dataset(dataset, download_path, unzip_path)
