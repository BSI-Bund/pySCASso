#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.4
# Title: Correct handling of serving PLMN ID mismatch
# Purpose:
# Verify that the SEPP under test is able to identify the mismatch between the PLMN-ID contained in
# the incoming N32-f message and the PLMN-ID in the related N32-f context, and take action
# accordingly.
#
# Execution Steps:
# ----------------
# 1. The tester computes an access token correctly, except that the PLMN ID appended in the subject
# claim of the access token is different from PLMN ID of the peer SEPP, and then includes the
# access token in a NF Service Request.
# 2. The peer SEPP sends to the SEPP under test a N32 message containing the NF Service Request
# with the access token.
# 3. The SEPP under test receives the incoming N32 message from the peer SEPP and verifies that
# the PLMN ID in the subject claim of the access token does not match the remote PLMN ID in the
# N32-f peer information in the N32-f context.
#
# Expected Results:
# ----------------
# - The SEPP under test sends an error signalling message containing the N32-f Message Id and error
# code to the peer SEPP on the N32-c connection.


def test_33517_g30_TC_PLMN_ID_MISMATCH():
    skip('Not implemented...')
