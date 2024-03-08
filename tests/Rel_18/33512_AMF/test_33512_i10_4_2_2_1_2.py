#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.1.2
# Title: RES* verification failure handling
# Purpose:
# 1. Verify that the SEAF/AMF correctly handles RES* verification failure detected in the SEAF/AMF
# or/and in the AUSF, when the SUCI is included in the initial NAS message.
# 2. Verify that the SEAF/AMF correctly handles RES* verification failure detected in the SEAF/AMF
# or/and in the AUSF, when the 5G-GUTI is included in the initial NAS message.
# 3. Verify that the SEAF/AMF correctly handles a missing Nausf_UEAuthentication_Authenticate
# Response message from the AUSF.
#
# Execution Steps:
# ----------------
# Test Case A:
# 1. The tester triggers the UE to send a Registration Request with SUCI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE, after receiving the Authentication Request message from the SEAF/AMF under test,
# returns an incorrect RES* (prepared by the tester) to the SEAF/AMF under test in the NAS
# Authentication Response message, which will trigger the AMF to compute HRES*, compare HRES* with
# HXRES* and send an authentication request to the AUSF. The tester captures the value of RES* in
# the request.
# 4. The AUSF returns the indication of RES* verification failure to the AMF under test.
# Test Case B:
# 1. The tester triggers the UE to send a Registration Request with a 5G-GUTI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE, after receiving the Authentication Request message from the SEAF/AMF under test,
# returns an incorrect RES* (prepared by the tester) to the SEAF/AMF in the NAS Authentication
# Response message, which will trigger the AMF to compute HRES* and compare HRES* with HXRES*, and
# send an authentication request to the AUSF. The tester captures the value of RES* in the request.
# 4. The AUSF returns an indication of RES* verification failure to the AMF under test.
# Test Case C:
# 1. The tester triggers the UE to send a Registration Request with SUCI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send to the received
# RES* to the AUSF.
# 4. The tester prepares the AUSF or intercepts and modifies its
# Nausf_UEAuthentication_Authenticate Response message to the SEAF/AMF to indicate that the RES*
# verification was not successful in the AUSF.
# Test Case D:
# 1. The tester triggers the UE to send a Registration Request with 5G-GUTI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send to the received
# RES* to the AUSF.
# 4. The tester prepares the AUSF or intercepts and modifies its
# Nausf_UEAuthentication_Authenticate Response message to the SEAF/AMF to indicate that the RES*
# verification was not successful in the AUSF.
# Test E:
# 1. The tester triggers the UE to send a Registration Request with SUCI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send the received
# RES* to the AUSF.
# 4. The tester prepares the AUSF to not return the Nausf_UEAuthentication_Authenticate Response
# message and therefore trigger a timeout at the SEAF/AMF.
# Test F:
# 1. The tester triggers the UE to send a Registration Request with 5G-GUTI to the SEAF/AMF under
# test, to trigger the SEAF/AMF under test to initiate the authentication, i.e. to send
# Nausf_UEAuthentication_Authenticate Request to the AUSF.
# 2. The AUSF, after receiving the request from the SEAF/AMF under test, responds with a
# Nausf_UEAuthentication_Authenticate Response message with an authentication vector to the
# SEAF/AMF under test.
# 3. The UE returns RES* to the SEAF/AMF under test in the NAS Authentication Response message,
# which will trigger the AMF to compute HRES*, compare HRES* with HXRES*, and send the received
# RES* to the AUSF.
# 4. The tester prepares the AUSF to not return the Nausf_UEAuthentication_Authenticate Response
# message and therefore trigger a timeout at the SEAF/AMF.
# NOTE: The timeout timer is the NAS timer T3520.
#
# Expected Results:
# ----------------
# For test case A and C, the SEAF/AMF rejects the authentication by sending an Authentication
# Reject to the UE.
# For test case B and D, the SEAF/AMF initiates an Identification procedure with the UE to retrieve
# the SUCI.
# For test case E and F, the SEAF/AMF rejects the authentication to the UE or initiate an
# Identification procedure with the UE.
# For test case A and B, a null value RES* is in the Nausf_UEAuthentication_Authenticate Request
# message sent from the SEAF/AMF to the AUSF. (stated in TS 29.509 [10], clause 5.2.2.2.2).


def test_33512_i10__TC_RES_STAR_VERIFICATION_FAILURE():
    skip('Not implemented...')
