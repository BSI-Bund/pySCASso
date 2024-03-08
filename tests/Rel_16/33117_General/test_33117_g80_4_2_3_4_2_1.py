#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.2.1
# Title: Account protection by at least one authentication attribute.
# Purpose:
# To ensure that all accounts are protected by at least one authentication attribute.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. After login via account with necessary access rights (e.g. Admin) search in the database for
# any undocumented account.
# 2. Attempt login to all predefined accounts identified (either documented or not) with and
# without using the respective authentication attribute.
# 3. Create a new account by following instructions in documentation.
# 4. Attempt login to the newly created account.
#
# Expected Results:
# ----------------
# 1. It is not possible to login to any predefined account without using at least one
# authentication attribute that satisfies the conditions in the requirement.
# 2. It is not possible to login to any newly created account without usage of at least one
# authentication attribute that satisfies the conditions in the requirement.


def test_33117_g80_TC_ACCOUNT_PROTECTION():
    skip('Not implemented...')
