#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.2.7
# Title: Filesystem Authorization privileges
# Purpose:
# Verify that only users that are authorized to modify files, data, directories or file systems
# have the necessary privileges to do so.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester checks that OS-level permissions are configured correctly for users that are
# authorized to modify files, data, directories or file systems on the system.
# 2. The tester tries to modify the files and directories for which the user has the necessary
# privileges.
# 3. The tester tries to modify the files and directories for which the user doesn't have the
# necessary privileges.
#
# Expected Results:
# ----------------
# The OS-level access permissions are set correctly for the users.
# The users can only modify files, data, directories or file systems for which he has the necessary
# privileges to do so.


def test_33117_g80_TC_FILESYSTEM_AUTHORIZATION_PRIVILEGES():
    skip('Not implemented...')
