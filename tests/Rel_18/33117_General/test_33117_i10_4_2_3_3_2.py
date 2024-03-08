#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.2.3.3.2
# Title: Boot from intended memory devices only
# Purpose:
# Verify that the network product can only boot from memory devices intended for this purpose
# (e.g. not from external memory like USB key).
#
# Execution Steps:
# ----------------
# 1. The tester verifies that the network product is configured to boot from memory devices
# declared in the network product document only.
# 2. The tester verifies that there is no possibility to access and modify the firmware of the
# network product without successful authentication and the authenticated subject (e.g., person or
# process) has no possibility to access and modify the firmware without privileged access rights.
#
# Expected Results:
# ----------------
# The network product cannot boot from a memory device that is not configured in its firmware, and
# access to the firmware is only possible with the correct authentication.


def test_33117_i10__TC_BOOT_INT_MEM_1():
    skip('Not implemented...')
