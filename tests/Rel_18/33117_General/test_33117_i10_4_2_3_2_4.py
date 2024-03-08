#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.2.3.2.4
# Title: Protecting data and information in transfer
# Purpose:
# Verify the mechanisms implemented to protect data and information in transfer to and from the
# Network Product's OAM interface.
# NOTE: The test is limited to the OAM interface although the requirement does not have this
# limitation because the protection of standardised interfaces will be covered by regular
# interoperability testing and the proprietary use of HTTPS is covered in clause 4.2.5.1.
#
# Execution Steps:
# ----------------
# 1. The tester shall check that compliance with the selected security profile can be inferred from
# detailed provisions in the product documentation.
# 2. The tester shall check that the default security parameters are the same as those stated in
# the product documentation.
# 3. The tester shall establish a secure connection between the network product and the peer and
# verify that all protocol versions and combinations of cryptographic algorithms that are mandated
# by the security profile are supported by the network product and the network product does not use
# the deprecated or unsecure protocol versions and algorithms.
# 4. The tester shall try to establish a secure connection between the network product and the peer
# and verify that this is not possible when the peer only offers a feature, including protocol
# version and combination of cryptographic algorithms, that is forbidden by the security profile.
#
# Expected Results:
# ----------------
# The traffic is properly protected, and insecure options are not accepted by the Network Product.


def test_33117_i10__TC_PROTECT_DATA_INFO_TRANSFER_1():
    skip('Not implemented...')
