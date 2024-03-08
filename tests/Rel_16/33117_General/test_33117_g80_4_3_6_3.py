#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.6.3
# Title: Unique key values in IEs
# Purpose:
# Verify that the API implementation fullfills the requirements as specified in 29.501 [13],
# clause 6.2.
#
# Execution Steps:
# ----------------
# 1. The test equipment sends requests with duplicate keys in message IE payload to the network
# product under test.
# 2. The test equipment sends valid requests to network product under test
#
# Expected Results:
# ----------------
# 1. Network product under tests responses with an error message
# 2. Network product under test still responses normally to valid requests


def test_33117_g80_4_3_6_3():
    skip('Missing test case name...')
