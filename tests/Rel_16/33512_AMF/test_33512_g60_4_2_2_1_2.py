#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.1.2
# Title: RES* verification failure handling
# Purpose:
# 1. Verify that the SEAF/AMF correctly handles RES* verification failure detected in the SEAF/AMF
# or/and in the AUSF, when the SUCI is included in the initial NAS message.
# 2. Verify that the SEAF/AMF correctly handles RES* verification failure detected in the SEAF/AMF
# or/and in the AUSF, when the 5G-GUTI is included in the initial NAS message.
#
# Execution Steps:
# ----------------
# A. Test Case 1
# 1. The UE sends RR with SUCI to the SEAF/AMF under test, to trigger the SEAF/AMF under test to
# initiate the authentication, i.e. to send Nausf_UEAuthentication_Authenticate Request to the
# AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE, after receiving the Authentication Request message from the SEAF/AMF under test,
# returns an incorrect RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES* and send an authentication
# request to the AUSF. The tester captures the value of RES* in the request.
# 4. The AUSF returns to the AMF under test the indication of RES* verification failure.
# B. Test Case 2
# 1. The UE sends RR with a 5G-GUTI to the SEAF/AMF under test, to trigger the SEAF/AMF under test
# to initiate the authentication, i.e. to send Nausf_UEAuthentication_Authenticate Request to the
# AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE, after receiving the Authentication Request message from the SEAF/AMF under test,
# returns an incorrect RES* to the SEAF/AMF in the NAS Authentication Response message, which will
# trigger the AMF to compute HRES* and compare HRES* with HXRES*, and send an authentication
# request to the AUSF. The tester captures the value of RES* in the request.
# 4. The AUSF returns to the AMF under test an indication of RES* verification failure.
# C. Test Case 3
# 1. The UE sends RR with SUCI to the SEAF/AMF under test, to trigger the SEAF/AMF under test to
# initiate the authentication, i.e. to send Nausf_UEAuthentication_Authenticate Request to the
# AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send to the received
# RES* to the AUSF.
# 4. The AUSF returns to the AMF under test an indication of RES* verification failure.
# D Test Case 4
# 1. The UE sends RR with 5G-GUTI to the SEAF/AMF under test, to trigger the SEAF/AMF under test to
# initiate the authentication, i.e. to send Nausf_UEAuthentication_Authenticate Request to
# the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send to the received
# RES* to the AUSF.
# 4. The AUSF returns to the AMF under test an indication of RES* verification failure.
#
# Expected Results:
# ----------------
# For test case 1 and 3, the SEAF/AMF rejects the authentication by sending an
# Authentication Reject to the UE.
# For test case 2 and 4, the SEAF/AMF initiates an Identification procedure with the UE to retrieve
# the SUCI.


def test_33512_g60_TC_RES_VERIFICATION_FAILURE():
    skip('Not implemented...')
