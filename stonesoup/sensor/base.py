# -*- coding: utf-8 -*-
from abc import abstractmethod

from ..base import Base, Property
from ..models import MeasurementModel


class Sensor(Base):
    """Sensor base class

    A sensor object that opperates according to a given
    :class:`~.MeasurementModel`.
    """

    measurement_model = Property(
        MeasurementModel, default=None, doc="Measurement model")

    @abstractmethod
    def gen_measurement(**kwargs):
        """Generate a measurement"""
        raise NotImplementedError
