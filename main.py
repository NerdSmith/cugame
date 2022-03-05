import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFrame

from ui_gui import Ui_MainWindow
from ui_game_controller import UIGameController


class Cugame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.grid = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_field()
        self.show()

        self.ui_game_controller = UIGameController(self)
        self.ui_game_controller.setup()

    def setup_field(self):
        self.ui.field = QFrame(self.ui.main_frame)
        self.ui.field.setObjectName(u"field")
        self.ui.field.setMinimumSize(QSize(400, 400))
        self.ui.field.setFrameShape(QFrame.StyledPanel)
        self.ui.field.setFrameShadow(QFrame.Raised)

        self.grid = QGridLayout()
        self.ui.field.setLayout(self.grid)

def main():
    app = QApplication(sys.argv)
    window = Cugame()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()