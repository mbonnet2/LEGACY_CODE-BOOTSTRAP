import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory, CreditOperation

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
INVALID_OPERATION = "Invalid operation"
INVALID_CHOICE = "Invalid choice, please select 1-4."
    
def test_application_credit_add(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('CREDIT', 100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert ACCOUNT_CREDITED + "1100" in captured.out
    

def test_application_credit_negative(capsys):

    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('CREDIT', -100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out


def test_application_credit_nul(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('CREDIT', 0)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out

def test_application_credit_full():

    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(CREDIT_KEY)
    
    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("100")

    child.expect(ACCOUNT_CREDITED + "1100", timeout=5)

    child.close()

def test_application_credit_class(capsys):
    op = CreditOperation(100)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_CREDITED + "1100.00" in captured.out

def test_application_credit_class(capsys):
    op = CreditOperation(0)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out

def test_application_credit_class_round_upper(capsys):
    op = CreditOperation(0.999)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_CREDITED + "1001.00" in captured.out

def test_application_credit_class_round_lower(capsys):
    op = CreditOperation(0.111)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_CREDITED + "1000.11" in captured.out