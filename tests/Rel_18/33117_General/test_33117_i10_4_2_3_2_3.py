#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.2.3.2.3
# Title: Protecting data and information in storage
# Purpose:
# Verify that Password storage uses a non-broken one-way cryptographic hash algorithm.
#
# Execution Steps:
# ----------------
# 1. The tester accesses the storage where the result of P1 is, and the corresponding hash value is
# recorded as A
# 2. The tester changes the password with P2, then the tester records the storage hash value of the
# new password as B
# 3. The tester repeats the step 2 to get other records with the following requirements for
# password P2:
# - at least one new password P2 differs from P1 by exactly one bit
# - at least one new password P2 shall be the same as P1
# - at least one new password P2 shall have a different length compared to P1
# 4. The tester verifies whether all the records comply with the characteristic of one-way
# cryptographic hash result.
# a. All collected records contain different hash values, even if the corresponding passwords were
# identical.
# NOTE 2: Even if P1 and P2 only differ by one bit, the resulting hash values should differ
# substantially. (Bit independence criterion)
# b. The bit length of the hash values is fixed and independent from the password length.
# c. The hash value does not contain any information that could be used for password disclosure.
# (e.g. contains part of the password in plain text or some sort of password length indicator)
# NOTE 3: Depending on the implementation the recorded hash values A and B could be stored with
# their salt combined in some way (e.g. salt is prefix or suffix of hash value). The tester needs
# to exclude the salt when comparing records
#
# Expected Results:
# ----------------
# All records comply with the characteristic of one-way cryptographic hash result.


def test_33117_i10__TC_PSW_STOR_SUPPORT():
    skip('Not implemented...')
