#!/usr/bin/python3

from pytest import skip

# Function: NWDAF
# Source: 33521-h20.md
# Section: 4.2.1.2.6
# Title: Protecting data and information -- Data masking on integration analysis
# Purpose:
# Verify that no privacy information of operators' users is revealed to the party who is not
# allowed to have.
#
# Execution Steps:
# ----------------
# 1. Review the documentation provided by the vendor describing how to create the account for
# accessing the analytics results provided by the NWDAF.
# 2. The tester creates the account, and retrieves the analytics results from the NWDAF using the
# account.
#
# Expected Results:
# ----------------
# The tester can create the account, and the account does not reveal subscriber permanent
# identifier.


def test_33521_h20_TC_DATA_MASKING():
    skip('Not implemented...')
