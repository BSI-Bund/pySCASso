#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.6.1
# Title: Authorization policy
# Purpose:
#
#
# Execution Steps:
# ----------------
# 1. Assign access rights (e.g. read only) to user accounts, data files, and applications.
# 2. Operations, that are allowed as per authorization policy (as defined in the network product
# documentation), are attempted via the different user accounts, data files, and applications.
#
# Expected Results:
# ----------------
# 1. User accounts, data files, and applications are allowed to be accessed (e.g. able to read but
# not write to a file, able to execute an application as a user account without administrator
# rights, etc.) according to the access rights assigned.
# 2. User accounts, data files, and applications are not allowed to be accessed above the access
# rights assigned (e.g. able to write to a read only file, able to execute an application as an
# administrator, etc.).


def test_33117_g80_4_2_3_4_6_1():
    skip('Missing test case name...')
