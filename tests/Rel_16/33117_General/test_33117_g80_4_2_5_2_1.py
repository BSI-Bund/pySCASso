#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.5.2.1
# Title: Webserver logging
# Purpose:
# Verify that all accesses to the webserver are logged with the required information.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester tries to login to the webserver using the correct and incorrect login credentials.
# 2. The tester verifies whether the login attempts were logged correctly with all of the required
# information.
#
# Expected Results:
# ----------------
# All webserver events are logged with all of the required information.


def test_33117_g80_TC_WEBSERVER_LOGGING():
    skip('Not implemented...')
