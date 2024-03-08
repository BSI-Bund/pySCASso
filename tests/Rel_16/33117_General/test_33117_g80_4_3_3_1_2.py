#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.2
# Title: Minimized kernel network functions
# Purpose:
# Verify that responses to ICMP broadcast packets are disabled by default on the network product.
# In particular this test case verifies that all ICMP ECHO and TIMESTAMP requests sent to the
# network product via broadcast/multicast are not answered.
#
# Execution Steps:
# ----------------
# 1. If the feature is available in a configuration file, verify that it is disabled by default. .
# 2. Send an ICMP ECHO message from Host 1 to ping a broadcast address (such as 255.255.255.255,
# or 192.168.1.255 on a 192.168.1.0/24 subnet)
# 3. Verify that the network product doesn't respond to the ping.
# 4. Send an ICMP timestamp request (ICMP type 13) from host 1 to a broadcast address
# (such as 255.255.255.255, or 192.168.1.255 on a 192.168.1.0/24 subnet).
# 5. Verify that the network product doesn't respond to the timestamp request.
#
# Expected Results:
# ----------------
# The network product doesn't respond to any ICMP packet with a broadcast address.


def test_33117_g80_TC_BROADCAST_ICMP_HANDLING():
    skip('Not implemented...')
