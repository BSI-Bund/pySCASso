#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.6.2
# Title: Role-based access control
# Purpose:
# Verify that users are granted access with role-based privileges.
#
# Execution Steps:
# ----------------
# 1. User accounts which are assigned to different access roles are created.
# 2. Operations, that are allowed by different roles (as defined in the network product
# documentation), are attempted via the different user accounts.
#
# Expected Results:
# ----------------
# 1. Users that are assigned to a role that is not allowed to execute an operation are prevented
# from executing the operation.
# 2. Users that are assigned to a role that is allowed to execute an operation can successfully
# execute the operation.


def test_33117_g80_4_2_3_4_6_2():
    skip('Missing test case name...')
