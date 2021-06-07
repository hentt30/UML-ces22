"""
Operation to make bank deposit
"""
from .operations import Operation


class BankDeposit(Operation):
    """
    Implementation of the command that makes a deposit
    """

    def __init__(self, account, value):
        """
        Start the class parameters

            Args:
                account (Account): Account for which you want to make the deposit
                value (float): value of the deposit
        """
        self._account = account
        self._value = value

    def execute(self):
        """
        Execute the method that makes the bank deposit
        """
        self._account.make_deposit(self._value)
