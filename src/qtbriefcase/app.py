"""The executable file for the qt_briefcase_test app"""
import sys

from PySide2.QtWidgets import QApplication

from qtbriefcase.controller.controller import Controller
from qtbriefcase.model.app_model import Model
from qtbriefcase.view.app_view import MainWindow


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = Controller(self.model)
        self.main_view = MainWindow(self.model, self.main_controller)
        self.main_view.show()

def main():
    app = App(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
