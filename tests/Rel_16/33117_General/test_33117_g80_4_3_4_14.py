#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.14
# Title: Restricted file access
# Purpose:
# To test whether the restrictive access rights are assigned to all files which are directly or
# indirectly in the web server's document directory and to verify whether path traversal is made
# improbable.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester verifies that access rights on the servable content (meaning directories and files)
# is set to the following:
# a. The files are owned by the user that runs the web server;
# b. The files are not writable to others, except the web server's account;
# 2. The tester verifies that the user running the web server is an unprivileged account;
# 3. For Operating Systems that have chrooted environments, the tester verifies that the web server
# runs inside a jail or chrooted environment.
#
# Expected Results:
# ----------------
# - Name of user running the web server with the privileges of the account;
# - Access rights of files and directories that the web server serves;
# - Configuration that shows that the web server is in a chrooted environment.


def test_33117_g80_TC_RESTRICTED_FILE_ACCESS():
    skip('Not implemented...')
