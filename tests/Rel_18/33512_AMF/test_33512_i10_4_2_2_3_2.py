#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.3.2
# Title: NAS NULL integrity protection
# Purpose:
# Verify that NAS NULL integrity protection algorithm is used correctly.
#
# Execution Steps:
# ----------------
# **Test case A:**
# 1. The tester triggers the UE to initiate an emergency registration.
# 2. The AMF derives the K~AMF~ and NAS signalling keys after successful authentication of the UE.
# 3. The AMF sends the NAS Security Mode Command message to the UE containing the selected NAS
# algorithms.
# **Test case B:**
# 1. The tester triggers the UE to initiate a non-emergency registration.
# 2. The AMF derives the K~AMF~ and NAS signalling keys after successful authentication of the UE.
# 3. The AMF sends the NAS Security Mode Command message to the UE containing the selected NAS
# algorithms.
#
# Expected Results:
# ----------------
# In both emergency and non-emergency registrations, the UE was successfully authentication and the
# integrity algorithm selected by the AMF in the NAS SMC message is different from NIA0.
# The NAS Security Mode Command message is integrity protected by the AMF.


def test_33512_i10__TC_NAS_NULL_INT_AMF():
    skip('Not implemented...')
