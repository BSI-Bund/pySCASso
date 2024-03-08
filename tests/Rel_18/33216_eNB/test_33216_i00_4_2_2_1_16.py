#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.16
# Title: Integrity protection of user data between the UE and the eNB
# Purpose:
#  To verify that the user data packets are integrity protected over the Uu interface.
#
# Execution Steps:
# ----------------
# 1. eNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 2. Check any User data sent by eNB after sending RRCConnectionReconfiguration and while the UE is
# in active state is integrity protected.
#
# Expected Results:
# ----------------
# Any user plane packets sent between UE and eNB over the Uu interface after eNB sending
# RRCConnectionReconfiguration is integrity protected.


def test_33216_i00__TC_UP_DATA_INT_eNB():
    skip('Not implemented...')
