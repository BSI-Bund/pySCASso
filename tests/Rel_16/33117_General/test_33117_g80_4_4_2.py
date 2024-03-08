#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.4.2
# Title: Port Scanning
# Purpose:
# To ensured that on all network interfaces, only documented ports on the transport layer respond
# to requests from outside the system
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. Verification of the compliance to the prerequisites:
# a. Verification that the list of available network services is available in the documentation of
# the Network Product
# b. Validation that all entries in the list of services are meaningful and reasonably necessary
# for the operation of the Network Product class
# 2. Identification of the open ports by means of capable port scanning tools or other suitable
# testing means
# 3. Verification that the list of identified open ports matches the list of available network
# services in the documentation of the Network Product
#
# Expected Results:
# ----------------
# The used tool(s) name, their unambiguous version (also for plug-ins if applicable), used
# settings, and the relevant output containing all the technically relevant information about test
# results is evidence and shall be part of the testing documentation.
# All discrepancies between the list of identified open ports and the list of available network
# services in the documentation shall be highlighted in the testing documentation.


def test_33117_g80_TC_BVT_PORT_SCANNING():
    skip('Not implemented...')
