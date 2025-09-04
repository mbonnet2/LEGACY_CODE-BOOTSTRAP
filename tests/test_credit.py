import pexpect
    
def test_application_credit():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("2")
    
    child.expect("credit")
    
    child.close()
    