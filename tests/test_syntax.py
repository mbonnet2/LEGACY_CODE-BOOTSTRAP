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

def test_application_selection_caracteres():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline("#4")

    child.expect(INVALID_CHOICE, timeout=5)

    child.close()

def test_application_selection_plus_number():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline("+1")

    child.expect(INVALID_CHOICE, timeout=5)

    child.close()

#Try to withdraw with a value that is not a number
def test_application_withdraw_money_not_a_number():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("a")

    child.expect(INVALID_OPERATION, timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to withdraw with an empty value
def test_application_withdraw_money_empty_value():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("")

    child.expect(INVALID_OPERATION, timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to withdraw with a heading space
def test_application_withdraw_money_heading_space():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("  100")

    child.expect(ACCOUNT_DEBITED + "900", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to withdraw with a trailing space
def test_application_withdraw_money_trailing_space():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("100  ")

    child.expect(ACCOUNT_DEBITED + "900", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to credit with a value that is not a number
def test_application_credit_money_not_a_number():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("a")

    child.expect(INVALID_OPERATION, timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to credit with an empty value
def test_application_credit_money_empty_value():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("")

    child.expect(INVALID_OPERATION, timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to credit with a heading space
def test_application_credit_money_heading_space():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("  100")

    child.expect(ACCOUNT_CREDITED + "1100", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0

#Try to credit with a trailing space
def test_application_credit_money_trailing_space():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(CREDIT_KEY)

    child.expect(CREDIT_ASK, timeout=5)

    child.sendline("100  ")

    child.expect(ACCOUNT_CREDITED + "1100", timeout=5)

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0