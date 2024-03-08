#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.11
# Title: AS protection algorithm selection in eNB change
# Purpose:
# Verify that AS protection algorithm is selected correctly.
#
# Execution Steps:
# ----------------
# Test Case 1:
# Source eNB transfers the ciphering and integrity algorithms used in the source cell to the target
# eNB in the handover request message.
# Target eNB verifies the algorithms and selects AS algorithms which have the highest priority
# according to the ordered lists. Target eNB includes the algorithm in the handover command.
# Test Case 2:
# MME sends the UE EPS security capability to the Target eNB.
# The target eNB selects the AS algorithms which have the highest priority according to the ordered
# lists in the HANDOVER COMMAND.
# The above test cases assume that the algorithms selected by the target eNB are different from the
# ones received from the source eNB.
#
# Expected Results:
# ----------------
# For both test cases:
# 1. The UE checks the message authentication code on the handover command message.
# 2. The MAC in the handover complete message is verified, and the AS integrity protection
# algorithm is selected and applied correctly.


def test_33216_g70_4_2_2_1_11():
    skip('Missing test case name...')
