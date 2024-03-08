#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.4.1.2.1
# Title: Authenticated Privilege Escalation only
# Purpose:
# To ensure that privileged operating system functions shall not be used without successful
# authentication and authorization, and that violations of this requirement are documented and
# strictly limited in number and functionality.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. The tester logs into the network product and verifies that list "A" is accurate, based on his
# expert knowledge of the operating system(s) used in the network product, and operating system
# documentation.
# 2. The tester verifies that entries in the list "A" require successful authentication for all
# users without exception, on basis of the user name and at least one authentication attribute.
# 3. The tester logs into the network product and verifies that list "B" is accurate, based on his
# expert knowledge of the operating system(s) used in the network product, and operating system
# documentation. Unix® example: To list files with SUID and SGID permissions, the following
# commands can be used:
# SUID: find / -perm -4000 -type f -exec ls {} \; > suid_files.txt
# SGID: find / -perm -2000 -type f -exec ls {} \; > sgid_files.txt
# 4. The tester verifies that file entries in the list "B" do not have write permissions for anyone
# else than the owner.
# 5. The tester verifies that entries in the list "B" only allow execution of specifically limited
# tasks which are needed on this network product, based on his expert knowledge of the operating
# system(s) used in the network product, and operating system documentation.
# 6. The tester logs into the network product and tests for every entry in the list "B" that it
# does not provide a means to execute arbitrary functions with administrator/root privileges,
# e.g. via a shell escape.
#
# Expected Results:
# ----------------
# 1. The network product does not allow a user to gain administrator/root privileges from another
# user account without re-authentication.
# 2. If a network product provides functions and files which execute specifically limited tasks
# automatically with higher privileges, it ensures that these limits cannot be bypassed.
# 3. The system documentation about means for a user to gain administrator/root privileges from
# another user account accurately describes the network product.


def test_33117_g80_TC_OS_PRIVILEGE():
    skip('Not implemented...')
