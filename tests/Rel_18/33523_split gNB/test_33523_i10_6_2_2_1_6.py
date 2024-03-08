#!/usr/bin/python3

from pytest import skip

# Function: split gNB
# Source: 33523-i10.md
# Section: 6.2.2.1.6
# Title: Integrity protection of user data between the UE and the gNB-CU-UP
# Purpose:
#  To verify that the user data packets are integrity protected over the NG RAN air interface.
#
# Execution Steps:
# ----------------
# 1. The NIA0 is disabled at UE and gNB-CU-UP.
# 2. The gNB-CU-UP is sent by the gNB-CU-CP a Bearer Context Setup Request message with integrity
# protection indication "on".
# 3. Check any User data sent by gNB-CU-UP after receiving the Bearer Context Setup Request message
# and before UE enters CM-Idle state is integrity protected.
#
# Expected Results:
# ----------------
# Any user plane packets sent between UE and gNB-CU-UP over the NG RAN air interface after
# gNB-CU-UP receives the Bearer Context Setup Request is integrity protected.


def test_33523_i10__TC_UP_DATA_INT_gNB_CU_UP():
    skip('Not implemented...')
