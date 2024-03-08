#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.4.1.1.3
# Title: Handling of IP options and extensions
# Purpose:
#  To verify that the network product provides functionality to filter out IP packets with
# unnecessary options or extension headers.
#
# Execution Steps:
# ----------------
# 1. The tester logs in the network product.
# 2. The tester configures on the network product a filtering rule to drop all IP packets
# containing an IP Option set
# a. The tester establishes an O&M session on if1 interface
# b. Using the tool (e.g. Scapy) the tester sends from the tester machine an IPv4 TCP SYN packet
# with an appropriate destination portto if1 interface without setting any IP Options
# c. Using the network traffic analyser, the tester verifies that the IP packet is received by the
# network product and the tester verifies that the corresponding ACK message is sent back.
# d. Using the tool (e.g. Scapy) the tester sends an IPv4 TCP SYN packet with an appropriate
# destination port and an IP Option set to the if1 interface
# e. Using the network traffic analyser, the tester verifies that the IP packet is received by the
# network product but no ACK message is sent back. This confirms the packet is dropped as expected
# from the filtering rule.
# 3. The tester configures on the network product a filtering rule to drop all incoming packets
# based on specific Extension Header Types, e.g. packets with the Routing Header extension. Step 3
# may be skipped if the network product does not support IPv6.
# a. Using the tool (e.g. Scapy) the tester sends from the tester machine an IPv6 TCP SYN packet
# with an appropriate destination port to if1 interface without setting any extension header
# b. Using the network traffic analyser, the tester verifies that the IP packet is received by the
# network product and the tester verifies that the corresponding ACK message is sent back.
# c. Using the tool (e.g. Scapy) the tester sends an IPv6 TCP SYN packet with an appropriate
# destination port and an extension header set to the if1 interface
# d. Using the network traffic analyser, the tester verifies that the IP packet is received by the
# network product but no ACK message is sent back. This confirms the packet is dropped as expected
# from the filtering rule.
#
# Expected Results:
# ----------------
# The network product discards IPv4 packets with unnecessary options or IPv6 packets (assuming the
# network product supports IPv6) with extension header.


def test_33117_g80_TC_HANDLING_IP_OPTIONS_AND_EXTENSIONS():
    skip('Not implemented...')
