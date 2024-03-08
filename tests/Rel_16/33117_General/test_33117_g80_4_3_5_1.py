#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.5.1
# Title: Traffic Separation
# Purpose:
# To test whether traffic belonging to different network domains is separated.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester checks whether the network product refuses traffic intended for one network domain
# on all interfaces meant for the other network domain, and vice versa.
# 2. Step 1 is to be performed for all pairs of different network domains.
#
# Expected Results:
# ----------------
# The two tests should be successful.


def test_33117_g80_TC_TRAFFIC_SEPARATION():
    skip('Not implemented...')
