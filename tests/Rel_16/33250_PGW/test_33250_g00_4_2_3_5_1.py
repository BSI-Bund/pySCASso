#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.3.5.1
# Title: Unpredictable GTP TEID
# Purpose:
# To verify that the GTP TEID is unpredictable
#
# Execution Steps:
# ----------------
# 1.  The tester intercepts the traffic between the P-GW and the S-GW.
# 2.  The tester triggers 10 consecutives CreateSessionRequest e.g. for an Initial UE Attach
# towards the P-GW (using a real or a simulated S-GW) with GTP header TEID set to 0 and F-TEID set
# to different values.
# 3.  The tester triggers one CreateSessionRequest, this request shall be for another UE and from
# another S-GW
# 4.  The P-GW creates a UE/S-GW context and communicates with the PCRF (real or simulated) for QOS
# and APN resolve. That procedures shall be successful in order to permit to the P-GW to send back
# to the S-GW a CreateSessionResponse containing at least :
# a.  A Success cause.
# b.  The P-GW's F-TEID for control plane
# c.  The PDN Address Allocation (PAA).
# d.  A Bearer Contexts Created.
# 5.  The tester tries to predict the F-TEID created for the final CreateSessionResponse from the
# initial 10 F-TEIDs.
#
# Expected Results:
# ----------------
# The tester cannot predict the F-TEID in the finalCreateSessionResponse.


def test_33250_g00_UNPRED_GTP_TEID():
    skip('Not implemented...')
