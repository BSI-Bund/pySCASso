#!/usr/bin/python3

from pytest import skip

# Function: VirtNP3GPP
# Source: 33527-i01.md
# Section: 4.2.3.3.5.2
# Title: VNF package and VNF image integrity
# Purpose:
# 1. To test whether the VNF package has been integrity protected or not.
# 2. To test whether the VNF image has been integrity protected or not.
#
# Execution Steps:
# ----------------
# Execute the following steps:
# 1. Review the documentation provided by the vendor describing how VNF package integrity is
# verified;
# 2. During VNF package on boarding, the tester uploads a valid VNF package into a NFVO. The NFVO
# verifies the integrity of the VNF package by validating the digital signature of the VNF package
# using the pre-configured certificate according to the documentation;
# 3. During VNF package on boarding, the tester uploads a not-valid VNF package into a NFVO. The
# NFVO validates the digital signature of the VNF package using the pre-configured certificate;
# 4. During VNF instantiation, the VIM selects a VNF image with a correct integrity protection
# value from the image repository to instantiate the VNF image.
# 5. During VNF instantiation, the VIM selects a VNF image with an incorrect integrity protection
# value from the image repository to instantiate the VNF image.
#
# Expected Results:
# ----------------
# 1. The VNF package is successfully on boarded into the NFVO;
# 2. The not-valid VNF package is not on boarded;
# 3. The VNF image with a correct integrity protection value is instantiated by the VIM;
# 4. The VNF image with an incorrect integrity protection value is not instantiated by the VIM.


def test_33527_i01__TC_VNF_PACKAGE_AND_IMAGE_INTEGRITY():
    skip('Not implemented...')
