"""Module with ueransim implementation"""
import time
from shutil import which

import pytest
import yaml

from scas.device_interfaces.device import ActionKey, Device
from scas.device_interfaces.device_config import ConfigKey, DeviceConfig
from scas.capture.capture import Capture, CaptureTarget
from scas.helper import run_local
from scas.logger import LOGGER


class UeransimBase(Device):
    """base implementation of ueransim device
    """
    def __init__(self):
        Device.__init__(self)
        self.paths["base"] = pytest.test_config["env"]["UERANSIM_PATH"]
        self.paths["bin"] = f"{self.paths['base']}/build"
        self.paths["config"] = f"{self.paths['base']}/config"
        self.session_name = None

    def is_available(self) -> bool:
        return self.paths_exist()

    def stop(self):
        run_local(self.name(), f"kill -p {self.pid}", action="Stopping")

    def teardown(self):
        pass

    def perform(self, action: ActionKey, **kwargs):
        pass

    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        pass


class UeransimUEConfig(DeviceConfig):
    """Interface to the UERANSIM UE config"""
    ue_config = None
    ue_config_file = ""

    def __init__(self, path) -> None:
        self.ue_config_file = path
        with open(self.ue_config_file, "r", encoding="utf-8") as stream:
            try:
                self.ue_config = yaml.safe_load(stream)
            except yaml.YAMLError:
                LOGGER.warning("Could not parse %s.", self.ue_config_file)
        super().__init__()

    def read(self, key: ConfigKey):
        # pylint complains about too many return statements, so we introduce a local var to capture
        # the return value
        return_value = None
        match key:
            case ConfigKey.UE_SUPI:
                return_value = self.ue_config['supi']
            case ConfigKey.UE_INTEGRITY_ALG_IA1:
                return_value = self.ue_config['integrity']['IA1']
            case ConfigKey.UE_INTEGRITY_ALG_IA2:
                return_value = self.ue_config['integrity']['IA2']
            case ConfigKey.UE_INTEGRITY_ALG_IA3:
                return_value = self.ue_config['integrity']['IA3']
            case ConfigKey.UE_CIPHERING_ALG_EA1:
                return_value = self.ue_config['ciphering']['EA1']
            case ConfigKey.UE_CIPHERING_ALG_EA2:
                return_value = self.ue_config['ciphering']['EA2']
            case ConfigKey.UE_CIPHERING_ALG_EA3:
                return_value = self.ue_config['ciphering']['EA3']
        return return_value

    def write(self, key: ConfigKey, value):
        match key:
            case ConfigKey.UE_INTEGRITY_ALG_IA1:
                self.ue_config['integrity']['IA1'] = value
            case ConfigKey.UE_INTEGRITY_ALG_IA2:
                self.ue_config['integrity']['IA2'] = value
            case ConfigKey.UE_INTEGRITY_ALG_IA3:
                self.ue_config['integrity']['IA3'] = value
            case ConfigKey.UE_CIPHERING_ALG_EA1:
                self.ue_config['ciphering']['EA1'] = value
            case ConfigKey.UE_CIPHERING_ALG_EA2:
                self.ue_config['ciphering']['EA2'] = value
            case ConfigKey.UE_CIPHERING_ALG_EA3:
                self.ue_config['ciphering']['EA3'] = value
            case _:
                LOGGER.warning("Could not write to %s: key %s value: %s",
                               self.ue_config, key, value)

        # TODO: maybe implement some commit method or we will do this on every change
        with open(self.ue_config_file, "w", encoding="utf-8") as file_handle:
            yaml.dump(self.ue_config, file_handle, sort_keys=False,
                      default_flow_style=False)

    def compare(self, _key: ConfigKey, _to_value):
        pass


class UeransimUE(UeransimBase):
    """Interface to the UERANSIM UE device"""
    def __init__(self):
        UeransimBase.__init__(self)
        self.session_name = f"{self.name()}_start"
        self.ue_config_file = ""

    def setup(self):
        if which("tmux") is None:
            pytest.exit("tmux is required to start UERANSIM_UE")

        # TODO: this could be harmful if we need multiple instances of this device...
        # to make shure that there is no zombie process running interfering with the current
        # process
        self.stop()

    def start(self):
        process = run_local(
            self.name(),
            f"tmux new -s {self.session_name} "
            f"'sudo {self.paths['bin']}/nr-ue -c {self.ue_config_file}'",
            ["PDU Session establishment is successful PSI", "UE switches to state [CM-IDLE]"])
        self.pid = process.pid

    def stop(self):
        if self.session_name:
            run_local(self.name(), f"tmux kill-session -t {self.session_name}", action="Stopping")
        if self.pid:
            run_local(self.name(), f"kill -p {self.pid}", action="Stopping")

    def perform(self, action: ActionKey, **_kwargs):
        match action:
            case ActionKey.SYNC_FAILURE:

                LOGGER.info("Forcing Sync Failure on next registration of %s",
                            self.get_config().read(ConfigKey.UE_SUPI))
                # force UE to perform sync failure on next registration
                process = run_local(
                    self.name(),
                    f"{self.paths['bin']}/nr-cli {self.get_config().read(ConfigKey.UE_SUPI)} "
                    f"-e force_sync_fail_once", action="Triggering Sync Fail")
                result = process.before

                # check if UERANSIM supports sync failure obligation
                if ("The next registration/authentication procedure will trigger a Sync Failure"
                        not in result):
                    LOGGER.error(
                        "Your version of UERANSIM seams not to support triggering sync failure."
                        "(get the patched version - BELO)")
                    pytest.fail()

                LOGGER.info("Deregister UE %s", self.get_config().read(ConfigKey.UE_SUPI))
                # perform deregister (the UE will re-register automatically)
                run_local(
                    self.name(),
                    f"{self.paths['bin']}/nr-cli {self.get_config().read(ConfigKey.UE_SUPI)} "
                    f"-e 'deregister normal'", action="UE Deregistration")

                # We should give the system a little bit of time to re-register
                # We periodicaly check the ue status:
                while True:
                    LOGGER.info("Waiting for re-registration of UE %s",
                                self.get_config().read(ConfigKey.UE_SUPI))
                    time.sleep(1)
                    process = run_local(
                        self.name(),
                        f"{self.paths['bin']}/nr-cli {self.get_config().read(ConfigKey.UE_SUPI)} "
                        f"-e status", action="Check UE Registartion Status")
                    lines = process.before
                    if 'mm-state: MM-REGISTERED/NORMAL-SERVICE' in lines:
                        LOGGER.info("Registration of UE %s successful.",
                                    self.get_config().read(ConfigKey.UE_SUPI))
                        return


class UeransimUEopen5gs(UeransimUE):
    """Interface to the UERANSIM UE device configured for open5gs"""
    def __init__(self):
        super().__init__()
        self.ue_config_file = f'{self.paths["config"]}/open5gs-ue.yaml'
        self.config = UeransimUEConfig(self.ue_config_file)


class UeransimUEfree5gc(UeransimUE):
    """Interface to the UERANSIM UE device configured for free5gc"""
    def __init__(self):
        super().__init__()
        self.ue_config_file = f'{self.paths["config"]}/free5gc-ue.yaml'
        self.config = UeransimUEConfig(self.ue_config_file)


class UeransimGnodeBConfig(DeviceConfig):
    """Interface for the generic UERANSIM gNodeB config"""
    gnb_config = None
    gnb_config_file = ""

    def __init__(self, path) -> None:
        self.gnb_config_file = path
        with open(self.gnb_config_file, "r", encoding="utf-8") as stream:
            try:
                self.gnb_config = yaml.safe_load(stream)
            except yaml.YAMLError:
                LOGGER.warning("Could not parse %s.", self.gnb_config_file)
        super().__init__()

    def read(self, _key: ConfigKey):
        pass

    def write(self, _key: ConfigKey, _value):
        pass

    def compare(self, _key: ConfigKey, _to_value):
        pass


class UeransimGnodeB(UeransimBase):
    """Interface for the generic UERANSIM gNodeB device"""
    def __init__(self):
        # default is open5gs gNodeB
        UeransimBase.__init__(self)
        self.session_name = f"{self.name()}_start"
        self.gnodeb_config_file = f'{self.paths["config"]}/open5gs-gnb.yaml'

    def setup(self):
        if which("tmux") is None:
            pytest.exit("tmux is required to start UERANSIM_UE")

        # TODO: this could be harmful if we need multiple instances of this device...
        # to make shure that there is no zombie process running interfering with the current
        # process
        self.stop()

    def start(self):
        process = run_local(
            self.name(),
            f"tmux new -s {self.session_name} '{self.paths['bin']}/nr-gnb -c "
            f"{self.gnodeb_config_file}'", ["NG Setup procedure is successful"])
        self.pid = process.pid

    def stop(self):
        if self.session_name:
            run_local(self.name(), f"tmux kill-session -t {self.session_name}", action="Stopping")
        run_local(self.name(), f"kill -p {self.pid}", action="Stopping")


class UeransimGnodeBopen5gs(UeransimGnodeB):
    """Interface for the UERANSIM gNodeB for open5gs"""
    def __init__(self):
        UeransimGnodeB.__init__(self)
        self.gnodeb_config_file = f'{self.paths["config"]}/open5gs-gnb.yaml'
        self.config = UeransimGnodeBConfig(self.gnodeb_config_file)


class UeransimGnodeBfree5gc(UeransimGnodeB):
    """Interface for the UERANSIM gNodeB for free5gc"""
    def __init__(self):
        UeransimGnodeB.__init__(self)
        self.gnodeb_config_file = f'{self.paths["config"]}/free5gc-gnb.yaml'
        self.config = UeransimGnodeBConfig(self.gnodeb_config_file)
