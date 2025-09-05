import pexpect
import constants


class TestOperationsProgram:
    """
    Tests for account operations (credit and debit).
    """

    def test_credit_valid_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("100")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001100.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_zero_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("0")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_negative_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("-1")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001000.00" in child.before, f"got '{child.before}'."
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_overflow_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("10000000000000000000")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 10000000000000001000.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_amount_bad_format(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("&#$!;")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_plus_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("+400")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_minus_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("-400")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_leading_spaces_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("  400")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_leading_spaces_minus_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("  -400")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_leading_spaces_plus_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("  +400")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_formatted_trailing_spaces_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("400  ")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_amount_decimal(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("400.99")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.99" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_amount_decimal_point_notation(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("-.50")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001000.50" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_amount_decimal_ceil(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("400.999")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001401.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_credit_amount_decimal_floor(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=1)
        child.sendline("400.991")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount credited. New balance: 001400.99" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_debit_valid_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=1)
        child.sendline("50")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount debited. New balance: 000950.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_debit_greater_than_balance(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=1)
        child.sendline("2000.00")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Insufficient funds for this debit." in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_debit_zero_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=1)
        child.sendline("0.00")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount debited. New balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)

    def test_debit_negative_amount(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=1)
        child.sendline("-100")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Amount debited. New balance: 001100.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)
