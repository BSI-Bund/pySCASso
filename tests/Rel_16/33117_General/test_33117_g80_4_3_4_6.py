#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.6
# Title: No CGI or other scripting for uploads
# Purpose:
# To test whether the upload directory is equal to the CGI/Scripting directory.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# The tester checks whether the upload directory is configured to be different from the
# CGI/Scripting directory.
#
# Expected Results:
# ----------------
# The configured upload directory is different from the CGI/Scripting directory.
# Additional evidence might be provided that shows that the web server has no write rights for the
# CGI/Scripting directory.


def test_33117_g80_TC_NO_CGI_OR_SCRIPTING_FOR_UPLOADS():
    skip('Not implemented...')
