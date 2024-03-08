#!/usr/bin/python3

from pytest import skip

# Function: VirtNP3GPP
# Source: 33527-i01.md
# Section: 4.3.6.2
# Title: Separation of inter-VNF and intra-VNF traffic
# Purpose:
# To test whether the traffics between inter-VNF traffic and intra-VNF traffic are separated.
# Procedure and execution steps:
#
# Execution Steps:
# ----------------
#
#
# Expected Results:
# ----------------
# In the step 1, the inter-VNF traffic and intra-VNF traffic are separated according the document
# by the vendor. In the step 2 and step 3, the VNFCI refuses traffic.


def test_33527_i01__TC_TRAFFIC_SEPARATION_INTER_VNF_INTRA_VNF():
    skip('Not implemented...')
