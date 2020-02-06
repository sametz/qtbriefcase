from PySide2.QtCore import QObject
from PySide2.QtCore import Slot as pyqtSlot


class Controller(QObject):
    """Interprets signals from the View that request a change to the Model.

    For this toy example, it seems to me that the Controller could be omitted
    and embedded directly into the Model. However, a more complicated example
    may require separation of concerns. For example, if the pysides GUI was
    replaced by another GUI, the model should not be affected (the model and
    the view should not be aware of each other's existence).
    """
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(float)
    def change_base(self, value):
        self._model.base = value

    @pyqtSlot(float)
    def change_exp(self, value):
        self._model.exp = value
