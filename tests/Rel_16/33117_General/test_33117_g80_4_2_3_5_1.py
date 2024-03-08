#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.5.1
# Title: Protecting sessions -- logout function
# Purpose:
# To ensure a signed in user can logout at any time.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. The tester creates a new account.
# 2. The tester uses the new account or an existing account to log into network product. After x
# minutes the tester tries to logout network product.
# NOTE: The value of x can be arbitrarily set by the tester.
#
# Expected Results:
# ----------------
# - The tester can use a new account or an existing account to log into network product and logout
# network product after x minutes.


def test_33117_g80_TC_PROTECTING_SESSION_LOGOUT():
    skip('Not implemented...')
