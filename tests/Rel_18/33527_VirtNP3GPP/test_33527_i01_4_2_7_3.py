#!/usr/bin/python3

from pytest import skip

# Function: VirtNP3GPP
# Source: 33527-i01.md
# Section: 4.2.7.3
# Title: Instantiating VNF from trusted VNF image
# Purpose:
# To test whether the instantiating VNF from trusted VNF image.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. Review the documentation provided by the vendor describing how digital signature of the VNF
# image is verified;
# 2. The tester uploads a VNF package included two trusted VNF images into a NFVO. The NFVO
# verifies the VNF images by validating each digital signature of the VNF image using the
# pre-configured certificate or the public key according to the documentation;
# 3. The tester uploads another VNF package included un-trusted VNF image into NFVO. The NFVO
# verifies the VNF image(s) by validating each digital signature of the VNF image using the
# pre-configured certificate or the public key according to the documentation.
# Note: The digital signature validation of the image is also described in clause 4.2.3.3.5.2 VNF
# package and VNF image integrity, but the two test cases have the different test purposes. This
# test case focuses on VNF image credibility, while clause 4.2.3.3.5.2 is concerned with VNF image
# integrity.
#
# Expected Results:
# ----------------
# 1. In the step 2, the signatures of the VNF images are successfully validated and the VNF package
# is successfully on boarded into the NFVO;
# 2. In the step 3, the signature of the un-trusted VNF image is failed to be validated and the VNF
# package is not on boarded into the NFVO;


def test_33527_i01__TC_INSTANTIATING_VNF__TRUSTED_IMAGE():
    skip('Not implemented...')
