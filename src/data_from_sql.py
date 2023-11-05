import mysql.connector as conn 
import pymysql
import sqlite3
from sqlite3 import *
import os
import sys
import pandas as pd
from src.exception import CustomException
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")


def get_sql_data():
    try:

        mydb = conn.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        df1 = pd.read_sql_query("select * from anime_characters", mydb)
        df1["power_level"] = [123,156,489,201,564,133]
        df = df1
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e, sys)




