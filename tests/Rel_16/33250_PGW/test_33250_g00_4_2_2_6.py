#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.2.6
# Title: Inactive emergency PDN connection release
# Purpose:
#  To verify whether the PGW releases all emergency PDN connections which are inactive for a
# configured inactive time to prevent resource exhaustion.
#
# Execution Steps:
# ----------------
# 1. The tester checks the PGW configuration file to find the PDN connection's inactive timeout
# value.
# 2. The tester initiates an emergency attach procedure.
# 3. The tester captures the packet over S5/S8 interface between PGW and S-GW using any packet
# analyser.
# 4. The tester filters the PDN CONNECTIVITY REQUEST message with request type "emergency" during
# the attach procedure.
# 5. The tester filters the DELETE BEARER REQUEST messages (Procedure Transaction Identifier,
# EPS Bearer Identity, Causes) sent from PGW to Serving GW.
# 6. The tester also filters the corresponding DELETE BEARER RESPONSE messages
# (EPS Bearer Identity, User Location Information) sent from Serving GW to PGW.
# 7. The tester verifies whether the Cause value of the DELETE BEARER REQUEST message is
# "PDN connection inactivity timer expires". If yes proceed, otherwise go to step 5.
# 8. To confirm the emergency bearer release, the tester compares whether the EPS Bearer identity
# of the UE is the same in all three messages
# (PDN CONNECTIVITY REQUEST, DELETE BEARER REQUEST and DELETE BEARER RESPONSE),
# otherwise it may be concluded that the inactive emergency PDN connection is not released even
# after the configured timeout.
#
# Expected Results:
# ----------------
# The PGW releases the inactive emergency bearers according to the configured timeout value.


def test_33250_g00_TC_PGW_EMRGENCY_CONNECTION_RELEASE():
    skip('Not implemented...')
