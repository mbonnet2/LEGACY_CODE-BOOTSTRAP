import pexpect

def test_application_start():
    """Correct display of basic application information"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.close()
    
def test_application_balance():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("1")
    
    child.expect("total")
    
    child.close()
    
def test_application_credit():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("2")
    
    child.expect("credit")
    
    child.close()
    
def test_application_debit():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("3")
    
    child.expect("debit")
    
    child.close()
    
    
def test_application_exit():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("4")
    
    child.expect("exit")
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

