#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.2
# Title: No system privileges for web server
# Purpose:
# Verify that the Web server is not run under system privileges.
#
# Execution Steps:
# ----------------
# 1. Check that no web server processes runs with system privileges. Check that this is the case
# even for processes that may have been started by a user with system privileges.
# 2. Check that relevant system settings and configurations are correct to ensure fulfilment of the
# requirement.
#
# Expected Results:
# ----------------
# - There are no findings of processes that run with system privileges.
# - System settings have been found correctly set to ensure that no processes will run with system
# privileges.


def test_33117_g80_TC_NO_SYSTEM_PRIVILEGES_WEB_SERVER():
    skip('Not implemented...')
