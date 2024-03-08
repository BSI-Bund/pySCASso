#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.6.2.4
# Title: GTP-U Filtering
# Purpose:
# To verify that the network product provides filtering functionalities for incoming GTP-U
# messages. In particular this test case verifies that:
# 1. The network product provides filtering of incoming GTP-U messages on any interface.
# 2. It is possible to block all GTP-U messages on those network product interfaces where they are
# unwanted.
# 3. It is possible to specify defined actions for each rule.
#
# Execution Steps:
# ----------------
# 1. The tester log in the network product.
# 2. The tester configures the network product with the following rules:
# a. Accept only GTP-U EchoRequest messages on if1.
# b. Discard all GTP-U messages on if2.
# c. For each rule above the accounting is also enabled.
# 3. The tester turns on the network traffic analyser on if2.
# 4. The tester sends on if2 EchoRequest messages replying a pcap file or using a network
# generator.
# a. Using the network analyser the tester verifies that the network product correctly receives the
# EchoRequest messages on if2.
# b. Using the accounting, the tester verifies that the messages are discarded and that any
# response is sent back by the network product.
# 5. The tester sends to if1 EchoRequest messages replying a pcap file or using a network
# generator.
# a. Using the network analyser, the tester verifies that the messages are correctly received by
# the network product.
# b. The tester verifies that the GTP-U EchoRequest messages are not discarded because EchoResponse
# messages are sent back by the network product.
# 6. The tester verifies that the matching messages are correctly accounted for both rules.
# 7. The tester sends to if1 GTP-U messages different from EchoRequest replying a pcap file or
# using a network generator.
# a. Using the network analyser, the tester verifies that the messages are correctly received by
# the network product.
# b. Using the accounting, the tester verifies that the messages are discarded and that any
# response is sent back by the network product.
# 8. The tester deletes the previous rules and configures a new rule, i.e. to accept only GTP-U
# EchoRequest on if1 coming from a certain IP Address named IP1.
# 9. The tester sends GTP-U EchoRequest messages with source IP Address set to IP1:
# a. Using the network analyser, the tester verifies that the messages are correctly received by
# the network product.
# b. The tester verifies that the GTP-U EchoRequest messages are not discarded and EchoResponse
# messages are sent back by the network product.
# 10. The tester sends GTP-U EchoRequest messages with source IP Address set to IP2 different from
# IP1 using a network traffic generator or replying a pcap file.
# a. Using the network analyser the tester verifies that the messages are correctly received by the
# network product.
# b. The tester verifies that the GTP-U EchoRequest messages are discarded and that no EchoResponse
# messages are sent back.
#
# Expected Results:
# ----------------
# - For steps 4, 5, 6 and 7 the tester receives GTP-U EchoResponse messages from if1 only.
# - For steps 4, 5, 6 and 7 the messages matching the rules are correctly accounted.
# - For steps 8, 9, 10 the tester receives GTP-U EchoResponse messages only for the authorized
# source IP address.


def test_33117_g80_TC_GTP_U_FILTERING():
    skip('Not implemented...')
