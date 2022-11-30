from sqlalchemy import Column, Integer, String, DATE, DateTime, DECIMAL, Boolean, VARCHAR, CHAR
from sqlalchemy_utils import ChoiceType
from enum import Enum

from {{cookiecutter.project_slug}}.dal.relational.base import SysBase


class ChoiceSet(Enum):
    key_1 = "value_1"

ANOTHER_CHOICE_SET = [
    ('key_a', 'value_a'),
    ('key_b', 'value_b'),
    ('key_c', 'value_c'),
    ('key_d', 'value_d'),
]


class DataModel(SysBase):

    __tablename__ = 'sample_model'
    __table_args__ = {'comment': 'sth'}

    id = Column('id', Integer,  primary_key=True, autoincrement=True, comment='id')
    string = Column('cust_id', String(32), nullable=True, default=None, comment='string_col')
    date = Column('DATE', DATE, nullable=False, comment='date_col')
    date_time = Column('date_time', DateTime, nullable=False, comment='date_time_col')
    choice = Column('choice', ChoiceType(ChoiceSet, impl=String(2)), nullable=False, index=True, comment='choice_col')
    another_choice = Column('another_choice', ChoiceType(ANOTHER_CHOICE_SET), nullable=False,comment='sec_choice_col')
    decimal = Column('decimal', DECIMAL(12, 4), nullable=False, comment='decimal_col')
    bool = Column('bool', Boolean, nullable=False, server_default=True, comment='bool_col')
    char = Column('char', CHAR(2), nullable=False, comment='char_col')
    varchar = Column('varchar', VARCHAR(10), comment='varchar_col')