import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory
    
def test_application_debit_add(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', 100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert "Amount debited. New balance: 900" in captured.out
    

def test_application_debit_negative(capsys):

    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', -100)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert "Invalid operation" in captured.out

def test_application_debit_nul(capsys):
    account = AccountData(1000)
    accountManager = AccountManager(account)

    op = OperationFactory.get_operation('DEBIT', 0)
    accountManager.perform_operation(op)

    captured = capsys.readouterr()

    assert "Invalid operation" in captured.out

def test_application_debit_full():

    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System", timeout=5)
    
    child.sendline("2")
    
    child.expect("Enter debit amount:", timeout=5)

    child.sendline("100")

    child.expect("Amount debited. New balance: 900", timeout=5)

    child.close()