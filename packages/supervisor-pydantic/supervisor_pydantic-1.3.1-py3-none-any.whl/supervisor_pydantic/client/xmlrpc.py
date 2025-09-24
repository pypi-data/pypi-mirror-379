from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from xmlrpc.client import Fault, ServerProxy

from pydantic import BaseModel

from ..config import SupervisorConvenienceConfiguration

__all__ = ("SupervisorRemoteXMLRPCClient", "ProcessState", "SupervisorState", "SupervisorMethodResult", "ProcessInfo")


class ProcessState(Enum):
    STOPPED = 0
    STARTING = 10
    RUNNING = 20
    BACKOFF = 30
    STOPPING = 40
    EXITED = 100
    FATAL = 200
    UNKNOWN = 1000

    @classmethod
    def _missing_(cls, code):
        if isinstance(code, str):
            return getattr(cls, code)
        if code not in (0, 10, 20, 30, 40, 100, 200):
            return super().__init__(1000)
        raise ValueError(code)


class SupervisorState(Enum):
    FATAL = 2
    RUNNING = 1
    RESTARTING = 0
    SHUTDOWN = -1

    @classmethod
    def _missing_(cls, code):
        if isinstance(code, str):
            return getattr(cls, code)
        raise ValueError(code)


class SupervisorMethodResult(Enum):
    # duplicated from https://github.com/Supervisor/supervisor/blob/29eeb9dd55c55da2e83c5497d01f3a859998ecf9/supervisor/xmlrpc.py
    UNKNOWN_METHOD = 1
    INCORRECT_PARAMETERS = 2
    BAD_ARGUMENTS = 3
    SIGNATURE_UNSUPPORTED = 4
    SHUTDOWN_STATE = 6
    BAD_NAME = 10
    BAD_SIGNAL = 11
    NO_FILE = 20
    NOT_EXECUTABLE = 21
    FAILED = 30
    ABNORMAL_TERMINATION = 40
    SPAWN_ERROR = 50
    ALREADY_STARTED = 60
    NOT_RUNNING = 70
    SUCCESS = 80
    ALREADY_ADDED = 90
    STILL_RUNNING = 91
    CANT_REREAD = 92


class ProcessInfo(BaseModel):
    name: str
    group: str
    state: ProcessState
    description: str
    start: datetime
    stop: datetime
    now: datetime
    spawner: str = ""
    exitstatus: int
    logfile: str
    stdout_logfile: str
    stderr_logfile: str
    pid: int

    def running(self):
        return self.state in (ProcessState.RUNNING, ProcessState.STOPPING)

    def stopped(self):
        return self.state in (ProcessState.STOPPED, ProcessState.EXITED, ProcessState.FATAL)

    def done(self, ok_exitstatuses=None):
        ok_exitstatuses = ok_exitstatuses or (0,)
        return self.state in (ProcessState.STOPPED,) or (self.state == ProcessState.EXITED and self.exitstatus in ok_exitstatuses)

    def ok(self, ok_exitstatuses=None):
        ok_exitstatuses = ok_exitstatuses or (0,)
        return self.state in (
            # ProcessState.STARTING,
            ProcessState.RUNNING,
            ProcessState.STOPPING,
            ProcessState.STOPPED,
        ) or (self.state == ProcessState.EXITED and self.exitstatus in ok_exitstatuses)

    def bad(self, ok_exitstatuses=None):
        ok_exitstatuses = ok_exitstatuses or (0,)
        return self.state in (ProcessState.FATAL, ProcessState.UNKNOWN) or (
            self.state == ProcessState.EXITED and self.exitstatus not in ok_exitstatuses
        )


class SupervisorRemoteXMLRPCClient(object):
    """A light wrapper over the supervisor xmlrpc api: http://supervisord.org/api.html"""

    def __init__(self, cfg: SupervisorConvenienceConfiguration):
        self._cfg = cfg
        self._host = cfg.host
        self._port = int(cfg.port.split(":")[-1])
        self._protocol = cfg.protocol
        self._rpcpath = "/" + cfg.rpcpath if not cfg.rpcpath.startswith("/") else cfg.rpcpath
        self._rpcurl = self._build_rpcurl(username=cfg.username, password=cfg.password)
        self._client = ServerProxy(self._rpcurl)

    def _build_rpcurl(self, username: Optional[str], password: Optional[str]) -> str:
        # Forces http or https based on port, otherwise resolves to given protocol
        protocol = {80: "http", 443: "https"}.get(self._port, self._protocol)
        port = "" if self._port in {80, 443} else f":{self._port}"
        authentication = f"{username}:{password.get_secret_value()}@" if username and password else ""
        return f"{protocol}://{authentication}{self._host}{port}{self._rpcpath}"

    #######################
    # supervisord methods #
    #######################
    def getAllProcessInfo(self) -> List[ProcessInfo]:
        return [ProcessInfo(**_) for _ in self._client.supervisor.getAllProcessInfo()]

    def getState(self) -> SupervisorState:
        return SupervisorState(self._client.supervisor.getState()["statecode"])

    # def readLog(self):
    #     return self._client.supervisor.readLog(0, 0)

    def restart(self) -> SupervisorState:
        self._client.supervisor.restart()
        return self.getState()

    def shutdown(self) -> SupervisorState:
        self._client.supervisor.shutdown()
        return self.getState()

    ###################
    # process methods #
    ###################
    def getProcessInfo(self, name: str) -> ProcessInfo:
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")
        return self._getProcessInfoInternal(name)

    def _getProcessInfoInternal(self, name: str) -> ProcessInfo:
        return ProcessInfo(**self._client.supervisor.getProcessInfo(name))

    def readProcessLog(self, name: str):
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")
        return self._client.supervisor.readProcessLog(name, 0, 0)

    def readProcessStderrLog(self, name: str):
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")

        return self._client.supervisor.readProcessStderrLog()

    def readProcessStdoutLog(self, name: str):
        return self._client.supervisor.readProcessStdoutLog()

    def startAllProcesses(self) -> Dict[str, ProcessInfo]:
        # start all
        self._client.supervisor.startAllProcesses()
        return {name: self.getProcessInfo(name) for name in self._cfg.program}

    def startProcess(self, name: str) -> ProcessInfo:
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")
        try:
            if self._client.supervisor.startProcess(name):
                return self.getProcessInfo(name)
        except Fault as f:
            if f.faultCode == SupervisorMethodResult.ALREADY_STARTED.value:
                return self.getProcessInfo(name)
            if f.faultCode == SupervisorMethodResult.SPAWN_ERROR.value:
                return self.getProcessInfo(name)
            raise f
        return self.getProcessInfo(name)

    def stopAllProcesses(self) -> Dict[str, ProcessInfo]:
        # start all
        self._client.supervisor.stopAllProcesses()
        return {name: self.getProcessInfo(name) for name in self._cfg.program}

    def stopProcess(self, name: str) -> ProcessInfo:
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")
        return self._stopProcessInternal(name)

    def _stopProcessInternal(self, name: str) -> ProcessInfo:
        try:
            if self._client.supervisor.stopProcess(name):
                return self._getProcessInfoInternal(name)
        except Fault as f:
            if f.faultCode == SupervisorMethodResult.NOT_RUNNING.value:
                return self._getProcessInfoInternal(name)
            raise f
        return self._getProcessInfoInternal(name)

    def reloadConfig(self, start_new: bool = False) -> SupervisorState:
        added, changed, removed = self._client.supervisor.reloadConfig()[0]
        proc_infos = []
        for name in removed:
            proc_infos.append(self._stopProcessInternal(name))
        for name in changed:
            self._stopProcessInternal(name)
            proc_infos.append(self.startProcess(name))
        # Don't need to start as we'll do this separately
        for name in added:
            self._client.supervisor.addProcessGroup(name)
            if start_new:
                proc_infos.append(self.startProcess(name))
        return proc_infos

    # def signalAllProcesses(self, signal):
    #     return self._client.supervisor.signalAllProcesses()

    def signalProcess(self, name: str, signal):
        if name not in self._cfg.program:
            raise RuntimeError(f"Unknown process: {name}")
        return self._client.supervisor.signalProcess()
