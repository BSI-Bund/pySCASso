#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-h10.md
# Section: 4.2.2.2.4.1
# Title: Correct handling of client credentials assertion validation failure
# Purpose:
# Verify that the NF under test correctly handles client credentials assertion validation failure.
# Editor's Note: This test case applies for Rel-16 NFs. The formulation for indicating the
# applicable release may need to be updated.
#
# Execution Steps:
# ----------------
# Test Case 1: Failed verification of the client credentials assertion integrity
# 1. The tester computes a client credentials assertion correctly, except that the signature is
# incorrect, and then includes the client credentials assertion in the service request sent from
# the consumer NF to the NF under test via the SCP.
# 2. The integrity verification of the client credentials assertion by the NF under test fails.
# Test Case 2: Incorrect audience claim in the client credentials assertion
# 1. The tester computes a client credentials assertion correctly, except that the audience claim
# is incorrect, i.e., the audience claim in the client credentials assertion does not match the
# type of the NF under test, and then includes the signed client credentials assertion in the
# service request sent from the consumer NF to the NF under test via the SCP.
# 2. The NF under test verifies that the audience claim in the client credentials assertion does
# not match its type.
# Test Case 3: Expired client credentials assertion
# 1. The tester computes an access token correctly, except that the expiration time (exp) has
# expired against the current time, and then includes the signed client credentials assertion in
# the service request sent from the consumer NF to the NF under test via the SCP.
# 2. The NF under test verifies that the expiration time in the client credentials assertion has
# expired against the current time.
#
# Expected Results:
# ----------------
# For test cases 1~3, the NF under test rejects the consumer NF's service request and sends back an
# error message.
# Editor's Note: the result needs to be aligned with the relevant error handling description to be
# added in TS 29.500.


def test_33117_h10_TC_CLIENT_CREDENTIALS_ASSERTION_VALIDATION():
    skip('Not implemented...')
