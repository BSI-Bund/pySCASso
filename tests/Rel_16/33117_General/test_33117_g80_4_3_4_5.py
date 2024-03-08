#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.4.5
# Title: No compiler
# Purpose:
# To verify that the Web server has deactivated unneeded add-ons and unneeded scripting components.
#
# Execution Steps:
# ----------------
# 1. Check that there are no compilers or interpreters (e.g., PERL interpreter,
# PHP interpreter/compiler, Tcl interpreter/compiler or operating system shells) in the
# directory/directories used for CGI or for other scripting tools
# (including PERL, PHP, and others).
# 2. Check that relevant system settings and configurations are correct to ensure fulfilment of the
# requirement.
#
# Expected Results:
# ----------------
# - System settings and configurations have been found adequately set, in all Web components of the
# system, to ensure that all unneeded add-ons or script components are deactivated.


def test_33117_g80_TC_NO_COMPILER_FOR_CGI():
    skip('Not implemented...')
