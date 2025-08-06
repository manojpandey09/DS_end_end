import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        
        # Correct way to extract exception details
        _, _, exc_tb = error_details.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in script: [{self.file_name}] "
            f"at line number: [{self.lineno}] "
            f"with error message: [{self.error_message}]"
        )

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(str(e), sys) from e
