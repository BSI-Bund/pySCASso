#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.9
# Title: No default content
# Purpose:
# To verify that there is no default content on the web server, that is not needed for web server
# operation, since such default content can be useful for an attacker.
#
# Execution Steps:
# ----------------
# 1. Check that all default content (examples, help files, documentation, aliases) that is provided
# with the standard installation of the web server has been removed.
#
# Expected Results:
# ----------------
# - No default content (examples, help files, documentation, aliases, un-needed directories or
# manuals) has been found to remain on any Web server component.


def test_33117_g80_TC_NO_DEFAULT_CONTENT():
    skip('Not implemented...')
