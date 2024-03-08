#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.2.2
# Title: Restricted reachability of services
# Purpose:
# To verify that it is possible to bind the services only to the interfaces from which they are
# expected to be reachable.
# Note: The test case developed for the requirement " 4.2.6.2.1 Packet Filtering" implicitly
# verifies that the network product permits to limit the reachability of the services only to
# legitimate communication peers,
#
# Execution Steps:
# ----------------
# **For every available interface if_n:**
# 1. The tester runs a network port scanner (e.g. nmap) or uses local network interface information
# on if_n and verifies that the configured services (according to the vendor documentation) are
# open/reachable.
# 2. The tester runs a network port scanner (e.g. nmap) or uses local network interface information
# on all other available interfaces (except if_n) and verifies that the services configured for
# if_n are not open/reachable.
#
# Expected Results:
# ----------------
# Services can be enabled on per-interface basis.


def test_33117_i10__TC_RESTRICTED_REACHABILITY_OF_SERVICES():
    skip('Not implemented...')
