import pexpect
import constants


class TestDataProgram:
    """
    Tests for data-related operations such as viewing the initial balance.
    """

    def test_read_initial_balance(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("1")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Current balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)
