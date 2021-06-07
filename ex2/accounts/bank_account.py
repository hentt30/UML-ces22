"""
Implements a bank account following the account interface
"""

from .account import Account
import uuid


class BankAccount(Account):
    """
    Implements concrete account
    """

    def __init__(self):
        """
        Init parameters
        """
        super().__init__()

    def make_deposit(self, value):
        """
        Make bank deposit
            
            Args:
                value(float): value of the deposit
        """
        self._balance += value
        self._transactions.append((value, self._id, self._id))

    def make_transaction(self, receiver_id, value):
        """
        Make bank transaction

            Args:
                receiver_id(str): Id of Who will receive the transaction
                value(float): value of the transaction
        """
        if(value > self._balance):
            print('Cannot make transaction')
        else:
            self._balance -= value
            self._transactions.append((value, self._id, receiver_id))

    def check_bank_balance(self):
        """
        Check account balance
        """
        print(f"Your account balance is {self._balance}")

    def print_bank_statement(self):
        """
        Print bank statement
        """
        for transaction in self._transactions:
            if self._is_deposit(transaction):
                print(f"Deposit of {transaction[0]} Reais")
            else:
                print(
                    f"Transaction of {transaction[0]} Reais made by {transaction[1]} and received by {transaction[2]}")

    def _is_deposit(self, transaction):
        """
        Verify if a transaction is a deposit

            Args:
                transaction(tuple): tuple represencting a transaction
        """
        source = transaction[1]
        target = transaction[2]

        if source == target:
            return True
        return False
