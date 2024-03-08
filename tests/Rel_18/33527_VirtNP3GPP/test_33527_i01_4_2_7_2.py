#!/usr/bin/python3

from pytest import skip

# Function: VirtNP3GPP
# Source: 33527-i01.md
# Section: 4.2.7.2
# Title: Security functional requirements on executive environment provision
# Purpose:
# 1. To test whether the VNF compares the owned resource state with the parsed resource state.
# 2. To test whether the VNF send an alarm to the OAM if the two resource states are inconsistent.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester utilizes the virtualization layer to change the resource state of VNF (e.g. change
# vCPU size of the VNF).
# 2. The tester uses the VNF to query the parsed resource state from the OAM.
# 3. The tester uses the OAM to query the parsed resource state of the VNF from the VNFM and send
# the received resource state to the VNF.
# 4. The tester checks whether the VNF sends an alarm to the OAM when the VNF receives the parsed
# resource state from the OAM and finds that the owned resource state and the parsed resource state
# are inconsistent.
#
# Expected Results:
# ----------------
# 1. The VNF send an alarm to the OAM when the VNF receives the parsed resource state from the OAM
# and find that the owned resource state and the parsed resource state are inconsistent.


def test_33527_i01__TC_SECURE_EXECUTIVE_ENVIRONMENT_PROVISION():
    skip('Not implemented...')
