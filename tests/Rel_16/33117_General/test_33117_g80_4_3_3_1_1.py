#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.1
# Title: IP-Source address spoofing mitigation
# Purpose:
# To verify that the network product provides anti-spoofing function that is, before a packet is
# processed, the network product checks whether the source IP of the received packet is reachable
# through the interface it comes in.
# To verify that if the received packet source address is not routable through the interface on
# which it comes, then the network product drops this packet.
#
# Execution Steps:
# ----------------
# 1. The tester starts to send ping messages to if1-np interface of the network product.
# 2. The tester verifies, through the network traffic analyser, that the ping reaches correctly the
# if1-np interface and that responses are sent back.
# 3. The tester disconnects the tester machine from if2-n1 interface of the node N1 and reconnects
# it to the interface if2-n2 of the node N2:
# - The testers uses the same network configuration of the tester machine.
# - The tester sends ping messages to if1-np interface of the network product.
# - The tester verifies, through the network traffic analyser, that the pings reach the if1-np
# interface of the network product, but they are dropped and no response is sent back since the
# source of the received packet is not reachable through the interface it came in.
# - The tester sends ping messages to if2-np interface of the network product.
# - The tester verifies, through the network traffic analyser, that the pings reach the if2-np
# interface of the network product, but they are dropped and no response is sent back since there
# is a default route via if2-np.
# - If the dropped packets are logged, the testers verifies that these packets are recorded.
#
# Expected Results:
# ----------------
# The network product supports an anti-spoofing mechanism (e.g. the RPF function) and it accepts a
# packet only if it reaches the network product on the expected interface (i.e. this packet has a
# source ip address belonging to the same network as the interface where it came in or if it is
# routable through the interface on which it came in), otherwise it discards the packet.


def test_33117_g80_TC_IP_SPOOFING_MITIGATION():
    skip('Not implemented...')
