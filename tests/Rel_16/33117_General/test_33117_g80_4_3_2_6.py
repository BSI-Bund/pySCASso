#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.2.6
# Title: Remote login restrictions for privileged users
# Purpose:
# Verify that root or equivalent highest privileged user will not be allowed to login to the system
# remotely.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester tries to remotely login to the network product using the credentials of the root or
# equivalent highest privileged user via the interfaces as described in the documentation.
# 2. The tester tries to login to the network product using the credentials of the root or
# equivalent highest privileged user from the physical console of the system.
#
# Expected Results:
# ----------------
# The tester is not able to login to the system remotely using the root credentials.
# The tester is able to login to the system from the physical console using the root credentials.


def test_33117_g80_TC_REMOTE_LOGIN_RESTRICTIONS_PRIVILEGED_USERS():
    skip('Not implemented...')
