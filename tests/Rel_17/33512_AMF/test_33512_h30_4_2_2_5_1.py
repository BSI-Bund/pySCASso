#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-h30.md
# Section: 4.2.2.5.1
# Title: 5G-GUTI allocation
# Purpose:
# Verify that a new 5G-GUTI is allocated by the AMF under test in these scenarios accordingly.
#
# Execution Steps:
# ----------------
# Test case 1:
# Upon receiving Registration Request message of type "initial registration" from a UE, the AMF
# sends a new 5G-GUTI to the UE during the registration procedure.
# Test case 2:
# Upon receiving Registration Request message of type "mobility registration update" from a UE,
# the AMF sends a new 5G-GUTI to the UE during the registration procedure.
# Test case 3:
# Upon receiving Service Request message sent by the UE in response to a Paging message,
# the AMF sends a new 5G-GUTI to the UE.
# Test case 4:
# The AMF under test is triggered to page the UE in CM Idle with Suspend Indicator. After paging
# the UE in CM-Idle with Suspend indicator, the AMF shall send a new 5G-GUTI to the UE.
# NOTE 1: Test case 4 is only applicable to AMF supporting UP CIoT 5GS Optimization.
#
# Expected Results:
# ----------------
# For Test case 1, 2, 3 and 4, the tester retrieves a new 5G-GUTI by accessing the NAS signalling
# packets sent by the AMF under test over N1 interface during registration procedure.
# For Test case 1, 2, 3 and 4, the NAS message encapsulating the new 5G-GUTI is confidentiality and
# integrity protected by the AMF under test using the NAS security context, which is same as the
# UE's NAS security context.
# The new 5G-GUTI is different from the old 5G-GUTI.


def test_33512_h30_TC_5G_GUTI_ALLOCATION_AMF():
    skip('Not implemented...')
