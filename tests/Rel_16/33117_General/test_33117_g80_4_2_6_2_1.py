#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.6.2.1
# Title: Packet filtering
# Purpose:
# Verify that the system provides functionality for incoming packet filtering
#
# Execution Steps:
# ----------------
# 1. The tester configures the Network Product to only allow ICMP traffic from host 1.
# 2. The tester initiates ping traffic from host 1.
# 3. The tester initiates ping traffic from host 2.
#
# Expected Results:
# ----------------
# Host 1 will receive a 'ping' answer back, but host 2 will not.


def test_33117_g80_TC_PACKET_FILTERING():
    skip('Not implemented...')
