"""Module containing pytest setup and fixtures"""
import logging
import os
import platform
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict

import allure
import pytest
import yaml
from pytest import CollectReport, StashKey, skip

import project_paths
from scas.device_interfaces import specific
from scas.device_interfaces.device import Device
from scas.logger import LOGGER

# Keys of our conftest.yaml config file
FALLBACK_KEY = "fallback"
CORE_KEY = "core"
RAN_KEY = "ran"
UE_KEY = "ue"


def pytest_addoption(parser):
    """adds the command line options for the pytest command
    """
    parser.addoption("--report", action="store_true",
                     default=False, help="Flag to produce a report for the executed test(s).")
    parser.addoption("--dummy", action="store_true",
                     default=False, help="Flag to perform tests with dummy devices for Core/RAN/UE"
                     " and prerecorded pcaps.")
    parser.addoption("--config", action="store", default=project_paths.TESTS + "/test_config.yaml",
                     help="Path to test config yaml file.")
    parser.addoption("--fallback", action="store_true",
                     default=False, help="Flag to allow fallback to fallback test settings rather"
                     " than skipping an unconfigured test")


def pytest_configure(config):
    """This functions allows us to dynamically modify the pytest config
    (e.g. based on command line parameters)"""
    # adding the allure dir to trigger allure report creation
    if config.getoption("--report"):
        config.option.allure_report_dir = f"{get_report_path()}/allure"

#######################################
# usual functions for use in fixtures #
#######################################


def error_and_exit(msg):
    """Wraps logging and pytest exit"""
    LOGGER.error(msg)
    pytest.exit(msg)


def get_device_from_config(test_name, device_class, force_dummy_cap) -> Device:
    """reads the provided test_config.yaml file and decides which device to use for a test"""
    module = specific
    class_string = "Dummy"

    if not force_dummy_cap:
        if test_name in pytest.test_config:
            if device_class in pytest.test_config[test_name]:
                class_string = pytest.test_config[test_name][device_class]
                # returns the test specific device
                # calls device constructor
                return getattr(module, class_string)()

        if device_class in pytest.test_config[FALLBACK_KEY]:
            class_string = pytest.test_config[FALLBACK_KEY][device_class]
            # returns the fallback device
            LOGGER.debug("No specific %s device for %s in config file. Fallback to %s device %s.",
                         device_class, test_name, device_class, class_string)
            return getattr(module, class_string)()

        LOGGER.warning("No %s device for %s in config file.", device_class, test_name)
        LOGGER.warning("Using %s for %s device.", class_string, device_class)

    # returns the dummy device
    return getattr(module, class_string)()


####################
# general fixtures #
####################

@pytest.fixture(autouse=True, scope="session", name="check_python_version")
def fixture_check_python_version():
    """Checks the installed python version"""
    major = sys.version_info[0]
    minor = sys.version_info[1]

    if major < 3 or major >= 3 and minor < 10:
        error_and_exit("Python version >=3.10 required")


@pytest.fixture(autouse=True, scope="session", name="check_external_dependencies")
def fixture_check_external_dependencies():
    """Checks if certain requirements are met before executing any test"""
    msg_dumpcap = "\nWireshark (dumpcap) permissions + capabilties missing.\n"\
                  "\tsudo chmod 750 /usr/bin/dumpcap\n"\
                  "\tsudo chown root:wireshark /usr/bin/dumpcap\n"\
                  "\tsudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap\n"\
                  "\tusermod -a -G wireshark $(id -un)\n"\
                  "You may have to logout/login to apply group changes to current user\n"

    msg_tcpreplay = "\ntcpreplay permissions + capabilties missing.\n"\
                    "\tsudo groupadd tcpreplay\n"\
                    "\tsudo usermod -a -G tcpreplay $(id -un)\n"\
                    "\tsudo chmod 750 /usr/bin/tcpreplay\n"\
                    "\tsudo chown root:tcpreplay /usr/bin/tcpreplay\n"\
                    "\tsudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/tcpreplay\n"\
                    "You may have to logout/login to apply group changes to current user\n"

    # check for binaries
    deps = [["tshark", "-v"], ["tcpreplay", "-V"], ["dumpcap", "-v"]]
    for dep in deps:
        try:
            subprocess.call(dep)
        except FileNotFoundError:
            if dep[0] == "dumpcap":
                LOGGER.error(msg_dumpcap)
            error_and_exit(
                f"{dep[0]} is missing but required to be installed!")
        except PermissionError:
            error_and_exit(
                f"{dep[0]} has the wrong permissions!")
                
    # check wireshark/tshark version - as of version 4.1.0 the filter names for NAS 5GS changed
    # from nas_5gs to nas-5gs
    # We adapted the new filters, therefore older versions of wireshark/tshark will fail all tests
    # regarding NAS protocol.
    output = subprocess.check_output(["tshark", "--version"])
    version_line = output.decode("utf-8").split("\n", maxsplit=1)[0]
    version = re.search(r"(\d+)\.?(\d+)\.?(\*|\d+)", version_line)
    major_version = int(version.group(1))
    minor_version = int(version.group(2))

    if major_version < 4 or major_version == 4 and minor_version < 1:
        error_and_exit("Tshark version <4.1.0 is not supported!")

    # check for capabilities
    output = subprocess.check_output(["/usr/sbin/getcap", "/usr/bin/dumpcap"])
    if b"cap_net_raw" not in output:
        error_and_exit(msg_dumpcap)

    output = subprocess.check_output(
        ["/usr/sbin/getcap", "/usr/bin/tcpreplay"])
    if b"cap_net_raw" not in output:
        error_and_exit(msg_tcpreplay)


def get_report_path():
    """Builds and returns the path to the current test report directory"""
    try:
        _ = pytest.report_path
    except AttributeError:
        now = datetime.now()
        report_path = f"{project_paths.PROJECT_ROOT_PATH}/reports/{now.strftime('%Y%m%d_%H%M%S')}"
        Path(report_path).mkdir(parents=True, exist_ok=True)
        pytest.report_path = report_path
    return pytest.report_path


@pytest.fixture(autouse=True, scope="session", name="create_report")
def fixture_create_report(request, _read_config, get_config_file):
    """Fixture for creating test reports"""
    pytest.create_report = request.config.getoption("--report")

    # HACK: making the session available (for switching formatter of logger on the fly)
    pytest.session = request.session

    if pytest.create_report:
        pytest.report_file_path = f"{get_report_path()}/report.txt"
        LOGGER.addHandler(logging.FileHandler(pytest.report_file_path))
        logging_plugin = request.config.pluginmanager.get_plugin(
            "logging-plugin")
        logging_plugin.set_log_path(pytest.report_file_path)

        # print current config at top of report
        LOGGER.info("Current Configuration:\n%s\nPython %s\n\n%s\n\n%s\n%s",
                    platform.platform(),
                    sys.version,
                    ' '.join(sys.argv),
                    get_config_file,
                    yaml.dump(pytest.test_config))


phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Handy fixture that stores the result status of every test case to be accessed while
    test excecution"""

    # using call to prevent linter warnings, _call does break the hookimpl
    _ = call

    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep


@pytest.fixture(autouse=True, scope="function", name="create_report_text_test_case")
def fixture_create_report_text_test_case(request):
    """Fixture for writing test excecution log to a file as part of a report"""
    if not pytest.create_report:
        yield
        return

    # save test file for allure
    allure.attach.file(
        request.node.location[0], attachment_type=allure.attachment_type.TEXT)

    test_name = request.node.location[2]
    pytest.current_test_name = test_name

    test_path = request.node.location[0]

    LOGGER.newline()
    LOGGER.info("%s -> %s", test_path, test_name)

    yield

    report = request.node.stash[phase_report_key]

    for phase in report.keys():
        status = report[phase].outcome

        # report status of call every time
        if phase == 'call':
            LOGGER.info("%s -> %s:\t%s", test_path, test_name, status.upper())
            continue

        # report status of other phases only on fail/skip etc
        if status != 'passed':
            LOGGER.info("%s -> %s:\t%s", test_path, test_name, status.upper())

    LOGGER.newline()


@pytest.fixture(autouse=True, scope="session", name="force_dummy_capture")
def fixture_force_dummy_capture(request):
    """Fixture that forces all tests to be executed with the dummy device"""
    pytest.dummy_capture = request.config.getoption("--dummy")
    return pytest.dummy_capture


@pytest.fixture(scope="session", name="get_config_file")
def fixture_get_config_file(request):
    """Returns the currently used test config file"""
    pytest.test_config_file = request.config.getoption("--config")
    return pytest.test_config_file


@pytest.fixture(autouse=True, scope="session", name="_read_config")
def fixture_read_config(get_config_file):
    """Parses the test config file"""
    test_config = get_config_file
    LOGGER.debug("Parsing test config: %s.", test_config)

    if not os.path.exists(test_config):
        LOGGER.error("Could not open %s. Please provide a valid test config file by copying or "
                     "renaming the default test_config.yaml.default to test_config.yaml or "
                     "provide a custom config file by applying the --config <path-to-config> "
                     "parameter", test_config)
        pytest.exit(f"Could not open {test_config}.")

    with open(test_config, "r", encoding="utf-8") as stream:
        try:
            # attach the self defined variable test_config to global pytest scope
            pytest.test_config = yaml.safe_load(stream)
        except yaml.YAMLError:
            LOGGER.warning("Could not parse %s. Fallback to dummy backends.", test_config)


# handle tests which have no config (steered by cli argument)
# -> either skip the test or fallback to fallback settings (--fallback arg)
@pytest.fixture(autouse=True, name="testcase_configured")
def fixture_testcase_configured(request, get_config_file, force_dummy_capture):
    """Checks if current test case is configured via test config. If not checks for
    --fallback flag. If this is not present the test gets skipped."""
    # skip if --dummy aka no live capture was passed
    if force_dummy_capture:
        return
    test_name = request.node.name
    if not request.config.getoption("--fallback") and test_name not in pytest.test_config:
        LOGGER.warning("%s not configured in %s and no --fallback desired.",
                       test_name, get_config_file)
        skip(f"{test_name} not configured in {get_config_file} and no --fallback desired.")


###################
# device fixtures #
###################

@pytest.fixture(name="provide_core_config")
def fixture_provide_core_config(request, force_dummy_capture):
    """Fixture that yields the core config of the used core device"""
    core = get_device_from_config(
        request.node.name, "core", force_dummy_capture)
    yield core.get_config()


@pytest.fixture(name="provide_ran_config")
def fixture_provide_ran_config(request, force_dummy_capture):
    """Fixture that yields the RAN config of the used RAN device"""
    ran = get_device_from_config(request.node.name, "ran", force_dummy_capture)
    yield ran.get_config()


@pytest.fixture(name="provide_ue_config")
def fixture_provide_ue_config(request, force_dummy_capture):
    """Fixture that yields the UE config of the used UE device"""
    ue_device = get_device_from_config(request.node.name, "ue", force_dummy_capture)
    yield ue_device.get_config()

# TODO: redundant - rebuild to use several devices in a test case without specifying core,
# RAN, UE etc. - but keep the test cases independent from the device implementation!


@pytest.fixture(name="provide_core")
def fixture_provide_core(request, force_dummy_capture):
    """Fixture that yields the core object of the used core device.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    core = get_device_from_config(
        request.node.name, "core", force_dummy_capture)
    LOGGER.info("Using Core: %s", core.name())
    yield core
    core.stop()
    core.teardown()


@pytest.fixture(name="provide_ran")
def fixture_provide_ran(request, force_dummy_capture):
    """Fixture that yields the RAN object of the used RAN device.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    ran = get_device_from_config(request.node.name, "ran", force_dummy_capture)
    LOGGER.info("Using RAN:  %s", ran.name())
    yield ran
    ran.stop()
    ran.teardown()


@pytest.fixture(name="provide_ue")
def fixture_provide_ue(request, force_dummy_capture):
    """Fixture that yields the UE object of the used UE device.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    ue_device = get_device_from_config(request.node.name, "ue", force_dummy_capture)
    LOGGER.info("Using UE:   %s", ue_device.name())
    yield ue_device
    ue_device.stop()
    ue_device.teardown()


@pytest.fixture(name="provide_running_core")
def fixture_provide_running_core(request, force_dummy_capture):
    """Fixture that yields the core object of the used core device.
    The methods setup and start are called before yield.
    The core is already running when the test case using this fixture is executed.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    core = get_device_from_config(
        request.node.name, "core", force_dummy_capture)
    core.setup()
    core.start()
    LOGGER.info("Using Core (auto setup & start): %s", core.name())
    yield core
    core.stop()
    core.teardown()


@pytest.fixture(name="provide_running_ran")
def fixture_provide_running_ran(request, force_dummy_capture):
    """Fixture that yields the RAN object of the used RAN device.
    The methods setup and start are called before yield.
    The RAN is already running when the test case using this fixture is executed.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    ran = get_device_from_config(request.node.name, "ran", force_dummy_capture)
    ran.setup()
    ran.start()
    LOGGER.info("Using RAN (auto setup & start):  %s", ran.name())
    yield ran
    ran.stop()
    ran.teardown()


@pytest.fixture(name="provide_running_ue")
def fixture_provide_running_ue(request, force_dummy_capture):
    """Fixture that yields the UE object of the used UE device.
    The methods setup and start are called before yield.
    The UE is already running when the test case using this fixture is executed.
    It also handels stop and teardown at the end of test cases (even in assert cases)"""
    ue_device = get_device_from_config(request.node.name, "ue", force_dummy_capture)
    ue_device.setup()
    ue_device.start()
    LOGGER.info("Using UE (auto setup & start):   %s", ue_device.name())
    yield ue_device
    ue_device.stop()
    ue_device.teardown()
