#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-i10.md
# Section: 4.2.2.1.18
# Title: Key update at the gNB on dual connectivity
# Purpose:
# Verify that the gNB under test acting as a Master Node (MN) performs K~NG-RAN~( AS root key)
# update when SN COUNTER is about to wrap around.
#
# Execution Steps:
# ----------------
# 1. The gNB under test establishes RRC connection and AS security context with the UE.
# 2. The gNB under test establishes security context between the UE and the SN for the given AS
# security context shared between the gNB under test and the UE; and generates a K~SN~ sent to the
# SN and increases the value of SN Counter.
# 3. A SCG bearer is set up between the UE and the SN.
# 4. The gNB under test is triggered to execute the SN Modification procedure to provide updated
# K~SN~ to SN, until the SN Counter value wraps around.
#
# Expected Results:
# ----------------
# - Before SN Counter wraps around, the gNB under test takes a new K~NG-RAN~ into use by e.g.
# triggering an intra-cell handover or triggering a transition from RRC_CONNECTED to RRC_IDLE or
# RRC_INACTIVE and then back to RRC_CONNECTED.


def test_33511_i10__TC_GNB_DC_KEY_UPDATE_SN_COUNTER():
    skip('Not implemented...')
