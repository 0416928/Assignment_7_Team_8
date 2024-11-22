"""
Description: This program is reading and validating the input data from a CSV file, and implementing custom data validation rules.
Name: Gaganpreet Kaur
Date: 11-22-2024
"""


__author__ = ""
__version__ = ""

# IMPORTS
import csv
import json
from os import path

# CLASS
class InputHandler:
    """
    class: InputHandler
    Purpose: This class is reading and validating the input data from a CSV file, and implementing custom data validation rules.
    
    Attributes: 
        file_path(str): The path of a file.
    Methods: 
        __init__(self,file_path)
        file_path(self) -> str
        get_file_format(self) -> str
        read_input_data(self) -> list
        read_csv_data(self) -> list
        read_json_data(self) -> list
    """

# METHODS
    def __init__(self, file_path: str):
        """
        Initializes the class with the given parameters.

        Parameters:
        - file_path (str): This is a path to the file.
        """

        self.__file_path = file_path

    @property   ## ACCESSOR
    def file_path(self) -> str:
        """
        This is a accessor method which allows controlled access to a private attribute.
        Return:
            str
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """
        This function is taking the file and extracting from file path.
        Return:
            str
        """
        return self.__file_path.split(".")[-1]

    def read_input_data(self) -> list:
        """
        This method is reading the file after choosing the format and saving it to a transactions list.
        Return:
            list
        """
        transactions = []
        file_format = self.get_file_format()
        
        if file_format == "csv":
            transactions =  self.read_csv_data()
        elif file_format == "json":
            transactions = self.read_json_data()
        return transactions

    def read_csv_data(self) -> list:
        """
        This method is opening the csv file and reading it.
        Return:
            list
        Raises:
            ValueError: "Invalid file extension to perform actions"
        """
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        transactions = []

        with open(self.__file_path, "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                transactions.append(row)
            
        return transactions
            
    def read_json_data(self) -> list:
        """
        This method is opening the json file and reading it.
        Return 
            list
        Raises:
            ValueError: "Invalid file extension to perform actions"

        """
        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data
        
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        with open(self.__file_path, "r") as input_file:
            transactions = json.load(input_file)

        return transactions
