"""Module contains example snippets for a generic device implementation"""
import logging
import sys
import time

import keyring
import paramiko
import pexpect
import sshtunnel

from scas.device_interfaces.device import ActionKey, Device
from scas.device_interfaces.device_config import ConfigKey, DeviceConfig
from scas.capture.capture import Capture, CaptureTarget
from scas.capture.local_file_capture import LocalFileCapture
from scas.logger import LOGGER

# paramiko shall not spam our output, unless it is important
logging.getLogger("paramiko").setLevel(logging.WARNING)

JUMPHOST_IP = "10.86.89.70"
JUMPHOST_ADDRESS = (JUMPHOST_IP, 22)

# prepare keyring: python3 -m keyring set vendor jumphost_user -> enter password


def get_jumphost():
    """returns a SSHClient instance that is connected to the jumphost
    """
    jumphost = paramiko.SSHClient()
    # AutoAddPolicy is bad, you should verify the public key!
    jumphost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jumphost.connect(JUMPHOST_IP, username='jumphost_user',
                     password=keyring.get_password('vendor', 'jumphost_user_pw'))
    return jumphost  # the caller is responsible for closing the connection!


def execute_on_host(command):
    """Executes a shell command on a host behind the jumphost.
    The command must return/exit otherwise this function will run forever!

    Args:
        command (str): the command to be executed
    """
    jumphost = get_jumphost()

    sftp = jumphost.open_sftp()

    # in this example we temporarily use the jumphosts private key to access the host
    with sftp.open(".ssh/id_rsa") as key_file:
        pkey = paramiko.RSAKey.from_private_key(key_file)

    channel = jumphost.get_transport().open_channel(
        "direct-tcpip", ("172.24.0.4", 22), JUMPHOST_ADDRESS)

    host = paramiko.SSHClient()
    # AutoAddPolicy is bad, you should verify the public key!
    host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host.connect("172.24.0.4", username="host_user", pkey=pkey, sock=channel)

    LOGGER.info("Excecuting command on the host: %s", command)
    _, stdout, _ = host.exec_command(command)
    stdout.channel.recv_exit_status()  # this is blocking

    LOGGER.debug("stdout: %s", stdout.read().decode())

    host.close()
    jumphost.close()


def execute_on_host_with_custom_shell(command):
    """Executes a command on a host behind the jumphost.
    Cause this host spawns a custom cli/shell, normal ssh clients do not work. Therefore we handle
    stdin/stdout ourselfs.
    The command must return/exit otherwise this function will run forever!

    Args:
        command (str): the command to be executed
    """
    jumphost = get_jumphost()

    channel = jumphost.get_transport().open_channel(
        "direct-tcpip", ("10.155.150.13", 22), JUMPHOST_ADDRESS)

    weird_host = paramiko.SSHClient()
    # AutoAddPolicy is bad, you should verify the public key!
    weird_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # this time we connect by providing a password, see execute_on_host for private key access
    weird_host.connect("10.155.150.13", username='weird_host_user',
                       password=keyring.get_password('vendor', 'weird_host_user_pw'), sock=channel)

    # exec command does not work because there is no normal shell spawning for user weird_host_user
    stdin, stdout, _stderr = weird_host.exec_command("", get_pty=True)

    # wait for custom shell/cli to be ready
    while line := stdout.readline():
        if "weird_host_user connected" in line:
            break

    # exec command by streaming it to stdin with \r\n for enter
    stdin.write(f"{command}\r\n")

    # consume first line, this was our command
    stdout.readline()

    result = []

    # wait to return to cli, collect stdout
    while line := stdout.readline():
        # this is the custom command prompt that will appear after the command exited
        if "weird_host_user@weird_host#" in line:
            break
        result.append(line.replace("\r\n", ""))
        # print(result[-1])


def get_traces_sftp_host_behind_jumphost():
    """Connecting to sftp via ssh jumphost was problematic.
    We built this tunnel by binding the remote sftp address through the ssh tunnel to a local port.
    Then we instrument the pexpect library to communicate with this local port aka the sftp server.
    """
    host_ip = "10.155.150.13"
    host_sftp_addr = (host_ip, 9023)

    ssh_newkey = r'Are you sure you want to continue connecting \(yes/no'

    with sshtunnel.open_tunnel(
        JUMPHOST_ADDRESS,
        ssh_username="jumphost_user",
        ssh_password=keyring.get_password('vendor', 'jumphost_user_pw'),
        remote_bind_address=host_sftp_addr,
        local_bind_address=('127.0.0.1', 10023)
    ) as _:
        logging.info("Spawn sftp process")
        sftp_proc = pexpect.spawn("sftp -P 10023 host_sftp_user@127.0.0.1")

        i = sftp_proc.expect([pexpect.TIMEOUT, ssh_newkey, '[Pp]assword: '])
        match i:
            case 0:
                LOGGER.error("SSH ERROR: %s\n%s", sftp_proc.before, sftp_proc.after)
                sys.exit()
            case 1:
                sftp_proc.sendline('yes')
                sftp_proc.expect('[Pp]assword: ')

        # Sending password
        sftp_proc.sendline(keyring.get_password("vendor", "host_sftp_user"))

        i = sftp_proc.expect("sftp>")

        sftp_proc.sendline("chdir traces")

        i = sftp_proc.expect("sftp>")

        sftp_proc.sendline("mget *")

        i = sftp_proc.expect("sftp>")

        print(sftp_proc.before.decode("utf-8"))


class GenericVendorNRFCapture(Capture):
    """Class that fraps functionality to capture pcaps at a generic vendor NRF
    """
    def record_event(self, event=None, timeout_sec=None, continue_after_event_sec=None):
        """Manages event recording at the  NRF and copies the results to the local machine
        for further analysis
        """
        LOGGER.info("Connecting to host...")
        jumphost = get_jumphost()

        # we temporarily use the jumphosts private key to access the host
        with jumphost.open_sftp() as jumphost_sftp:
            with jumphost_sftp.open(".ssh/id_rsa") as key_file:
                pkey = paramiko.RSAKey.from_private_key(key_file)

        channel = jumphost.get_transport().open_channel(
            "direct-tcpip", ("172.24.0.4", 22), JUMPHOST_ADDRESS)

        host = paramiko.SSHClient()
        # AutoAddPolicy is bad, you should verify the public key!
        host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host.connect("172.24.0.4", username="host_user", sock=channel,
                     pkey=pkey, auth_timeout=10, banner_timeout=10)
        LOGGER.info("Connecting to host... Done!")
        LOGGER.info("Calling tcpdump...")

        # start tcpdump to trace local traffic (e.g. SBI traffic)
        _, stdout, _ = host.exec_command(
            "sudo tcpdump -i any host 106.2.4.80 -w /tmp/nrf.pcap &")
        stdout.channel.recv_exit_status()  # Blocking call

        # this event must be blocking!
        # otherwise tcpdump will get killed and does not capture the events traffic
        event()

        LOGGER.info("Killing tcpdump...")

        time.sleep(2)  # wait a little before killing tcp dump

        # this is not nice, but receiving the pid and trying to kill the process via pid did not
        # work sometimes... this does always work but depends on the pcaps name and path
        _, stdout, _ = host.exec_command(
            "sudo kill $(ps aux | grep '/tmp/nrf.pcap' | awk '{print $2}')")
        stdout.channel.recv_exit_status()  # Blocking call

        # let host user own the capture file
        _, stdout, _ = host.exec_command("sudo chown host:host /tmp/nrf.pcap")
        stdout.channel.recv_exit_status()  # Blocking call

        LOGGER.info("Fetching nrf.pcap from host...")
        with host.open_sftp() as host_sftp:
            # because we setup the channel for the jumphost, the pcap will directly moved to our
            # test machine.
            host_sftp.get("/tmp/nrf.pcap", "/tmp/nrf.pcap")

        host.close()
        jumphost.close()

        return LocalFileCapture() \
            .set_capture_file("/tmp/nrf.pcap") \
            .set_include_raw(True) \



class GenericVendorCore(Device):
    """Generic vendor core implementation"""
    def __init__(self):
        super().__init__()
        self.config = GenericVendorConfig()

    def setup(self):
        return

    def start(self):
        # connect via jumphost and start the core if it is not running already
        return

    def stop(self):
        # connect via jumphost and start the core if it is not running already
        return

    def perform(self, action: ActionKey, **kwargs):
        match action:
            case ActionKey.NRF_REGISTRATION:
                requester_nf_type = kwargs['requester_nf_type']
                requester_nf_ip_addr = kwargs['requester_nf_ip_addr']
                requester_nf_instance_id = kwargs['requester_nf_instance_id']
                # requester_nf_nssais_sst = kwargs['requester_nf_nssais_sst']
                # for simplicity we assume sst 1 (= eMBB)
                requester_nf_nssais_sd = kwargs['requester_nf_nssais_sd']

                data = (
                    f'{{"nfInstanceId":"{requester_nf_instance_id}", '
                    f'"nfType":"{requester_nf_type}", "nfStatus":"REGISTERED", '
                    f'"ipv4Addresses":["{requester_nf_ip_addr}"], '
                    f'"sNssais":[{{"sst":1,"sd":"{requester_nf_nssais_sd}"}}],'
                    f'"allowedNssais":[{{"sst":1,"sd":"{requester_nf_nssais_sd}"}}]}}')
                #                                                       bracket hell xD
                curl_command = (
                    f'curl --http2-prior-knowledge -X PUT -H '
                    f'"User-Agent: {requester_nf_type}" -H "Content-Tye: application/json"'
                    f' -H "Accept: application/json" -d \'{data}\' '
                    f'"http://{self.config.read(ConfigKey.NRF_IP)}:'
                    f'{self.config.read(ConfigKey.NRF_PORT)}/nnrf-nfm/v1/'
                    f'nf-instances/{requester_nf_instance_id}"')
                execute_on_host(curl_command)
            case ActionKey.NRF_DISCOVERY:
                requester_nf_type = kwargs['requester_nf_type']
                requester_nf_nssais_sd = kwargs['requester_nf_nssais_sd']
                target_nf_type = kwargs['target_nf_type']

                curl_command = (
                    f'curl --http2-prior-knowledge -X GET -H "User-Agent: {requester_nf_type}"'
                    f' -H "Accept: application/json" "http://{self.config.read(ConfigKey.NRF_IP)}'
                    f':{self.config.read(ConfigKey.NRF_PORT)}/nnrf-disc/v1/'
                    f'nf-instances?target-nf-type={target_nf_type}&'
                    f'requester-nf-type={requester_nf_type}&requester_snssais[sst]=1&'
                    f'requester_snssais[sd]={requester_nf_nssais_sd}"')
                execute_on_host(curl_command)
            case _:
                raise RuntimeError(
                    f"Generic vendor interface does not implement action for key: {action}")

    def teardown(self):
        return

    def is_available(self) -> bool:
        # TODO we could ping or ssh to jumphost here (?)
        return True

    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        match target:
            case CaptureTarget.NRF:
                return GenericVendorNRFCapture()
        LOGGER.error("No capture class specified for %s!", target)
        return LocalFileCapture()


class GenericVendorConfig(DeviceConfig):
    """Class implementing the interfaces to the generic vendor configs"""
    core_config = None
    ordered_alg_list = []

    def __init__(self) -> None:
        pass

    def read(self, key: ConfigKey, **_kwargs):
        match key:
            case ConfigKey.AMF_INTEGRITY_PROT_ALG_ORDERED_LIST:
                # # Should be faster if the order only gets retrieved when the actual key is used.
                # # This means that in test the key needs to be assigned to a variable, otherwise
                # # the performance would be worse.

                # ordered_alg_list = []

                # # Slow Variant where alg order gets updated everytime the constructor gets
                # # called.
                # conn1 = Connection(host="10.86.89.70", user="jumphost_user",
                #     connect_kwargs={"password": keyring.get_password("vendor",
                # "jumphost_user_pw")})
                # conn2 = Connection(host="10.155.150.33", user="amf_user",
                #     connect_kwargs={"password": keyring.get_password("vendor", "amf_user_pw")},
                #     gateway=conn1)

                # result = conn2.run("propriatory_shell list_nia_algorithm all")
                # alg_list = result.stdout.split("\n")[2:-1]
                # alg_list.sort(key=lambda prio: prio[-1], reverse=True)

                # # List needs to be sorted once more, since 0 has the lowest priority
                # for i in alg_list:
                #     # The 29th position in the string is the nia #. It get's descended to fit
                #     # with the other cores.
                #     nia_number = int(i[29]) - 1
                #     if (i[-1] == "0"):
                #         ordered_alg_list.append('NIA'+str(nia_number))
                #      else:
                #         ordered_alg_list.insert(0,'NIA'+str(nia_number))

                # return ordered_alg_list

                # This is translated to the wireshark representation
                return [self.config_algorithm_by_name(alg) for alg in self.ordered_alg_list]
            case ConfigKey.UDM_SDM_OPENAPI_VERSION:
                return 2
            case ConfigKey.NRF_IP:
                return "106.2.4.80"
            case ConfigKey.NRF_PORT:
                return "80"
            case _:
                return None

    def write(self, key: ConfigKey, value):
        match key:
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_INTEGRITY:
                LOGGER.warning("Generic vendor does not provide this setting in the config.")
            case ConfigKey.SMF_NAS_SECURITY_INDICATION_CONFIDENTIALITY:
                LOGGER.warning("Generic vendor does not provide this setting in the config.")

    def compare(self, key: ConfigKey, to_value):
        return True
