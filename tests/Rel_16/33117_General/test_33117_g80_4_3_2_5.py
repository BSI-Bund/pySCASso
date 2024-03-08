#!/usr/bin/python3

from pytest import skip

# Function: General
# Source: 33117-g80.md
# Section: 4.3.2.5
# Title: No unsupported components
# Purpose:
# To ensure that there is no unsupported software that is running in the network product which is
# not supported anymore and has reached its end-of-life or end-of-support.
#
# Execution Steps:
# ----------------
# The accredited evaluator's test lab is required to execute the following steps:
# 1. Identification of the hardware and software components, version information and the kind of
# support available for the software provided by the vendor, the producer, the developer or other
# contractual partner of the operator using any tool or any other suitable means of determination.
# 2. Validate that there are no entries in the list of hardware and software installed in the
# system which are not supported as given by the vendor of network product in the attached
# documentation.
#
# Expected Results:
# ----------------
# The report will contain the names and versions of the tool(s) used for finding out what software
# and hardware components are installed in the system. The detailed report will contain the name
# and version of the software and hardware used in the system, and the period of support for each
# of these components.
# The list of all available software and hardware components and their associated support
# information which has been deemed necessary for the operation of the network product by the
# vendor shall also be included as the test result. Any software or component which is not
# supported any longer by the vendor will be highlighted and brought out as a part of the report.
# There should be no software installed in the network product which is unsupported as of the day
# of testing.


def test_33117_g80_TC_NO_UNSUPPORTED_COMPONENTS():
    skip('Not implemented...')
