#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.11
# Title: Web server information in HTTP headers
# Purpose:
# To verify that HTTP headers do not include information on the version of the web server and the
# modules/add-ons used.
#
# Execution Steps:
# ----------------
# 1. Check that HTTP headers do not include information on the version of the web server and the
# modules/add-ons used.
#
# Expected Results:
# ----------------
# - Evidence that HTTP headers do not include information on the version of the web server and the
# modules/add-ons used.


def test_33117_g80_TC_NO_WEB_SERVER_HEADER_INFORMATION():
    skip('Not implemented...')
