"""Module holds the global logger object and some setup code for special cases"""
import logging

import pytest

# https://stackoverflow.com/questions/4673373/logging-within-pytest-tests
# set log level in pyproject.toml [DEBUG, INFO, WARNING, ERROR, CRITICAL]
LOGGER = logging.getLogger(__name__)

# hacky way to add simple new line without date, loglevel etc


def newline():
    """hacky (and slow) function that allows new lines in the (file) log
    without the cluttered date, loglevel etc
    """
    if not hasattr(pytest, 'session'):
        return

    logging_plugin = pytest.session.config.pluginmanager.get_plugin(
        "logging-plugin")

    # save the formats
    old_fmt = logging_plugin.formatter
    old_cli_fmt = logging_plugin.log_cli_handler.formatter
    old_file_fmt = logging_plugin.log_file_handler.formatter

    # override formats
    logging_plugin.formatter = logging.Formatter("")
    logging_plugin.log_cli_handler.setFormatter(logging.Formatter(""))
    logging_plugin.log_file_handler.setFormatter(logging.Formatter(""))

    # print newline
    LOGGER.info("")

    # recover the formats
    logging_plugin.formatter = old_fmt
    logging_plugin.log_cli_handler.setFormatter(old_cli_fmt)
    logging_plugin.log_file_handler.setFormatter(old_file_fmt)


# add function pointer
LOGGER.newline = newline
