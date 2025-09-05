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

#Try to withdraw more than the money from the account
def test_application_wrong_withdraw_money_too_much():
    child = pexpect.spawn("python src/main.py")
    
    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("1200")

    child.expect(INVALID_OPERATION, timeout=5)

    child.sendline(DEBIT_KEY)

    child.expect(DEBIT_ASK, timeout=5)

    child.sendline("200")

    child.expect(ACCOUNT_DEBITED + "800")

    child.expect(PROMPT_MESSAGE, timeout=5)

    child.sendline(EXIT_KEY)
    
    child.expect(EXIT_MESSAGE, timeout=5)
    
    child.expect(pexpect.EOF)
    child.close()
    
    assert child.exitstatus == 0


