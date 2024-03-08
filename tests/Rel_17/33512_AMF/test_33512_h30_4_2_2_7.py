#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-h30.md
# Section: 4.2.2.7
# Title: RRCRestablishment in Control Plane CIoT 5GS Optimization
# Purpose:
#  To verify that the verification of RRC Reestablishment is applied correctly.
#
# Execution Steps:
# ----------------
# A. Test Case 1
# 1. The UE sends the RRC Connection Reestablishment Request message to the ng-eNB.
# 2. The ng-eNB sends RAN CP RELOCATION INDICATION message to the AMF.
# B. Test Case 2
# 1. The UE sends the RRC Connection Reestablishment Request message to the ng-eNB.
# 2. The ng-eNB sends RAN CP RELOCATION INDICATION message to the AMF. The ng-eNB modifies
# UL NAS MAC in UL CP Security Information
#
# Expected Results:
# ----------------
# For test case 1, the AMF sends CONNECTION ESTABLISHMENT INDICATION to the ng-eNB,
# and DL CP Security Information is included.
# For test case 2, the AMF sends CONNECTION ESTABLISHMENT INDICATION to the ng-eNB,
# and DL CP Security Information is not included.


def test_33512_h30_TC_AMF_REEST_CP_CIOT():
    skip('Not implemented...')
