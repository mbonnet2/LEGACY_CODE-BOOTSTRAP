import pexpect
    
def test_application_exit():
    """View Current Balance"""
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System", timeout=5)
    
    child.sendline("4")
    
    child.expect("Exiting the program. Goodbye!", timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

