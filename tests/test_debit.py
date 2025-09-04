import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory
    
def test_application_debit_add():
    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('DEBIT', 100)
    accountManager.perform_operation(op)
    
    child.expect("Amount debited. New balance: 900", timeout=20)

    child.close()

def test_application_debit_negative():

    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('DEBIT', -100)
    accountManager.perform_operation(op)

    child.expect("Invalid operation", timeout=20)

    child.close()

def test_application_debit_nul():
    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('DEBIT', 0)
    accountManager.perform_operation(op)

    child.expect("Invalid operation", timeout=20)

    child.close()

def test_application_debit_full():

    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System", timeout=20)
    
    child.sendline("2")
    
    child.expect("Enter debit amount:", timeout=20)

    child.sendline("100")

    child.expect("Amount debited. New balance: 900", timeout=20)

    child.close()