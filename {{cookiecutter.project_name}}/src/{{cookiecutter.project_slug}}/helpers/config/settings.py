"""
one level bidict
"""
from enum import Enum
from enum import unique


def _check_mutable():
    pass


@unique
class Bidict(Enum):
    """
        {name_1:
        attr_1: b
        attr_2: c
        free:attr,
        ...}
        {name_2:
        attr_1: b
        attr_2: c}
    """
    def __init__(self, settings):
        pass

    @staticmethod
    def _parse_input(settings):
        schema = None

        for which, setting in settings.items():
            if not schema:
                schema = setting


    @classmethod
    def get(cls, attr_key, attr_value):
        return NotImplemented


