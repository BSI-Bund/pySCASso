#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.7.7.4
# Title: Potential security functional requirements on trusted platform
# Purpose:
# To test the platform is trusted.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester tampers a BIOS or a file in the host OS kernel and restart the host.
# 2. The tester checks whether the measurement is implemented or not.
#
# Expected Results:
# ----------------
# The measurement is implemented, the restart process is interrupted.


def test_33818_h10_TC_TRUSTED_PLATFORM():
    skip('Not implemented...')
