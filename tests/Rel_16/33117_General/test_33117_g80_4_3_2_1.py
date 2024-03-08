#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.2.1
# Title: No unnecessary or insecure services / protocols
# Purpose:
# To ensure that on all network interfaces, there are no unsecure services or protocols that might
# be running.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. Verification of the compliance to the prerequisites:
# a. Verification that the list of available network services and protocol handlers is available
# in the documentation of the Network Product.
# b. Validation that all entries in the list are meaningful and reasonably necessary for the
# operation of the Network Product class.
# 2. Identification of the network services and protocol handlers by means of capable tools or any
# other suitable testing means.
# 3. Validation that there are no entries in the list of network services and handlers apart from
# the ones that have been mentioned and deemed necessary for the operation of the Network Product
# in the attached documentation.
# 4. The tester shall reboot the network product and re-execute execution steps 2 and 3 without
# further configuration.
#
# Expected Results:
# ----------------
# The report will contain:
# - The names and version of the tool(s) used.
# - Information of all the protocol handlers and services running in the network product.
# Result will show:
# - There are no unnecessary services running in the network product except for the ones which are
# deemed necessary for its operation.
# - Any undocumented services running on the network product should be highlighted and brought out
# in the report.
# - The network product behaves the same after reboot as before.


def test_33117_g80_TC_NO_UNNECESSARY_SERVICE():
    skip('Not implemented...')
