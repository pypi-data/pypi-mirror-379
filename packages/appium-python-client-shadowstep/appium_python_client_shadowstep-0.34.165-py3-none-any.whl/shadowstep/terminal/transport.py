# shadowstep/terminal/transport.py

import logging
from typing import cast

import paramiko
from scp import SCPClient

# Configure the root logger (basic configuration)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Transport:
    """
    Allows you to connect to the server and execute terminal commands via ssh.
    And also copy files to the server and from server.
    Uses the paramiko and scp libraries for this

    This class include to attribute of Shadowstep class and allow use transport, like:
    app.transport.ssh.some_paramiko_method
    app.transport.scp.some_scp_method
    """
    def __init__(self, server: str, port: int, user: str, password: str):
        self.ssh = self._create_ssh_client(server=server, port=port, user=user, password=password)
        self.scp = SCPClient(cast(paramiko.Transport, self.ssh.get_transport()))

    @staticmethod
    def _create_ssh_client(server: str, port: int, user: str, password: str):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # noqa: S507
        client.connect(server, port, user, password)
        return client

