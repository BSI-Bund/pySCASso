#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-i10.md
# Section: 4.2.2.1.12
# Title: AS algorithms selection
# Purpose:
# Verify that the gNB selects the algorithms with the highest priority in its configured list.
#
# Execution Steps:
# ----------------
# 1. The UE sends registration request message to the gNB.
# 2. The gNB receives UE context setup request message.
# 3. The gNB sends the AS SECURITY MODE COMMAND message.
# 4. The UE replies with the AS SECURITY MODE COMPLETE message.
#
# Expected Results:
# ----------------
# The gNB initiates the SECURITY MODE COMMAND message that includes the chosen algorithm with the
# highest priority according to the ordered lists and is contained in the UE NR security
# capabilities.
# The MAC in the AS SECURITY MODE COMPLETE message is verified, and the AS protection algorithms
# are selected and applied correctly.


def test_33511_i10__TC_AS_alg_select_gNB():
    skip('Not implemented...')
