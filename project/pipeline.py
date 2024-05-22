import requests
import pandas as pd
import io
import os


def fetch_csv_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        csv_data = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_data))
        
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None

def save_dataframe_to_csv(df, file_path):
    try:
        df.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# URL of the CSV file
csv_url = "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv"
csv_url2= "https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv"

# Fetch CSV data from URL
dataframe = fetch_csv_from_url(csv_url)
dataframe1 = fetch_csv_from_url(csv_url2)

if dataframe is not None:
    # Display first few rows of the DataFrame
    print(dataframe.head())
    
    # Save DataFrame to local CSV file (optional)
    save_path = "./data/surfaceTemperature.csv"
    save_dataframe_to_csv(dataframe, save_path)

if dataframe1 is not None:
    # Display first few rows of the DataFrame
    print(dataframe.head())
    
    # Save DataFrame to local CSV file (optional)
    save_path = "./data/disasterFrequency.csv"
    save_dataframe_to_csv(dataframe1, save_path)


def merge_csv_files(file1, file2, drop_columns, save_path, output_filename):
 
    try:
        # Load the CSV files into DataFrames
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        
        # Drop specified columns from both DataFrames
        df1 = df1.drop(columns=drop_columns, errors='ignore')
        df2 = df2.drop(columns=drop_columns, errors='ignore')
        
        # Merge the DataFrames
        merged_df = pd.concat([df1, df2], ignore_index=True)
        
        # Ensure the save directory exists
        os.makedirs(save_path, exist_ok=True)
        
        # Create the full path for the output file
        output_file = os.path.join(save_path, output_filename)
        
        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv(output_file, index=False)
        print(f"Data successfully merged and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file1 = './data/disasterFrequency.csv'
file2 = './data/surfaceTemperature.csv'
drop_columns = ['ObjectId','Country','ISO2','ISO3','Indicator', 'Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor']
save_path = './data/'
output_filename = 'mergedCSV.csv'

merge_csv_files(file1, file2, drop_columns, save_path, output_filename)

csv = pd.read_csv("./data/mergedCSV.csv")
print(csv.isnull().sum)
