#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.5
# Title: Protection from buffer overflows
# Purpose:
# To ensure that the system supports mechanisms that protect against buffer overflow.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. The tester verifies that there is:
# a. A technical description of the buffer overflow protection mechanisms that have been
# implemented on the system.
# b. Details of whether the buffer overflow protection mechanisms are implemented by default or if
# additional actions (e.g. scripts or commands manually executed) are required.
# c. If manually executed actions are required then detailed instructions should be included in the
# technical description.
# 2. The tester verifies that the test results:
# a. Describe test procedures used to verify the buffer overflow protection mechanisms,
# b. Contain data which demonstrates/indicates that the buffer overflow protection mechanisms
# described in the technical description document have been implemented.
# c. Contains details of the test set-up for the testing of the buffer overflow protection
# mechanisms. Where simulators and/or scripts are used to artificially create the conditions to
# trigger the buffer overflow protection mechanism then details of these should also be included.
#
# Expected Results:
# ----------------
# 1. A technical description of the buffer overflow protection mechanisms that have been
# implemented on the system.
# - Details of whether the buffer overflow protection mechanisms are implemented by default or if
# additional actions (e.g. scripts or commands manually executed) are required.
# - If manually executed actions are required then detailed instructions should be included in the
# technical description.
# 2. The test results should:
# - Describe test procedures used to verify the buffer overflow protection mechanisms,
# - Contain data which demonstrates/indicates that the buffer overflow protection mechanisms
# described in the technical description document have been implemented.
# - Contain details of the test set-up for the testing of the buffer overflow protection
# mechanisms. Where simulators and/or scripts are used to artificially create the conditions to
# trigger the buffer overflow protection mechanism then details of these should also be included.


def test_33117_g80_TC_PROTECTION_FROM_BUFFER_OVERFLOW():
    skip('Not implemented...')
