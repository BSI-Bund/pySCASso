#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.3.1
# Title: Password Structure
# Purpose:
# To verify that password structure adheres to the password complexity criteria.
# To verify that password structure is configurable as per the complexity criteria.
#
# Execution Steps:
# ----------------
# Execute the following steps:
# A. Test Case 1
# 1. The tester logs into Network Product application using admin account.
# 2. The tester creates user A following the password complexity criteria.
# 3. The tester logs in as user A and attempts to change their password which contains characters
# from all four categories mentioned in the password complexity criteria.
# B. Test Case 2
# 1. The tester logins with privileged account.
# 2. The tester modifies password structure policy on the network product by strengthening the
# policy (e.g. changing the minimum password length to 8+x, changing the minimum number of
# character Unicode categories to 4).
# 3. The tester logs in as user A and attempts to change their password to a password with a
# strength of less than that permitted by the policy strengthened in step 2 above.
#
# Expected Results:
# ----------------
# Tester can change password only if new password fulfil the password complexity criteria


def test_33117_g80_TC_PASSWORD_STRUCT():
    skip('Not implemented...')
