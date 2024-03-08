#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.4
# Title: No unused add-ons
# Purpose:
# To verify that the Web server has deactivated unneeded add-ons and unneeded scripting components.
#
# Execution Steps:
# ----------------
# 1. Check that the web server is only running and listening on known ports
# (e.g. tcp port 80 and/or 443). Check that CGI or other scripting components, Server Side Includes
# (SSI), and WebDAV are deactivated if they are not required. See also guidance under 4.3.4.12.
# 2. Check that nothing else has been installed than the web server.
# 3. Check that relevant system settings and configurations are correct to ensure fulfilment of the
# requirement.
#
# Expected Results:
# ----------------
# - System settings and configurations have been found adequately set, in all Web components of the
# system, to ensure that all unneeded add-ons or script components are deactivated.


def test_33117_g80_TC_NO_UNUSED_ADD_ONS():
    skip('Not implemented...')
