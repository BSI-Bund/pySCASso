#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-h10.md
# Section: 4.2.2.2.3.1
# Title: Authorization token verification failure handling wthin one PLMN
# Purpose:
# Verify that the NF service producer does not grant service access if the verification of
# authorization token from a NF service consumer in the same PLMN fails.
#
# Execution Steps:
# ----------------
# The network product under test receives the access token sent from the NF service consumer,
# verifies the access token based on Oauth 2.0.
# Test Cases 1~4 are tests on failure handling by the network product under test when the mandatory
# claims in access token failed verification.
# Test Case 1: Verification failure of the access token integrity
# 1. The tester computes an access token correctly, except that the signature or the MAC is
# incorrect, e.g., the signature or the MAC is randomly selected, and then includes the access
# token in the NF Service Request sent from the NF service consumer to the network product under
# test.
# 2. The integrity verification of the access token by the network product under test fails.
# Test Case 2: Incorrect audience claim in the access token
# 1. The tester computes an access token correctly, except that the audience claim is incorrect,
# i.e., the audience claim in the access token does not match the identity or the type of the
# network product under test, and then includes the access token in the NF Service Request sent
# from NF service consumer to the network product under test.
# 2. The network product under test verifies that the integrity of the access token is valid.
# However, the audience claim in the access token does not match its identity or type.
# Test Case 3: Incorrect scope claim in the access token
# 1. The tester computes an access token correctly, except that the scope is incorrect, i.e., the
# scope does not match the requested service operation, and then includes the access token in the
# NF Service Request sent from the NF service consumer to the network product under test.
# 2. The network product under test verifies that the integrity of the access token and the
# audience claim are valid. However, the scope does not match the requested service operation.
# Test Case 4: Expired access token
# 1. The tester computes an access token correctly, except that the expiration time has expired
# against the current data/time, and then includes the access token in the NF Service Request sent
# from the NF service consumer to the network product under test.
# 2. The network product under test verifies that the integrity of the access token, the audience
# and scope claims are all valid. However, the expiration time in the access token has expired
# against the current data/time.
# Test Cases 5~8 are tests on failure handling by the network product under test when the optional
# claims in access token failed verification.
# NOTE: The test cases below only apply to the NFs which support identifying and understanding the
# optioanl claims in the received access token.
# Test Case 5: Incorrect list of S-NSSAIs in the access token
# 1. The tester computes an access token correctly, except that the list of S-NSSAIs is incorrect,
# i.e., the network product under test does not serve the slices indicated in the list of S-NSSAIs,
# and then includes the access token in the NF Service Request sent from NF service consumer to the
# network product under test.
# 2. The network product under test verifies that the integrity of the access token, the audience,
# scope and expiration time claims are all valid. Then it further checks the list of S--NSSAIs
# included in the access token.
# Test Case 6: Incorrect list of NSIs in the access token
# 1. The tester computes an access token correctly, except that the list of NSIs is incorrect,
# i.e., the network product under test does not serve the slices indicated in the list of NSIs, and
# then includes the access token in the NF Service Request sent from NF service consumer to the
# network product under test.
# 2. The network product under test verifies that the integrity of the access token, the audience,
# scope and expiration time claims are all valid. Then it further checks the list of NSIs included
# in the access token.
# Test Case 7: Incorrect NF Set ID in the access token
# 1. The tester computes an access token correctly, except that the NF Set ID is incorrect, i.e.
# the NF Set ID in the claim does not match the NF Set ID of the network product under test, and
# then includes the access token in the NF Service Request sent from NF service consumer to the
# network product under test.
# 2. The network product under test verifies that the integrity of the access token, the audience,
# scope and expiration time claims are all valid. Then it further checks the NF Set ID included in
# the access token.
# Test Case 8: Incorrect additional scope in the access token
# 1. The tester computes an access token correctly, except that the additional scope information is
# incorrect, i.e. the allowed resources and allowed actions on the resources do not match the
# requested service operations, and then includes the access token in the NF Service Request sent
# from the NF service consumer to the network product under test.
# 2. The network product under test verifies that the integrity of the access token, the audience,
# scope and expiration time claims are all valid. Then it further checks the additional scope
# included in the access token.
#
# Expected Results:
# ----------------
# For test cases 1~4 on verification failure of mandatory claims in the access token, the network
# product under test rejects the NF service consumer's service request based on Oauth 2.0 error
# response defined in RFC 6749 [12].
# For test cases 5~8 on verification failure of optional claims in the access token, if the network
# product under test understands these optional claims
# (list of S-NSSAIs, list of NSIs, NF Set ID, additional scope),
# it rejects the NF service consumer's service request based on Oauth 2.0 error response defined in
# RFC 6749 [12].


def test_33117_h10_TC_AUTHORIZATION_TOKEN_VERIFICATION_FAILURE_ONE_PLMN():
    skip('Not implemented...')
