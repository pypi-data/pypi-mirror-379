from logging import getLogger
from pathlib import Path
from typing import List, Optional

from pydantic import Field, PrivateAttr, SecretStr, field_serializer, field_validator, model_validator

from .base import HostPort, Signal, SupervisorLocation, UnixUserName
from .inet_http_server import InetHttpServerConfiguration
from .rpcinterface import RpcInterfaceConfiguration
from .supervisor import SupervisorConfiguration

__all__ = ("SupervisorConvenienceConfiguration", "load_convenience_config")

_log = getLogger(__name__)


class SupervisorConvenienceConfiguration(SupervisorConfiguration):
    """Convenience layer, settings that MUST be set when running via convenience API"""

    _pydantic_path: Path = PrivateAttr(default="pydantic.json")

    ############
    # programs #
    ############
    # autostart = False
    # autorestart = False
    startsecs: Optional[int] = Field(
        default=1,
        description="The total number of seconds which the program needs to stay running after a startup to consider the start successful (moving the process from the STARTING state to the RUNNING state). Set to 0 to indicate that the program needn’t stay running for any particular amount of time. Even if a process exits with an “expected” exit code (see exitcodes), the start will still be considered a failure if the process exits quicker than startsecs.",
    )
    startretries: Optional[int] = Field(
        default=None,
        description="The number of serial failure attempts that supervisord will allow when attempting to start the program before giving up and putting the process into an FATAL state. After each failed restart, process will be put in BACKOFF state and each retry attempt will take increasingly more time.",
    )
    exitcodes: Optional[List[int]] = Field(
        default=[0],
        description="The list of “expected” exit codes for this program used with autorestart. If the autorestart parameter is set to unexpected, and the process exits in any other way than as a result of a supervisor stop request, supervisord will restart the process if it exits with an exit code that is not defined in this list.",
    )
    stopsignal: Optional[Signal] = Field(
        default="TERM",
        description="The signal used to kill the program when a stop is requested. This can be specified using the signal’s name or its number. It is normally one of: TERM, HUP, INT, QUIT, KILL, USR1, or USR2.",
    )
    stopwaitsecs: Optional[int] = Field(
        default=30,
        description="The number of seconds to wait for the OS to return a SIGCHLD to supervisord after the program has been sent a stopsignal. If this number of seconds elapses before supervisord receives a SIGCHLD from the process, supervisord will attempt to kill it with a final SIGKILL.",
    )
    stopasgroup: Optional[bool] = Field(
        default=True,
        description="If True, the stopsignal will be sent to the process group of the program, rather than just the program itself. This is useful for programs that spawn child processes.",
    )
    killasgroup: Optional[bool] = Field(
        default=True,
        description="If True, the stopsignal will be sent to the process group of the program, rather than just the program itself. This is useful for programs that spawn child processes.",
    )

    ####################
    # inet_http_server #
    ####################
    # port not optional
    port: HostPort = Field(
        default="*:9001",
        description="A TCP host:port value or (e.g. 127.0.0.1:9001) on which supervisor will listen for HTTP/XML-RPC requests. supervisorctl will use XML-RPC to communicate with supervisord over this port. To listen on all interfaces in the machine, use :9001 or *:9001. Please read the security warning above.",
    )
    username: Optional[UnixUserName] = Field(default=None, description="The username required for authentication to the HTTP/Unix Server.")
    password: Optional[SecretStr] = Field(
        default=None,
        description="The password required for authentication to the HTTP/Unix server. This can be a cleartext password, or can be specified as a SHA-1 hash if prefixed by the string {SHA}. For example, {SHA}82ab876d1387bfafe46cc1c8a2ef074eae50cb1d is the SHA-stored version of the password “thepassword”. Note that hashed password must be in hex format.",
    )

    #################
    # rpc_interface #
    ###################
    rpcinterface_factory: str = Field(
        default="supervisor.rpcinterface:make_main_rpcinterface",
        description="pkg_resources “entry point” dotted name to your RPC interface’s factory function.",
    )

    #########
    # Other #
    #########
    local_or_remote: Optional[SupervisorLocation] = Field(
        default="local",
        description="Location of supervisor, either local for same-machine or remote. If same-machine, communicates via Unix sockets by default, if remote, communicates via inet http server",
    )
    host: str = Field(
        default="localhost",
        description="Hostname of the supervisor host. Used by the XMLRPC client",
    )
    protocol: str = Field(
        default="http",
        description="Protocol of the supervisor XMLRPC HTTP API. Used by the XMLRPC client",
    )
    rpcpath: str = Field(
        default="/RPC2",
        description="Path for supervisor XMLRPC HTTP API. Used by the XMLRPC client",
    )

    #########
    # Other #
    #########
    command_timeout: int = Field(
        default=60,
        description="Timeout for convenience commands sent to the supervisor, in seconds",
    )

    @field_serializer("exitcodes", when_used="json")
    def _dump_exitcodes(self, v):
        if v:
            return ",".join(str(_) for _ in v)
        return None

    @field_validator("exitcodes", mode="before")
    @classmethod
    def _load_exitcodes(cls, v):
        if isinstance(v, str):
            v = v.split(",")
        if isinstance(v, list):
            return [int(_) for _ in v]
        return v

    @field_serializer("password", when_used="json")
    def _dump_password(self, v):
        return v.get_secret_value() if v else None

    def _write_self(self):
        # TODO make config driven
        self.write()
        _log.info(f"Writing model json: {self._pydantic_path}")
        Path(self._pydantic_path).write_text(self.model_dump_json(exclude_unset=True))

    @model_validator(mode="after")
    def _setup_convenience_defaults(self):
        """Method to overload configuration with values needed for the setup
        of convenience tasks that we construct"""
        if self.local_or_remote == "remote" and self.port.startswith(("localhost", "127.0.0.1")):
            _log.warning("Supervisor binds only to loopback (localhost/127.0.0.1), but asked for remote")
        if self.local_or_remote == "remote" and self.host.startswith(("localhost", "127.0.0.1")):
            _log.warning("Supervisor client expecting hostname, got localhost/127.0.0.1")

        # inet_http_server
        if not self.inet_http_server:
            self.inet_http_server = InetHttpServerConfiguration()

        self.inet_http_server.port = self.port
        self.inet_http_server.username = self.username
        self.inet_http_server.password = self.password

        self.supervisorctl.serverurl = f"{self.protocol}://{self.host}:{self.port.split(':')[-1]}/"

        # rpcinterface
        if not self.rpcinterface:
            self.rpcinterface = {"supervisor": RpcInterfaceConfiguration()}
        self.rpcinterface["supervisor"].rpcinterface_factory = self.rpcinterface_factory

        # supervisord
        self.supervisord.nodaemon = False
        self.supervisord.identifier = "supervisor"

        # programs
        for name, config in self.program.items():
            config.autostart = False
            config.autorestart = False
            config.startsecs = self.startsecs
            config.startretries = self.startretries
            config.exitcodes = self.exitcodes
            config.stopsignal = self.stopsignal
            config.stopwaitsecs = self.stopwaitsecs
            config.stopasgroup = self.stopasgroup
            config.killasgroup = self.killasgroup
            config.stdout_logfile = self.working_dir / name / "output.log"
            config.stderr_logfile = self.working_dir / name / "error.log"

        # other
        if str(self.working_dir) not in str(self._pydantic_path):
            self._pydantic_path = self.working_dir / "pydantic.json"
        return self


load_convenience_config = SupervisorConvenienceConfiguration.load
