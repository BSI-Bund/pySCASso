#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.4.1.1.1
# Title: Handling of growing content
# Purpose:
# To verify that the growing or dynamic content does not influence system functions.
#
# Execution Steps:
# ----------------
# 1. Tester checks that the sources that are susceptible to being exhausted have been documented
# and measures aimed to counteract this are described.
# 2. Tester enables monitoring of the system operation.
# 3. Tester initiates traffic that causes increase of log files and monitors the system behaviour
# until the log file either reaches its quota or until file system is exhausted.
# 4. In case file uploading is allowed (e.g. via SFTP) the tester initiates file uploading and
# tries to exhaust the file system.
#
# Expected Results:
# ----------------
# 1. It is verified that the taken measures are sufficient so that system operation is not
# influenced by growing or dynamic content at any case.


def test_33117_g80_TC_HANDLING_OF_GROWING_CONTENT():
    skip('Not implemented...')
