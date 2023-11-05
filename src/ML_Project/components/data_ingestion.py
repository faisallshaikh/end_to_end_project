# Data Ingestion 

from dataclasses import dataclass
import os
import sys
from src.exception import CustomException
from src.data_from_sql import get_sql_data
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd

# creating files 

@dataclass 
class DataConfig:
    raw_data_path : str = os.path.join('artifact', 'raw_data.csv')
    train_data_path : str = os.path.join('artifact', 'train_data.csv')
    test_data_path : str = os.path.join('artifact', 'test_data.csv')


class DataIngestion:
    def __init__(self):
        self.data_config = DataConfig()

    def initiate_data_ingestion(self):
        try:
            df = get_sql_data()

            os.makedirs(os.path.dirname(self.data_config.raw_data_path),exist_ok=True)

            df.to_csv(self.data_config.raw_data_path,index=False,header=True)
            X_train_data, X_test_data = train_test_split(df,test_size=0.1,random_state=1)
            X_train_data.to_csv(self.data_config.train_data_path,index=False,header=True)
            X_test_data.to_csv(self.data_config.test_data_path,index=False,header=True)

            return (
                self.data_config.train_data_path,
                self.data_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
