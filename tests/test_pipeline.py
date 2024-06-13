import unittest
from unittest.mock import patch, MagicMock, call
import pandas as pd
import os
import requests

from project.pipeline import fetch_csv_from_url, save_dataframe_to_csv, merge_csv_files, save_csv_to_sqlite

class TestPipelineMethods(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_csv_from_url(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'col1,col2\n1,2\n3,4'
        
        url = 'https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv'
        df = fetch_csv_from_url(url)
        
        expected_df = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
        pd.testing.assert_frame_equal(df, expected_df)
        
        mock_get.return_value.content = b'col1,col2\n5,6\n7,8'
        
        url2 = 'https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv'
        df2 = fetch_csv_from_url(url2)
        
        expected_df2 = pd.DataFrame({'col1': [5, 7], 'col2': [6, 8]})
        pd.testing.assert_frame_equal(df2, expected_df2)
        
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
        
        df = fetch_csv_from_url(url)
        self.assertIsNone(df)

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv(self, mock_to_csv, mock_makedirs):
        df = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
        file_path = 'test_dir/test.csv'
        
        save_dataframe_to_csv(df, file_path)
        
        mock_makedirs.assert_called_once_with(os.path.dirname(file_path), exist_ok=True)
        mock_to_csv.assert_called_once_with(file_path, index=False)
        
    @patch('pandas.read_csv')
    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_merge_csv_files(self, mock_to_csv, mock_makedirs, mock_read_csv):
        df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

    @patch('pandas.read_csv')
    @patch('pandas.DataFrame.to_sql')
    @patch('sqlite3.connect')
    def test_save_csv_to_sqlite(self, mock_connect, mock_to_sql, mock_read_csv):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_read_csv.return_value = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
    
        csv_file_path = 'test_dir/mergedCSV.csv'
        db_path = 'test_dir/merged_data.db'
        table_name = 'merged_data'
    
        df_from_db = save_csv_to_sqlite(csv_file_path, db_path, table_name)
    
        mock_read_csv.assert_called_once_with(csv_file_path)
        mock_to_sql.assert_called_once_with(table_name, mock_conn, if_exists='replace', index=False)
        mock_conn.close.assert_called_once()
        self.assertIsInstance(df_from_db, pd.DataFrame)

