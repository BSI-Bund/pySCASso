#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.6
# Title: Ciphering of RRC-signalling
# Purpose:
#  To verify that the RRC-signalling data sent between UE and gNB over the NG RAN air interface are
# confidentiality protected.
#
# Execution Steps:
# ----------------
# 1. The UE sends a Registraton Request to the AMF.
# 2. The AMF sends a KgNB and the UE security capability to the gNB.
# 3. The gNB selects an algorithm and sends AS SMC to the UE.
# 4. The gNB receive AS SMP from the UE.**Expected Results:**
# Control plane packets sent to the UE after the gNB sends AS SMC is ciphered.
#
# Expected Results:
# ----------------
#


def test_33511_g80_TC_CP_DATA_CIP_RRC_SIGN_gNB():
    skip('Not implemented...')
