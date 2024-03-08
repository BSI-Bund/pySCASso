#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.4.7
# Title: No execution of system commands with SSI
# Purpose:
# To test whether it is possible to use the exec directive and if so, whether it can be used for
# system commands.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1.-The tester checks whether execution of system commands is disabled in the web server
# configuration.
# 2. The tester actually attempts to use the exec directive in an SSI file with and without system
# commands.
#
# Expected Results:
# ----------------
# - The execution of system commands via SSIs exec directive is disabled in the web server
# configuration.
# - It is impossible to execute system commands via SSIs exec directive.


def test_33117_i10__TC_NO_EXECUTION_OF_SYSTEM_COMMANDS():
    skip('Not implemented...')
