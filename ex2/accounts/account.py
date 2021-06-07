"""
Account interface
"""
from abc import ABC, abstractmethod
import uuid


class Account(ABC):
    """
    Implements account interface
    """

    def __init__(self):
        """
        Init parameters
        """
        self._id = uuid.uuid1()
        self._balance = 0
        self._transactions = []

    @abstractmethod
    def make_deposit(self, value):
        """
        Make bank deposit
            
            Args:
                value(float): value of the deposit
        """

    @abstractmethod
    def make_transaction(self, receiver_id, value):
        """
        Make bank transaction

            Args:
                receiver_id(str): Id of Who will receive the transaction
                value(float): value of the transaction
        """

    @abstractmethod
    def check_bank_balance(self):
        """
        Check account balance
        """
    @abstractmethod
    def print_bank_statement(self):
        """
        Print bank statement
        """
