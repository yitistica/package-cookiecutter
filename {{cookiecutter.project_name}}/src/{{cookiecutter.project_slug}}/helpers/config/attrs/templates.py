"""
config template;
"""

from dataclasses import dataclass


@dataclass
class _ConfigBase(object):
    pass


@dataclass(kw_only=True)
class KwargsConfig(_ConfigBase):
    pass


@dataclass
class _ConnConfig(_ConfigBase):
    pass


@dataclass
class _RelationalConnConfig(_ConnConfig):
    host: str
    port: str


