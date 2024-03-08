#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.18
# Title: Key update at the gNB on dual connectivity
# Purpose:
# Verify that the gNB under test acting as a Master Node (MN) performs K~SN~ update when DRB-IDs
# are about to be reused.
#
# Execution Steps:
# ----------------
# 1. The gNB under test establishes RRC connection and AS security context with the UE.
# 2. The gNB under test establishes security context between the UE and the SN for the given AS
# security context shared between the gNB under test and the UE; and generates a K~SN~ sent to
# the SN.
# 3. A SCG bearer is set up between the UE and the SN.
# 4. The gNB under test is triggered to execute the SN Modification procedure to provide additional
# available DRB IDs to be used for SN terminated bearers (e.g. by the UE making multiple IMS calls,
# or by the SMF requesting PDU session modification and deactivation via the AMF), until
# the DRB IDs are reused.
#
# Expected Results:
# ----------------
# - Before DRB ID reuse, the gNB under test generates a new K~SN~ and sends it via the
# SN Modification Request message to the SN.


def test_33511_g80_TC_GNB_DC_KEY_UPDATE_DRB_ID():
    skip('Not implemented...')
