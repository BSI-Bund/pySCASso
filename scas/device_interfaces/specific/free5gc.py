"""Module containing the free5gc device implementation"""
import os

import pytest
import yaml
from pymongo import MongoClient

from scas.device_interfaces.device import ActionKey, Device
from scas.device_interfaces.device_config import ConfigKey, DeviceConfig
from scas.capture.capture import Capture, CaptureTarget
from scas.capture.local_live_capture import LocalLiveCapture
from scas.helper import run_local
from scas.logger import LOGGER


class Free5GCConfig(DeviceConfig):
    """Interface for accessing the free5gc config"""
    amf_config = None
    smf_config = None
    udm_config = None
    ausf_config = None
    nrf_config = None

    def __init__(self, paths) -> None:
        self.paths = paths
        amf_config_path = f"{self.paths['config']}/amfcfg.yaml"
        smf_config_path = f"{self.paths['config']}/smfcfg.yaml"
        udm_config_path = f"{self.paths['config']}/udmcfg.yaml"
        nrf_config_path = f"{self.paths['config']}/nrfcfg.yaml"
        ausf_config_path = f"{self.paths['config']}/ausfcfg.yaml"

        if self.amf_config is None:
            with open(amf_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.amf_config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s.", amf_config_path)

        if self.smf_config is None:
            with open(smf_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.smf_config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s.", smf_config_path)

        if self.udm_config is None:
            with open(udm_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.udm_config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s.", udm_config_path)

        if self.nrf_config is None:
            with open(nrf_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.nrf_config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s.", nrf_config_path)

        if self.ausf_config is None:
            with open(ausf_config_path, "r", encoding="utf-8") as stream:
                try:
                    self.ausf_config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s.", ausf_config_path)

    def get_database(self):
        """returns handle to the local free5gc database"""
        return MongoClient("mongodb://127.0.0.1")['free5gc']

    def read(self, key: ConfigKey, **kwargs):
        """returns the config values for a given key"""
        # pylint complains about too many return statements, so we introduce a local var to capture
        # the return value
        return_value = None
        match key:
            case ConfigKey.AMF_INTEGRITY_PROT_ALG_ORDERED_LIST:
                # This is translated to the wireshark representation
                return_value = [self.config_algorithm_by_name(alg) for alg in
                                self.amf_config['configuration']['security']['integrityOrder']]
            case ConfigKey.AMF_IP:
                return_value = self.amf_config['configuration']['sbi']['bindingIPv4']
            case ConfigKey.AMF_PORT:
                return_value = self.amf_config['configuration']['sbi']['port']
            case ConfigKey.SMF_IP:
                return_value = self.smf_config['configuration']['sbi']['bindingIPv4']
            case ConfigKey.SMF_PORT:
                return_value = self.smf_config['configuration']['sbi']['port']
            case ConfigKey.AUSF_IP:
                return_value = self.ausf_config['configuration']['sbi']['bindingIPv4']
            case ConfigKey.AUSF_PORT:
                return_value = self.ausf_config['configuration']['sbi']['port']
            case ConfigKey.UDM_IP:
                return_value = self.udm_config['configuration']['sbi']['bindingIPv4']
            case ConfigKey.UDM_PORT:
                return_value = self.udm_config['configuration']['sbi']['port']
            case ConfigKey.UDM_SDM_OPENAPI_VERSION:
                return_value = "1"
            case ConfigKey.UDM_UEAU_OPENAPI_VERSION:
                return_value = "1"
            case ConfigKey.UDM_AUTHENTICATION_STATUS:
                collection = self.get_database(
                )['subscriptionData']['authenticationData']['authenticationStatus']
                return_value = collection.find_one({"ueId": kwargs['ueId']})
            case ConfigKey.SM_CONTEXT_REF:
                # free5gc only places the smContextRef in the location field, which is not standard
                # conform
                return_value = kwargs['header_location']
            case ConfigKey.NRF_IP:
                return_value = self.nrf_config['configuration']['sbi']['bindingIPv4']
            case ConfigKey.NRF_PORT:
                return self.nrf_config['configuration']['sbi']['port']
        return return_value

    def write(self, key: ConfigKey, value):
        """writes to the config by providing a key and a value"""
        match key:
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_INTEGRITY:
                # hardcoded this in sm_context.go NewSMContext because there does not seem to be a
                # yaml key for this
                LOGGER.warning("Free 5GC does not provide this setting in the config.")
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_CONFIDENTIALITY:
                # hardcoded this in sm_context.go NewSMContext because there does not seem to be a
                # yaml key for this
                LOGGER.warning("Free 5GC does not provide this setting in the config.")

        # with open(self.core_config_path, "w") as f:
        #     yaml.safe_dump(self.core_config, f)

    def compare(self, key: ConfigKey, to_value):
        return True


class Free5GCCore(Device):
    """Core implementation of free5gc"""

    def is_available(self) -> bool:
        """checks if the pathes to the locally build free5gc folders exist"""
        self.paths["base"] = pytest.test_config["env"]["FREE5GC_PATH"]
        self.paths["bin"] = f"{self.paths['base']}"
        self.paths["config"] = f"{self.paths['base']}/config"
        self.paths["log"] = f"{self.paths['base']}/log"
        return self.paths_exist()

    def __init__(self):
        super().__init__()
        self.config = Free5GCConfig(self.paths)

    def setup(self):
        """some preparation for free5gc to run, e.g. kill artifact of previous run"""
        with open(f"{self.paths['base']}/force_kill.sh", "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()

        if "Killed all free5gc processes" not in last_line:
            with open(f"{self.paths['base']}/force_kill.sh", "a", encoding="utf-8") as file:
                file.write("echo Killed all free5gc processes\n")

    def start(self):
        """start free5gc"""
        run_local(self.name(), f"sudo {self.paths['base']}/run.sh 2>&1", [
                  "ausf context =", "Use NF certPath: cert/chf.pem"], cwd=self.paths['base'])

    def stop(self):
        """stop free5gc"""
        # The parent process spawnes some other ones that do not get killed, so we kill all
        # matching processes
        run_local(self.name(), f"sudo {self.paths['base']}/force_kill.sh", [
                  "Killed all free5gc processes"], action="Stopping", cwd=self.paths['base'])

    def perform(self, action: ActionKey, **kwargs):
        """performs a specific action with free5gc"""
        match action:
            case ActionKey.EXEC_IN_CONTEXT:
                event = kwargs['event']
                LOGGER.info("Excecuting event free5gc:\n%s", event)
                event()
            case ActionKey.REPLAY_PACKET:
                replay_file = kwargs['packet']
                command = f"tcpreplay -q -i lo {replay_file}"
                LOGGER.info("Replaying packet for free5gc with command:\n%s", command)
                run_local(self.name(), command, action="PacketReplay")
            case _:
                raise RuntimeError(f"Free5GC does not implement action for key: {action}")

    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        return LocalLiveCapture()

    def teardown(self):
        pass


class Free5GCCoreNRF(Free5GCCore):
    """class for running only the NRF of free5gc (and not the whole core)"""
    def start(self):
        run_local(self.name(),
                  f"{self.paths['base']}/bin/nrf 2>&1", ["Binding addr"], cwd=self.paths['base'])
