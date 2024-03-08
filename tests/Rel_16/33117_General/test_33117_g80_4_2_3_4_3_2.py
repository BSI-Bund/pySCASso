#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.4.3.2
# Title: Password changes
# Purpose:
# - To check whether the network product is provisioned with the functionality that enables its
# user to change the password at any time.
# - The network product enforces password change after initial login.
# - To verify the new password adheres to the password management policy and also to verify whether
# it has password expiry rule.
# - The network product is configured to disallow specified number of previously used passwords
# (Password History).
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# A. Positive Test
# Case 1:
# Test case to enforce password change after initial login is covered in clause 4.2.3.4.2.3.
# Case 2:
# 1 The tester logs into network product application using a privileged account .
# 2 The network product application generates password expiry notification for user Y to force user
# Y to change the password.
# 3 The tester logs out as a privileged user and logs on as user Y.
# 4. The tester is prompted to change his password and creates a new password by following the
# password policy management.
# 5 The network product application confirms change in password by, for example, displaying
# "Password Changed Successfully".
# 6 The tester successfully logs-in the network product application as user Y using the new
# password.
# Case 3:
# 1. The tester logs into network product application using a privileged account.
# 2. Tester configures the network product application for number of disallowed previously used
# passwords to x
# 3. The tester requests for a password change for user Y.
# 4. The tester logs out of the privileged account and logs on as user Y
# 5. The tester creates a new password by following the password policy management.
# 6. If the password is not equal to any of the x previously used passwords, the network product
# application still accepts the new password and displays "Password Changed Successfully".
# B. Negative Test
# Case 1:
# Test case to enforce password change after initial login is covered in clause 4.2.3.4.2.3.
# Case 2:
# No negative test case for this scenario.
# Case 3:
# 1. The tester logs into network product application using privileged account.
# 2. Tester configures the network product application for number of disallowed previously used
# passwords to x for user Y.
# 3. The tester logs out of the privileged account and logs in as user Y
# 4. The tester requests for a password change.
# 5. The tester sets the new password to a value that is among the last x passwords used previously
# x times.
#
# Expected Results:
# ----------------
# A. Positive Test
# Case 1:
# Expected result for enforcing password change after initial login is covered in
# clause 4.2.3.4.2.3.
# Case 2:
# Tester can successfully change the password.
# Case 3:
# Tester can successfully change the password.
# B. Negative Test
# If the negative test case passes, this shows that network product application does not work
# properly and it violates the requirement.
# Case 1:
# Expected result for enforcing password change after initial login is covered in
# clause 4.2.3.4.2.3.
# Case 2:
# No negative test case for this scenario.
# Case 3:
# The tester cannot successfully change the password.


def test_33117_g80_TC_PASSWORD_CHANGES():
    skip('Not implemented...')
