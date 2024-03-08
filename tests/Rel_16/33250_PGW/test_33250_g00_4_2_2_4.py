#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.2.4
# Title: TEID UNIQUENESS
# Purpose:
# Verify that the TEID generated for each new GTP tunnel is unique for both control and user plane.
#
# Execution Steps:
# ----------------
# 1. The tester intercepts the traffic between the P-GW and the S-GW.
# 2. The tester triggers more than one (e.g. at least 10000) consecutives CreateSessionRequest e.g.
# for an Initial UE Attach towards the P-GW (using a real or a simulated S-GW) with GTP header TEID
# set to 0 and F-TEID set to different values.
# 3. The P-GW creates a UE/S-GW context and communicates with the PCRF (real or simulated) for QOS
# and APN resolve. That procedures shall be successfully in order to permit to the P-GW to send
# back to the S-GW a CreateSessionResponse containing at least :
# a. A Success cause.
# b. The P-GW's F-TEID for control plane
# c. The PDN Address Allocation (PAA).
# d. A Bearer Contexts Created.
# 4. The tester verifies that the F-TEID created for each generated CreateSessionResponse is
# unique.
#
# Expected Results:
# ----------------
# The F-TEID set into each different CreateSessionResponse is unique.


def test_33250_g00_4_2_2_4():
    skip('Missing test case name...')
