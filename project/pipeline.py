import requests
import pandas as pd
import io
import os

def fetch_csv_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        csv_data = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_data))
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None

def save_dataframe_to_csv(df, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

csv_url = "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv"
csv_url2 = "https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv"

dataframe = fetch_csv_from_url(csv_url)
dataframe1 = fetch_csv_from_url(csv_url2)

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

if dataframe is not None:
    print(dataframe.head())
    save_path = os.path.join(data_dir, 'surfaceTemperature.csv')
    save_dataframe_to_csv(dataframe, save_path)

if dataframe1 is not None:
    print(dataframe1.head())
    save_path = os.path.join(data_dir, 'disasterFrequency.csv')
    save_dataframe_to_csv(dataframe1, save_path)

import os
import pandas as pd

import os
import pandas as pd

import os
import pandas as pd

def merge_csv_files(file1, file2, drop_columns, save_path, output_filename):
    try:

        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
 
        df1 = df1.drop(columns=[col for col in drop_columns if col not in ['Country', 'ISO3', 'Indicator']], errors='ignore')
        df2 = df2.drop(columns=[col for col in drop_columns if col not in ['Country', 'ISO3', 'Indicator']], errors='ignore')

        columns_to_drop = [f'F{year}' for year in range(1961, 1980)]
        df2 = df2.drop(columns=columns_to_drop, errors='ignore')

        start_year = 1980
        end_year = 2022
        temperature_columns = [f'F{year}' for year in range(start_year, end_year + 1)]
        disaster_columns = [f'F{year}' for year in range(start_year, end_year + 1)]

        df2 = df2[['Country', 'ISO3', 'Indicator'] + temperature_columns]
        df1 = df1[['Country', 'ISO3', 'Indicator'] + disaster_columns]

        common_countries = set(df2['Country']).intersection(set(df1['Country']))
        df2 = df2[df2['Country'].isin(common_countries)]
        df1 = df1[df1['Country'].isin(common_countries)]

        numeric_columns = df1.select_dtypes(include=[float, int]).columns.tolist()
        df1_aggregated = df1.groupby('Country')[numeric_columns].mean().reset_index()

        merged_df = pd.merge(df2, df1_aggregated, on='Country', suffixes=('_temp', '_disaster'))

        os.makedirs(save_path, exist_ok=True)
        output_file = os.path.join(save_path, output_filename)
        merged_df.to_csv(output_file, index=False)

        print(f"Data successfully merged and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

file1 = os.path.join(data_dir, 'disasterFrequency.csv')
file2 = os.path.join(data_dir, 'surfaceTemperature.csv')
drop_columns = ['ObjectId', 'ISO2', 'Unit', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor']
save_path = data_dir
output_filename = 'mergedCSV.csv'

merge_csv_files(file1, file2, drop_columns, save_path, output_filename)


import sqlite3

def save_csv_to_sqlite(csv_file_path, db_path, table_name):
    try:
        df = pd.read_csv(csv_file_path)
        
        conn = sqlite3.connect(db_path)
        
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        df_from_db = pd.read_sql(f'SELECT * FROM {table_name}', conn)
        
        conn.close()
        
        print(f"Data successfully saved to the {table_name} table in {db_path}")
        return df_from_db 
    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.close()

csv_file_path = os.path.join(data_dir, 'mergedCSV.csv')
db_path = os.path.join(data_dir, 'merged_data.db')
table_name = 'merged_data'

df_from_db = save_csv_to_sqlite(csv_file_path, db_path, table_name)
