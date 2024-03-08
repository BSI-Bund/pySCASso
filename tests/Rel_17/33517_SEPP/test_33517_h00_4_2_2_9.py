#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-h00.md
# Section: 4.2.2.9
# Title: Correct Handling of Inter-PLMN Routing
# Purpose:
# Verify that the SEPP under test correctly route the NF request to a remote PLMN when receving
# both a 3gpp-Sbi-Target-apiRoot header and a telescopic FQDN contained in the Request URI in the
# HTTP request from a NF.
#
# Execution Steps:
# ----------------
# 1. The NF sets up a TLS connection with the authoritative server for the configured telescopic
# FQDN, i.e. the SEPP under test.
# 2. The NF sends a HTTP service request with the request URI containing the configured telescopic
# FQDN within the TLS connection to the SEPP under test, before which the tester inserts in the
# HTTP request a 3gpp-Sbi-Target-apiRoot header set to the apiRoot of a NF producer in another PLMN
# different from the remote PLMN.
# 3. The NF sends a HTTP service request within the TLS connection to the SEPP under test, before
# which the tester inserts in the HTTP request a 3gpp-Sbi-Target-apiRoot header set to the apiRoot
# of the NF producer in the remote PLMN and changes the telescopic FQDN in request URI to be
# different from the configured one.
#
# Expected Results:
# ----------------
# After step 2), the peer SEPP received the HTTP request from the NF through the SEPP under test.
# After step 3), the peer SEPP did not receive the HTTP request from the NF through the SEPP under
# test


def test_33517_h00_TC_CORRECT_INTER_PLMN_ROUTING():
    skip('Not implemented...')
