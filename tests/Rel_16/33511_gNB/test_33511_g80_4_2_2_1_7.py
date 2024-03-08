#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.7
# Title: Ciphering of user data between the UE and the gNB
# Purpose:
#  To verify that the user data packets are confidentiality protected over the NG RAN air
# interface.
#
# Execution Steps:
# ----------------
# 1. The UE sends PDU session establishment Request to the SMF.
# 2. The SMF sends a UP security policy with UP ciphering required or preferred to the gNB.
# 3. The gNB sends RRCConnectionReconfiguration with ciphering protection indication "on".
# 4. Check any user data sent by the gNB after sending RRCConnectionReconfiguration and before the
# UE enters into CM-Idle state.
#
# Expected Results:
# ----------------
# The user plane packets sent to the UE after the gNB sends RRCConnectionReconfiguration is
# confidentiality protected.


def test_33511_g80_TC_UP_DATA_CIP_gNB():
    skip('Not implemented...')
