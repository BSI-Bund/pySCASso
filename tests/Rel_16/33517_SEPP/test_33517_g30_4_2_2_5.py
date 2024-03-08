#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.5
# Title: Confidential IEs replacement handling in original N32-f message
# Purpose:
# Verify that the SEPP under test correctly replaces information elements requiring encryption with
# the value " encBlockIdx ".
#
# Execution Steps:
# ----------------
# 1. Both SEPPs establish a mutual N32-c connection.
# 2. Via the PLMN-internal interface, the tester provides the SEPP under test with a message to be
# forwarded to the peer SEPP on N32. This message needs to contain at least one information element
# that requires encryption according to the locally configured Data-type encryption policy.
# 3. The tester captures the related N32-f message after transformation by the SEPP under test.
#
# Expected Results:
# ----------------
# Information elements in the original message that require encryption according to the Data-type
# encryption policy are replaced with the value " encBlockIdx ".


def test_33517_g30_4_2_2_5():
    skip('Missing test case name...')
