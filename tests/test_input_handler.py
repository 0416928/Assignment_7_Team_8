"""
Description: Used for unit testing.
Author: Gaganpreet Kaur
Date: November 24, 2024
"""

__author__ = ""
__version__ = ""

# IMPORTS
import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler
from unittest.mock import patch
import csv

# CLASS
class InputHandlerTests(TestCase):
    """Defines the unit tests for the InputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when testing the InputHandler class in 
        the tests that follow.
        
        Example:
            >>> data_processor = DataProcessor(self.FILE_CONTENTS)
        """
        self.FILE_CONTENTS = \
            ("Transaction ID,Account number,Date,Transaction type,"
            + "Amount,Currency,Description\n"
            + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
            + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
            + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries")

    # Define unit test functions below

    def test_get_file_format(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            input_handler= InputHandler("input_data.csv")
            mock_input.side_effect = "input_data.csv"
            expected = "csv"
            # Act
            actual = input_handler.get_file_format()
            # Assert
            self.assertEqual(expected, actual)


    def test_read_csv_data_error(self):
        # Arrange
        expected = "File: Invalid File does not exist."
        input_handler= InputHandler("Invalid File")
        # Act and assert
        with self.assertRaises(FileNotFoundError) as context:
            input_handler.read_csv_data()
        self.assertEqual(expected, str(context.exception))


    def test_read_csv_data_return(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = "input/input_data.csv"
            input_handler= InputHandler("input/input_data.csv")
            actual = []
            expected = "[{'Transaction ID': '1', 'Account number': '1001', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1000', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '2', 'Account number': '1002', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1500', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '3', 'Account number': '1001', 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': '200', 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': '4', 'Account number': '1001', 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': '500', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '5', 'Account number': '1002', 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': '300', 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': '6', 'Account number': '1002', 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': '100', 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': '7', 'Account number': '1001', 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': '100', 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': '8', 'Account number': '1002', 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': '200', 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': '9', 'Account number': '1001', 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': '150', 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': '10', 'Account number': '1002', 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': '250', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '11', 'Account number': '1001', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '12000', 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': '12', 'Account number': '1002', 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': '11000', 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': '13', 'Account number': '1001', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '250', 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': '14', 'Account number': '1002', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '450', 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '15', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '5000', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '16', 'Account number': '1004', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '11500', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '17', 'Account number': '1005', 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': '2200', 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': '18', 'Account number': '1006', 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': '5050', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '19', 'Account number': '1007', 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': '1300', 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': '20', 'Account number': '1003', 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': '1100', 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': '21', 'Account number': '1004', 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': '22', 'Account number': '1005', 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': '222', 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': '23', 'Account number': '1006', 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': '155', 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': '24', 'Account number': '1007', 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': '252', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '25', 'Account number': '1003', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': '26', 'Account number': '1004', 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': '1100', 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': '27', 'Account number': '1005', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '2030', 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': '28', 'Account number': '1006', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '1520', 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '29', 'Account number': '1007', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '100', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '30', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '150', 'Currency': 'CAD', 'Description': 'Salary'}]"
            # Act
            actual = input_handler.read_csv_data()
            # Assert
            actual =str(actual)

            self.assertEqual(expected,actual)


    def test_read_input_data_csv_file(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = "input/input_data.csv"
            input_handler= InputHandler("input/input_data.csv")
            actual = []
            expected = "[{'Transaction ID': '1', 'Account number': '1001', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1000', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '2', 'Account number': '1002', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '1500', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '3', 'Account number': '1001', 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': '200', 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': '4', 'Account number': '1001', 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': '500', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '5', 'Account number': '1002', 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': '300', 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': '6', 'Account number': '1002', 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': '100', 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': '7', 'Account number': '1001', 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': '100', 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': '8', 'Account number': '1002', 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': '200', 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': '9', 'Account number': '1001', 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': '150', 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': '10', 'Account number': '1002', 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': '250', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '11', 'Account number': '1001', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '12000', 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': '12', 'Account number': '1002', 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': '11000', 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': '13', 'Account number': '1001', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '250', 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': '14', 'Account number': '1002', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '450', 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '15', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '5000', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '16', 'Account number': '1004', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '11500', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '17', 'Account number': '1005', 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': '2200', 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': '18', 'Account number': '1006', 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': '5050', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '19', 'Account number': '1007', 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': '1300', 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': '20', 'Account number': '1003', 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': '1100', 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': '21', 'Account number': '1004', 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': '22', 'Account number': '1005', 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': '222', 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': '23', 'Account number': '1006', 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': '155', 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': '24', 'Account number': '1007', 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': '252', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '25', 'Account number': '1003', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': '26', 'Account number': '1004', 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': '1100', 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': '27', 'Account number': '1005', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '2030', 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': '28', 'Account number': '1006', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '1520', 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '29', 'Account number': '1007', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '100', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '30', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '150', 'Currency': 'CAD', 'Description': 'Salary'}]"
            # Act
            actual = input_handler.read_csv_data()
            actual =str(actual)
            # Assert
            self.assertEqual(expected,actual)



    def test_read_input_data_json_file(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = "input/input_data.json"
            input_handler= InputHandler("input/input_data.json")
            actual = []
            expected = "[{'Transaction ID': 1, 'Account number': 1001, 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': 1200, 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': 2, 'Account number': 1002, 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': 1800, 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': 3, 'Account number': 1001, 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': 300, 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': 4, 'Account number': 1001, 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': 800, 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': 5, 'Account number': 1002, 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': 400, 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': 6, 'Account number': 1002, 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': 150, 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': 7, 'Account number': 1001, 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': 120, 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': 8, 'Account number': 1002, 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': 250, 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': 9, 'Account number': 1001, 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': 170, 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': 10, 'Account number': 1002, 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': 300, 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': 11, 'Account number': 1001, 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': 13000, 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': 12, 'Account number': 1002, 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': 12000, 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': 13, 'Account number': 1001, 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': 300, 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': 14, 'Account number': 1002, 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': 500, 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '15', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '5000', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '16', 'Account number': '1004', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '11500', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '17', 'Account number': '1005', 'Date': '2023-03-02', 'Transaction type': 'withdrawal', 'Amount': '2200', 'Currency': 'CAD', 'Description': 'Groceries'}, {'Transaction ID': '18', 'Account number': '1006', 'Date': '2023-03-03', 'Transaction type': 'transfer', 'Amount': '5050', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '19', 'Account number': '1007', 'Date': '2023-03-03', 'Transaction type': 'withdrawal', 'Amount': '1300', 'Currency': 'CAD', 'Description': 'Shopping'}, {'Transaction ID': '20', 'Account number': '1003', 'Date': '2023-03-05', 'Transaction type': 'deposit', 'Amount': '1100', 'Currency': 'EUR', 'Description': 'Gift'}, {'Transaction ID': '21', 'Account number': '1004', 'Date': '2023-03-07', 'Transaction type': 'withdrawal', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Bills'}, {'Transaction ID': '22', 'Account number': '1005', 'Date': '2023-03-10', 'Transaction type': 'deposit', 'Amount': '222', 'Currency': 'CAD', 'Description': 'Refund'}, {'Transaction ID': '23', 'Account number': '1006', 'Date': '2023-03-12', 'Transaction type': 'withdrawal', 'Amount': '155', 'Currency': 'CAD', 'Description': 'Entertainment'}, {'Transaction ID': '24', 'Account number': '1007', 'Date': '2023-03-12', 'Transaction type': 'transfer', 'Amount': '252', 'Currency': 'CAD', 'Description': 'Transfer to Savings'}, {'Transaction ID': '25', 'Account number': '1003', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '1200', 'Currency': 'CAD', 'Description': 'Car Sale'}, {'Transaction ID': '26', 'Account number': '1004', 'Date': '2023-03-14', 'Transaction type': 'withdrawal', 'Amount': '1100', 'Currency': 'CAD', 'Description': 'House Down Payment'}, {'Transaction ID': '27', 'Account number': '1005', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '2030', 'Currency': 'XRP', 'Description': 'Crypto Investment'}, {'Transaction ID': '28', 'Account number': '1006', 'Date': '2023-03-14', 'Transaction type': 'deposit', 'Amount': '1520', 'Currency': 'LTC', 'Description': 'Crypto Investment'}, {'Transaction ID': '29', 'Account number': '1007', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '100', 'Currency': 'CAD', 'Description': 'Salary'}, {'Transaction ID': '30', 'Account number': '1003', 'Date': '2023-03-01', 'Transaction type': 'deposit', 'Amount': '150', 'Currency': 'CAD', 'Description': 'Salary'}]"
            # Act
            actual = input_handler.read_input_data()
            actual = str(actual)
            # Assert
            self.assertEqual(expected,actual)


    def test_read_input_data_empty(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            input_handler= InputHandler("input/input_data.docx")
            actual = []
            expected = "[]"
            # Act
            actual = input_handler.read_input_data()
            actual = str(actual)
            # Assert
            self.assertEqual(expected,actual)         


if __name__ == "__main__":
    unittest.main()