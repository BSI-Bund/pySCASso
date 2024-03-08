#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.9
# Title: AS Security Mode Command Procedure
# Purpose:
# Verify that AS integrity protection algorithm is selected and applied correctly.
#
# Execution Steps:
# ----------------
# The eNB sends the SECURITY MODE COMMAND message. The UE replies with the SECURITY MODE COMPLETE
# message.
#
# Expected Results:
# ----------------
# 1. The eNB has selected the integrity algorithm which has the highest priority according to the
# ordered lists and is contained in the UE EPS security capabilities. The eNB checks the
# message authentication code on the SECURITY MODE COMPLETE message.
# 2. The MAC in the SECURITY MODE COMPLETE is verified, and the AS integrity protection algorithm
# is selected and applied correctly.


def test_33216_g70_4_2_2_1_9():
    skip('Missing test case name...')
