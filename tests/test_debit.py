import pexpect
    
def test_application_debit():
    child = pexpect.spawn("python src/main.py")
    
    child.expect("Account Management System")
    
    child.sendline("3")
    
    child.expect("Enter debit amount:")

    child.sendline("100")

    child.expect("Amount debited. New balance: 900.00")
    
    child.close()

