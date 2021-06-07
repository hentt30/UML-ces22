"""
Operation to make bank transaction
"""
from .operations import Operation


class BankTransaction(Operation):
    """
    Implementation of the command that makes the bank transaction
    """

    def __init__(self, source, receiver_id, value):
        """
        Start the class parameter

            Args:
                source (Account): Who will carry out the transaction
                receiver_id(str): Id of Who will receive the transaction
                value(float): value of the transaction
        """
        self._source = source
        self._receiver_id = receiver_id
        self._value = value

    def execute(self):
        """
        Execute the method that generates performs bank transaction
        """
        self._source.make_transaction(self._receiver_id, self._value)
