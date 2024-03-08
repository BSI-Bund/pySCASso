#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.3.3.1.3
# Title: No automatic launch of removable media
# Purpose:
# To verify that the network product does not launch any applications automatically when a
# removable media device is connected. Any such feature should be deactivated.
#
# Execution Steps:
# ----------------
# 1. The tester log in the network product.
# 2. For all available physical ports which are externally accessible:
# a. The tester prepares a removable media device
# (e.g. CD, DVD, USB-Sticks and/or USB-Storage drives) that contain any kind of autostart file
# suitable for this port type.
# b. The tester inserts the prepared media device into the network product under test.
# 3. The tester verifies that the media device is not automatically mounted and there is no
# automatic application launch triggered by its insertion.
#
# Expected Results:
# ----------------
# The network product does not launch any applications to open the contents in the removable media
# device.
# In Linux® machines, the removable media device is not automatically mounted in the filesystem.


def test_33117_i10__TC_NO_AUTO_LAUNCH_OF_REMOVABLE_MEDIA():
    skip('Not implemented...')
