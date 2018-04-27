# -*- coding: utf-8 -*-
from ..base import Base, Property


class Type(Base):
    """Base type"""


class Probability(Type, float):
    """Probability type.

    Same as float, but value must be between 0 and 1."""
    value = Property(float)

    def __new__(cls, value, *args, **kwargs):
        if not 0 <= value <= 1:
            raise ValueError("Probability must be between 0 and 1")
        return super().__new__(cls, value, *args, **kwargs)