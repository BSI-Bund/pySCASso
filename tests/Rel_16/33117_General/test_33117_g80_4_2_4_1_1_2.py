#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.4.1.1.2
# Title: Handling of ICMP
# Purpose:
# To verify that the network product does not reply to certain ICMP types in accordance with the
# requirement. To verify that the network product does not send 'Time Exceeded'.
# To verify that the network product does not process the following ICMPv4 and ICMPv6 types:
# - "Redirect (5)"
# - Router Solicitation
# - Router Advertisement
#
# Execution Steps:
# ----------------
# The following needs to be done for all IP protocol versions (IPv4 and/or IPv6) supported by the
# network element.
# For verifying that the network product does not reply to ICMP messages with types where this is
# not permitted: The tester sends samples of the applicable ICMP messages from the tester machine
# to the network product and verifies by appropriate means that
# - the messages are dropped on receipt by the network product (e.g. by means of appropriate
# firewall rules),
# - or no response is sent out towards the test machine,
# - or there are other means ensuring that the ICMP messages cannot trigger a response.
# For verifying that the network product does not change its configuration due to receiving ICMP
# messages with types where this is not permitted: The tester sends samples of the applicable ICMP
# messages from the tester machine to the network product and verifies by appropriate means that
# - the messages are dropped on receipt by the network product (e.g. by means of appropriate
# firewall rules),
# - or the network product's applicable system configuration remains unchanged upon receipt of the
# messages,
# - or there are other means ensuring that the ICMP messages cannot lead to configuration changes.
# The tester utilizes appropriate means to verify consistency between the documentation in regard
# to ICMP and the network product.
#
# Expected Results:
# ----------------
# The ICMP messages which are "Not Permitted" to generate a response from the network product do
# not generate a response.
# The ICMP messages which are "Not Permitted" to change the configuration of the network element
# do not change the configuration.
# ICMP message types which lead to responses or to configuration changes on receipt, if neither
# mentioned in the requirement nor in the documentation, are not enabled.


def test_33117_g80_TC_HANDLING_OF_ICMP():
    skip('Not implemented...')
