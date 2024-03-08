#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.4
# Title: SYN Flood Prevention
# Purpose:
# Verify that the Network Product supports a Syn Flood Prevention technique.
#
# Execution Steps:
# ----------------
# 1. The tester configures the tool to send a huge amount of TCP Syn packets against the Network
# Product (e.g.
# hping3 -i <waiting time between each packet> -S -p <TCP port> -c <Number of packets> <MME IP>)
# 2. The Network Product is still up and running normally, its services are still available and
# reachable, the memory is not exhausted, there is no crash.
#
# Expected Results:
# ----------------
# The Network Product does not become inoperative.


def test_33117_g80_TC_SYN_FLOOD_PREVENTION():
    skip('Not implemented...')
