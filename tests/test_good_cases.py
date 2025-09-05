import pexpect

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

def test_application_check_balance_withdrawn_money():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(BALANCE_KEY)
    
    child.expect(CURRENT_BALANCE + "1000.00", timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("300")

    child.expect(ACCOUNT_DEBITED + "700", timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

def test_application_check_balance_withdraw_all_money():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(BALANCE_KEY)
    
    child.expect(CURRENT_BALANCE + "1000.00", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("1000")

    child.expect(ACCOUNT_DEBITED + "0", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

def test_application_check_balance_add_money():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(BALANCE_KEY)
    
    child.expect(CURRENT_BALANCE + "1000.00", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("250")

    child.expect(ACCOUNT_CREDITED + "1250", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

def test_application_check_balance_add_big_money():
    
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)
    
    child.sendline(BALANCE_KEY)
    
    child.expect(CURRENT_BALANCE + "1000.00", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("99999999999999")

    child.expect(ACCOUNT_CREDITED + "100000000000999.00", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

def test_application_check_long_manipulation():

    child = pexpect.spawn("python src/main.py")

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("2000")

    child.expect(ACCOUNT_CREDITED + "3000", timeout=1)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("2600")

    child.expect(ACCOUNT_DEBITED + "400", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(BALANCE_KEY)

    child.expect(CURRENT_BALANCE + "400", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(BALANCE_KEY)

    child.expect(CURRENT_BALANCE + "400", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()

def test_application_selection_heading_spaces():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline("  1")

    child.expect(CURRENT_BALANCE + "1000", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()

def test_application_selection_trailing_spaces():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline("1   ")

    child.expect(CURRENT_BALANCE + "1000", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()

