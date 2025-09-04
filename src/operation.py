from abc import ABC, abstractmethod
from data import AccountData

class Operation(ABC):
    @abstractmethod
    def execute(self, account: AccountData) -> None:
        pass

class BalanceOperation(Operation):
    def execute(self, account: AccountData) -> None:
        print(f"Current balance: {account.read_balance():,.2f}")

class CreditOperation(Operation):
    def __init__(self, amount: float):
        self.amount = amount

    def execute(self, account: AccountData) -> None:
        if self.amount > 0:
            balance = account.read_balance() + self.amount
            account.write_balance(balance)
            print(f"Amount credited. New balance: {balance:,.2f}")
        else:
            print(f"Invalid operation type")

class DebitOperation(Operation):
    def __init__(self, amount: float):
        self.amount = amount

    def execute(self, account: AccountData) -> None:
        if self.amount <= account.read_balance() and self.amount > 0:
            balance = account.read_balance() - self.amount
            account.write_balance(balance)
            print(f"Amount debited. New balance: {balance:,.2f}")
        else:
            print(f"Invalid operation type")

class AccountManager:
    def __init__(self):
        self.account = AccountData(1000)

    def perform_operation(self, operation: Operation) -> None:
        operation.execute(self.account)

class OperationFactory:
    _operations = {
        'BALANCE': BalanceOperation,
        'CREDIT': CreditOperation,
        'DEBIT': DebitOperation
    }

    @classmethod
    def get_operation(cls, name, *args):
        operation_class = cls._operations.get(name.upper())
        if operation_class:
            return operation_class(*args)
        else:
            print(f"Invalid operation type")