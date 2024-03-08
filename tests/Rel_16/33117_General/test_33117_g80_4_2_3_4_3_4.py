#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.3.4
# Title: Hiding password display
# Purpose:
# Verify that the given password is not visible to the casual local observer.
# Procedure and execution steps:
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The network product will display the login screen.
# 2. The tester enters the username.
# 3. The tester enters the password.
#
# Expected Results:
# ----------------
# The password shall not be displayed in such a way that it could be seen and misused by a casual
# local observer. Typically, the individual characters of the password are replaced by a character
# such as "*". Under certain circumstances it may be permissible for an individual character to be
# displayed briefly during input. Such a function is used, for ex ample, on smartphones to make
# input easier. However, the entire password is never output to the display in plaintext.


def test_33117_g80_TC_HIDING_PASSWORD_DISPLAY():
    skip('Not implemented...')
