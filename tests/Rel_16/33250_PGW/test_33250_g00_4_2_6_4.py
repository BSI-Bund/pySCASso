#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.6.4
# Title: MS/UE-Mutual Access Prevention
# Purpose:
# Verify that the Network Product supports a MS/UE-Mutual Access Prevention technique.
#
# Execution Steps:
# ----------------
# 1. The tester configures the PGW to block direct UE to UE traffic according to product
# documentation.
# 2. The tester configures a filtering rule that UEs with IP address in IPSeg 1cannot access to
# servers with IP address in IPSeg 2 and vice versa.
# 3. The PGW allocate the IP1 within the IPSeg 1 to UE 1.
# 4. The PGW allocate the IP2 within the IPSeg 2 to UE 2.
# 5. The UE1 sends a packet with destination IP Address set to IP3 different from IP1 within the
# IPSeg 1.
# 6. The UE1 sends a packet with destination IP Address set to IP2.
# 7. The UE2 sends a packet with destination IP Address set to IP4 different from IP2 within the
# IPSeg 2.
# 8. The UE2 sends a packet with destination IP Address set to IP1.
#
# Expected Results:
# ----------------
# Using the network analyser the tester verifies that the packets are correctly received and
# discarded by the PGW. The tester verifies that the packets are correctly sent by the UE through
# the packet analyzer on the UEs.
# NOTE: The IP address segments allocated to UEs are separate from the IP address segments of
# PDN servers.


def test_33250_g00_TC_MS_UE_MUTUAL_ACCESS_PREVENTION():
    skip('Not implemented...')
