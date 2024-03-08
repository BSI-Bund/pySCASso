#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.2.2
# Title: Per-user based packet filtering
# Purpose:
# Verify that PGW supports a Per-user based packet filtering.
#
# Execution Steps:
# ----------------
# 1. The tester configures the different filtering policy for the UE1and the UE2 on the PGW, e.g.
# the PGW forwards the packets from the UE1 to SGi and drops the packets from the UE2.
# 2. The tester sends the packets from the UE1 to the PGW.
# 3. The tester sends the packets from the UE2 to the PGW.
# 4. The tester checks the filtered packets using the network traffic analyser.
#
# Expected Results:
# ----------------
# The PGW can filter the packets per- user according the configured filtering policy, e.g. the
# PGW forwards the packets from the UE1 to SGi in the step 2 and drops the packets from the UE2 in
# the step 3.


def test_33250_g00_4_2_2_2():
    skip('Missing test case name...')
