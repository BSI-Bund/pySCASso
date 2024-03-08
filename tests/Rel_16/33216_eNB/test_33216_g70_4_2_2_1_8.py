#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.8
# Title: Key refresh at the eNB
# Purpose:
# Verify that the eNB performs K~eNB~ refresh when DRB-IDs are about to be reused under the
# following conditions:
# -   the successive Radio Bearer establishment uses the same RB identity while the PDCP COUNT is
# reset to 0, or
# -   the PDCP COUNT is reset to 0 but the RB identity is increased after multiple calls and wraps
# around.
#
# Execution Steps:
# ----------------
# 1. The eNB sends the AS Security Mode Command message to the UE.
# 2. the UE responds with the AS Security Mode Complete message.
# 3. A DRB is set up.
# 4. DRB is set up and torn down for multiple times within one active radio connection without the
# UE going to idle (e.g. by the UE making multiple IMS calls, or by the MME requesting bearer setup
# and bearer deactivation), until the DRB ID is reused.
#
# Expected Results:
# ----------------
# Before DRB ID reuse, the eNB takes a new K~eNB~ into use by e.g. triggering an intra-cell
# handover or triggering a transition from RRC_CONNECTED to RRC_IDLE or RRC_INACTIVE and then back
# to RRC_CONNECTED.


def test_33216_g70_TC_ENB_KEY_REFRESH_DRB_ID():
    skip('Not implemented...')
