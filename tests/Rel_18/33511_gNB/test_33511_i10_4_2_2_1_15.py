#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-i10.md
# Section: 4.2.2.1.15
# Title: AS protection algorithm selection in gNB change
# Purpose:
# Verify that AS protection algorithm is selected correctly.
#
# Execution Steps:
# ----------------
# Test Case 1:
# Source gNB transfers the ciphering and integrity algorithms used in the source cell to the target
# gNB in the handover request message.
# Target gNB verifies the algorithms and selects AS algorithms which have the highest priority
# according to the ordered lists. Target gNB includes the algorithm in the handover command.
# Test Case 2:
# AMF sends the UE NR security capability to the Target gNB.
# The target gNB selects the AS algorithms which have the highest priority according to the ordered
# lists in the HANDOVER COMMAND.
# The above test cases assume that the algorithms selected by the target gNB are different from the
# ones received from the source gNB.
#
# Expected Results:
# ----------------
# For both test cases:
# 1. The UE checks the message authentication code on the handover command message.
# 2. The MAC in the handover complete message is verified, and the AS integrity protection
# algorithm is selected and applied correctly.


def test_33511_i10__Alg_select_change_gNB():
    skip('Not implemented...')
