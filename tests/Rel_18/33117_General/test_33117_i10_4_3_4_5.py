#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.4.5
# Title: No compiler
# Purpose:
# To verify that there are no compilers, interpreters or shell accessible via CGI or other
# scripting components.
#
# Execution Steps:
# ----------------
# 1. Consult the web server configuration to identify all directories used for CGI or other
# scripting components.
# 2. Check that there are no compilers or interpreters (e.g., PERL® interpreter,
# PHP interpreter/compiler, Tcl interpreter/compiler or operating system shells) in the
# directory/directories used for CGI or for other scripting tools (including PERL®, PHP,
# and others).
#
# Expected Results:
# ----------------
# There are no compilers, interpreters or shells in directories accessible via CGI or other
# scripting components.


def test_33117_i10__TC_NO_COMPILER_FOR_CGI():
    skip('Not implemented...')
