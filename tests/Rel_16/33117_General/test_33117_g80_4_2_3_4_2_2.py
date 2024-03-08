#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.2.2
# Title: Predefined accounts shall be deleted or disabled.
# Purpose:
# To ensure that predefined accounts are deleted or disabled unless there is specific exception as
# defined in the requirement 4.2.3.4.2.2.
#
# Execution Steps:
# ----------------
# 1. Check in documentation of the existence of any documented predefined account and what is the
# reason for existence.
# 2. After login via account with necessary access rights (e.g. Admin) search in the database for
# any undocumented account.
# 3. Check the password complexity of such existing predefined accounts according to the test
# provided in clause 4.2.3.4.3.1.
# 4. Attempt remote login to such predefined accounts.
#
# Expected Results:
# ----------------
# 1. Predefined accounts are either deleted/ disabled or, if existing, the reason is in accordance
# with the requirement exception.
# 2. If there are active predefined accounts in accordance with the requirement exception then
# there is no remote login possibility.
# 3. If predefined account is either disabled or locked then it shall anyway fulfil the complex
# password requirements as specified in clause 4.2.3.4.3.1 after enabling or unlocking it.


def test_33117_g80_TC_PREDEFINED_ACCOUNT_DELETION():
    skip('Not implemented...')
