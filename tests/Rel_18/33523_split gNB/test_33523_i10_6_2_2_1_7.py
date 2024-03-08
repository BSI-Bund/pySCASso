#!/usr/bin/python3

from pytest import skip

# Function: split gNB
# Source: 33523-i10.md
# Section: 6.2.2.1.7
# Title: Ciphering of user data between the UE and the gNB-CU-UP
# Purpose:
#  To verify that the user data packets are confidentiality protected over the NG RAN air
# interface.
#
# Execution Steps:
# ----------------
# 1. The gNB-CU-UP is sent by the gNB-CU-CP a Bearer Context Setup Request message with ciphering
# protection indication "on".
# 2. Check any user data sent by the gNB-CU-UP after receiving the
# Bearer Context Setup Request message and before the UE enters into CM-Idle state.
#
# Expected Results:
# ----------------
# The user plane packets sent to the UE after the gNB-CU-UP receives the
# Bearer Context Setup Request is confidentiality protected.


def test_33523_i10__TC_UP_DATA_CIP_gNB():
    skip('Not implemented...')
