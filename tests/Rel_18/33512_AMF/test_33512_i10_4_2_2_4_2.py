#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.4.2
# Title: NAS protection algorithm selection in AMF change
# Purpose:
# Verify that NAS protection algorithms are selected correctly.
#
# Execution Steps:
# ----------------
# Test case 1: N2-Handover
# 1. The AMF under test receives the UE security capabilities and the NAS algorithms used by the
# source AMF from the source AMF. The AMF under test selects the NAS algorithms which have the
# highest priority according to the ordered lists. The lists are configured such that the
# algorithms selected by the AMF under test are different from the ones received from the source
# AMF.
# 2. he tester captures the NGAP HANDOVER REQUEST message containing the NASC IE (NAS Container)
# sent by the AMF under test to the gNB.
# Test case 2: Mobility registration update
# The AMF under test receives the UE security capabilities and the NAS algorithms used by the
# source AMF from the source AMF. The AMF under test selects the NAS algorithms which have the
# highest priority according to the ordered lists. The lists are configured such that the
# algorithms selected by the AMF under test are different from the ones received from the source
# AMF.
#
# Expected Results:
# ----------------
# For Test case 1, the NASC IE of the captured NGAP HANDOVER REQUEST message sent by the AMF under
# test to the gNB includes the chosen algorithm.
# For Test case 2, the AMF under test initiates a NAS security mode command procedure and includes
# the chosen algorithms.


def test_33512_i10__TC_NAS_ALG_AMF_CHANGE_AMF():
    skip('Not implemented...')
