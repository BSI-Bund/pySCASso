"""Module holding the abstract device config definition"""
from abc import ABC, abstractmethod
from enum import Enum, auto

from scas.packet_type.common import SecurityAlgorithm, SecurityAlgorithmMapping


class ConfigKey(Enum):
    """Enum class with all the config keys. This is used to abstract the actual config value for
    every device and keep the test implementation generic.
    """
    SMF_IP = auto()
    SMF_PORT = auto()
    SMF_NAS_SECURITY_INDICATION_INTEGRITY = auto()
    SMF_NAS_SECURITY_INDICATION_CONFIDENTIALITY = auto()
    AMF_IP = auto()
    AMF_PORT = auto()
    AMF_INTEGRITY_PROT_ALG_ORDERED_LIST = auto()
    UDM_IP = auto()
    UDM_PORT = auto()
    UDM_AUTHENTICATION_STATUS = auto()
    UDM_SDM_OPENAPI_VERSION = auto()
    UDM_UEAU_OPENAPI_VERSION = auto()
    AUSF_IP = auto()
    AUSF_PORT = auto()
    NRF_IP = auto()
    NRF_PORT = auto()
    UE_SUPI = auto()
    SM_CONTEXT_REF = auto()
    UE_INTEGRITY_ALG_IA0 = auto()
    UE_INTEGRITY_ALG_IA1 = auto()
    UE_INTEGRITY_ALG_IA2 = auto()
    UE_INTEGRITY_ALG_IA3 = auto()
    UE_CIPHERING_ALG_EA0 = auto()
    UE_CIPHERING_ALG_EA1 = auto()
    UE_CIPHERING_ALG_EA2 = auto()
    UE_CIPHERING_ALG_EA3 = auto()


class DeviceConfig(ABC):
    """Generic Device Config class definition"""

    # initialized as 1:1 mapping (e.g. for dummy dev.)
    algorithm_mapping = SecurityAlgorithmMapping()
    # can be used to modify individual mappings in subclasses (e.g. only for NEA0 - NEA3)
    custom_algorithm_mapping = []

    def config_algorithm_by_enum(self, algo: SecurityAlgorithm) -> str:
        """converts the Security Algorithm to a specific name the current device config instance
        uses

        Args:
            algo (SecurityAlgorithm): the wanted algorithm

        Returns:
            str: the device specific name for this algorithm
        """
        return self.algorithm_mapping.get_mapping(algo)

    def config_algorithm_by_name(self, name: str) -> SecurityAlgorithm:
        """converts the device specific security algorithm name to the corresponding Security
        Algorithm enum object

        Args:
            name (str): device config specific name of the algorithm

        Returns:
            SecurityAlgorithm: corresponding algorithm enum object
        """
        return self.algorithm_mapping.get_original(name)

    @abstractmethod
    def read(self, key: ConfigKey):
        """Abstract method for reading a value from the device config"""
        raise NotImplementedError

    @abstractmethod
    def write(self, key: ConfigKey, value):
        """Abstract method for writing a value to the device config"""
        raise NotImplementedError

    @abstractmethod
    def compare(self, key: ConfigKey, to_value):
        """Abstract method to compare a value of the device config with a given value"""
        raise NotImplementedError
