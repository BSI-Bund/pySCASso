#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.4.2
# Title: NAS protection algorithm selection in AMF change
# Purpose:
# Verify that NAS protection algorithms are selected correctly.
#
# Execution Steps:
# ----------------
# Test case 1: N2-Handover
# The AMF under test receives the UE security capabilities and the NAS algorithms used by the
# source AMF from the source AMF. The AMF under test selects the NAS algorithms which have the
# highest priority according to the ordered lists. The lists are configured such that the
# algorithms selected by the AMF under test are different from the ones received from the
# source AMF.
# Test case 2: Mobility registration update
# The AMF under test receives the UE security capabilities and the NAS algorithms used by the
# source AMF from the source AMF. The AMF under test selects the NAS algorithms which have the
# highest priority according to the ordered lists. The lists are configured such that the
# algorithms selected by the AMF under test are different from the ones received from the
# source AMF.
#
# Expected Results:
# ----------------
# For Test case 1, the tester captures the NASC of the NGAP HANDOVER REQUEST message sent by the
# AMF under test to the gNB, which includes the chosen algorithm.
# For Test case 2, the AMF under test initiates a NAS security mode command procedure and includes
# the chosen algorithms.


def test_33512_g60_TC_NAS_ALG_AMF_CHANGE_AMF():
    skip('Not implemented...')
