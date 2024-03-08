#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.3.5.1
# Title: Traffic separation
# Purpose:
# To test whether O&M traffic is separated from user plane traffic, control plane traffic is
# separated from user plane traffic.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester checks whether the PGW refuses O&M traffic on all interfaces meant for
# user plane traffic.
# 2. The tester checks whether the PGW refuses user plane traffic on all O&M interfaces.
# 3. The tester checks whether the PGW refuses control plane traffic on all interfaces meant for
# user plane traffic.
# 4. The tester checks whether the PGW refuses user plane traffic on all control plane interfaces.
#
# Expected Results:
# ----------------
# The six tests should be successful, i.e. the PGW refuses traffic in all of the four steps.


def test_33250_g00_TC_TRAFFIC_SEPARATION():
    skip('Not implemented...')
