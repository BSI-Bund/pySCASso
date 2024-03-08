#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.2.3
# Title: Protecting data and information in storage
# Purpose:
# Verify that Password storage use one-way hash algorithm.
#
# Execution Steps:
# ----------------
# 1. The tester accesses the storage where the result of P1 is, and the corresponding hash value is
# recorded as A
# 2. The tester changes the password with P2, then the tester records the storage hash value of the
# new password as B
# 3. The tester repeats the step 2 to get other records.
# 4. The tester verifies whether all the records comply with the characteristic of one-way hash
# result.
#
# Expected Results:
# ----------------
# All records comply with the characteristic of one-way hash result.


def test_33117_g80_TC_PSW_STOR_SUPPORT():
    skip('Not implemented...')
