import sys
from Network_Security.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys) -> None:
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self) -> str:
        return f"\nError occured in python script name: {self.file_name}\nline number: {self.line_no}\nerror message:\n{self.error_message}"
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error( NetworkSecurityException(error_message=e, error_details=sys))
        raise NetworkSecurityException(error_message=e, error_details=sys)