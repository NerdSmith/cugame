import os
from functools import partial

from PySide6.QtGui import QAction, QPixmap, QColor
from PySide6.QtWidgets import QLabel, QMessageBox

from direction import Direction
from PicBtn import PicButton
from level import LevelController, Level


class UIGameController:
    def __init__(self, ui):
        self.ui = ui
        self.lvl_controller: LevelController = None
        self.lvl_folder = "levels"
        self.ball_btns = []
        self.curr_ball = None

    def setup(self):
        filenames = []
        lvls_menu = self.ui.ui.menuBar.addMenu("&Levels")

        for filename in os.listdir(self.lvl_folder):
            filenames.append(filename)
            action = QAction(filename, self.ui)
            action.triggered.connect(partial(self.load_lvl, filename))
            lvls_menu.addAction(action)

        self.ui.ui.menuBar.addMenu(lvls_menu)

        self.setup_directions_btns()

    def setup_directions_btns(self):
        self.ui.ui.down_btn.clicked.connect(partial(self.dir_btn_triggered, Direction.DOWN))
        self.ui.ui.up_btn.clicked.connect(partial(self.dir_btn_triggered, Direction.UP))
        self.ui.ui.left_btn.clicked.connect(partial(self.dir_btn_triggered, Direction.LEFT))
        self.ui.ui.right_btn.clicked.connect(partial(self.dir_btn_triggered, Direction.RIGHT))

    def load_lvl(self, filename):
        lvl = Level()
        lvl.load_file(os.path.join(self.lvl_folder, filename))
        self.lvl_controller = LevelController(lvl)

        self.show()

    def show(self):
        if self.lvl_controller is not None:
            for i in reversed(range(self.ui.grid.count())):
                self.ui.grid.itemAt(i).widget().setParent(None)
            grid = self.lvl_controller.level.grid
            for r_idx in range(len(grid)):
                for c_idx in range(len(grid[r_idx])):
                    e = grid[r_idx][c_idx]
                    if isinstance(e, Level.Wall):
                        label = QLabel(self.ui)
                        pixmap = QPixmap('res/wall.jpeg')
                        label.setPixmap(pixmap)
                        self.ui.grid.addWidget(label, r_idx, c_idx)
                    elif isinstance(e, Level.ExitWall):
                        label = QLabel(self.ui)
                        pixmap = QPixmap('res/wall.jpeg')
                        p = self.change_color(pixmap, QColor(*self.hex_to_rgb(e.color)))
                        label.setPixmap(p)
                        self.ui.grid.addWidget(label, r_idx, c_idx)
                    elif isinstance(e, Level.Ball):
                        pixmap = QPixmap('res/ball.jpeg')
                        p = self.change_color(pixmap, QColor(*self.hex_to_rgb(e.color)))
                        pressed_pixmap = self.mark_pixmap(p)
                        ball = PicButton(p, p, pressed_pixmap)
                        ball.clicked.connect(partial(self.select_ball, e, ball))
                        if e == self.curr_ball:
                            ball.set_pressed()
                        self.ball_btns.append(ball)
                        self.ui.grid.addWidget(ball, r_idx, c_idx)

        self.ui.repaint()

    def change_color(self, pixmap: QPixmap, color):
        tmp = pixmap.toImage()
        for y in range(tmp.height()):
            for x in range(tmp.width()):
                if tmp.pixelColor(x, y) != QColor(255, 255, 255, 255):

                    tmp.setPixelColor(x, y, color)
        return QPixmap.fromImage(tmp)

    def mark_pixmap(self, pixmap):
        tmp = pixmap.toImage()
        for y in range(tmp.height()//3, 2*tmp.height()//3):
            for x in range(tmp.width()//3, 2*tmp.width()//3):
                tmp.setPixelColor(x, y, QColor(0, 0, 0, 255))
        return QPixmap.fromImage(tmp)

    def hex_to_rgb(self, hex):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i + 2], 16)
            rgb.append(decimal)

        return tuple(rgb)

    def select_ball(self, ball, ball_btn):
        for b in self.ball_btns:
            b.set_unpressed()
        ball_btn.set_pressed()
        self.curr_ball = ball
        self.ui.repaint()

    def dir_btn_triggered(self, direction):
        if self.curr_ball is not None:
            self.lvl_controller.move_ball(self.curr_ball, direction)
            self.show()

            if self.lvl_controller.check_win_cond():
                QMessageBox.about(self.ui, "Congratulations!!!", "Level passed")
