#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.3.5
# Title: Network Product software package integrity
# Purpose:
# Verify that:
# 1. The Network Product validates the software package integrity during the installation/upgrade
# stage.
# 2. The software package integrity validation mechanism is performed using cryptographic
# mechanisms, e.g. digital signature using the public keys or certificates configured in the
# network product.
# 3. Software that fails an integrity check is rejected by the network product.
# 4. Only authorized users are allowed to install software.
#
# Execution Steps:
# ----------------
# The tester checks the permissions required to install software on the network product ensuring
# that a user is properly authenticated by the network product and that they have the required
# access privileges to perform the installation activity.
# The tester checks, when a software package is attempted to be installed on the network product,
# that the software package integrity check is executed (check for evidence of execution as
# described in network product documentation) and that valid software is allowed to be installed
# but invalid software is rejected.
# The tester checks the access control permissions for the software package integrity checking
# process, the list of public keys of authorised software sources, and any related credentials or
# keys for the process, to ensure that the process cannot be controlled by persons that are not
# authorized to do so.
#
# Expected Results:
# ----------------
# - Evidence that the software package integrity check has been executed for both cases of software
# installation (valid and invalid software packages).
# - Authentication and access control mechanisms are in operation for software package installation
# and around the software package integrity checking mechanism.
# - The installation/upgrade operation fails when using an invalid software package.
# - The installation/upgrade operation is successful when using a valid software package.


def test_33117_g80_TC_SW_PKG_INTEGRITY_1():
    skip('Not implemented...')
