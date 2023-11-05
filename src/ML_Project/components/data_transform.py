from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os 
import sys 
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
import pickle
@dataclass
# creating a path
class DataTransformationConfig:
    pickle_file_path = os.path.join('artifact', 'preprocessor.pkl')

class DataTransformation:

    def __init__(self):
        self.data_transformation = DataTransformationConfig()

    def PuttingAllTogether(self):

        cat_features = ["anime"]
        cat_imputer = Pipeline(steps=[
            ("cat_imputer", SimpleImputer(strategy="most_frequent")),
            ("One_Hot", OneHotEncoder(handle_unknown="ignore"))
        ])

        ordinal = ["beast", "MUI", "super saiyan blue", "nine tails", "sharingan", "titan"]

        ordinal_features = ["power"]
        ordinal_imputer = Pipeline(steps=[
            ("Ordinal_Imputer", OrdinalEncoder(categories=[ordinal]))
        ])

        preprocessor = ColumnTransformer(transformers=[
            ("cat_imputer", cat_imputer,cat_features),
            ("ordinal_imputer", ordinal_imputer,ordinal_features)
        ],remainder="passthrough")

        return preprocessor
    

    def initiate_data_transform(self,train_path, test_path):

        try:
            logging.info("Initiating Data Transform")
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)

            target_col = "power_level"

            X_train = df_train.drop(target_col,axis=1)
            y_train = df_train[target_col]

            X_test = df_test.drop(target_col,axis=1)
            y_test = df_test[target_col]

            preprocessor_object = self.PuttingAllTogether()

            transformed_X_train = preprocessor_object.fit_transform(X_train)
            transformed_X_test = preprocessor_object.transform(X_test)

            X_train_arr = np.c_[transformed_X_train, np.array( y_train)]
            X_test_arr = np.c_[transformed_X_test,np.array(y_test)]

            file_path = self.data_transformation.pickle_file_path
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path, 'wb') as file:
                pickle.dump(preprocessor_object,file)

            logging.info("Data Transformation Completed")

            return (
                X_train_arr,
                X_test_arr,
                self.data_transformation.pickle_file_path
            )
        except Exception as e:
            logging.info("Data Transformation Interrupted")
            raise CustomException(e ,sys)

