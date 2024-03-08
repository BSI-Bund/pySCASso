#!/usr/bin/python3

from pytest import skip

# Function: AKMA_AAnF
# Source: 33537-i20.md
# Section: 4.2.2.1
# Title: AKMA key storage and update
# Purpose:
# Verify that the AAnF stores only the latest AKMA context received by the AUSF.
#
# Execution Steps:
# ----------------
# Test A:
# 1. Primary authentication is simulated for a specific UE, leading to the simulated AUSF pushing
# SUPI, A-KID1, K~AKMA~1 to the AAnF.
# 2. The AF requests a K~AF~ from the AAnF by proving A-KID1 and AF_ID.
# 3. Another primary authentication is simulated for the same UE, leading to the simulated AUSF
# pushing SUPI, A-KID2, K~AKMA~2 to the AAnF.
# 4. The AF requests a K~AF~ by providing A-KID1 to the AAnF.
# 5. The AF requests a K~AF~ by providing A-KID2 to the AAnF.
#
# Expected Results:
# ----------------
# The AF received an error message indicating the AKMA context related to A-KID 1 is not found
# after step 4). After step 5), the AF received a K~AF~ which is different from the K~AF~ that
# received after step 2).


def test_33537_i20__TC_AKMA_Key_Storage_Update():
    skip('Not implemented...')
