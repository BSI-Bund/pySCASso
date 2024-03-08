#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.3.1.4
# Title: SYN Flood Prevention
# Purpose:
# Verify that the Network Product supports a Syn Flood Prevention technique.
#
# Execution Steps:
# ----------------
# 1. The tester verifies the prevention mechanism or setting described in the vendor documentation.
# 2. The tester configures the tool to send a huge amount of TCP Syn packets against the Network
# Product (e.g. hping3 -i <waiting time between each packet> -S -p <TCP port> -c
# <Number of packets> < Network Product IP>)
# 3. The tester verifies that the Network Product is still up and running normally, its services
# are still available and reachable, the service is able to respond to typical service function
# requests, the memory or CPU usage is not exhausted, there is no crash or deadlock.
# a. While the SYN Flood attack is ongoing.
# b. After the SYN Flood attack was executed.
#
# Expected Results:
# ----------------
# The Network Product does not become inoperative.


def test_33117_i10__TC_SYN_FLOOD_PREVENTION():
    skip('Not implemented...')
