#!/usr/bin/python3

from pytest import skip

# Function: split gNB
# Source: 33523-i10.md
# Section: 5.2.2.1.4
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
# "required" or "not needed" to the gNB-CU-CP.
# 3. The tester shall capture the Bearer Context Setup Request message sent to the gNB-CU-UP over
# the E1 interface.
# 4. The tester shall decrypt the Bearer Context Setup Request message.
# 5. The tester shall capture the RRC connection reconfiguration procedure between gNB-CU-CP to UE
# over NG RAN air interface. And filter the RRC connection reconfiguration message sent by
# gNB-CU-CP to UE.
# 6. The tester shall decrypt the RRC connection Reconfiguration message and retrieve the UP
# ciphering protection indication presenting in the decrypted message.
# 7. The tester shall verify if the UP ciphering policy received at gNB-CU-CP is same as the UP
# ciphering protection indication notified by the gNB-CU-CP to the UE in the
# RRC connection Reconfiguration message and the gNB-CU-UP in the
# Bearer Context Setup Request message.
#
# Expected Results:
# ----------------
# Both the messages indicate that ciphering is to be used inline with the received policy.


def test_33523_i10__TC_UP_DATA_CIP_SMF_gNB_CU_CP():
    skip('Not implemented...')
