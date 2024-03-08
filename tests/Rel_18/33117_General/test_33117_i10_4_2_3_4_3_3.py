#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-i10.md
# Section: 4.2.3.4.3.3
# Title: Protection against brute force and dictionary attacks
# Purpose:
# To ensure that the system uses a mechanism with adequate protection against brute force and
# dictionary attacks
# To check whether system follows commonly used preventive measures which are mentioned below.
# 1. Using the timer delay (e.g. doubling wait times after every incorrect attempt, or 5 minutes
# delay, or 10 minutes delay) after each incorrect password input ("tar pit").
# 2. Blocking an account following a specified number of incorrect attempts (typically 5). However
# administrator has to keep in account that this solution needs a process for unlocking and an
# attacker can utilize this process to deactivate the accounts and make them unusable.
# 3. Using CAPTCHA to prevent automated attempts (often used for Web interface).
# 4. Using a password blacklist to prevent vulnerable passwords.
#
# Execution Steps:
# ----------------
# Execute the following steps:
# A. Positive Test
# Case 1:
# Test case to use the timer delay after each incorrect password input is covered in
# clause 4.2.3.4.5.
# Case 2:
# Test case to block an account following a specified number of incorrect attempts is covered in
# clause 4.2.3.4.5.
# Case 3:
# If the network product's login web interface is configured with a CAPTCHA feature, the tester
# enters the valid password and correct CAPTCHA.
# Case 4:
# If the recommended protection measures mentioned in the Requirement Description are not
# implemented in the Network Product, the tester checks if the alternative measures described in
# the vendor provided documentation are meaningful and develops suitable test cases to verify their
# correct implementation.
# In some cases the network product class can have two or more of the attack prevention methods
# available, which are a combination of Cases 1-3. In such cases the tester will need to run a
# combination of these test cases.
# B. Negative Test
# Case 1:
# Test case to use the timer delay after each incorrect password input is covered in
# clause 4.2.3.4.5.
# Case 2:
# Test case to block an account following a specified number of incorrect attempts is covered in
# clause 4.2.3.4.5.
# Case 3:
# If the network product's login web interface is configured with a CAPTCHA feature, the tester
# enters the valid password without and with incorrect CAPTCHA.
# Case 4:
# 1. The tester tries to change the password to the blacklisted password.
#
# Expected Results:
# ----------------
# A. Positive Test
# Case 1:
# Expected result for the test case to use the timer delay after each incorrect password input is
# covered in clause 4.2.3.4.5.
# Case 2:
# Expected result for the test case to block an account following a specified number of incorrect
# attempts is covered in clause 4.2.3.4.5.
# Case 3:
# Tester can login only after entering the correct password and CAPTCHA.
# Case 4:
# The tester assesses the alternative measures for brute force and dictionary attack mitigation as
# meaningful and all developed test cases can be completed successfully.
# B. Negative Test
# Case 1:
# Expected result for the use the timer delay after each incorrect password input is covered in
# clause 4.2.3.4.5.
# Case 2:
# Expected result for the test case to block an account following a specified number of incorrect
# attempts is covered in clause 4.2.3.4.5.
# Case 3:
# Tester cannot successfully log in to the network product.
# Case 4:
# Tester cannot successfully change the password to the blacklisted password.


def test_33117_i10__TC_PROTECT_AGAINST_BRUTE_FORCE_AND_DICTIONARY_ATTACKS():
    skip('Not implemented...')
