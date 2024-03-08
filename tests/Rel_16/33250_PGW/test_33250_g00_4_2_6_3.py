#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.2.6.3
# Title: IP Address reallocation interval
# Purpose:
# Verify that the PGW supports an IP address reallocation interval technique.
#
# Execution Steps:
# ----------------
# 1.  Configure the IP address reallocation interval to T according to the product documentation.
# 2.  Allocate an IP address IP1 to UE1.
# 3.  Make UE1 release the IP address IP1.
# 4.  Within an interval of T after the release of IP1, make the PGW allocate the IP address IP1 to
# UE2.
# 5.  Attempt the step 4 in more time than T after the release of IP1.
#
# Expected Results:
# ----------------
# 1. In execution step 4, the reallocation attempt is rejected.
# 2. In execution step 5, the reallocation attempt is accepted.


def test_33250_g00_TC_IP_ADDRESS_REALLOCATION_INTERVAL():
    skip('Not implemented...')
