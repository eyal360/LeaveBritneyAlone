# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbjYOGe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QLocale

import Britney_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(871, 660)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(56, 56, 56);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.link_text = QTextEdit(self.centralwidget)
        self.link_text.setObjectName(u"link_text")
        self.link_text.setGeometry(QRect(90, 130, 701, 71))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(7)
        self.link_text.setFont(font)
        self.link_text.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.link_text.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	background-color: rgb(202, 202, 202);\n"
"	color: rgb(56, 56, 56);\n"
"}\n"
"")
        self.link_text.setLocale(QLocale(QLocale.Duala, QLocale.Cameroon))
        self.link_text.setFrameShape(QFrame.WinPanel)
        self.link_text.setFrameShadow(QFrame.Plain)
        self.link_text.setLineWidth(5)
        self.link_text.setMidLineWidth(5)
        self.link_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.link_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.link_text.setAutoFormatting(QTextEdit.AutoBulletList)
        self.link_text.setTabChangesFocus(True)
        self.link_text.setTabStopWidth(80)
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(190, 250, 511, 271))
        self.start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 30pt \"Segoe UI Semibold\";\n"
"	border-radius: 60px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.headline_brit = QLabel(self.centralwidget)
        self.headline_brit.setObjectName(u"headline_brit")
        self.headline_brit.setGeometry(QRect(170, 0, 121, 91))
        self.headline_brit.setStyleSheet(u"image: url(:/britney/britney.png);")
        self.information_lbl = QLabel(self.centralwidget)
        self.information_lbl.setObjectName(u"information_lbl")
        self.information_lbl.setGeometry(QRect(100, 600, 721, 41))
        self.information_lbl.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(170, 255, 255);\n"
"color: rgb(255, 255, 127);")
        self.information_lbl.setAlignment(Qt.AlignCenter)
        self.information_lbl.setTextInteractionFlags(Qt.NoTextInteraction)
        self.restart_btn = QPushButton(self.centralwidget)
        self.restart_btn.setObjectName(u"restart_btn")
        self.restart_btn.setGeometry(QRect(10, 600, 61, 51))
        self.restart_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restart_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/britney/restart.png);\n"
"	border: 0px solid;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"}")
        self.headline_lbl = QLabel(self.centralwidget)
        self.headline_lbl.setObjectName(u"headline_lbl")
        self.headline_lbl.setGeometry(QRect(270, 20, 371, 51))
        self.headline_lbl.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.mid_brit = QLabel(self.centralwidget)
        self.mid_brit.setObjectName(u"mid_brit")
        self.mid_brit.setGeometry(QRect(240, 170, 421, 351))
        self.mid_brit.setStyleSheet(u"image: url(:/britney/britney.png);")
        self.loader_lbl = QLabel(self.centralwidget)
        self.loader_lbl.setObjectName(u"loader_lbl")
        self.loader_lbl.setGeometry(QRect(210, 100, 571, 481))
        MainWindow.setCentralWidget(self.centralwidget)
        self.start_btn.raise_()
        self.mid_brit.raise_()
        self.loader_lbl.raise_()
        self.link_text.raise_()
        self.headline_brit.raise_()
        self.information_lbl.raise_()
        self.restart_btn.raise_()
        self.headline_lbl.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.link_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.link_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"                                               \u05dc\u05d9\u05e0\u05e7 \u05dc\u05e4\u05d5\u05e1\u05d8", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"\u05d7\u05dc\u05e5 \u05ea\u05d2\u05d5\u05d1\u05d5\u05ea", None))
        self.headline_brit.setText("")
        self.information_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffff7f;\">\u05e7\u05d5\u05d1\u05e5 \u05d4\u05d0\u05e7\u05e1\u05dc \u05d9\u05d9\u05e9\u05de\u05e8 \u05d1\u05d0\u05d5\u05ea\u05d4 \u05d4\u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05e9\u05d1\u05d4 \u05e0\u05de\u05e6\u05d0\u05ea \u05d4\u05d0\u05e4\u05dc\u05d9\u05e7\u05e6\u05d9\u05d4</span></p></body></html>", None))
        self.restart_btn.setText("")
        self.headline_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Leave britney Alone..!</span></p></body></html>", None))
        self.mid_brit.setText("")
        self.loader_lbl.setText("")
    # retranslateUi