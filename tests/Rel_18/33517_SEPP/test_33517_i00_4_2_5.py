#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-i00.md
# Section: 4.2.5
# Title: Web Servers
# Purpose:
# Verify that the SEPP under test correctly implements trust anchoring when setting up HTTPS (TLS)
# connections.
#
# Execution Steps:
# ----------------
# 1. The tester selects two different PLMN IDs, denoted ID1 and ID2, e.g. ID1={MCC=262, MNC=01} and
# ID2={MCC=262, MNC=02}.
# 2. The tester configures two trust anchors in the SEPP under test, as follows:
# - ID1 gets associated with RCA1 and
# - ID2 gets associated with RCA2.
# 3. The tester generates a server certificate for the SEPP under test with which it authenticates
# itself towards a peer SEPP. The peer SEPP is configured to accept these certificates.
# 4. The tester generates four TLS client certificates C1, C2, C3, C4 for the peer SEPP, as
# follows:
# - C1 contains ID1 and is signed by RCA1 (or a subCA which is signed only by RCA1)
# - C2 contains ID2 and is signed by RCA2 (or a subCA which is signed only by RCA2)
# - C3 contains ID1 and is signed by RCA2 (or a subCA which is signed only by RCA2)and
# - C4 contains both ID1 and ID2 and is signed by RCA1 or RCA2
# (or a subCA which is signed by RCA1 or RCA2).
# NOTE 1: The expression "contains IDX" means that there exists a Subject Alternative Name (SAN)
# field in the certificate that contains the value chosen in step 1. Examples of the SAN field
# contents are example.sepp.5gc.mnc02mcc262.3gppnetwork.org and
# example.sepp.5gc.mnc01mcc262.exampleipx.ipxnetwork.org
# 5. The peer SEPP is configured to authenticate itself using C1. If C1 was issued by a SubCA, then
# the SubCA certificate is included in the certificate chain which the peer SEPP uses to
# authenticate itself. The tester initiates an N32c connection from the SEPP under test towards the
# peer SEPP and observes whether the HTTPS connection succeeds, and, if not, documents the failure
# reasons as shown in the log files of the SEPP under test.
# 6. The tester repeats step 5, replacing C1 with C2, C3, and C4 iteratively.
# 7. Steps 3 to 6 are repeated in order to test for reversed client/server roles. Specifically, in
# step 3 the tester generates a client certificate (instead of a server certificate), in step 4 the
# tester generates four server certificates (instead of four client certificates), and in step 5
# the tester initiates the connection from the peer SEPP (instead of initiating the connection from
# the SEPP under test).
#
# Expected Results:
# ----------------
# In step 5, the TLS (HTTPS) connection setup succeeds for the iterations with C1 and C2 and fails
# for the iterations with C3 and C4.
# NOTE 2: The iteration with C3 fails because the PLMN-ID indicated in the client certificate does
# not match any of the trusted certificates in the corresponding trust anchor. The iteration with
# C4 fails because the PLMN-IDs indicated in the client certificate are not associated with the
# same trust anchor.


def test_33517_i00__TC_CORRECT_TRUST_ANCHORING():
    skip('Not implemented...')
