import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import requests
import zipfile
import chardet

class DataLoader:
    def __init__(self, link):
        """
        Initializes the DataLoader with a Google Drive link to the zip file.
        
        Args:
            link (str): The Google Drive link to the zip file.
        """
        self.link = link
        self.file_id = self.extract_file_id(link)
        self.download_url = f'https://drive.google.com/uc?id={self.file_id}&export=download'

    def extract_file_id(self, link):
        """
        Extracts the file ID from the Google Drive link.
        
        Args:
            link (str): The Google Drive link to the zip file.
        
        Returns:
            str: The file ID.
        """
        return link.split('/')[-2]

    def load_data_from_drive_zip(self, link):
        """
        Loads data from a zip file on Google Drive containing a text file with pipe-separated data.
        
        Args:
            link (str): The Google Drive link to the zip file.
        
        Returns:
            pandas.DataFrame: The data as a pandas DataFrame.
        """
        try:
            # Extract the file ID from the link
            file_id = link.split('/')[-2]
            
            # Construct the download URL
            download_url = f'https://drive.google.com/uc?id={file_id}&export=download'


            # Download the zip file
            response = requests.get(download_url)
            response.raise_for_status()  # Raise an exception for bad responses

            # Extract the text file from the zip
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                text_file_name = z.namelist()[0]  # Assuming only one file in the zip
                with z.open(text_file_name) as text_file:
                    # Detect encoding
                    rawdata = text_file.read(10000)
                    encoding = chardet.detect(rawdata)['encoding']
                    print(f"Detected encoding: {encoding}")
                    
                    # Read the data into a pandas DataFrame
                    text_file.seek(0)  # Reset file pointer
                    df = pd.read_csv(text_file, sep='|', encoding=encoding)
                    
            return df

        except Exception as e:
            print(f"Error loading data: {e}")
            return None