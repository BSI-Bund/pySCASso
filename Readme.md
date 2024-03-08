# pySCASso

## Summary

This project offers a Python 3 framework for automating 3GPP defined SCAS tests. It is not a finished, polished, or production-ready piece of software. Instead, it should be viewed as an example, blueprint, or proof of concept for a generic automation of 3GPP defined SCAS tests.

| There is and will be no intent to provide full test coverage.

| This repository does and will never include vendor specific device implementations.

> This framework should only be used in a secure environment. Some potential risks are:
> - Probable insecure usage of temp file/directory
> - Paramiko call with policy set to automatically trust the unknown host key
> - Possible shell injection via Paramiko call
> - Usage of subprocess calls


**pySCASso** uses [_pytest_](https://docs.pytest.org/en) for test execution and provides a variety of features:

- tests being executed on a remote machine - no/little pollution of tested systems
- test implementation is test product agnostic
- abstraction of test product via interfaces
- automated starting, stopping, configuration read/write of test product
- packet capture and replay (local only, intercept and modification WIP)
- test execution with real/simulated test product (live capture) or with previously captured pcaps

## Overview
~~~
.
├── Dockerfile
├── LICENSE
├── pcaps
│   └── ... # this pcaps are used by the dummy device (e.g. for sanity check of this framework)
├── project_paths.py # helps with project paths 
├── pyproject.toml # general python project setup and log configuration for pytest
├── Readme.md
├── requirements.txt # python dependencies (install with pip install -r requirements.txt)
├── run_docker.sh # script to run the test framework from a docker environment
├── run_podman.sh # script to run the test framework from a podman environment
├── scas
│   ├── device_interfaces
│   │   ├── device_config.py # generic base class for defining the device config interface
│   │   ├── device.py # generic base class for defining the device interface
│   │   └── specific # contains some (incomplete) implementations of devices and device configs (dummy, open5gs, ...)
│   │       └── ...
│   ├── capture # contains generic and specific implementations of the packet capture interface 
│   │   └── ...
│   ├── helper.py # contains general helper functions, e.g. function to run local commands with timeouts, waiting for specific stdout
│   ├── logger.py # definition of global logger
│   ├── packet_builder.py # helper functions for building NGAP and NAS packets
│   ├── packet_sender.py # helper functions for sending NGAP packets
│   └── packet_type # definitions of used packet types, this heavily uses wireshark dissectors
│       └── ...
└── tests
    ├── conftest.py # basic test setup and fixture definition
    ├── Rel_16 # Rel 16 test case implementation
    ├── Rel_17 # Rel 17 test case implementation
    ├── Rel_18 # Rel 18 test case implementation
    └── test_config.yaml.default # default test configuration file, pls copy to 'test_config.yaml' and adapt to your environment
~~~

## Installation and Setup

### Docker/Podman (optional)

The scripts `run_docker.sh` or `run_podman.sh` can be used to build and run the test framework without having to handle dependencies and setup.

### Dependencies

The framework utilizes several external tools. Make sure to install the following packages or their pendants from your distribution:

- _curl_
  - _libcurl_
  - Debian/Ubuntu:
    - _libcurl4-openssl-dev_
    - _libssl-dev_ 
- _wireshark/tshark_ (Version >= 4.1.0)
  - make sure to set capabilities for dumpcap!
    ~~~sh
    sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap
    ~~~
  - make sure the current user is in the `wireshark` group!
    ~~~sh
    sudo usermod -a -G wireshark $USER
    ~~~
- _tcpreplay_
  - On Arch Linux
    - _libnetfilter\_queue_
  - On Debian/Ubuntu
    - _libnetfilter\_queue1_
  - make shure to set up capabilities and access rights
    ~~~sh
    sudo groupadd tcpreplay
    sudo usermod -a -G tcpreplay $(id -un) # adding the current user to the `tcpreplay` group
    sudo chmod 750 /usr/bin/tcpreplay
    sudo chown root:tcpreplay /usr/bin/tcpreplay
    sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/tcpreplay
    ~~~
- _tmux_

### Python dependencies

This project was tested with **python 3.10** and **python 3.11**.

Additional python packages are required for test execution. Those are listed in the [`requirements.txt`](requirements.txt) file  
and can be installed in two different ways.

Installation via virtual environment:
Python virtual environment via `venv` (or any other virtual environment):

~~~sh
# install pip if necessary (example for Debian / Ubuntu)
sudo apt install python3-pip
# install pythonX.XX-venv that matches your python version e.g. python3.10 and python3.10-venv
sudo apt install python3.10-venv
# change to directory where your python project resides
cd /path/to/your/python_project
# initialize and activate python-venv
python3.10 -m venv .venv
source .venv/bin/activate
# install further python packages
pip3 install -r requirements.txt
~~~

When you are done with your python project related tasks, you should deactivate `venv` or simply exit the current terminal session.

~~~sh
# execute where your python project lives
deactivate
~~~

Global installation:
Not recommended; some distributions do not allow this.

~~~sh
# install pip if necessary (example for Debian / Ubuntu)
sudo apt install python3-pip
# install further python packages
pip3 install -r requirements.txt
~~~

## Configuration

The framework can be configured through two config files with different intentions.

Since one of them is user-specific, a template file is provided for generating custom configuration. Copy it for first use with the following command and edit as you like.

~~~sh
cp tests/test_config.yaml.default tests/test_config.yaml
~~~

### `pyproject.toml`

This file is used to setup the python environment (dependencies, versions etc.). It's also used to edit the global pytest configuration for test execution under the `[tool.pytest.ini_options]` section. For debugging purposes pytests log level can be configured here via `log_cli_level` (default is INFO, more information is given by DEBUG).

### `tests/test_config.yaml`

This file is used to configure the test execution.
There are global settings to set up the installation paths of the (simulated) mobile network elements that are to be used (e.g. Open5GS or UERANSIM).

Additionally, this file defines which devices to use for which test. The device string must be derived from the class name of an available device-class-inherited Subclass.
As an example, the following section configures the test `TC_NAS_REPLAY_AMF` to be executed against an Open5GS SA instance for 5G core and UERANSIM for RAN and UE:

~~~yaml
test_TC_NAS_REPLAY_AMF:
  core: Open5gsCore
  ran: UeransimGnodeBopen5gs
  ue: UeransimUEopen5gs
~~~

If there is no test case specific config, the settings in the `fallback` section will be used if the parameter `--fallback` is applied.

~~~yaml
fallback:
  core: Open5gsCore
  ran: UeransimGnodeBopen5gs
  ue: UeransimUEopen5gs
  interface: lo
~~~

## Setup Open5GS, free5GC and UERANSIM

This framework includes the (incomplete) device drivers/interfaces for two common open source core implementations, Open5GS and free5GC.
Furthermore a device implementation for simulating the RAN and UE via UERANSIM can be used.
At the current state the drivers expect all those "devices" to be build from source, with the usual default config files applied and the executables and config files to be accessible via file system in the default locations of the build procedure. The device drivers do not work with a VM, container or network deployment or deployment as services (e.g. when installing via Package Managers), but could easily be adapted to do so.

Please make sure you add the default subscribers to Open5GS and/or free5GC or configure the core, RAN and UE configs to work properly together. A sanity check would be to manually boot up core, RAN and one UE and check if the UE registers and gets a PDU session.

## Test execution

The following commands can be used to execute all tests or a specific subset of them.

- run all tests using live capture:
  ~~~sh
  pytest
  ~~~

- run all tests using dummy devices and prerecorded pcaps (no live capture):
  ~~~sh
  pytest --dummy
  ~~~

- run all tests in a specific release:
  ~~~sh
  pytest tests/Rel_16
  ~~~

- run all tests of specific SCAS document (e.g. for a single network product):
  ~~~sh
  pytest tests/Rel_16/33512_AMF
  ~~~

- run specific test:
  ~~~sh
  pytest tests/Rel_16/33512_AMF/test_33512_g60_4_2_2_3_1.py
  ~~~

- run specific test, use fallback config and create report
  ~~~sh
  pytest --fallback --report tests/Rel_16/33512_AMF/test_33512_g60_4_2_2_3_1.py
  ~~~

- if you want to do interactive debugging with ipdb, add the -s parameter
  ~~~sh
  pytest -s tests/Rel_16/33512_AMF/test_33512_g60_4_2_2_3_1.py
  ~~~

- inject captures into `lo` interface to be used in a test:
  ~~~sh
  sudo tcpreplay -i lo capture.pcap
  ~~~

- run via docker/podman by replacing the `pytest` command with call to `run_docker.sh` or `run_podman.sh`:
  ~~~sh
  ./run_podman.sh tests/Rel_16/33512_AMF/test_33512_g60_4_2_2_3_2.py --dummy
  ~~~

## Test reporting

By passing the `--report` flag, one can create a log file, copies of all used pcaps and a web visualization of the test results. The report data can be found in the `reports/<execution date/time>` subfolder. 

### Test Visualization

The allure package can be used for test report visualization as an optional dependency.
Allure reporting will automatically be activated if the `--report` flag is applied.

The python-allure package gets installed via `requirements.txt` but in order to run the allure report server you have to install the package for your distribution.

- https://allurereport.org/docs/gettingstarted-installation/

- start allure server to view results in browser:
~~~sh
allure serve reports/<execution date/time>/allure
~~~
