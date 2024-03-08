#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.17
# Title: Local UP integrity protection configuration
# Purpose:
#  To verify that the eNB is locally configured with a UP integrity protection policy
#
# Execution Steps:
# ----------------
# 1. MME sends EPS security capability with EIA7 indicating the UP integrity protection is
# supported by the UE. But the MME does not send a UP integrity protection policy to the eNB.
# 2. eNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 3. Check any User data sent by eNB after sending RRCConnectionReconfiguration and while the UE is
# in active state is integrity protected.
#
# Expected Results:
# ----------------
# Any user plane packets sent between UE and eNB over the Uu interface after eNB sending
# RRCConnectionReconfiguration is integrity protected.


def test_33216_i00__TC_LOCAL_UP_INTEGRITY_PROTECTION_CONFIGURATION():
    skip('Not implemented...')
