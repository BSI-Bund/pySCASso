#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.6
# Title: Verify RRC integrity protection
# Purpose:
# Verify that the message is discarded in case of failed integrity check (i.e. faulty or missing
# MAC-I).
#
# Execution Steps:
# ----------------
# Positive:
# The eNB receives a RRC message with a right MAC-I.
# Negative:
# The eNB receives a RRC message with a wrong MAC-I or missing MAC-I.
#
# Expected Results:
# ----------------
# The RRC message is discarded in the negative test.


def test_33216_g70_4_2_2_1_6():
    skip('Missing test case name...')
