#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.5.2
# Title: Protecting sessions -- Inactivity timeout
# Purpose:
# To ensure an OAM user interactive session shall be terminated at inactivity timeout.
#
# Execution Steps:
# ----------------
# 1. The tester creates OAM user A interaction session.
# 2. The tester configures the inactivity time-out period for user A to x minute, for example 1
# minute.
# 3. The tester does not make any actions on the network production in x minutes. After that, the
# tester checks whether OAM user A interaction session has been terminated automatically.
#
# Expected Results:
# ----------------
# - In step 3, OAM user A interaction session has been terminated automatically after x minute.


def test_33117_g80_TC_PROTECTING_SESSION_INAC_TIMEOUT():
    skip('Not implemented...')
