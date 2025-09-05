import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory, DebitOperation
    
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

def test_application_debit_add(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', 100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert ACCOUNT_DEBITED + "900" in captured.out
    

def test_application_debit_negative(capsys):

    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', -100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out

def test_application_debit_nul(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', 0)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out

def test_application_debit_full():

    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(DEBIT_KEY)
    
    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("100")

    child.expect(ACCOUNT_DEBITED + "900", timeout=5)

    child.close()

def test_application_debit_class(capsys):
    op = DebitOperation(100)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_DEBITED + "900.00" in captured.out

def test_application_debit_class(capsys):
    op = DebitOperation(0)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert INVALID_OPERATION in captured.out

def test_application_debit_class_round_upper(capsys):
    op = DebitOperation(0.999)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_DEBITED + "999.00" in captured.out

def test_application_debit_class_round_lower(capsys):
    op = DebitOperation(0.111)
    account = AccountData(1000)

    op.execute(account)

    captured = capsys.readouterr()

    assert ACCOUNT_DEBITED + "999.89" in captured.out