#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.7
# Title: No execution of system commands with SSI
# Purpose:
# To test whether it is possible to use the exec directive and if so, whether it can be used for
# system commands.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# The tester checks whether execution of system commands is disabled in the web server
# configuration.
#
# Expected Results:
# ----------------
# For example, a configuration file that shows that the IncludesNOEXEC (APACHE) or ssiExecDisable
# (IIS) is set.


def test_33117_g80_TC_NO_EXECUTION_OF_SYSTEM_COMMANDS():
    skip('Not implemented...')
