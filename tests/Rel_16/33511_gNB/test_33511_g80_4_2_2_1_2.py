#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.2
# Title: Integrity protection of user data between the UE and the gNB
# Purpose:
#  To verify that the user data packets are integrity protected over the NG RAN air interface.
#
# Execution Steps:
# ----------------
# 1. The NIA0 is disabled at UE and gNB.
# 2. gNB sends RRCConnectionReconfiguration with integrity protection indication "on".
# 3. Check any User data sent by gNB after sending RRCConnectionReconfiguration and before UE
# enters CM-Idle state is Integrity protected.
#
# Expected Results:
# ----------------
# Any user plane packets sent between UE and gNB over the NG RAN air interface after gNB sending
# RRCConnectionReconfiguration is integrity protected.


def test_33511_g80_TC_UP_DATA_INT_gNB():
    skip('Not implemented...')
