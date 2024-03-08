#!/usr/bin/python3

from pytest import skip

# Function: SEPP
# Source: 33517-g30.md
# Section: 4.2.2.8
# Title: No misplacement of encrypted IEs in JSON object by IPX
# Purpose:
# Verify that the SEPP under test is able to verify that an intermediate IPX has not misplaced
# (moved or copied) an encrypted IE to a different location in a JSON object that would be
# reflected from the producer NF for an IE without encryption.
#
# Execution Steps:
# ----------------
# 1. Both SEPPs are configured for N32-f communication via the simulated IPX-system.
# 2. Both SEPPs establish a mutual N32-c connection.
# 3. The tester sends a N32-f message from the secondary SEPP via the IPX-system towards the SEPP
# under test. This message needs to contain at least one information element that requires
# encryption according to the locally configured Data-type encryption policy.
# 4. The IPX-system modifies the N32-f message according to its configured modification policy. The
# tester then inserts the encBlockIDx into a cleartext IE in the modified N32-f message before
# sending to the SEPP under test.
# 5. The IPX-system sends the modified N32-f message to the SEPP under test.
# 6. Based on the internal log files, the tester validates how the received N32-f message is
# handled by the SEPP under test.
#
# Expected Results:
# ----------------
# - The N32-f message is discarded by the SEPP under test. The error defined in the
# clause 6.1.5.3.7 of TS 29.573[6] is sent by the SEPP via N32-c interface.


def test_33517_g30_TC_NO_ENCRYPTED_IE_MISPLACEMENT():
    skip('Not implemented...')
