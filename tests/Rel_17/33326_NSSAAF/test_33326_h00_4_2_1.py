#!/usr/bin/python3

from pytest import skip

# Function: NSSAAF
# Source: 33326-h00.md
# Section: 4.2.1
# Title: Routes the S-NSSAI to the right place
# Purpose:
# Verify that the NSSAAF forwards the NSSAA request to the right receiving end.
#
# Execution Steps:
# ----------------
# 1. The AMF sends Nssaaf_NSSAA_Authenticate Req to the NSSAAF including one of the S-NSSAI.
# 2. The NSSAAF sends AAA message to an AAA-P.
# 3. Repeat step 1 and 2 with the other S-NSSAI, and the NSSAAF sends AAA message to an AAA-S.
#
# Expected Results:
# ----------------
# The NSSAAF forwards the NSSAA request to the correct AAA-S or AAA-P on the S-NSSAI.


def test_33326_h00_TC_NSSAAF_CORRECT_ROUTING():
    skip('Not implemented...')
