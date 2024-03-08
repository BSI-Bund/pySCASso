#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.1.1
# Title: System functions shall not be used without successful authentication and authorization.
# Purpose:
# To ensure that system functions shall not be used without successful authentication and
# authorization.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. The tester verifies, based on his/her own experience, that the list is adequate.
# 2. The tester verifies that the access entries to use system functions, which are listed by the
# manufacturer, require successful authentication on basis of the user name and at least one
# authentication attribute. This applies to both system functions that are locally accessible and
# those that are remotely accessible via a network interface.
#
# Expected Results:
# ----------------
# 1. The network product does not allow access to any system function provided by the manufacturer
# without a successful user authentication.


def test_33117_g80_TC_SYS_FUN_USAGE():
    skip('Not implemented...')
