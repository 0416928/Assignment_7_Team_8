"""
Description: Unit tests for DataProcessor Class.
Usage: to execute tests:
    py -m unittest -v tests/test_data_processor.py
"""

__author__ = "Shannon Petkau"
__version__ = "branch_issue_5"

import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor
import main


class TestDataProcessor(TestCase):
    """Defines the unit tests for the DataProcessor class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when creating DataProcessor class objects 
        in the tests that follow.  
        
        Example:
            >>> data_processor = DataProcessor(self.transactions)
        """
        self.transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1000,
                "Currency": "CAD",
                "Description": "Salary"
            }, 
            {
                "Transaction ID": "2",
                "Account number": "1002",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1500,
                "Currency": "CAD",
                "Description": "Salary"
            }
        ]

    # Define unit test functions below

    def test_update_account_summary_deposit(self):
        # Arrange
        account_summaries = {
                "account_number": 1001,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }
        
        transaction = {"account_number": 1001,
                       "transaction_type": "deposit",
                       "amount": 1200}
        
        account_number = transaction["account_number"]
        transaction_type = transaction["transaction_type"]
        amount = float(transaction["amount"])

        account_summaries["balance"] += amount
        account_summaries["total_deposits"] += amount

        # Act
        expected = {
                "account_number": 1001,
                "balance": 1200,
                "total_deposits": 1200,
                "total_withdrawals": 0
            }
        
        actual = account_summaries

        # Assert
        self.assertEqual(expected, actual)


    def test_update_account_summary_withdraw(self):
        # Arrange
        account_summaries = {
                "account_number": 1001,
                "balance": 1200,
                "total_deposits": 0,
                "total_withdrawals": 0
            }
        
        transaction = {"account_number": 1001,
                       "transaction_type": "withdraw",
                       "amount": 300}
        
        account_number = transaction["account_number"]
        transaction_type = transaction["transaction_type"]
        amount = float(transaction["amount"])

        account_summaries["balance"] -= amount
        account_summaries["total_withdrawals"] += amount

        # Act
        expected = {
                "account_number": 1001,
                "balance": 900,
                "total_deposits": 0,
                "total_withdrawals": 300
            }
        
        actual = account_summaries

        # Assert
        self.assertEqual(expected, actual)
    

    def test_check_suspicious_transactions_large_amount(self):
        # Arrange
        transaction_over_threshold = {"Transaction ID": 11, 
                                      "Account number": 1001, 
                                      "Date": "2023-03-13", 
                                      "Transaction type": "deposit", 
                                      "Amount": 12000, 
                                      "Currency": "CAD", 
                                      "Description": "Car Sale"}
        
        processor = DataProcessor([])

        # Act
        processor.check_suspicious_transactions(transaction_over_threshold)

        # Assert
        self.assertIn(transaction_over_threshold, processor.suspicious_transactions)


    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        transaction_uncommon_currency = {"Transaction ID": 27, 
                                      "Account number": 1005, 
                                      "Date": "2023-03-14", 
                                      "Transaction type": "deposit", 
                                      "Amount": 2030, 
                                      "Currency": "XRP", 
                                      "Description": "Crypto Investment"}
        
        processor = DataProcessor([])

        # Act
        processor.check_suspicious_transactions(transaction_uncommon_currency)

        # Assert
        self.assertIn(transaction_uncommon_currency, processor.suspicious_transactions)

    def test_check_suspicious_transactions_not_suspicious(self):
        # Arrange
        not_in_suspicious_transactions = {"Transaction ID": 3,
                                          "Account number": 1001,
                                          "Date": "2023-03-02",
                                          "Transaction type": "withdrawal",
                                          "Amount": 300,
                                          "Currency": "CAD",
                                          "Description": "Groceries"}
        
        processor = DataProcessor([])

        # Act
        processor.check_suspicious_transactions(not_in_suspicious_transactions)

        # Assert
        self.assertNotIn(not_in_suspicious_transactions, processor.suspicious_transactions)
    

    def test_update_transaction_statistics(self):
        # Arrange
        transaction_withdraw = {
            "Transaction type": "withdrawal",
            "Amount": 100.0
        }
        transaction_deposit = {
            "Transaction type": "deposit",
            "Amount": 200.0
        }
        transaction_transfer = {
            "Transaction type": "transfer",
            "Amount": 50.0
        }
        
        processor = DataProcessor({})

        # Act
        processor.update_transaction_statistics(transaction_withdraw)
        processor.update_transaction_statistics(transaction_deposit)
        processor.update_transaction_statistics(transaction_transfer)

        # Assert
        self.assertIn("withdrawal", processor._DataProcessor__transaction_statistics)
        self.assertEqual(processor._DataProcessor__transaction_statistics["withdrawal"]["total_amount"], 100.0)
        self.assertEqual(processor._DataProcessor__transaction_statistics["withdrawal"]["transaction_count"], 1)

        self.assertIn("deposit", processor._DataProcessor__transaction_statistics)
        self.assertEqual(processor._DataProcessor__transaction_statistics["deposit"]["total_amount"], 200.0)
        self.assertEqual(processor._DataProcessor__transaction_statistics["deposit"]["transaction_count"], 1)

        self.assertIn("transfer", processor._DataProcessor__transaction_statistics)
        self.assertEqual(processor._DataProcessor__transaction_statistics["transfer"]["total_amount"], 50.0)
        self.assertEqual(processor._DataProcessor__transaction_statistics["transfer"]["transaction_count"], 1)

    def test_suspicious_transaction_logging_warning(self):
        # Arrange
        self.processor = DataProcessor(transactions=[])
        transaction = {"Amount": 10001, "Currency": "CAD"}

        # Act and Assert
        with self.assertLogs(self.processor.logger, level='WARNING') as log:
            self.processor.check_suspicious_transactions(transaction)
            self.assertTrue(any("Suspicious transaction" in message for message in log.output))

    def test_log_file(self):
        # Arrange
        with self.assertLogs(level='INFO') as log:
           main.main()

        # Act and Assert
        self.assertIn("Data Processing Complete", log.output[63])
        self.assertIn("Account summary updated: 1001", log.output[0])
        self.assertIn("Suspicious transaction: {'Transaction ID': '11', 'Account number': '1001', 'Date': '2023-03-13', 'Transaction type': 'deposit', 'Amount': '12000', 'Currency': 'CAD', 'Description': 'Car Sale'}"
                      , log.output[19])
        self.assertIn("Updated transaction for deposit", log.output[1])

if __name__ == "__main__":
    unittest.main()
