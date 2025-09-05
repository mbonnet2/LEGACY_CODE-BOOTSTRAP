import pexpect
import constants


class TestMainProgram:
    """
    Tests for main program control flow
    """

    def test_exit_application(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("4")
        child.expect(constants.EXIT_MESSAGE, timeout=1)
        child.expect(pexpect.EOF, timeout=1)
        assert child.wait() == 0

    def test_invalid_input1(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("42")
        child.expect(constants.EXIT_MESSAGE, timeout=1)
        child.expect(pexpect.EOF, timeout=1)
        assert child.wait() == 0

    def test_invalid_input2(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("&#*+=")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Invalid choice, please select 1-4." in child.before

    def test_empty_input(self):
        child = pexpect.spawn(constants.EXECUTABLE, encoding='utf-8')
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        child.sendline("")
        child.expect(constants.PROMPT_MESSAGE, timeout=1)
        assert "Invalid choice, please select 1-4." in child.before
