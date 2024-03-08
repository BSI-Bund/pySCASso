#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.2.5
# Title: Mobility binding
# Purpose:
#  To test whether the PGW validates the MN-HA authentication extension correctly.
#
# Execution Steps:
# ----------------
# The PGW (home agent for the UE) is active in a 3GPP access network.
# The tester captures packets over S6b and S2a interfaces using any packet analyser.
# The tester filters the MN-HA Key transported in the authentication and authorization information
# from the 3GPP AAA server to PGW over S6b interface.
# The UE sends a Registration Request message to PGW via the trusted non-3GPP IP access network.
# The tester filters the Registration Request sent by UE to PGW and Registration Reply sent by PGW
# to UE over the S2a interface.
# The tester uses the SPI value in Registration Request to identify the MN-HA key to compute the
# Authenticator value of the authentication extension.
# The tester verifies that the computed Authenticator value is same as the Authenticator value in
# the Registration Request message.
# The tester also checks the Reply Code in the Registration Reply message to verify the correctness
# of the validation at PGW.
#
# Expected Results:
# ----------------
# The Reply code is '0' in the Registration Reply message.


def test_33250_g00_TC_PGW_MIP_AUTH_Non_3GPP():
    skip('Not implemented...')
