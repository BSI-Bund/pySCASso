#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.6.2
# Title: No code execution or inclusion of external resources by JSON parsers
# Purpose:
# NFs implementing SBI transfer application data serialized as JSON objects. When receiving such
# data, an NF parses this JSON representation and creates equivalent internal data structures.
# Since the contents of the JSON objects must be considered untrusted, blindly executing code
# fragments or loading resources from a local path or Uniform Resource Identifier (URI) must not be
# possible.
#
# Execution Steps:
# ----------------
# 1. Execution of available WAS test tools against the network product's API endpoints via its
# Service Based Interfaces.
# 2. Using a network traffic analyser on the network product, e.g. TCPDUMP or an external traffic
# analyser directly connected to the network product, the tester verifies that no external
# resources get loaded during JSON parsing.
# 3. Depending on the actual JavaScript code in the HTTP message, the tester verifies that the
# network product does not execute any of the contained actions.
#
# Expected Results:
# ----------------
# - The NF does not load any resources external to the JSON object itself.
# - The NF does not execute any JavaScript code contained in JSON objects.


def test_33117_g80_TC_JSON_PARSER_CODE_EXEC_INCL():
    skip('Not implemented...')
