#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.19
# Title: UP IP policy selection in S1 Handover
# Purpose:
#  To verify that the eNB has correct selection on UP IP policy in S1 handover
#
# Execution Steps:
# ----------------
# Test Case 1:
# 1. MME sends EPS security capability with EIA7 indicating the UP IP is supported by the UE. And
# the MME sends a UP IP policy with REQUIRED to the target eNB.
# 2. Source eNB sends UP IP policy with NOT NEEDED in the source-to-target container to the target
# eNB.
# 3. eNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 4. Check any User data sent by eNB after sending RRCConnectionReconfiguration and before UE
# enters CM-Idle state is integrity protected.
# Test Case 2:
# 1. MME sends EPS security capability with EIA7 indicating the UP IP is supported by the UE. And
# the MME does not send a UP IP policy to the target eNB.
# 2. Source eNB sends UP IP policy with REQUIRED in the source-to-target container to the target
# eNB.
# 3. eNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 4. Check any User data sent by eNB after sending RRCConnectionReconfiguration and before UE
# enters CM-Idle state is integrity protected.
# Test Case 3:
# 1. MME sends EPS security capability with EIA7 indicating the UP IP is supported by the UE. And
# the MME does not send a UP IP policy to the target eNB.
# 2. Source eNB does not send UP IP policy in the source-to-target container to the target eNB.
# 3. eNB sends RRCConnectionReconfiguration with integrity protection indication "off".
# 4. Check any User data sent by eNB after sending RRCConnectionReconfiguration and before UE
# enters CM-Idle state is not integrity protected.
#
# Expected Results:
# ----------------
# For test case 1 and 2, any user plane packets sent between UE and eNB over the Uu interface after
# eNB sending RRCConnectionReconfiguration is integrity protected.
# For test case 3, any user plane packets sent between UE and eNB over the Uu interface after eNB
# sending RRCConnectionReconfiguration is not integrity protected.


def test_33216_i00__TC_UP_IP_POLICY_Selection_S1_Handover():
    skip('Not implemented...')
