#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-h00.md
# Section: 4.2.2.10
# Title: Correct Handling of Custom HTTP Header with PRINS Security
# Purpose:
# Verify that the SEPP under test correctly handle the 3gpp-Sbi-Target-apiRoot custom HTTP header
# received from a NF when PRINS security is negotiated with the peer SEPP in a remote PLMN.
#
# Execution Steps:
# ----------------
# 1. The NF initiates a HTTP message sent to the SEPP under test, which includes the
# 3gpp-Sbi-Target-apiRoot header containing the apiRoot of the target URI in the remote PLMN and
# the apiRoot in the request URI set to the apiRoot of the SEPP under test.
# 2. The SEPP under test forwards the HTTP request to the peer SEPP in the remote PLMN within the
# N32-f TLS tunnel.
#
# Expected Results:
# ----------------
# The peer SEPP received the protected HTTP Request from the NF through the SEPP under test, in
# which the apiRoot in the request URI is the apiRoot of the target URI in the remote PLMN and no
# 3gpp-Sbi-Target-apiRoot header is present.


def test_33517_h00_TC_HANDLING_CUSTOM_HTTPHEADER_WITH_PRINS():
    skip('Not implemented...')
