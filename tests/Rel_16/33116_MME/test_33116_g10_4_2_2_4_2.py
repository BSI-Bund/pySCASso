#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.4.2
# Title: NAS integrity protection algorithm selection in MME change
# Purpose:
# Verify that NAS integrity protection algorithm is selected correctly.
#
# Execution Steps:
# ----------------
# The target MME receives the UE EPS security capabilities and the NAS algorithms used by the
# source MME from the source MME over the S10 interface. The target MME selects the NAS algorithms
# which have the highest priority according to the ordered lists. The lists are assumed such that
# the algorithms selected by the target MME are different from the ones received from the
# source MME.
#
# Expected Results:
# ----------------
# The target MME initiates a NAS security mode command procedure and include the chosen algorithms
# and the UE security capabilities.


def test_33116_g10_4_2_2_4_2():
    skip('Missing test case name...')
