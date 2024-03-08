#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.2.3.3.3
# Title: System handling during excessive overload situations
# Purpose:
# Verify that the network product:
# - has a detailed technical description of the overload control mechanisms used to deal with
# overload scenarios;
# - has test results verifying the operation of the overload control mechanisms.
#
# Execution Steps:
# ----------------
# - The tester verifies that there is:
# - A technical description providing a high-level overview of the overload control design:
# - An overview of the types of overload scenarios that the network product overload control
# mechanisms are expected to handle.
# - An overview of the overload control thresholds that the network product uses to trigger
# overload control mechanisms.
# - Description of the types of attacks that may cause an overload to the network product and how
# these are handled.
# - A description of how the network product discards or handles input during various overload
# situations including excessive overloads. i.e. where the overload is significantly greater than
# the thresholds where overload detection is triggered.
# - A description of how the network product security functions operate and perform during
# overload.
# - A description of how the network product shuts down or performs or takes other abatement or
# corrective actions during excessive overload conditions.
# - The tester verifies that the test results:
# - Contain details of the overload conditions used in the test execution that are consistent with
# the technical description document.
# - Describe test procedures used to verify the overload control mechanisms.
# - Contain data which demonstrates/indicates that the overload control mechanisms described in the
# technical description document have been implemented.
# - Contain details of the test set-up including the mechanisms for creating the overload. Where
# simulators and/or scripts are used to artificially create a load then details of these should
# also be included.
#
# Expected Results:
# ----------------
# - A technical description provides a high-level overview of the overload control design.
# - A overview of the types of overload scenarios and overload control thresholds that are
# considered.
# - Description on the types of attacks that may cause an overload to the system and how these are
# handled.
# - A description of how the network product discards or handles input during various overload
# situations.
# - Describes if or how the network product security functions operate and perform during overload.
# - If parts of the system shutdown or take other abatement or corrective actions these should be
# described.
# Note: If some of the items listed above are not applicable to a network product then, in those
# cases, it should be clarified by the vendor why these items are not applicable.
# The test results should:
# - Contain details of the overload conditions used in the test execution that are consistent with
# the technical description document.
# - Describe the test procedures used to verify the overload control mechanisms.
# - Contain data which demonstrates/indicates that the overload control mechanisms described in the
# technical description document have been implemented.
# - Contain details of the test set-up including the mechanisms for creating the overload.


def test_33117_g80_TC_SYSTEM_HANDLING_OF_OVERLOAD_SITUATIONS():
    skip('Not implemented...')
