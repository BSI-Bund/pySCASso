#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.10
# Title: Ciphering of user data based on the security policy sent by the SMF
# Purpose:
#  To verify that the user data packets are confidentiality protected based on the security policy
# sent by the SMF via AMF
#
# Execution Steps:
# ----------------
# 1. The tester triggers PDU session establishment procedure by sending PDU session establishment
# request message.
# 2. Tester shall trigger the SMF to send the UP security policy with ciphering protection
# "required" or "not needed" to the gNB.
# 3. The tester shall capture the RRC connection reconfiguration procedure between gNB to UE over
# NG RAN air interface. And filter the RRC connection reconfiguration message sent by gNB to UE.
# 4. The tester shall decrypt the RRC connection Reconfiguration message and retrieve the
# UP ciphering protection indication presenting in the decrypted message.
# 5. The tester shall verify if the UP security policy received at gNB is same as the
# UP ciphering protection indication notified by the gNB to the UE in the
# RRC connection Reconfiguration message.
# 6. Tester shall capture the RRC connection Reconfiguration complete message sent between UE and
# gNB.
# 6a. Tester shall capture the user plane data sent between UE and gNB using any network analyser.
# 7. Tester shall check that the captured UP data is activated/de-activated according to the
# UP security policy.
#
# Expected Results:
# ----------------
# When the received UP cipher protection indication is set to "required",
# the captured user plane data appear to be garbled (i.e. no longer plaintext) and the
# user plane packets are confidentiality protected based on the UP security policy sent by the SMF.
# When the received UP cipher protection indication is set to "not needed",
# the captured user plane data appear to be plaintext and the user plane packets are not
# confidentiality protected based on the UP security policy sent by the SMF.


def test_33511_g80_TC_UP_DATA_CIP_SMF():
    skip('Not implemented...')
