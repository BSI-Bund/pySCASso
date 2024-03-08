#!/usr/bin/python3

from pytest import skip

# Function: UPF
# Source: 33513-h00.md
# Section: 4.2.2.7
# Title: IPUPS
# Purpose:
# Verify that the packets not belonging to an active PDU session is discarded.
#
# Execution Steps:
# ----------------
# 1. The V-SMF requests the UPF with IPUPS functionality under test to establish an N4 session for
# a PDU session in home-routing roaming. The UPF with IPUPS functionality under test responds to
# the SMF with the F-TEID for the N9 tunnel towards the H-UPF, and the F-TEID for the N3 tunnel
# towards the gNB.
# 2. The V-SMF requests the H-SMF to establish a PDU session providing the received F-TEID for the
# N9 tunnel.
# 3. The H-SMF requests the H-UPF to establish an N4 session providing the received F-TEID for the
# N9 tunnel. H-UPF in the response provides its F-TEID for the N9 tunnel. The H-SMF provides the
# received F-TEID from the H-UPF to the V-SMF.
# 4. The V-SMF requests the gNB to allocate resource for the PDU session providing the F-TEID for
# the N3 tunnel received at step 1. The gNB replies with its F-TEID for the N3 tunnel to the V-SMF.
# 5. The V-SMF provides the UPF with IPUPS functionality under test with the received F-TEID
# assigned by the gNB for the N3 tunnel and the received F-TEID assigned by the H-UPF for th
# N9 tunnel.
# 6. The H-UPF is triggered to send GTP-U packets using the F-TEID assigned by the V-UPF for the
# N9 tunnel.
# 7. The H-UPF is triggered to send GTP-U packets using an F-TEID different than the one assigned
# by V-UPF for N9 tunnel.
#
# Expected Results:
# ----------------
# When the H-UPF is triggered to send GTP-U packets using the F-TEID assigned by the V-UPF for the
# N9 tunnel (step 6 in the execution steps), GTP-U packets are witnessed over the N3 tunnel.
# When the H-UPF is triggered to send GTP-U packets using an F-TEID different than the one assigned
# by the V-UPF (step 7 in the execution steps), no GTP-U packets are witnessed over the N3 tunnel.


def test_33513_h00_TC_IPUPS_PACKET_HANDLING():
    skip('Not implemented...')
