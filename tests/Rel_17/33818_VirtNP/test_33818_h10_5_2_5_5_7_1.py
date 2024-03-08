#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.5.7.1
# Title: Potential security functional requirements on GVNP lifecycle management
# Purpose:
# 1. To test the VNF authenticates VNFM when VNFM initiates a communication to VNF.
# 2. To test the VNF establishes secure connection with the VNFM after successful authentication.
# 3. To test the VNF check whether VNFM has been authorized when VNFM access to VNF's API.
# 4. To check whether VNF logs the lifecycle management operations from VNFM.
# Note: This test case is optional when the VNF and VNFM belongs to the same VNF vendor. If the VNF
# and VNFM belongs to the same VNF vendor and the interface between VNF and VNFM is proprietary
# interface, the API level authorization is not needed.
#
# Execution Steps:
# ----------------
#
#
# Expected Results:
# ----------------
# 1. Secure communication is established between VNF and VNFM with integrity and confidentiality
# protection.
# 2. The VNFM successfully accesses the VNF's API.
# 3. The VNF logs the operations from VNFM.


def test_33818_h10_TC_LIFECYCLE_MANAGEMENT_SECURITY():
    skip('Not implemented...')
