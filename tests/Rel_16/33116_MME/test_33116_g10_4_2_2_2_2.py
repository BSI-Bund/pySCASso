#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.2.2
# Title: Re-synchronization
# Purpose:
#
#
# Execution Steps:
# ----------------
# The MME receives an AUTHENTICATION FAILURE message, with the EMM cause #21 "synch failure" and a
# re‑synchronization token AUTS.
#
# Expected Results:
# ----------------
# The MME includes the stored RAND and the received AUTS in the *authentication data request* to
# the HSS.
# NOTE: When RAND and AUTS are not included in the authentication data request to the HSS then the
# HSS will return a new authentication vector (AV) based on its current value of the sequence
# number SQN~HE~ (cf. TS 33.102, clause 6.3.5) A new authentication procedure between MME and UE
# using this new AV will be successful just the same if the cause of the synchronisation failure
# was the sending of a "stale" challenge, i.e. one that the UE had seen before or deemed to be too
# old. But if the cause of the synchronisation failure was a problem with the sequence number
# SQN~HE~ in the HSS (which should be very rare), and the RAND and AUTS are not included in the
# authentication data request to the HSS, then an update of SQN~HE~ based on AUTS will not occur
# in the HSS, and the new authentication procedure between MME and UE using the new AV will fail
# again. This can be considered a security-relevant failure case as it may lead to a subscriber
# being shut out from the system permanently.


def test_33116_g10_4_2_2_2_2():
    skip('Missing test case name...')
