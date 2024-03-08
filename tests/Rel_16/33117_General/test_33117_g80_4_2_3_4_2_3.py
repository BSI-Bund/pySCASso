#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.2.3
# Title: Predefined or default authentication attributes shall be deleted or disabled.
# Purpose:
# To ensure that predefined or default authentication attributes are deleted or disabled as defined
# in the requirement 4.2.3.4.2.3.
#
# Execution Steps:
# ----------------
# 1. Check in documentation of the existence of any documented predefined account and what is the
# login password or if any cryptographic key for such accounts is preinstalled.
# 2. After login via account with necessary access rights (e.g. Admin) search in the database for
# any undocumented account.
# 3. Attempt login to such predefined accounts if existing.
#
# Expected Results:
# ----------------
# 1. When login is attempted to any predefined account the user is automatically forced to change
# login password at first time login to the system.
# 2. If there is no automatic password change enforced then recommendation and clear instructions
# of how to manually change the password or how to create and reinstall a new cryptographic key
# exist in the documentation.


def test_33117_g80_TC_PREDEFINED_AUTHENTICATION_ATTRIBUTES_DELETION():
    skip('Not implemented...')
