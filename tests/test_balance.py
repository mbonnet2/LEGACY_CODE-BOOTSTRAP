import pexpect
    
def test_application_balance():
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("1")
    
    child.expect("Current balance: 1000.00")
    
    child.close()
    
