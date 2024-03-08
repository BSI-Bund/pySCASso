"""Module with open5gs implementation"""
import json
import shutil
from io import BytesIO

import pycurl
import pytest
# the open5gs yaml uses yaml 1.1 format
# in newer formats yes|no get converted to true|false which will trigger open5gs to use TLS
# The RoundtripLoader/Dumper does not convert
import ruamel.yaml
from yaml import YAMLError

from scas.device_interfaces.device import ActionKey, Device
from scas.device_interfaces.device_config import ConfigKey, DeviceConfig
from scas.capture.capture import Capture, CaptureTarget
from scas.capture.local_live_capture import LocalLiveCapture
from scas.helper import run_local
from scas.logger import LOGGER

yaml = ruamel.yaml.YAML()  # defaults to RoundtripLoader/Dumper
######


class Open5GSBase(Device):
    """Base class of the open5gs device"""
    def is_available(self) -> bool:
        self.paths["base"] = pytest.test_config["env"]["OPEN5GS_PATH"]
        self.paths["bin"] = f"{self.paths['base']}/install/bin"
        self.paths["config"] = f"{self.paths['base']}/install/etc/open5gs"
        self.paths["log"] = f"{self.paths['base']}/install/var/log/open5gs"

        return self.paths_exist()

    def setup(self):
        run_local(self.name(), "pkill -f open5gs-", action="Setup")
        run_local(
            self.name(), f"sudo {self.paths['base']}/misc/netconf.sh", action="Setup")

    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        return LocalLiveCapture()

    def teardown(self):
        pass


class Open5gsCoreConfig(DeviceConfig):
    """Interface to the open5gs config"""
    core_config = None
    core_config_path = ""

    def __init__(self, paths):
        super().__init__()
        self.paths = paths
        self.core_config_path = f"{self.paths['base']}/build/configs/sample.yaml"

        shutil.copy2(self.core_config_path, f"{self.core_config_path}_backup")

        if self.core_config is None:
            with open(self.core_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.core_config = yaml.load(stream)
                except YAMLError:
                    LOGGER.warning("Could not parse %s.", self.core_config_path)

    def read(self, key: ConfigKey, **kwargs):
        # pylint complains about too many return statements, so we introduce a local var to capture
        # the return value
        return_value = None
        match key:
            case ConfigKey.AMF_INTEGRITY_PROT_ALG_ORDERED_LIST:
                # This is translated to the wireshark representation
                return_value = [self.config_algorithm_by_name(alg) for alg in
                                self.core_config['amf']['security']['integrity_order']]
            case ConfigKey.AMF_IP:
                return_value = self.core_config['amf']['sbi']['server'][0]['address']
            case ConfigKey.AMF_PORT:
                return_value = self.core_config['amf']['sbi']['server'][0]['port']
            case ConfigKey.SMF_IP:
                return_value = self.core_config['smf']['sbi']['server'][0]['address']
            case ConfigKey.SMF_PORT:
                return_value = self.core_config['smf']['sbi']['server'][0]['port']
            case ConfigKey.UDM_IP:
                return_value = self.core_config['udm']['sbi']['server'][0]['address']
            case ConfigKey.UDM_PORT:
                return_value = self.core_config['udm']['sbi']['server'][0]['port']
            case ConfigKey.AUSF_IP:
                return_value = self.core_config['ausf']['sbi']['server'][0]['address']
            case ConfigKey.AUSF_PORT:
                return_value = self.core_config['ausf']['sbi']['server'][0]['port']
            case ConfigKey.UDM_SDM_OPENAPI_VERSION:
                return_value = "2"
            case ConfigKey.UDM_UEAU_OPENAPI_VERSION:
                return_value = "1"
            case ConfigKey.UDM_AUTHENTICATION_STATUS:
                raise RuntimeError(
                    "Open5GS v26 keeps the UEs auth status in memory only"
                    " - no good way to get this here :(")
            case ConfigKey.SM_CONTEXT_REF:
                return_value = kwargs['header_location'].split("/")[-1]
            case ConfigKey.NRF_IP:
                return_value = self.core_config['nrf']['sbi']['server'][0]['address']
            case ConfigKey.NRF_PORT:
                return_value = self.core_config['nrf']['sbi']['server'][0]['port']

        return return_value

    def write(self, key: ConfigKey, value):
        match key:
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_INTEGRITY:
                # this is not enabled by default
                if 'security_indication' not in self.core_config['smf']:
                    self.core_config['smf']['security_indication'] = {}
                sec_indication = self.core_config['smf']['security_indication']
                sec_indication['integrity_protection_indication'] = value
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_CONFIDENTIALITY:
                if 'security_indication' not in self.core_config['smf']:
                    self.core_config['smf']['security_indication'] = {}
                sec_indication = self.core_config['smf']['security_indication']
                sec_indication['confidentiality_protection_indication'] = value

        # TODO: maybe implement some commit method or we will do this on every change
        with open(self.core_config_path, "w", encoding="utf-8") as file_handle:
            yaml.dump(self.core_config, file_handle)

    def compare(self, _key: ConfigKey, _to_value):
        return True


class Open5gsCore(Open5GSBase):
    """Interface implementation of the open5gs core device"""
    def __init__(self):
        super().__init__()
        self.config = Open5gsCoreConfig(self.paths)

    def start(self):
        process = run_local(
            self.name(),
            f"{self.paths['base']}/build/tests/app/5gc -c "
            f"{self.paths['base']}/build/configs/sample.yaml",
            ["UDR initialize...done", "NF Service [nudr-dr]"])
        self.pid = process.pid

    def stop(self):
        run_local(self.name(), f"kill -p {self.pid}", action="Stopping")

    def perform(self, action: ActionKey, **kwargs):
        match action:
            case ActionKey.EXEC_IN_CONTEXT:
                event = kwargs['event']
                LOGGER.info("Excecuting event open5gs:\n%s", event)
                event()
            case ActionKey.REPLAY_PACKET:
                replay_file = kwargs['packet']
                command = f"tcpreplay -q -i lo {replay_file}"
                LOGGER.info("Replaying packet for open5gs with command:\n%s", command)
                run_local(self.name(), command, action="PacketReplay")
            case _:
                raise RuntimeError(
                    f"Open5GS does not implement action for key: {action}")


class Open5gsNRF(Open5gsCore):
    """Interface implementation of the open5gs NRF device (without running the whole core)"""
    def __init__(self):
        super().__init__()
        self.tmux_session_name = f"{self.name()}_start"

    def perform(self, action: ActionKey, **kwargs):
        match action:
            case ActionKey.NRF_REGISTRATION:
                LOGGER.info("Trying to register a NF in open5gs NRF")
                requester_nf_type = kwargs['requester_nf_type']
                requester_nf_ip_addr = kwargs['requester_nf_ip_addr']
                requester_nf_instance_id = kwargs['requester_nf_instance_id']
                # requester_nf_nssais_sst = kwargs['requester_nf_nssais_sst']
                # for simplicity we assume sst 1 (= eMBB)
                requester_nf_nssais_sd = kwargs['requester_nf_nssais_sd']

                nf1_nrf_reg_url = (
                    f"http://{self.config.read(ConfigKey.NRF_IP)}:"
                    f"{self.config.read(ConfigKey.NRF_PORT)}/nnrf-nfm/v1/nf-instances/"
                    f"{requester_nf_instance_id}")

                data = {
                    "nfInstanceId": requester_nf_instance_id,
                    "nfType": requester_nf_type,
                    "nfStatus": "REGISTERED",
                    "ipv4Addresses": [requester_nf_ip_addr],
                    "sNssais": [{"sst": 1, "sd": requester_nf_nssais_sd}],
                    "allowedNssais": [{"sst": 1, "sd": requester_nf_nssais_sd}],
                }

                buffer = BytesIO(json.dumps(data).encode('utf-8'))

                client = pycurl.Curl()
                client.setopt(pycurl.URL, nf1_nrf_reg_url)
                client.setopt(pycurl.USERAGENT, requester_nf_type)
                client.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE)
                client.setopt(pycurl.HTTPHEADER, [
                              "Content-Type: application/x-www-form-urlencode",
                              "Accept: application/json"])
                client.setopt(pycurl.UPLOAD, 1)
                client.setopt(pycurl.READDATA, buffer)
                # prevent pycurl to print stuff in terminal
                client.setopt(pycurl.WRITEFUNCTION, lambda x: None)

                client.perform()

                assert client.getinfo(pycurl.RESPONSE_CODE) == 200 or client.getinfo(
                    pycurl.RESPONSE_CODE) == 201
                LOGGER.info("Registered %s with slice %s in NRF",
                            requester_nf_type, requester_nf_nssais_sd)

                client.close()
            case ActionKey.NRF_DISCOVERY:
                requester_nf_type = kwargs['requester_nf_type']
                target_nf_type = kwargs['target_nf_type']

                params = f"target-nf-type={target_nf_type}&requester-nf-type={requester_nf_type}"
                nrf_disc_url = (
                    f"http://{self.config.read(ConfigKey.NRF_IP)}:"
                    f"{self.config.read(ConfigKey.NRF_PORT)}/nnrf-disc/v1/nf-instances?{params}")

                buffer = BytesIO()

                client = pycurl.Curl()
                client.setopt(pycurl.URL, nrf_disc_url)
                client.setopt(pycurl.USERAGENT, requester_nf_type)
                client.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE)
                client.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
                client.setopt(pycurl.WRITEDATA, buffer)

                client.perform()

                response_data = json.loads(buffer.getvalue())
                LOGGER.info("NRF response: %s", response_data)

                client.close()

    def setup(self):
        run_local(self.name(), "pkill -f open5gs-nrfd")
        if shutil.which("tmux") is None:
            pytest.exit("tmux is required to start Open5GS_Core_SA_NRF")

    def start(self):
        process = run_local(
            self.name(),
            f"tmux new -s {self.tmux_session_name} "
            f"'{self.paths['base']}/install/bin/open5gs-nrfd 2>&1'",
            ["NRF initialize...done"])
        self.pid = process.pid

    def stop(self):
        run_local(self.name(), f"tmux kill-session -t {self.tmux_session_name}", action="Stopping")
        run_local(self.name(), f"kill -p {self.pid}", action="Stopping")
