#!/usr/bin/python3

from pytest import skip

# Function: VirtNP
# Source: 33818-h10.md
# Section: 5.2.5.7.7.2
# Title: Potential security functional requirements on hardware resource management
# Purpose:
# To test the hardware alerts the error of the hardware resource configuration from the VIM.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester utilizes the VIM to make an error hardware resource configuration (e.g. error
# firmware upgrade).
# 2. The tester checks whether an alert is triggered or not.
#
# Expected Results:
# ----------------
# The hardware triggers an alert.


def test_33818_h10_TC_SECURE_HARDWARE_RESOURCE_MANAGEMENT():
    skip('Not implemented...')
