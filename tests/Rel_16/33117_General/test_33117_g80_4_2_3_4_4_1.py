#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.4.1
# Title: Network Product Management and Maintenance interfaces
# Purpose:
#
#
# Execution Steps:
# ----------------
# 1. The tester checks that the authentication mechanisms have been configured on the network
# product.
# 2. The tester triggers communication between network product and a test entity that has a
# legitimate authentication credential.
# 3. Then, the tester triggers communication between network product and a test entity that
# doesn't have a legitimate authentication credential.
#
# Expected Results:
# ----------------
# - Mutual authentication is successful and communication between network product and the entity
# with correct credentials can be established.
# - Mutual authentication fails and communication between the network product and the entity with
# incorrect credentials cannot be established.


def test_33117_g80_4_2_3_4_4_1():
    skip('Missing test case name...')
