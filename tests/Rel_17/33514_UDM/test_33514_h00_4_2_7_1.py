#!/usr/bin/python3

from pytest import skip

# Function: UDM
# Source: 33514-h00.md
# Section: 4.2.7.1
# Title: UP Security enforcement configuration for TSC service
# Purpose:
# Verify that UP security enforcement information is set to "required" for dedicated TSC service.
#
# Execution Steps:
# ----------------
# 1. During the PDU session establishment procedure, the SMF sends a Nudm_SDM_Get Request message
# to the UDM under test with a dedicated DNN/S-NSSAI combination.
# 2. The UDM under test sends the Nudm_SDM_Get Response back to the SMF with UP security
# enforcement information.
#
# Expected Results:
# ----------------
# The confidentiality and integrity protection requirements of the UP security enforcement
# information are set to "required".


def test_33514_h00_4_2_7_1():
    skip('Missing test case name...')
