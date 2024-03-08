#!/usr/bin/python3

from pytest import skip

# Function: PGW
# Source: 33250-g00.md
# Section: 4.3.5.2
# Title: User Plane Traffic Differentiation
# Purpose:
# 1. To test whether the user plane traffics is differentiated by setting the specific APNs.
# 2. To test whether the traffic is isolated based on the APNs.
#
# Execution Steps:
# ----------------
# **Execute the following steps:**
# 1. The tester intercepts the VPN packets between the P-GW and PDN, as well as the GTP-U packets
# between P-GW and S-GW/UE;
# 2. The tester checks triggers APN1's traffic with the P-GW, then the tester verifies that the
# tunnel id of the VPN packets sent by the P-GW indicates VPN1 as well as the TEID of the
# GTP-U packets sent by the P-GW indicates APN1;
# 3. The tester triggers APN2's traffic with the P-GW, then the tester verifies that the tunnel id
# of the VPN packets sent by the P-GW indicates VPN2 as well as the TEID of the GTP-U packets sent
# by the P-GW indicates APN2;;
# 4. The tester checks triggers APN1's traffic with the P-GW, then the tester verifies that the
# tunnel id of the VPN packets sent by the P-GW does not indicate VPN2 as well as the TEID of
# the GTP-U packets sent by the P-GW does not indicate APN2;
# 5. The tester triggers APN2's traffic with the P-GW, then the tester verifies that the tunnel id
# of the VPN packets sent by the P-GW does not indicate VPN1 as well as the TEID of
# the GTP-U packets sent by the P-GW does not indicate APN1.
#
# Expected Results:
# ----------------
# The four verification should be successful.


def test_33250_g00_TC_USER_PLANE_TRAFFIC_DIFFERENTIATION():
    skip('Not implemented...')
