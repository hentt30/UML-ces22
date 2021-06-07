"""
Interface for operations that the system can perform
"""
from abc import ABC, abstractclassmethod,abstractmethod

class Operation(ABC):
    """
    Abstract class representing a generic operation
    """
    @abstractmethod
    def execute(self):
        """
        Execute operation
        """
        pass