"""
config template;
"""
from abc import ABC
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Literal
import ipaddress


@dataclass
class _ConfigBase(ABC):
    """move this to base"""
    pass

    @classmethod
    def fields(cls):
        pass


@dataclass(kw_only=True)
class KwargsConfig(_ConfigBase):
    pass


@dataclass
class _ConnConfig(KwargsConfig):
    pass


class IPVersion(Enum):
    ipv4: str = 'ipv4'
    ipv6: str = 'ipv6'


@dataclass
class IP(KwargsConfig):
    _ip_version: Literal[IPVersion.ipv4, IPVersion.ipv6] = field(init=False)
    host: str
    port: Optional[int | str] = None

    def __post_init__(self):
        ip_version, host, port = self.validate(host=self.host, port=self.port)
        self._ip_version = ip_version
        self.host = host
        self.port = port

    @staticmethod
    def validate_host(host):

        ip_version = IPVersion.ipv4

        if host == 'localhost':
            pass
        else:
            _ip = ipaddress.ip_address(host)
            if isinstance(_ip, ipaddress.IPv6Address):
                ip_version = IPVersion.ipv6

        return ip_version, host

    @staticmethod
    def validate_port(port):

        if port is not None:
            port = int(port)

            if not (1 <= port <= 65535):
                raise ValueError(f"port `{port}` is not valid.")

        return port

    @staticmethod
    def validate(host, port=None):

        ip_version, host = IP.validate_host(host=host)
        port = IP.validate_port(port=port)

        return ip_version, host, port

    @property
    def ip_address(self):
        address = f"{self.host}"
        if self.port is not None:
            address = f"{address}:{self.port}"

        return address

    def if_ipv4(self):
        if self._ip_version == IPVersion.ipv4:
            return True
        else:
            return False

    def if_ipv6(self):
        if self._ip_version == IPVersion.ipv6:
            return True
        else:
            return False


@dataclass
class RelationalConnConfig(_ConfigBase):
    ip: IP
    database: str = 'sqlite'



