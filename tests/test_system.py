import os
import unittest
import sqlite3
import pandas as pd

class TestPipelineSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.csv_url1 = "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv"
        cls.csv_url2 = "https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv"
        cls.data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        cls.file1_path = os.path.join(cls.data_dir, 'surfaceTemperature.csv')
        cls.file2_path = os.path.join(cls.data_dir, 'disasterFrequency.csv')
        cls.merged_file_path = os.path.join(cls.data_dir, 'mergedCSV.csv')
        cls.db_path = os.path.join(cls.data_dir, 'merged_data.db')
        
        
        os.makedirs(cls.data_dir, exist_ok=True)

    def test_pipeline_execution(self):
        
        import project.pipeline
        
        self.assertTrue(os.path.exists(self.merged_file_path), "Merged CSV file should exist after running the pipeline")
        
        self.assertTrue(os.path.exists(self.db_path), "Database file should exist after running the pipeline")
        
        conn = sqlite3.connect(self.db_path)
        df_from_db = pd.read_sql('SELECT * FROM merged_data', conn)
        conn.close()
        
        self.assertIsInstance(df_from_db, pd.DataFrame, "Expected a pandas DataFrame from database")
        self.assertGreater(len(df_from_db), 0, "DataFrame from database should not be empty")

if __name__ == '__main__':
    unittest.main()
