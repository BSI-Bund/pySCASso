"""Module holds miscellaneous, useful functions."""
import os
import re
from typing import List

import keyring
import pexpect
import pytest

from scas.logger import LOGGER


def run_local(caller: str, cmd: str, wait_for_stdout_lines: List[str] = None, action: str = None,
              timeout=10, cwd=None):
    """Wrapper for localy executed commands

    Args:
        caller (str): A string representing the calling class instance or method. Helps while
            logging.
        cmd (str): The command as string.
        wait_for_stdout_lines (List[str], optional): List with the outputs this functions waits
            for to be printed to stdin. When this is not None the function will block until one
            matching output was found (or timeout). Defaults to None.
        action (str, optional): A string naming the action. Helps while logging. Defaults to None.
        timeout (int, optional): Timeout in seconds. The command execution will block until the
            command returns or a specific output is observed. If none of this happens the timeout
            will be triggered. Defaults to 10.
        cwd (_type_, optional): Some commands need to be executed from a specific directory.
            Chaining 'cd' does not work, therefore we have this argument. Defaults to None.

    Returns:
        pecpect.spawn: spawn object, this contains the pid, among other things
    """
    LOGGER.debug(
        "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")

    if not caller:
        caller = "Command"

    if not action:
        action = "Starting"

    LOGGER.debug("%s %s %s", action, caller, cmd)

    sudo_pw = re.escape(f'[sudo] password for {os.getlogin()}: ')
    result_patterns = [pexpect.EOF, pexpect.TIMEOUT, sudo_pw]

    wait_for_output = wait_for_stdout_lines is not None

    def run_condition(i, wait_for_output):
        if wait_for_output:
            return i < 3
        return i != 0

    if wait_for_output:
        LOGGER.debug("%s %s looking for: %s", action, caller, wait_for_stdout_lines)
        result_patterns.extend(map(re.escape, wait_for_stdout_lines))

    # TODO: Investigate! Some processes (looking at you UERANSIM or separately spawned Open5Gs NFs)
    # get killed instantly after beeing started with pexpect.
    # This does not happen, if we interrupt with ipdb or spawn the process as a piped process with
    # popen_spawn or in a tmux session.
    # If we spawn the command with a popen_spawn, password passing and expect will not work.
    # If we spawn a tmux session, we have to kill it later and it could mess with debug output!
    # child = PopenSpawn(cmd, timeout=None, encoding='utf-8', cwd = cwd)

    child = pexpect.spawn(cmd, timeout=None, encoding='utf-8', cwd=cwd)

    i = child.expect(result_patterns, timeout=timeout)

    # i is determined by the index of the matching pattern in result_patterns
    while run_condition(i, wait_for_stdout_lines):
        match i:
            case 0:  # EOF
                if wait_for_output:
                    LOGGER.error(
                        "Exited %s %s. Was waiting for specific output...", action, caller)
                    LOGGER.error(
                        "Exited %s %s last output:\n%s", action, caller, child.before)
                    pytest.exit(f"Process exited: {cmd}")
            case 1:  # timeout
                LOGGER.error(
                    "Timeout %s %s last output:\n%s", action, caller, child.before)
                pytest.exit(f"Timeout executing: {cmd}")
            case 2:  # sudo asking for password
                password = keyring.get_password(
                    service_name="sudo", username=os.getlogin())

                if password is None:
                    LOGGER.error(
                        "Missing credentials %s %s."
                        "Please set credentials for user %s with python keyring.",
                        action, caller, os.getlogin())
                    LOGGER.error(
                        "Missing credentials %s %s."
                        "'python3 -m keyring set sudo %s'",
                        action, caller, os.getlogin())
                    pytest.exit(f"Missing credentials: {cmd}")

                child.sendline(f'{password}\r\n')
                i = child.expect(result_patterns, timeout=timeout)

    LOGGER.debug("%s %s output:\n%s", action, caller, child.before)
    LOGGER.debug("%s %s last output: %s", action, caller, child.after)
    LOGGER.debug("%s %s found line: %s", action, caller, result_patterns[i])
    LOGGER.debug("%s %s... Done! (pid: %s)", action, caller, child.pid)
    LOGGER.debug(
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return child
