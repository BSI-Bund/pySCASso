#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.2.5
# Title: Logging access to personal data
# Purpose:
# Verify that in cases where a network product presents personal data in clear text, access
# attempts to such data are logged and the log information includes the user identity that has
# accessed the data. The test case also verifies that the personal data itself is not included in
# clear text in the log.
#
# Execution Steps:
# ----------------
# - The tester verifies, for cases where personal data is accessible in clear text, that attempts
# to access it are recorded in a log, that the log includes the identity of the user that has
# attempted to access the data, and that the log does not include the actual personal data in
# clear-text.
# - The tester repeats the check for each case where personal data is accessible.
#
# Expected Results:
# ----------------
# All access attempts to personal data (in clear text) are recorded in the described logs, with the
# user identity included and no personal data visible in the log.


def test_33117_g80_TC_LOGGING_ACCESS_TO_PERSONAL_DATA():
    skip('Not implemented...')
