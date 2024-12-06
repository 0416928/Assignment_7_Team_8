"""REQUIRED MODULE DOCUMENTATION
"""

__author__ = "RajanDeep Kaur"
__version__ = "3.11"

from unittest import TestCase, main
from output_handler.output_handler import OutputHandler
from unittest.mock import patch, mock_open

class TestOutputHandler(TestCase):
    """Defines the unit tests for the OutputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test function."""
        self.account_summaries = { 
            "1001": {
                "account_number": "1001", 
                "balance": 50, 
                "total_deposits": 100, 
                "total_withdrawals": 50
            },
            "1002": {
                "account_number": "1002", 
                "balance": 200, 
                "total_deposits": 200, 
                "total_withdrawals": 0
            },
            "1003": {
                "account_number": "1003", 
                "balance": 300, 
                "total_deposits": 300, 
                "total_withdrawals": 0
            }
        }

        self.suspicious_transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-14",
                "Transaction type": "deposit",
                "Amount": 250,
                "Currency": "XRP",
                "Description": "crypto investment"
            }
        ]

        self.transaction_statistics = {
            "deposit": {
                "total_amount": 300, 
                "transaction_count": 2
            }, 
            "withdrawal": {
                "total_amount": 50, 
                "transaction_count": 1
            }
        }

    def test_filter_account_summaries_true(self):
        """Tests filtering with mode True (greater than or equal)."""
        output_handler = OutputHandler(self.account_summaries, self.suspicious_transactions, self.transaction_statistics)
        filtered = output_handler.filter_account_summaries("balance", 100, True)
        self.assertEqual(len(filtered), 2)  

    def test_filter_account_summaries_false(self):
        """Tests filtering with mode False (less than or equal)."""
        output_handler = OutputHandler(self.account_summaries, self.suspicious_transactions, self.transaction_statistics)
        filtered = output_handler.filter_account_summaries("balance", 100, False)
        self.assertEqual(len(filtered), 1)  

    def test_write_filtered_summaries_to_csv(self):
        """Tests writing filtered summaries to a CSV file."""
        output_handler = OutputHandler(self.account_summaries, self.suspicious_transactions, self.transaction_statistics)
        filtered_data = output_handler.filter_account_summaries("balance", 100, True)
        filename = "fdp_filter_team_1.csv"  

        with patch("builtins.open", mock_open()) as mocked_file:
            output_handler.write_filtered_summaries_to_csv(filtered_data, filename)

            mocked_file.assert_called_once_with(filename, 'w', newline='')

            handle = mocked_file()
            handle.write.assert_any_call("Account number,Balance,Total Deposits,Total Withdrawals\n")

            for summary in filtered_data:
                handle.write.assert_any_call(f"{summary['account_number']},{summary['balance']},{summary['total_deposits']},{summary['total_withdrawals']}\n")

    def test_write_filtered_summaries_to_csv_empty(self):
        """Tests writing an empty filtered summaries to a CSV file."""
        output_handler = OutputHandler(self.account_summaries, self.suspicious_transactions, self.transaction_statistics)
        filtered_data = output_handler.filter_account_summaries("balance", 500, True)  
        filename = "fdp_filter_team_1.csv" 

        with patch("builtins.open", mock_open()) as mocked_file:
            output_handler.write_filtered_summaries_to_csv(filtered_data, filename)

            mocked_file.assert_called_once_with(filename, 'w', newline='')

            handle = mocked_file()
            handle.write.assert_called_once_with("Account number,Balance,Total Deposits,Total Withdrawals\n")
            handle.write.assert_called_once()

if __name__ == "__main__":
    main()