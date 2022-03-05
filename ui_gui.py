# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiawcAtm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.field = QFrame(self.main_frame)
        self.field.setObjectName(u"field")
        self.field.setMinimumSize(QSize(400, 400))
        self.field.setFrameShape(QFrame.StyledPanel)
        self.field.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.field, 1, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.left_btn = QPushButton(self.frame_2)
        self.left_btn.setObjectName(u"left_btn")
        self.left_btn.setMinimumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(25)
        self.left_btn.setFont(font)

        self.gridLayout_2.addWidget(self.left_btn, 1, 1, 1, 1)

        self.right_btn = QPushButton(self.frame_2)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setMinimumSize(QSize(50, 50))
        self.right_btn.setFont(font)

        self.gridLayout_2.addWidget(self.right_btn, 1, 3, 1, 1)

        self.up_btn = QPushButton(self.frame_2)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setMinimumSize(QSize(50, 50))
        self.up_btn.setFont(font)

        self.gridLayout_2.addWidget(self.up_btn, 0, 2, 1, 1)

        self.down_btn = QPushButton(self.frame_2)
        self.down_btn.setObjectName(u"down_btn")
        self.down_btn.setMinimumSize(QSize(50, 50))
        self.down_btn.setFont(font)

        self.gridLayout_2.addWidget(self.down_btn, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 4, 1, 1)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 974, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_btn.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.right_btn.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.up_btn.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.down_btn.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
    # retranslateUi

