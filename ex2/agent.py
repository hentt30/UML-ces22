"""
Mediator class
"""
from operations import Operation


class Agent():
    """
    Class that executes and stores all operations
    """

    def __init__(self):
        """
        Init class parameters
        """
        self._operation_queue = []

    def add_operation(self, operation: Operation):
        """
        Add operations to queue

            Args:
                operation(Operation): operation to be added
        """
        self._operation_queue.append(operation)

    def execute_all_operations(self):
        """
        Executes all operations in the queue
        """
        for operation in self._operation_queue:
            operation.execute()

        self._operation_queue = []
