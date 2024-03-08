#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.6.2
# Title: Log transfer to centralized storage
# Purpose:
# To ensure log shall be transferred to centralized storage.
#
# Execution Steps:
# ----------------
# 1. The tester configures the network product to forward event logs to an external system
# (according to bullet a) of requirement) and related logs are sent out.
# 2. The tester checks whether the used transport protocol is secure protocol.
# 3. The tester checks whether the central location or external system for network product log
# functions has stored the related logs.
# 4. The tester configures the network product for secure upload of event log files to an external
# system (according to bullet b) of requirement) and performs a log file upload.
# 5. The tester checks whether the used transport protocol for log file upload is a secure standard
# protocol.
# 6. The tester checks whether the central location or external system for network product log
# functions has stored the related logs.
#
# Expected Results:
# ----------------
# - The listed transport protocols are secure protocols.
# - The used transport protocol for log file upload is a secure standard protocol.
# - The tester finds that the central location or external system for network product log functions
# has stored the related logs.


def test_33117_g80_TC_LOG_TRANS_TO_CENTR_STORAGE():
    skip('Not implemented...')
