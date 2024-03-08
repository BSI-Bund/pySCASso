#!/usr/bin/python3

from pytest import skip

# Function: UPF
# Source: 33513-g20.md
# Section: 4.2.2.2
# Title: Integrity protection of user data transported over N3 interface
# Purpose:
# Verify that the transported user data between gNB and UPF are integrity protected
# over N3 interface.
#
# Execution Steps:
# ----------------
# The requirement mentioned in this clause is tested in accordance to the procedure
# mentioned in clause 4.2.3.2.4 of TS 33.117 [3].
#
# Expected Results:
# ----------------
# The user data transported between gNB and UPF is integrity protected.


def test_33513_g20_TC_UP_DATA_INT_UPF():
    skip('Not implemented...')
