#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.5
# Title: AS algorithms selection
# Purpose:
# Verify that the eNB selects the algorithms with the highest priority in its configured list.
#
# Execution Steps:
# ----------------
# 1. The UE sends attach request message to the eNB.
# 2. The eNB receives S1 context setup request message.
# 3. The eNB sends the SECURITY MODE COMMAND message.
# 4. The UE replies with the AS SECURITY MODE COMPLETE message.
#
# Expected Results:
# ----------------
# The eNB initiates the SECURITY MODE COMMAND message that includes the chosen algorithm with the
# highest priority according to the ordered lists and is contained in the UE EPS security
# capabilities.
# The MAC in the AS SECURITY MODE COMPLETE message is verified, and the AS protection algorithms
# are selected and applied correctly.


def test_33216_i00_4_2_2_1_5():
    skip('Missing test case name...')
