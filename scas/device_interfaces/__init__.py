"""Module provides abstract devices and the available device implementations"""
from scas.device_interfaces.device import Device, ActionKey
from scas.device_interfaces.device_config import DeviceConfig, ConfigKey

__all__ = ['Device', 'ActionKey', 'DeviceConfig', 'ConfigKey']
