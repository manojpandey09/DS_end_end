import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)  # ✅ Proper exception chaining
        self.error_message = error_message
        
        # ✅ Correct way to get exception info using sys
        _, _, exc_tb = sys.exc_info()
        
        self.lineno = exc_tb.tb_lineno if exc_tb else None  # ✅ safer
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    
    def __str__(self):
        return (
            f"Error occurred in Python script [{self.file_name}] "
            f"at line number [{self.lineno}] with message: [{self.error_message}]"
        )

if __name__ == "__main__":
    try:
        a = 1 / 0 # ⚠️ Will raise ZeroDivisionError
    except Exception as e:
        raise CustomException(e, sys)
