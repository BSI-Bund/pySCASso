#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.6.7.2
# Title: Potential security functional requirements on virtualisation resource management
# Purpose:
# 1. To test whether the VNF alerts to the OAM when find the abnormal situation, e.g. a VNFCI is
# deleted by VIM.
# 2. VNF shall log the access from the VIM.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester logs to the VIM and deletes a VM of a VNF;
#
# Expected Results:
# ----------------
# 1. The VNF alerts to the OAM. The alert from the VNF is found in the OAM.
# 2. The VNF logs the alert.


def test_33818_h10_TC_SECURE_VIRTUALISATION_RESOURCE_MANAGEMENT():
    skip('Not implemented...')
