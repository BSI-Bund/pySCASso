#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.5.3
# Title: HTTP User sessions
# Purpose:
# Verify that the above 12 session ID and session cookie requirements have been met.
#
# Execution Steps:
# ----------------
# 1. The tester logs in repeatedly with different user IDs and a number of times with the same user
# ID in a row and collects the session IDs according to the documentation and the user IDs
# associated with them. The tester verifies that:
# a. The session IDs are different between sessions of the same and different users;
# b. The session IDs seems random based on his/her own experience. The tester may use tests like
# the bitstream test or the count-the-1s-tests from the diehard test suite. The tester documents
# how randomness was verified;
# c. The session IDs are always different between sessions, also when the user ID is the same.
# 2. The tester verifies that when session cookies are used
# a. neither the "expire" or the "max-age" is set;
# b. the 'HttpOnly' is set to true;
# c. the 'domain' attribute is set to the correct domain;
# d. the 'path' attribute is set to the correct directory or sub-directory.
# 3. The tester verifies that it is impossible to:
# a. access a session by retrieving the session ID and communicating the session ID through a POST
# or GET variable.
# b. generate a session ID on the client by attempting to login with a custom generated session ID.
# c. keep a session alive for longer than the configured maximum lifetime (by default 8 hours).
#
# Expected Results:
# ----------------
# 1. A list of session IDs and user IDs that are different between sessions even when the tester
# has logged in with the same user and that are unpredictable as is confirmed by the entropy
# calculation.
# 2. A confirmation from the tester that the correct variables are indeed set.
# 3. A denied access to the tester when attempting the two login steps of step 3 and an expired
# session in step 3c.


def test_33117_g80_4_2_5_3():
    skip('Missing test case name...')
