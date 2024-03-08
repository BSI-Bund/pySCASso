#!/usr/bin/python3

from pytest import skip

# Function: NEF
# Source: 33519-g20.md
# Section: 4.2.2.1
# Title: Security functional requirements on the NEF deriving from 3GPP specifications --
# TS 33.501 [2]
# Purpose:
#  To verify that the NEF can authorize application function.
#
# Execution Steps:
# ----------------
# Test 1: without token:
# 1. The application function invokes Obtain_Authorization service towards the authorization server
# to get a token from the authorization server for accessing the NEF northbound API A.
# 2. The application function invokes NEF northbound API A.
# 3. The tester triggers the application function to invoke another northbound API of the NEF
# network product, called NEF northbound API B, without token.
# Test 2: With incorrect token:
# 1. The application function invokes Obtain_Authorization service towards the authorization server
# to get a token from the authorization server for accessing the NEF northbound API A.
# 2. The application function invokes NEF northbound API A.
# 3. The tester triggers the application function to invoke the NEF northbound API B with a fake
# token.
#
# Expected Results:
# ----------------
# The invoking of NEF northbound API A succeeds, while the invoking of NEF northbound API B fails.


def test_33519_g20_TC_CP_AUTHOR_AF_NEF():
    skip('Not implemented...')
