#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
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
# 1. The network product's login web interface is configured with CAPTCHA feature.
# 2. Tester enters the valid password and correct CAPTCHA
# 3. Tester can successfully log into the network product.
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
# 1. The network product's login web interface is configured with CAPTCHA feature.
# 2. Tester enters the valid password without CAPTCHA.
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


def test_33117_g80_TC_PROTECT_AGAINST_BRUTE_FORCE_AND_DICTIONARY_ATTACKS():
    skip('Not implemented...')
