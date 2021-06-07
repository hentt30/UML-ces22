"""
Operation to generate bank statement
"""
from .operations import Operation


class BankStatement(Operation):
    """
    Implementation of the command that generates the bank statement
    """

    def __init__(self, account):
        """
        Start the class parameters

            Args:
                account (Account): Account for which you want to obtain the statement
        """
        self._account = account

    def execute(self):
        """
        Execute the method that generates the bank statement
        """
        self._account.print_bank_statement()
