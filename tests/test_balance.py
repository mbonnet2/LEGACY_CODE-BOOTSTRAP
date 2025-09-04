import pexpect
from src.data import AccountData
from src.operation import AccountManager, OperationFactory
    
def test_application_balance():
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System", timeout=5)
    
    child.sendline("1")
    
    child.expect("Current balance: 1000.00", timeout=5)
    
    child.close()
    
def test_application_balance_full():
    account = AccountData(1000)
    accountManager = AccountManager(account)
    child = pexpect.spawn("python src/main.py")

    op = OperationFactory.get_operation('BALANCE')
    accountManager.perform_operation(op)
    
    child.expect("Amount debited. New balance: 1000.00", timeout=5)

    child.close()
