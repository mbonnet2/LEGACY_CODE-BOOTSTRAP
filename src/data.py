class AccountData:
    def __init__(self, initial_balance: float = 1000.00):
        self._balance = initial_balance

    def read_balance(self) -> float:
        return self._balance

    def write_balance(self, new_balance: float) -> None:
        self._balance = new_balance