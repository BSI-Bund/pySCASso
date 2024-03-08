#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.4.2.2
# Title: System account identification
# Purpose:
#  To verify that UNIX® account UIDs are assigned uniquely.
#
# Execution Steps:
# ----------------
# 1. Create several UNIX® accounts.
# 2. Check UIDs of created accounts and of existing system accounts and, in particular, the root
# account.
#
# Expected Results:
# ----------------
# only the root account has UID = 0.


def test_33117_g80_TC_UNIQUE_SYSTEM_ACCOUNT_IDENTIFICATION():
    skip('Not implemented...')
