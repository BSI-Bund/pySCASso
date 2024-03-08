#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.3
# Title: No automatic launch of removable media
# Purpose:
# To verify that the network product does not launch any applications automatically when a
# removable media device is connected. Any such feature should be deactivated.
#
# Execution Steps:
# ----------------
# 1. The tester log in the network product.
# 2. The tester inserts a removable media device (CD-, DVD-, USB-Sticks and/or USB-Storage drives)
# in the network product.
#
# Expected Results:
# ----------------
# The network product does not launch any applications to open the contents in the removable
# media device.
# In Linux® machines, the removable media device is not automatically mounted in the filesystem.


def test_33117_g80_TC_NO_AUTO_LAUNCH_OF_REMOVABLE_MEDIA():
    skip('Not implemented...')
