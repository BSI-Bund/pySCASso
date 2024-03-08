#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.7
# Title: RRCRestablishment in Control Plane CIoT 5GS Optimization
# Purpose:
#  To verify that the verification of RRC Reestablishment is applied correctly.
#
# Execution Steps:
# ----------------
# Test Case A
# 1. The tester triggers the UE to send the RRC Connection Reestablishment Request message to the
# ng-eNB.
# 2. The ng-eNB sends RAN CP RELOCATION INDICATION message to the AMF.
# Test Case B
# 1. The tester triggers the UE to send the RRC Connection Reestablishment Request message to the
# ng-eNB.
# 2. The ng-eNB sends RAN CP RELOCATION INDICATION message to the AMF. The ng-eNB modifies
# UL NAS MAC in UL CP Security Information
#
# Expected Results:
# ----------------
# For test case A, the AMF sends CONNECTION ESTABLISHMENT INDICATION to the ng-eNB, and
# DL CP Security Information is included.
# For test case B, the AMF sends CONNECTION ESTABLISHMENT INDICATION to the ng-eNB, and
# DL CP Security Information is not included.


def test_33512_i10__TC_AMF_REEST_CP_CIOT():
    skip('Not implemented...')
