"""Module with dummy implementation"""
import pathlib

import yaml

from scas.device_interfaces import ConfigKey, Device
from scas.device_interfaces.device import ActionKey
from scas.device_interfaces.device_config import DeviceConfig
from scas.capture.capture import Capture, CaptureTarget
from scas.capture.local_file_capture import LocalFileCapture
from scas.logger import LOGGER


class DummyConfig(DeviceConfig):
    """Dummy Config implementation
    """
    config = None

    def __init__(self) -> None:
        super().__init__()
        config_path = f"{pathlib.Path(__file__).parent.resolve()}/dummy.yaml"
        if self.config is None:
            with open(config_path, "r", encoding="utf-8") as stream:
                try:
                    self.config = yaml.safe_load(stream)
                except yaml.YAMLError:
                    LOGGER.warning("Could not parse %s", self.config)

    def read(self, key: ConfigKey, **kwargs):
        # pylint complains about too many return statements, so we introduce a local var to capture
        # the return value
        return_val = None
        match key:
            case ConfigKey.SMF_IP:
                return_val = "127.0.0.4"
            case ConfigKey.SM_CONTEXT_REF:
                return_val = kwargs['header_location'].split("/")[-1]
            case ConfigKey.UDM_IP:
                return_val = "127.0.0.12"
            case ConfigKey.UDM_SDM_OPENAPI_VERSION:
                # this mimics open5gs cause the dummy device uses pcaps recoreded with open5gs
                return_val = "2"
            case ConfigKey.UDM_UEAU_OPENAPI_VERSION:
                # this mimics open5gs cause the dummy device uses pcaps recoreded with open5gs
                return_val = "1"
            case ConfigKey.UDM_AUTHENTICATION_STATUS:
                raise RuntimeError(
                    "Dummy device mimics Open5GS v26 that keeps the UEs auth status "
                    "in memory only - no good way to get this here :(")
            case ConfigKey.AMF_IP:
                return_val = "127.0.0.5"
            case ConfigKey.AMF_INTEGRITY_PROT_ALG_ORDERED_LIST:
                return_val = [self.algorithm_mapping.get_original(alg)
                              for alg in self.config['amf']['security']['integrity_order']]
            case ConfigKey.AUSF_IP:
                return_val = "127.0.0.11"
            case ConfigKey.UE_SUPI:
                return_val = "imsi-999700000000001"
            case ConfigKey.NRF_IP:
                return_val = "127.0.0.10"
            case ConfigKey.NRF_PORT:
                return_val = "7777"
        return return_val

    def write(self, key: ConfigKey, _value):
        pass

    def compare(self, key: ConfigKey, _to_value):
        return True


class Dummy(Device):
    """
    The Dummy device does nothing and is a drop-in replacement for non-live-capture.
    """

    def __init__(self):
        super().__init__()
        self.config = DummyConfig()

    def is_available(self) -> bool:
        return True

    def setup(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def teardown(self):
        pass

    def perform(self, action: ActionKey, **kwargs):
        pass

    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        return LocalFileCapture()
