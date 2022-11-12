"""
Assuming the repo relative structure:
project:
    configurations:
        default templates;
    src:
        config:
"""
import os
from enum import Enum

# [auto generated]
# (parsed) configuration dir path:
_PARSE_CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))

# source code dir path:
_SRC_DIR = os.path.dirname(os.path.dirname(_PARSE_CONFIG_DIR))

# project dir path:
_PROJECT_DIR = os.path.dirname(_SRC_DIR)

# default configurations files dir:
_CONFIGURATION_SUB_DIR_NAME = 'configurations'
_CONFIGURATIONS_DIR = os.path.join(_PROJECT_DIR, _CONFIGURATION_SUB_DIR_NAME)


class Paths(Enum):
    project = _PROJECT_DIR
    configs = _CONFIGURATIONS_DIR
    src = _SRC_DIR
    configured = _PARSE_CONFIG_DIR

    @property
    def path(self):
        return self.value


# do not assume configurations come from one place, could be config-map;