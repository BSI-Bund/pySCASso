#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.2.2
# Title: Protecting data and information -- Confidential System Internal Data
# Purpose:
# Verify that no system function reveals sensitive data in the clear
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. Review the documentation provided by the vendor describing how confidential system internal
# information is handled by system functions.
# 2. The tester checks whether any system functions as described in the product documentation
# (e.g. local or remote OAM CLI or GUI, logging messages, alarms, error messages,
# configuration file exports, stack traces) reveal any confidential system internal data in the
# clear (for example, passphrases).
#
# Expected Results:
# ----------------
# There should be no confidential system internal data revealed in the clear by any system function.


def test_33117_g80_TC_CONFIDENTIAL_SYSTEM_INTERNAL_DATA():
    skip('Not implemented...')
