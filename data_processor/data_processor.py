"""
Description: A class created to process account data.
Usage: To incorporate this class into a class or program,
import this using:
from data_processor.data_processor import DataProcessor
"""

__author__ = "Shannon Petkau"
__version__ = "branch_issue_2"

class DataProcessor:
    """
    A class that processes data.

    Attributes:
        __transactions (list): creates a list of input data
    
    Methods (instance methods):
        process_data (dict): creates a dictionary of an account summary 
                                using processed data.
        update_account_summary(): updates the dictionary of the account summary.
        check_suspicious_transactions(): checks if transaction is a suspicious transaction.
        update_transaction_statistics(): updates transaction_statistics
        get_average_transaction_amount(): gets what the average transaction is       
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    """
    Highest amount of money that can be depositted or withdrawn before 
    code will flag for suspicious transaction.
    """

    UNCOMMON_CURRENCIES = ["XRP", "LTC"]
    """
    Currencies that are uncommon that the program will flag for
    suspicious transaction.
    """

    def __init__(self, transactions: list):
        """
        Initialize a new DataProcessor list, with transactions,
        account_summaries, suspicious_transactions, and transaction_statistics.
        
        Args:
            transactions(str): the transaction type.
            account_summaries(dict): a summary of account activity
            suspicious_transactions(list): list of any suspicious transactions
            transaction_statistics(dict): a dictionary of an average of what types
            of transactions a user has engaged in.
        
        Returns:
            None
        """
        self.__transactions = transactions
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}

    @property
    def input_data(self) -> list:
        """
        Accessor for a list of input_data.
        """
        return self.__transactions
    
    @property
    def account_summaries(self) -> dict:
        """
        Accessor for a dict of account_summaries.
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """
        Accessor for a list of suspicious_transactions.
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """
        Accessor for a dictionary of transaction_statistics.
        """
        return self.__transaction_statistics

    def process_data(self) -> dict:
        """
        Processes the data of the account and turns it into a dictionary.

        Returns:
            account_summaries: for accounts processed
            suspicious_transaction: if transaction is suspicious
            transaction_statistics: shows statistics of transactions for account
        """
        for transaction in self.__transactions:
            self.update_account_summary(transaction)
            self.check_suspicious_transactions(transaction)
            self.update_transaction_statistics(transaction)

        return {
            "account_summaries": self.__account_summaries,
            "suspicious_transactions": self.__suspicious_transactions,
            "transaction_statistics": self.__transaction_statistics
        }

    def update_account_summary(self, transaction: dict) -> None:
        """
        Updates account summary if new transaction has gone through.
        
        Args:
            account_number(int): the account number of the account processed
            transaction_type(str): the type of transaction the account holder
            used.
            amount(float): the amount of money used in the transaction
        
        Returns:
            None
        """
        account_number = transaction["Account number"]
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, transaction: dict) -> None:
        """
        Checks if the transaction is suspicious by looking to see if amount is 
        higher than LARGE_TRANSACTION_THRESHOLD or currency is in UNCOMMON_CURRENCIES.
        
        Args:
            amount(float): the amount of money that the transaction is doing 
            something to.
            currency(str): the type of currencies that the money is in.
        
        Returns:
            None
        """
        amount = float(transaction["Amount"])
        currency = transaction["Currency"]

        if amount > self.LARGE_TRANSACTION_THRESHOLD \
            or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(transaction)

    def update_transaction_statistics(self, transaction: dict) -> None:
        """
        Updates transaction statistics when to transaction dictionary 
        when user enters a new transaction.
        
        Args:
            transaction_type(str): the type of transaction entered.
            amount(float): the amount of money entered.
        
        Returns:
            None
        """
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Gets the average transaction amount.
        
        Args:
            total_amount(float): the total amount of transaction
            transaction_count(float): the count of transactions entered
        
        Returns:
            the total_amount / transaction_count if the transaction_count is above zero                
        """
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
    
        return 0 if transaction_count == 0 else total_amount / transaction_count
