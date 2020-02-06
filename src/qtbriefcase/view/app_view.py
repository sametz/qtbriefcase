from pyqtgraph import PlotWidget
from PySide2.QtCore import Slot as pyqtSlot
from PySide2.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                               QDoubleSpinBox, QVBoxLayout, QWidget)


class Ui_MainWindow:
    """This class holds all the UI structral info:
    widgets and their organization.

    main_window is the parent app window, which handles hooking the GUI
    widgets up to the controller/model."""
    def setupUi(self, main_window):
        main_window.setObjectName('main_window')
        main_window.setWindowTitle('qt_mvc Demo')
        main_window.resize(800, 600)

        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName('centralwidget')
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setObjectName('centrallayout')
        self.top_bar_layout = QHBoxLayout()
        self.top_bar_layout.setObjectName('top_barlayout')
        self.base_label = QLabel('Base: ')
        self.base_entry = QDoubleSpinBox()
        self.base_entry.setObjectName('base_entry')
        self.exp_label = QLabel('Exponent: ')
        self.exp_entry = QDoubleSpinBox()
        self.exp_entry.setObjectName('exp_entry')
        self.base_entry.setValue(1)
        self.base_entry.setMinimum(0.1)
        self.exp_entry = QDoubleSpinBox()
        self.exp_entry.setValue(2)
        for widget in [self.base_label, self.base_entry,
                       self.exp_label, self.exp_entry]:
            self.top_bar_layout.addWidget(widget)
        self.central_layout.addLayout(self.top_bar_layout)
        self.plot = PlotWidget()
        self.central_layout.addWidget(self.plot)

        main_window.setCentralWidget(self.central_widget)

        # TODO: look into using connectSlotsByName
        # QtCore.QMetaObject.connectSlotsByName(main_window)


class MainWindow(QMainWindow):
    """The main app window. Embeds an instance of Ui_Mainwindow within it,
    and hooks its widgets up to the model and controller."""
    def __init__(self, model, controller):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # GUI update -> controller
        self._ui.base_entry.valueChanged.connect(self._controller.change_base)
        self._ui.exp_entry.valueChanged.connect(self._controller.change_exp)

        # model update -> GUI
        # TODO: although this is how the SO answer handled this, this breaks
        # separation of concern--the Model and View should be unaware of each
        # other. This should belong in the Controller, I think.
        self._model.value_changed.connect(self.on_value_changed)

        # initialize the plot
        self._ui.plot.plot(self._model.x, self._model.y)

    @pyqtSlot(tuple)
    def on_value_changed(self, xy):
        # Note: self._ui.plot.setData(x, y) does not work for some reason--
        # but this method worked in my pydnmr project.
        self._ui.plot.clearPlots()
        self._ui.plot.plot(*xy)
