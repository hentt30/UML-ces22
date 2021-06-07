"""
Operation to check bank balance
"""
from .operations import Operation


class BankBalance(Operation):
    """
    Implementation of the command that generates the bank balance
    """

    def __init__(self, account):
        """
        Start the class parameters

            Args:
                account (Account): Account for which you want to obtain the balance
        """
        self._account = account

    def execute(self):
        """
        Execute the method that checks the bank balance
        """
        self._account.check_bank_balance()
