import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory
    
def test_application_credit_add():
    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('CREDIT', 100)
    accountManager.perform_operation(op)
    
    child.expect("Amount credited. New balance: 1100", timeout=20)

    child.close()

def test_application_credit_negative():

    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('CREDIT', -100)
    accountManager.perform_operation(op)

    child.expect("Invalid operation", timeout=20)

    child.close()

def test_application_credit_nul():
    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('CREDIT', 0)
    accountManager.perform_operation(op)

    child.expect("Invalid operation", timeout=20)

    child.close()

def test_application_credit_full():

    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System", timeout=20)
    
    child.sendline("2")
    
    child.expect("Enter credit amount:", timeout=20)

    child.sendline("100")

    child.expect("Amount credited. New balance: 1100", timeout=20)

    child.close()