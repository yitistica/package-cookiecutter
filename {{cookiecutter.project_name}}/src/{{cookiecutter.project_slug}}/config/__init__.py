"""
here imports and parses the needed configurations;
"""

from meta import Paths
from utils import load_yaml

app_configs = load_yaml(Paths.configs)
