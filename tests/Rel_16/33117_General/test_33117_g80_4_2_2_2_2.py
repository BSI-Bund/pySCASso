#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.2.2.2
# Title: Protection at the transport layer
# Purpose:
# Verify that TLS protocol for NF mutual authentication and NF transport layer protection is
# implemented in the network products based on the profile required.
#
# Execution Steps:
# ----------------
# 1. The tester shall check that compliance with the TLS profile can be inferred from detailed
# provisions in the network product documentation.
# 2. The tester shall establish a secure connection between the network product under test and the
# peer and verify that all TLS protocol versions and combinations of cryptographic algorithms that
# are mandated by the TLS profile are supported by the network product under test.
# 3. The tester shall try to establish a secure connection between the network product under test
# and the peer and verify that this is not possible when the peer only offers a feature, including
# protocol version and combination of cryptographic algorithms, that is forbidden by the
# TLS profile.
#
# Expected Results:
# ----------------
# - The network product under test and the peer establish TLS if the TLS profiles used by the peer
# are compliant with the profile requirements in TS 33.310 [9] Annex E and RFC 7540 [11].
# - The network product under test and the peer fail to establish TLS if the TLS profiles used by
# the peer are forbidden in TS 33.310 [9] Annex E or RFC 7540 [11].


def test_33117_g80_TC_PROTECT_TRANSPORT_LAYER():
    skip('Not implemented...')
