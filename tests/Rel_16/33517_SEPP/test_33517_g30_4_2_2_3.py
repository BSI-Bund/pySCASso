#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.3
# Title: Connection-specific scope of cryptographic material by IPX-providers
# Purpose:
# Verify that the SEPP to be tested does not use cryptographic material from IPX-providers other
# than the ones whose raw public key/certificate has been exchanged in the related N32-c connection
# to authenticate N32-f message modifications.
#
# Execution Steps:
# ----------------
# 1. Both SEPPs are configured for N32-f communication via the simulated IPX-system.
# 2. Both SEPPs establish a mutual N32-c connection. As part of the *IPX security information list*
# , the secondary SEPP provides one of the prepared raw public keys/certificates of the
# IPX-providers (KEY_A) to the SEPP under test.
# 3. Parallel to the N32 connection in step 1, an additional connection is established between the
# two SEPPs. Within this connection, an alternate raw public key/certificate of the
# IPX-providers (KEY_B) shall be exchanged.
# 4. Within the N32 connection established in step 1, the tester sends an N32-f message from the
# secondary SEPP towards the SEPP under test. The intermediate IPX-system appends an arbitrary
# JSON-(NULL-)patch, which is signed with the private key belonging to KEY_B, i.e. the one out of
# scope of this particular N32 connection. The modified message is then forwarded to the SEPP to
# be tested.
# 5. Based on the log files of the SEPP under test, the tester validates how the received N32-f
# message is handled.
#
# Expected Results:
# ----------------
# - N32-f message modifications which have been signed by IPX-providers whose information has not
# been exchanged as part of the related N32-c connection are discarded by the SEPP under test.


def test_33517_g30_TC_CONNECTION_SPECIFIC_SCOPE_CRYPT_MATERIAL():
    skip('Not implemented...')
