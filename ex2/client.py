"""
Mocks a typical bank client doing operations
"""
import uuid
from accounts import BankAccount
from operations import BankDeposit, BankStatement, BankBalance, BankTransaction
from agent import Agent

# CLient
account = BankAccount()
client_operations = [
    BankDeposit(account, 150),
    BankTransaction(account, uuid.uuid1(), 200),
    BankBalance(account),
    BankTransaction(account, uuid.uuid1(), 10),
    BankBalance(account),
    BankTransaction(account, uuid.uuid1(), 50), BankTransaction(
        account, uuid.uuid1(), 50),
    BankDeposit(account, 50),
    BankStatement(account)]

# Invoker
agent = Agent()
for operation in client_operations:
    agent.add_operation(operation)

agent.execute_all_operations()
