#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.7.7.3
# Title: Potential security functional requirements on tampering hardware resource management
# information
# Purpose:
# To test the hardware alerts the error of the hardware resource configuration.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester tampers a received hardware resource configuration that the virtualisation layer
# received from the VIM.
# 2. The tester checks whether the hardware alerts when the tampered hardware resource
# configuration is implemented.
#
# Expected Results:
# ----------------
# The hardware alerts the error of the hardware resource configuration.


def test_33818_h10_TC_SECURE_HARDWARE_RESOURCE_MANAGEMENT_INFORMATION():
    skip('Not implemented...')
