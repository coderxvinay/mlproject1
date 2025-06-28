import logging
import sys
from logger import logging

import sys
'''any exception that is getting controlled, the sys library will automatically have that information'''

def error_message_detail(error, error_detail:sys):  ##Whenever an exception gets raised, we want to push this on own custom message
    ##error_detail is present inside sys
    _,_,exc_tb = error_detail.exc_info() #error_detail.exc_info() gives 3 infos but we need just the third one
    ##this info will give from where the exception has occured eg line and file.
    file_name = exc_tb.tb_frame.f_code.co_filename  ##Gives the file name where error occured
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{}]".format(
        ##.format(param1, param2, param3) to replace [{0}] [{1}] [{2}] place holder
    file_name, exc_tb.tb_lineno,str(error))
    return error_message
##Whenever any error raises we will call the above function
class CustomException(Exception):  ##CustomException class inheriting from Exception class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message ##whenever we try to print it, we get error message over here
    
##Whenever we raise custom exception, it's inheriting the parent exception
##whatever error message is, it's coming from error_message_detail function
##error_detail is tracked by sys

'''Whenever we use try catch and inside catch block you raise custom exception this type of message will be coming
ie error occured in python script name __ line no __ and so on'''


# if __name__ == "__main__":
#     try:
#         a= 1/0
#     except Exception as e :
#         logging.info("checking if exception works fine")
#         raise CustomException(e,sys)