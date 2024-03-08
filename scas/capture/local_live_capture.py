"""Module holding the capture implementation for local capturing"""
import inspect
import os
import signal
import time

from scas.capture.capture import Capture
from scas.capture.local_file_capture import LocalFileCapture
from scas.helper import run_local
from scas.logger import LOGGER


class BackgroundShark():
    """Class that instruments tshark (wireshark terminal implementation) for local live capture
      of network traffic.
    """
    def __init__(self, interface, dump_file, capture_filter=None):
        self.interface = interface
        self.output = dump_file
        # display filter are not supported with -w
        self.capture_filter = capture_filter

        self._process = None

    def start(self):
        """Starts a local live capture
        """
        LOGGER.debug("Starting BackgroundShark (%s)...", self.output)
        cmd = f"tshark -q -i {self.interface} -w {self.output}"
        if self.capture_filter:
            cmd += f" -f {self.capture_filter}"

        self._process = run_local("tshark", cmd, wait_for_stdout_lines=[
                                  "Capture started.", "Capturing on"], timeout=None)

    def stop(self):
        """Stops a local live capture (waits half a second before)
        """
        # XXX: sometimes it needs some extra time before shut down, otherwise we loose packets
        # maybe we should hack display_filter support in trigcap for a better solution
        time.sleep(0.5)
        LOGGER.debug("Killing BackgroundShark...")
        self._process.terminate()
        status = self._process.wait()
        LOGGER.debug(
            "Killing BackgroundShark... Done! (Return Code:%s)", status)

        os.chmod(self.output, int("664", 8))


class LocalLiveCapture(Capture):
    """Capture implementation for local live capture of network traffic on a given interface

    Args:
        Capture (_type_): _description_
    """
    def __init__(self, capture_file="/tmp/dump.pcap", interface="lo"):
        super().__init__()
        self._capture_file = capture_file
        self._interface = interface

    def set_interface(self, interface):
        """specifies the interface to capture from

        Args:
            interface (str): the interface name

        Returns:
            Capture: returns self for method chaining syntax
        """
        self._interface = interface
        return self

    def record_event(self, event=None, timeout_sec=None, continue_after_event_sec=None):
        """Records a pcap while executing an event. This event must be BLOCKING in order to capture
          something with tshark."""
        event_string = "Not specified"
        if event:
            event_string = str(inspect.getsourcelines(event)[0]).replace(
                '\\n', '').replace('[\'', '').replace('\']', '').strip()

        dump = BackgroundShark(self._interface, dump_file=self._capture_file)

        if timeout_sec:
            def timeout_handler(_signum, _frame):
                dump.stop()
                raise TimeoutError(
                    f"Timeout ({timeout_sec} sec) during event: {event_string}")

            signal.signal(signal.SIGALRM, timeout_handler)

        LOGGER.info("Recording...\n%s", event_string)
        dump.start()

        # start the alarm
        if timeout_sec:
            LOGGER.info("Registered timeout for %s seconds...", timeout_sec)
            signal.alarm(timeout_sec)

        try:
            # fire the event (MUST BE BLOCKING!)
            if event:
                event()

            # if we got past the event - cancel the alarm
            if timeout_sec:
                LOGGER.info("Registered timeout canceled...")
                signal.alarm(0)

            # should we wait after the event e.g. to receive reactions?
            if continue_after_event_sec:
                LOGGER.info("Waiting for %s seconds...",
                            continue_after_event_sec)
                time.sleep(continue_after_event_sec)
        except TimeoutError:
            pass

        dump.stop()
        LOGGER.info("Recording... Done!")

        return LocalFileCapture() \
            .set_capture_file(self._capture_file) \
            .set_include_raw(self._include_raw)
