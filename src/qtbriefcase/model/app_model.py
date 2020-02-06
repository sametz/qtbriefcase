import numpy as np
from PySide2.QtCore import QObject
from PySide2.QtCore import Signal as pyqtSignal


class Model(QObject):
    """Responsible for holding and managing the data/state of the simulation."""
    value_changed = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        # TODO: hard coding _base/_exp values here is a bad code smell.
        # There should be one code source for these values,
        # for initializing both the model and the view
        # (default values for QDoubleSpinBox entries).
        self._base = 1
        self._exp = 2
        self._x = np.linspace(0, 10, 800)
        self._update_y()

    def _update_y(self):
        self._y = (self._x * self._base) ** self._exp

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def update(self):
        # self._base = base
        # self._exp = exp
        self._update_y()

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value
        self.update()
        self.value_changed.emit((self._x, self._y))

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value
        self.update()
        self.value_changed.emit((self._x, self._y))
