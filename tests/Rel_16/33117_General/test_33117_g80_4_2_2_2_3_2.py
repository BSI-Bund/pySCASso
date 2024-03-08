#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.2.2.3.2
# Title: Authorization token verification failure handling in different PLMNs
# Purpose:
# Verify that the NF service producer does not grant service access if the verification of
# authorization token from a NF service consumer in a different PLMN fails.
#
# Execution Steps:
# ----------------
# The network product under test receives the access token sent from the NF service consumer,
# verifies the access token in accordance with the execution steps in 4.2.2.1.2.1, with the
# following additional test cases:
# Test Case 1: incorrect PLMN ID of the NF service producer in the access token
# 1. The test computes an access token correctly, except that the PLMN ID in the producerPlmnId
# claim of the access token is empty or different from the home PLMN ID of the network product
# under test, and then includes the access token in the NF Service Request sent from the NF service
# consumer to the network product under test through the SEPPs.
# 2. The network product under test receives the access token sent from the NF service consumer
# through the SEPPs, verifies that the PLMN ID in the producerPlmnId claim of the access token is
# different from its own home PLMN identity**.**
# Test Case 2: absent PLMN ID of the NF service producer in the access token
# 1. The test computes an access token correctly, except that no producerPlmnId claim is included
# in the access token, and then includes the access token in the NF Service Request sent from the
# NF service consumer to the network product under test through the SEPPs.
# 2. The network product under test receives the access token sent from the NF service consumer
# through the SEPPs, verifies that the access token is not a token to be used by the NF service
# consumer in a different PLMN, based on the absence of PLMN ID of the NF service producer in the
# access token.
#
# Expected Results:
# ----------------
# For both test cases 1 and 2, the network product under test rejects the NF service consumer's
# service request based on Oauth 2.0 error response defined in RFC 6749 [12].


def test_33117_g80_TC_AUTHORIZATION_TOKEN_VERIFICATION_FAILURE_DIFF_PLMN():
    skip('Not implemented...')
