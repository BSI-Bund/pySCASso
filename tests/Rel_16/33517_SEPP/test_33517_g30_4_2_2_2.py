#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.2
# Title: Correct handling of cryptographic material of peer SEPPs and IPX providers
# Purpose:
# Verify that the SEPP under test does not accept raw public keys/certificates by intermediate
# IPX-providers for N32-c TLS connection establishment. The opposite is to be ensured as well:
# The SEPP under test shall not accept N32-f JSON patches signed with raw public keys/certificates
# of peer SEPPs.
#
# Execution Steps:
# ----------------
# 1.1 Both SEPPs are configured for N32-f communication via the simulated IPX-system.
# 1.2 Both SEPPs establish a N32 connection with each other. The secondary SEPP provides the
# IPX-provider's public key/certificate to the SEPP under test as part of the *IPX security
# information list* via N32-c.
# 1.3 While the N32 connection from the previous step is still active, the tester attempts to
# establish an additional N32-c TLS connection using the IPX-providers private key.
# 1.4 Based on the internal log files, the tester validates how the SEPP under test handles the
# N32-c connection attempt.
# 2.1 Both SEPPs are configured for N32-f communication via the simulated IPX-system.
# 2.2 Both SEPPs establish a N32-c connection with each other. The secondary SEPP provides the
# IPX-provider's public key/certificate to the SEPP under test as part of the *IPX security
# information list* via N32-c.
# 2.3 The tester sends a N32-f message from the secondary SEPP via the IPX-system towards the SEPP
# under test.
# 2.4 The intermediate IPX-system appends an arbitrary JSON-(NULL-)patch to the N32-f message and
# signs it not with its own private key, but the private key of the secondary SEPP. The modified
# message is then forwarded to the SEPP under test.
# 2.5 Based on the internal log files, the tester validates how the received N32-f message is
# handled by the SEPP under test.
# Expected Results:
# - The N32-c TLS connection establishment using the cryptographic material of the intermediate
# IPX-system fails with the SEPP to be tested (step 1.4).
# - The JSON patch signed with the peer SEPP's private key is discarded by the SEPP under test
# (step 2.5).
#
# Expected Results:
# ----------------
#


def test_33517_g30_TC_CRYPT_MATERIAL_SEPP_IPX_SEPARATION():
    skip('Not implemented...')
