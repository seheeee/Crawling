# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(582, 470)
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(70, 360, 291, 61))
        font = QFont()
        font.setFamilies([u"\uc0c8\uad74\ub9bc"])
        font.setPointSize(15)
        self.login_btn.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 60, 251, 81))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 190, 251, 81))
        self.label_2.setFont(font1)
        self.id = QLineEdit(Form)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(190, 80, 201, 51))
        self.pw = QLineEdit(Form)
        self.pw.setObjectName(u"pw")
        self.pw.setGeometry(QRect(190, 200, 201, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\ub85c\uadf8\uc778", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc544\uc774\ub514", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638", None))
    # retranslateUi

