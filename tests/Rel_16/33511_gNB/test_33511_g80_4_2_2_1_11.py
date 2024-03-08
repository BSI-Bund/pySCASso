#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.11
# Title: Integrity of user data based on the security policy sent by the SMF
# Purpose:
#  To verify that the user data packets are integrity protected based on the security policy sent
# by the SMF.
#
# Execution Steps:
# ----------------
# 1. The tester triggers PDU session establishment procedure by sending PDU session establishment
# request message.
# 2. Tester shall trigger the SMF to send the UP security policy with integrity protection is
# "required" or "not needed" to the gNB.
# 3. The tester shall capture the RRC connection reconfiguration message sent by gNB to UE over
# NG RAN air interface.
# 4. The tester shall decrypt the RRC connection reconfiguration message and retrieve the
# UP integrity protection indication presenting in the decrypted message.
# 5. Tester shall check whether UP integrity is enabled /disabled to verify if the
# UP security policy received at gNB is same as the UP integrity protection indication notified by
# the gNB to the UE in the RRC connection reconfiguration message.
# 6. Tester shall capture the user plane data sent between UE and gNB using any network analyser.
# 7. The tester shall check whether the user plane data packet contains a
# message authentication code.
#
# Expected Results:
# ----------------
# When the received UP integrity protection is set to "required", the user plane data packet
# contains a message authentication code and the user plane packets are integrity protected based
# on the security policy sent by the SMF.
# When the received UP interity protection is set to "not needed",
# the user plane data packet message authentication code is not present and the user plane packets
# are not integrity protected based on the security policy sent by the SMF.


def test_33511_g80_TC_UP_DATA_INT_SMF():
    skip('Not implemented...')
