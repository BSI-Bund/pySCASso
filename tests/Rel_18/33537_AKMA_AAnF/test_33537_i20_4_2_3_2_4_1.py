#!/usr/bin/python3

from pytest import skip

# Function: AKMA_AAnF
# Source: 33537-i20.md
# Section: 4.2.3.2.4.1
# Title: Confidentiality
# Purpose:
# Verify that the transported data between AAnF and AUSF are confidentiality, integrity and replay
# protected over SBA interface.
#
# Execution Steps:
# ----------------
# The requirement mentioned in this clause is tested in accordance with the procedure mentioned in
# clause 4.2.2.2.2 of TS 33.117 [2].
#
# Expected Results:
# ----------------
# The user data transported between AAnF and AUSF is confidentiality, integrity and
# replay protected.


def test_33537_i20__TC_PROTECT_SBA_AAnF_AUSF():
    skip('Not implemented...')
