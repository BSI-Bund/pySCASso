#!/usr/bin/python3

from pytest import skip

# Function: UDM
# Source: 33514-h00.md
# Section: 4.2.8.1
# Title: UP security policy configuration for 5G LAN service
# Purpose:
# Verify that UP security policy is set to the same for all the 5G LAN UEs.
#
# Execution Steps:
# ----------------
# 1. During the PDU session establishment procedure initiated by the UE1, the SMF1 sends a
# Nudm_SDM_Get Request message to the UDM under test with a dedicated DNN/S-NSSAI combination,
# and SUPI1.
# 2. The UDM under test sends the Nudm_SDM_Get Response back to the SMF1 with UP security policy1.
# 3. During the PDU session establishment procedure initiated by the UE2, the SMF2 sends a
# Nudm_SDM_Get Request message to the UDM under test with a dedicated DNN/S-NSSAI combination,
# and SUPI2.
# 4. The UDM under test sends the Nudm_SDM_Get Response back to the SMF2 with UP security policy2.
# NOTE 2: SMF1 and SMF2 could be the same network function.
#
# Expected Results:
# ----------------
# The confidentiality and integrity protection requirements of the UP security policy1 and
# UP security policy2 are the same.


def test_33514_h00_4_2_8_1():
    skip('Missing test case name...')
