#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.12
# Title: RRC and UP downlink ciphering at the eNB
# Purpose:
#  To verify that the eNB performs RRC and UP downlink ciphering after sending the AS security mode
# command message.
#
# Execution Steps:
# ----------------
# 1. The tester shall POWER ON the UE to trigger the registration procedures (Attach and SMC).
# 2. The tester performs packet capturing over the Uu interface using any packet analyser.
# 3. The tester filters the AS SMC command message and the following RRC and UP downlink packets
# from eNB to UE.
# 4. The tester proceeds the testing based on the parameters
# (algorithm identifier and algorithm distinguisher) present in the AS SMC command message.
# Case 1: If the parameters refer to null ciphering algorithm, the tester verifies that the
# downlink packets filtered in step 3 are unciphered.
# Case 2: If the parameters refer to algorithms such as SNOW, AES, ZUC, the tester verifies that
# the downlink packets filtered in step 3 are ciphered.
# The tester also checks if the packets are ciphered in accordance with the selected algorithm
# stated in the AS SMC command message.
# NOTE: The requirement mentioned in this clause is tested in accordance with the procedure
# mentioned in clause 4.2.3.2.4 of TS 33.117 [2].
#
# Expected Results:
# ----------------
# - The downlink packets following the AS SMC command message are ciphered except NULL ciphering
# algorithm case.


def test_33216_g70_TC_eNB_DL_Cipher():
    skip('Not implemented...')
