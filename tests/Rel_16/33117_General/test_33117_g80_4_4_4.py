#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.4.4
# Title: Robustness and fuzz testing
# Purpose:
# To verify that the network product provides externally reachable services which are robust
# against unexpected input. The target of this test are the protocol stacks (e.g. diameter stack)
# rather than the applications (e.g. web app).
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. Execution of available effective fuzzing tools against the protocols available via interfaces
# providing IP-based protocols of the Network Product for an amount of time sufficient to be
# effective.
# 2. Execution of available effective robustness test tools against the protocols available via
# interfaces providing IP-based protocols of the Network Product for an amount of time sufficient
# to be effective.
# 3. For both step 1 and 2:
# a. Using a network traffic analyser on the network product (e.g. TCPDUMP) or an external traffic
# analyser directly connected to the network product, the tester verifies that the packets are
# correctly processed by the network product.
# b. The testers verifies that the network product and any running network service does not crash.
# c. The execution of tests shall run sufficient times.
#
# Expected Results:
# ----------------
# A list of all of the protocols of the network product reachable externally on an IP-based
# interface, together with an indication whether effective available robustness and fuzz testing
# tools have been used against them, shall be part of the testing documentation. If no tool can be
# acquired for a protocol, a free form statement should explain why not.
# The used tool(s) name, their unambiguous version (also for plug-ins if applicable), used
# settings, and the relevant output is evidence and shall be part of the testing documentation.
# Any input causing unspecified, undocumented, or unexpected behaviour, and a description of this
# behaviour shall be highlighted in the testing documentation.
# COTS fuzzing tools, by their nature, may have an acceptable failure rate (e.g. 0.1%) due to
# different non-deterministic variables in their implementation. At some point the tool's
# documentation may even mention that the failing test shall be repeated to check whether it is
# really a recurring problem or not. The tester shall make best effort to determine if there is an
# issue with NE or the test tool and if necessary, work with the vendor of the network product to
# come to a consensus on the test result outcome.


def test_33117_g80_TC_BVT_ROBUSTNESS_AND_FUZZ_TESTING():
    skip('Not implemented...')
