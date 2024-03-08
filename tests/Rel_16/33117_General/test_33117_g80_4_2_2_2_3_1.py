#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
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
# Test Case 1: Verification failure of the access token integrity
# 1. The tester computes an access token correctly, except that the signature or the MAC is
# incorrect, e.g., the signature or the MAC is randomly selected, and then includes the access
# token in the NF Service Request sent from the NF service consumer to the network product
# under test.
# 2. The integrity verification of the access token by the network product under test fails.
# Test Case 2: Incorrect audience claim in the access token
# 1. The tester computes an access token correctly, except that the audience claim is incorrect,
# i.e., the audience claim in the access token does not match the identity or the type of the
# network product under test, and then includes the access token in the NF Service Request sent
# from NF service consumer to the network product under test.
# 2. The network product under test verifies that the audience claim in the access token does not
# match its identity or type.
# Test Case 3: Incorrect scope claim in the access token
# 1. The tester computes an access token correctly, except that the scope is incorrect, i.e., the
# scope does not match the requested service operation, and then includes the access token in the
# NF Service Request sent from the NF service consumer to the network product under test.
# 2. The network product under test verifies that the integrity verification of the access token
# and audience claim verification are correct. However, the scope does not match the requested
# service operation.
# Test Case 4: Expired access token
# 1. The tester computes an access token correctly, except that the expiration time has expired
# against the current data/time, and then includes the access token in the NF Service Request sent
# from the NF service consumer to the network product under test.
# 2. The network product under test verifies that the expiration time in the access token has
# expired against the current data/time.
#
# Expected Results:
# ----------------
# For test cases 1~4, the network product under test rejects the NF service consumer's service
# request based on Oauth 2.0 error response defined in RFC 6749 [12].


def test_33117_g80_TC_AUTHORIZATION_TOKEN_VERIFICATION_FAILURE_ONE_PLMN():
    skip('Not implemented...')
