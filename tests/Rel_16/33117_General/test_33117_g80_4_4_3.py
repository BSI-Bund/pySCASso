#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.4.3
# Title: Vulnerability scanning
# Purpose:
# The purpose of vulnerability scanning is to ensure that there are no known vulnerabilities
# (or that relevant vulnerabilities are identified and remediation plans in place to mitigate them)
# on the Network Product that can be detected by means of automatic testing tools via the
# Internet Protocol enabled network interfaces.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. Execution of the suitable vulnerability scanning tool against all interfaces providing
# IP-based protocols of the Network Product.
# 2. Evaluation of the results based on their severity.
#
# Expected Results:
# ----------------
# The used tool(s) name, their unambiguous version (also for plug-ins if applicable),
# used settings, and the relevant output is evidence and shall be part of the testing
# documentation.
# The discovered vulnerabilities (including source, example CVE ID), together with a rating of
# their severity, shall be highlighted in the testing documentation.
# COTS Vulnerability scanners, by their nature, (e.g. depending on how they are configured) may
# result in false findings/positives. The tool's documentation may even mention that the failing
# test shall be repeated to check whether it is really a recurring problem or not. The tester shall
# make best effort to determine if there is an issue with NE or the test tool and if necessary,
# work with the vendor of the network product to come to a consensus on the test result outcome.
# NOTE 2: This testing documentation is input to the vulnerability mitigation process (that may
# include patching). This is part of the product lifecycle management process developed by
# GSMA SECAG.


def test_33117_g80_TC_BVT_VULNERABILITY_SCANNING():
    skip('Not implemented...')
