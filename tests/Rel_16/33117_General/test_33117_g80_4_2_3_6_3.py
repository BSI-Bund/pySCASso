#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.6.3
# Title: Protection of security event log files
# Purpose:
# Verify that the log(s) is(are) only accessible by privileged user(s).
#
# Execution Steps:
# ----------------
# 1. The tester attempts to access log files using users accounts with and without the correct
# permissions for accessing log files.
# 2. Repeat the test as described in step 1 using each of the interfaces as described in the
# Network Product documentation.
#
# Expected Results:
# ----------------
# The tester checks that log files are accessible when a user with the appropriate authorisation
# attempts to access them and fails when a user without the correct permissions attempts to access
# them


def test_33117_g80_4_2_3_6_3():
    skip('Missing test case name...')
