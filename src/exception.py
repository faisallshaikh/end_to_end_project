import os 
import sys
# from src.logger import logging

def get_error_message(error, error_detail:sys):
    typ,er,er_tb = error_detail.exc_info()
    file_name = er_tb.tb_frame.f_code.co_filename
    error_message = f"Error [{file_name}] at Line_no [{er_tb.tb_lineno}] Error Message : [{error}]"

    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        self.error_mes = get_error_message(error, error_detail)

    def __str__(self):
        # logging.info("Returning Error Message")
        return self.error_mes
    

