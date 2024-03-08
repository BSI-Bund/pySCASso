#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.3
# Title: User plane data ciphering and deciphering at the eNB
# Purpose:
#  To verify that the user data packets are confidentiality protected over the air interface.
#
# Execution Steps:
# ----------------
# 1. The UE sends an attach request to the MME.
# 2. The MME sends a KeNB and the UE security capability to the eNB.
# 3. eNB selects an algorithm and sends AS SMC to the UE,
# 4. eNB receive AS SMP from the UE.
#
# Expected Results:
# ----------------
# User plane packets sent by the eNB after eNB sending AS SMC is ciphered.


def test_33216_i00__TC_DATA_CIP_eNB_S1_X2():
    skip('Not implemented...')
