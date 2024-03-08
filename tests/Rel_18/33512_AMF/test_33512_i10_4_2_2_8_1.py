#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.8.1
# Title: Validation of S-NSSAIs in PDU session establishment request
# Purpose:
# Verify that S-NSSAIs which are not within Allowed NSSAI list are not accepted by the AMF under
# test in PDU session establishment procedure.
#
# Execution Steps:
# ----------------
# Test Case A
# 1. The tester triggers the UE to send the S-NSSAI that require NSSAA to the AMF under test using
# registration request message.
# 2. After receiving the NSSAA request from the AMF, the NSSAAF sends EAP success to AMF.
# 3. The UE sends PDU session establishment request to the AMF with the S-NSSAI.
# Test Case B
# 1. The tester triggers the UE to send the S-NSSAI that require NSSAA to the AMF under test using
# registration request message.
# 2. After receiving the NSSAA request from the AMF, the NSSAAF sends EAP failure to AMF.
# 3. The UE sends PDU session establishment request to the AMF with the S-NSSAI.
#
# Expected Results:
# ----------------
# For test case A, the AMF continues the PDU session establishment procedure by sending a
# Nsmf_PDUSession_CreateSMContext Request to the SMF.
# For test case B, the AMF aborts the PDU session establishment procedure by sending back the 5GSM
# message to the UE.


def test_33512_i10__TC_VALIDTATION_SNSSAI_IN_PDU_REQUEST():
    skip('Not implemented...')
