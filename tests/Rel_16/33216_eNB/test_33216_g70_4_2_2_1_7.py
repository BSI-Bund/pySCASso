#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.7
# Title: The selection of EIA0
# Purpose:
# Verify that AS NULL integrity algorithm is used correctly.
#
# Execution Steps:
# ----------------
# Positive:
# 1. The eNB receives a UE security capability only containing EIA0 from S1 context setup message.
# 2. The eNB sends AS SMC to the UE.
# Negative:
# 1. The eNB receives a UE security capability that contains EIA0 and other integrity algorithm(s).
# 2. The eNB sends AS SMC to the UE.
#
# Expected Results:
# ----------------
# EIA0 is only selected in the Positive test.


def test_33216_g70_4_2_2_1_7():
    skip('Missing test case name...')
