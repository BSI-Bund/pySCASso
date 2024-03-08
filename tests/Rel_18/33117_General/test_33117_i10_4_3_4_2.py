#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.4.2
# Title: No system privileges for web server
# Purpose:
# Verify that the Web server is not run under system privileges.
#
# Execution Steps:
# ----------------
# 1. Check that no web server processes runs with system privileges. Check that this is the case
# even for processes that may have been started by a user with system privileges.
# a. Start the web server process as web server user and check process privileges.
# b. If possible, sStart the web server procvess as with system privileges and check if process
# privileges get dropped.
# 2. Check in relevant system settings and web server configurations that a web server user is
# configured with minimal privileges needed to run the web server and the web server is executable
# by that user.
#
# Expected Results:
# ----------------
# - There are no findings of web server processes that run with system privileges.
# - System settings have been found correctly set to ensure that no processes will run with system
# privileges.


def test_33117_i10__TC_NO_SYSTEM_PRIVILEGES_WEB_SERVER():
    skip('Not implemented...')
