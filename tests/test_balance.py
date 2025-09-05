import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory, BalanceOperation

BALANCE_KEY = "1"
CREDIT_KEY = "2"
DEBIT_KEY = "3"
EXIT_KEY = "4"

PROMPT_MESSAGE = r"Enter your choice \(1-4\):"
EXIT_MESSAGE = "Exiting the program. Goodbye!"
CURRENT_BALANCE = "Current balance: "
DEBIT_ASK = "Enter debit amount:"
CREDIT_ASK = "Enter credit amount:"
ACCOUNT_DEBITED = "Amount debited. New balance: "
ACCOUNT_CREDITED = "Amount credited. New balance: "
    
def test_application_balance():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(BALANCE_KEY)
    
    child.expect(CURRENT_BALANCE + "1000.00", timeout=5)
    
    child.close()
    
def test_application_balance_full(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('BALANCE')
    accountManager.perform_operation(op)
    
    captured = capsys.readouterr()

    assert CURRENT_BALANCE + "1000.00" in captured.out

def test_application_balance_class(capsys):
    op = BalanceOperation()
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert CURRENT_BALANCE + "1000.00" in captured.out
