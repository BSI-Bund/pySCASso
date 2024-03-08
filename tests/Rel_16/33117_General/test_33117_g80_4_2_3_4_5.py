#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.5
# Title: Policy regarding consecutive failed login attempts
# Purpose:
# To ensure that the policy regarding failed login attempts is adhered to.
# **Case 1: Testing for requirement 4.2.3.4.5 a)**
#
# Execution Steps:
# ----------------
# The accredited evaluator's tes**t** lab is required to execute the following steps:
# 1. Check default values from precondition 2.
# 2. Perform consecutive failed login attempts for the user account until the default maximum
# number of precondition 2 is reached.
# 3. Attempt again one extra login, which fails again.
# 4. Attempt one extra login in more time than the default for the delay of precondition 3, using
# the correct credentials.
# 5a. If supported enable permanent locking of accounts exceeding the maximum permissible number of
# consecutive failed user account login attempts and repeat steps 1-4 for a normal user.
# 5b. If supported enable permanent locking of accounts exceeding the maximum permissible number of
# consecutive failed user account login attempts and repeat steps 1-4 for a user with
# administrative access rights.
#
# Expected Results:
# ----------------
# In execution step 5a it is verified that the user cannot login at any execution step.
# In execution step 5b it is verified that an administrator user can successfully login only at
# execution step 5b.
# Expected format of evidence: tba


def test_33117_g80_TC_FAILED_LOGIN_ATTEMPTS():
    skip('Not implemented...')
