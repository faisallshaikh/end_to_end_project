from src.exception import CustomException
from src.logger import logging
from src.data_from_sql import get_sql_data
import sys
import mysql.connector as conn
import pandas as pd
from src.ML_Project.components.data_ingestion import DataConfig, DataIngestion
from src.ML_Project.components.data_transform import DataTransformationConfig, DataTransformation



if __name__ == '__main__':
    # try :
    #     1/0
    # except Exception as e:
    #     logging.info("Exception Raised")
    #     raise CustomException(e, sys)

    # get_sql_data()

    ob_ject = DataIngestion()
    train_data_path, test_data_path = ob_ject.initiate_data_ingestion()

    final_data_transformation = DataTransformation()
    final_data_transformation.initiate_data_transform(train_data_path, test_data_path)

