#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.2.3
# Title: Charging ID Uniqueness
# Purpose:
# Verify that the Charging ID value set in the Information Element Bearer Context within a
# CreateSessionResponse is unique.
#
# Execution Steps:
# ----------------
# 1. The tester intercepts the traffic between the P-GW and the S-GW.
# 2. The tester trigger more than one (e.g. at least 10000) consecutive CreateSessionRequest for an
# Initial UE Attach towards the P-GW (using a real or a simulated S-GW) in order to setup a new
# IP-CAN bearer.
# 3. The P-GW creates a UE/S-GW context and communicates with the PCRF (real or simulated) for QOS
# and APN resolve. That procedures shall be successfully in order to permit to the P-GW to send
# back to the S-GW a CreateSessionResponse containing at least :
# a. A Success cause.
# b. The P-GW's F-TEID for control plane
# c. The PDN Address Allocation (PAA)
# d. A Bearer Contexts Created.
# 4. The tester verifies that the Charging ID within Bearer Contexts Created in each generated
# CreateSessionResponse are different.
#
# Expected Results:
# ----------------
# The Charging ID assigned to every IP-CAN bearer requested by different CreateSessionRequest is
# unique.


def test_33250_g00_4_2_2_3():
    skip('Missing test case name...')
