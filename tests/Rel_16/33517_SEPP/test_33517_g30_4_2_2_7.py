#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.7
# Title: JWS profile restriction
# Purpose:
# Verify that the SEPP under test is able to restrict the JWS profile to only use ES256 algorithm
# with IPX entities.
#
# Execution Steps:
# ----------------
# 1. The tester shall check that the supported JWS algorithms in the network product documentation
# complies with the requirement on the restriction.
# 2. The tester sends a N32-f message from the peer SEPP via the intermediate IPX node towards the
# SEPP under test.
# 3. The IPX node modifies one or more attributes of the N32-f message from the peer SEPP and
# creates a modifiedDataToIntegrityProtect object, which is protected by the IPX node using the
# JWS algorithm configured by the tester.
# 4. The IPX node forwards the modified N32-f message to the SEPP under test.
# 5. Based on the internal log files, the tester validates how the received N32-f message is
# handled by the SEPP under test.
#
# Expected Results:
# ----------------
# - The modified N32-f message from the IPX node is discarded by the SEPP under test.


def test_33517_g30_TC_JWS_PROFILE_RESTRICTION():
    skip('Not implemented...')
