#!/usr/bin/python3

from pytest import skip

# Function: UPF
# Source: 33513-h00.md
# Section: 4.2.2.8
# Title: Protection against malformed GTP-U messages
# Purpose:
# Verify that malformed messages are discarded by UPF.
#
# Execution Steps:
# ----------------
# The execution steps follow those in clause 4.4.4 of TS 33.117 [3], except that the protocol the
# fuzzing tool is executed against is GTP-U and the interface is N9.
#
# Expected Results:
# ----------------
# The expected results in clause 4.4.4 of TS 33.117 [3] apply except that the protocol and the
# interface contained in the testing documentation are GTP-U and N9 respectively.


def test_33513_h00_TC_IPUPS_MALFORED_MESSAGES():
    skip('Not implemented...')
