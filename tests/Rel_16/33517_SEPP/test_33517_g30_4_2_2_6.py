#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.6
# Title: Correct handling of protection policy mismatch
# Purpose:
# Verify that the SEPP under test is able to identify the mismatch between the protection policies
# manually configured for a specific roaming partner and IPX provider and the protection policies
# received on N32-c connection, and take action accordingly.
#
# Execution Steps:
# ----------------
# For each of the three cases above, the following is executed:
# 1. The peer SEPP sends a Security Parameter Exchange Request message to the SEPP under test
# including the peer SEPP's Data-type encryption policy *d'*, and the Modification policy *m'*.
# 2. The SEPP under test stores the received Data-type encryption policy *d'* and the Modification
# policy *m'*, then compare them with the Data-type encryption policy *d* and the Modification
# policy *m* configured on it.
#
# Expected Results:
# ----------------
# - The SEPP under test sends an error signalling message to the peer SEPP on the N32-c connection
# or logs the error.


def test_33517_g30_TC_SEPP_POLICY_MISMATCH():
    skip('Not implemented...')
