#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.5.3
# Title: No access with 2G SIM via SRVCC
# Purpose:
# Verify that GSM subscribers cannot obtain service in EPS via SRVCC into E-UTRAN.
#
# Execution Steps:
# ----------------
# The target MME receives the GPRS Kc' and the CKSN'~PS~ in the CS to PS handover request.
#
# Expected Results:
# ----------------
# The MME rejects the request.


def test_33116_g10_4_2_2_5_3():
    skip('Missing test case name...')
