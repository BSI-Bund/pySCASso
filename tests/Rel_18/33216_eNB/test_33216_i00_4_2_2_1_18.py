#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.18
# Title: UP IP policy selection
# Purpose:
#  To verify that the eNB has a locally configured UP IP policy
#
# Execution Steps:
# ----------------
# 1. MME sends EPS security capability with EIA7 indicating the UP IP is supported by the UE. But
# the MME does sends a UP IP policy with REQUIRED to the eNB.
# 2. eNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 3. Check any User data sent by eNB after sending RRCConnectionReconfiguration and while the UE is
# in active state is integrity protected.
#
# Expected Results:
# ----------------
# Any user plane packets sent between UE and eNB over the Uu interface after eNB sending
# RRCConnectionReconfiguration is integrity protected.


def test_33216_i00__TC_UP_IP_POLICY_Selection():
    skip('Not implemented...')
