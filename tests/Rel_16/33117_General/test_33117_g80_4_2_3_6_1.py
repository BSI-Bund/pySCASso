#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.6.1
# Title: Security event logging
# Purpose:
# To verify that the network product correctly logs all required security event types.
#
# Execution Steps:
# ----------------
# For each O&M service perform the following test steps
# - The Tester sequentially triggers each security event listed in the requirement, while covering
# each option detailed in the individual security event descriptions.
# - The Tester verifies whether the security events, and their individual options, were correctly
# logged. In particular it is verified whether they include at least the event data specified as
# required to be logged.
#
# Expected Results:
# ----------------
# All security events are appropriately logged, including all required event data.


def test_33117_g80_TC_SECURITY_EVENT_LOGGING():
    skip('Not implemented...')
