#!/usr/bin/python3

import re

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import DisplayFilter
from scas.packet_type.http2 import HTTP2Data, HTTP2HeaderPost, HTTP2HeaderPut

# Function: UDM
# Source: 33514-i10.md
# Section: 4.2.2.2
# Title: Storing of authentication status of UE by UDM
# Purpose:
# Verify that the UDM under test stores the authentication status of UE, which is identical to the
# UE authentication information sent to/from the AUSF and the AMF.
#
# Execution Steps:
# ----------------
# 1. The tester shall capture the entire authentication procedure and authentication confirmation
# procedure over N12 and N13 interface using any network analyser.
# 2. the tester shall filter the Nudm_UEAuthentication_Get Request message sent over the N13
# interface to retrieve serving network name.
# 3. The tester shall filter the Nudm_UEAuthentication_Get Response message sent over N13 interface
# to find the SUPI.
# 4. The tester shall filter the Nausf_UEAuthentication_Authenticate Response message sent over N12
# interface to retrieve the Authentication result (EAP success/failure for EAP-AKA' or Result for
# 5G AKA).
# 5. The tester shall filter the Nudm_UEAuthentication_ResultConfirmation Request message to
# retrieve the authentication result and time of authentication procedure sent from the AUSF to the
# UDM over N13 interface.
# 6. The tester shall compare the serving network name stored in the UDM against the serving
# network name retrieved from the Nudm_UEAuthentication_Get Request message and the serving network
# name retrieved from the Nudm_UEAuthentication_ResultConfirmation Request message.
# 7. The tester shall compare the authentication status stored in the UDM against the
# authentication result retrieved from N12 interface.
# 8. The tester shall compare the SUPI stored in the UDM against the SUPI retrieved from the
# Nudm_UEAuthentication_Get Response message and the SUPI retrieved from the
# Nudm_UEAuthentication_ResultConfirmation Request message.
# 9. The tester shall compare the timestamp stored in the UDM against the time of authentication
# procedure retrieved from the Nudm_UEAuthentication_ResultConfirmation Request message.
#
# Expected Results:
# ----------------
# The storing of authentication status (SUPI, authentication result, timestamp, and the serving
# network name) of UE at the UDM is verified.


def test_33514_g40_TC_AUTH_STATUS_STORE_UDM(provide_running_core, provide_core_config,
                                            provide_running_ran, provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran

    ue = provide_ue
    ue.setup()

    # 1. Step
    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_sbi.pcap") \
        .record_event(lambda: (ue.start()))

    # this is an intermediate step to receive the supiOrSuci
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nausf-auth/v1/ue-authentications"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )
    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "HTTP POST Request /nausf-auth/v1/ue-authentications for AUSF found")

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info("HTTP Data /nausf-auth/v1/ue-authentications for AUSF found")

    supiorsuci = post_data_data.json()['supiOrSuci']

    # 4.
    # post response data
    post_response_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", post_data_data.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )

    assert (post_response_data_data :=
            cap.get_first_packet_of_type(post_response_data))
    LOGGER.info(
        "HTTP response data /nausf-auth/v1/ue-authentications for UDM found")

    # TODO implement the case for EAP auth confirmation, not just 5g-aka!
    # there is an authtype in the post_response_data_data.json() pointing out the auth method
    auth_confirm_url = post_response_data_data.json()[
                                                    '_links']['5g-aka']['href']
    auth_confirm_url_part = re.search(
        r"(?<=.)(\/nausf-auth.*)", auth_confirm_url).groups()[0]

    put = HTTP2HeaderPut(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==", auth_confirm_url_part),
        ]
    )

    assert (real_put := cap.get_first_packet_of_type(put))
    LOGGER.info("AuthConfirmation PUT found")

    put_response_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_put.streamid()),
            DisplayFilter("frame.number", ">=", real_put.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )

    assert (put_response_data_data :=
            cap.get_first_packet_of_type(put_response_data))
    LOGGER.info("AuthConfirmation PUT resonse data received")

    Nausf_UEAuthentication_Authenticate_authResult = put_response_data_data.json()[
                                                                                 'authResult']

    # 2. Step
    # Nudm_UEAuthentication_Get Request message
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          f"/nudm-ueau/v{core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION)}"
                          f"/{supiorsuci}/security-information/generate-auth-data"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info("UEAuthentication Request for UDM found.")

    data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (request_data := cap.get_first_packet_of_type(data))
    LOGGER.info("UEAuthentication Response for AUSF found.")

    Nudm_UEAuthentication_Get_servingNetworkName = request_data.json()[
                                                                     'servingNetworkName']

    # 3. Step
    # Nudm_UEAuthentication_Get Response data
    # this is the response data to the former post request -> see ip.src instead of ip.dst!
    # AuthenticationInfoResult
    data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (response_data := cap.get_first_packet_of_type(data))
    LOGGER.info("UEAuthentication Response for AUSF found.")

    Nudm_UEAuthentication_Get_supi = response_data.json()['supi']

    # 5. Step
    auth_event_post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          f"/nudm-ueau/v{core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION)}"
                          f"/{Nudm_UEAuthentication_Get_supi}/auth-events"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (real_auth_event_post :=
            cap.get_first_packet_of_type(auth_event_post))
    LOGGER.info(
        "Nudm_UEAuthentication_ResultConfirmation Request message found")

    auth_event_post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==",
                          real_auth_event_post.streamid()),
            DisplayFilter("frame.number", ">=",
                          real_auth_event_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (real_auth_event_post_data :=
            cap.get_first_packet_of_type(auth_event_post_data))
    LOGGER.info("Nudm_UEAuthentication_ResultConfirmation Request data found")

    Nudm_UEAuthentication_ResultConfirmation_authStatus = real_auth_event_post_data.json()

    # Get the infos from the UDM
    # This fails on open5gs! (see todo below)
    authenticationStatus = core_config.read(
        ConfigKey.UDM_AUTHENTICATION_STATUS, ueId=Nudm_UEAuthentication_Get_supi)

    # TODO: currently all this does only work for free5gc, make it more generic
    # open5gs does keep the autentication state of an UE in memory - there is no good way to get
    # those values

    # 6. SNN@UDM vs Nudm_Authentication_Get Request message and
    # Nudm_UEAuthentication_ResultConfirmation Request message
    assert Nudm_UEAuthentication_Get_servingNetworkName == authenticationStatus[
        'servingNetworkName']
    assert Nudm_UEAuthentication_ResultConfirmation_authStatus[
        'servingNetworkName'] == authenticationStatus['servingNetworkName']

    # 7. auth status@UDM vs authentication result retrieved from N12 interface.
    if authenticationStatus['success']:
        assert Nausf_UEAuthentication_Authenticate_authResult == 'AUTHENTICATION_SUCCESS'
    else:
        # if this is the case, we should not reach this point anyway...
        assert Nausf_UEAuthentication_Authenticate_authResult != 'AUTHENTICATION_SUCCESS'

    # 8. SUPI@UDM vs SUPI Nudm_Authentication_Get Response message and
        # Nudm_UEAuthentication_ResultConfirmation Request message
    assert Nudm_UEAuthentication_Get_supi == authenticationStatus['ueId']
    # since we filter for a Nudm_UEAuthentication_ResultConfirmation Request message with the
    # Nudm_UEAuthentication_Get_supi, we dont need to check here

    # 9. timestamp@UDM vs time of authentication procedure from
    # Nudm_UEAuthentication_ResultConfirmation Request message
    assert Nudm_UEAuthentication_ResultConfirmation_authStatus[
        'timeStamp'] == authenticationStatus['timeStamp']
