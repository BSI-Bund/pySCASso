#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-h30.md
# Section: 4.2.2.1.3
# Title: NAS based redirection from 5GS to EPS
# Purpose:
# Verify that AMF under test does not send a Registration Reject message containing an EMM cause
# indicating to the UE that the UE shall not use 5GC , if NAS security is not established. .
# NOTE 2: This test case only applies to the AMF under test which supports the security handling
# in CIoT.
#
# Execution Steps:
# ----------------
# 1. UE initiates initial registration procedure with the AMF.
# 2. The AMF under test determines that the UE shall not use 5GC, and needs to redirect the UE from
# 5GC to EPC.
# 3. The AMF under test sends a Registration Reject message with a 5GMM cause indicating to the UE
# that the UE shall not use 5GC.
#
# Expected Results:
# ----------------
# The NAS SMC is performed before sending the Registration Reject message.


def test_33512_h30_TC_AMF_REDIRCTION_5GS_EPS():
    skip('Not implemented...')
