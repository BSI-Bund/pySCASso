#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.3.1.6
# Title: External file system mount restrictions
# Purpose:
# Verify that OS-level restrictions are set properly for users that are allowed to mount external
# file systems (attached locally or via the network). This is to prevent privilege escalation or
# extended access permissions due to the contents of the mounted file systems.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester shall verify that OS-level restrictions are set properly in order to prevent
# privilege escalation due to the contents of the mounted file systems (e.g. In Linux® systems,
# administrators shall set the options nodev and nosuid in the /etc/fstab for all filesystems,
# which also have the "user" option). The tester checks that OS-level parameters are configured
# correctly on the system.
# 2. The tester mounts an external filesystem prepared by the tester with files exploiting
# privilege escalation methods (e.g. with writable SUID/GUID files).
# 3. The tester tries to gain privileged access to system by using a suitable privilege escalation
# method using the contents of the mounted file system and then confirms that privilege escalation
# doesn't happen.
#
# Expected Results:
# ----------------
# The OS-level restrictions are set properly in order to prevent privilege escalation or extended
# access permissions due to the contents of the mounted file systems.
# Any privilege escalation method used by the tester should be blocked.


def test_33117_g80_TC_EXTERNAL_FILE_SYSTEM_MOUNT_RESTRICTIONS():
    skip('Not implemented...')
