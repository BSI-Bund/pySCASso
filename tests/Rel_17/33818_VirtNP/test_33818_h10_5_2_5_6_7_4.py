#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.6.7.4
# Title: Potential security functional requirements on VM escape
# Purpose:
# To test the virtualisation layer rejects the abnormal access from the VNF and logs the attacks
# from the VNF.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester logs the VNF and makes an abnormal access (e.g. the VNF accesses the memory which
# is not allocated to the VNF) to the virtualisation layer.
# 2. The tester checks whether the virtualisation layer rejects the abnormal access from the VNF
# and logs the attacks.
#
# Expected Results:
# ----------------
# The virtualisation layer rejects the abnormal access from the VNF and logs the attacks.


def test_33818_h10_TC_VM_ESCAPE_PROTECTION():
    skip('Not implemented...')
