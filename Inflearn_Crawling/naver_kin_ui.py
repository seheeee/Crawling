# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'naver_kin.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(637, 534)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"\ub3cb\uc6c0"])
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.keyword_label = QLabel(Form)
        self.keyword_label.setObjectName(u"keyword_label")
        self.keyword_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.keyword_label)

        self.keyword = QLineEdit(Form)
        self.keyword.setObjectName(u"keyword")
        self.keyword.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.keyword)

        self.page_label = QLabel(Form)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.page_label)

        self.page = QLineEdit(Form)
        self.page.setObjectName(u"page")
        self.page.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.page)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font)

        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_bnt = QPushButton(Form)
        self.start_bnt.setObjectName(u"start_bnt")
        self.start_bnt.setFont(font)

        self.verticalLayout.addWidget(self.start_bnt)

        self.reset_bnt = QPushButton(Form)
        self.reset_bnt.setObjectName(u"reset_bnt")
        self.reset_bnt.setFont(font)

        self.verticalLayout.addWidget(self.reset_bnt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.save_bnt = QPushButton(Form)
        self.save_bnt.setObjectName(u"save_bnt")
        self.save_bnt.setFont(font)

        self.verticalLayout.addWidget(self.save_bnt)

        self.quit_bnt = QPushButton(Form)
        self.quit_bnt.setObjectName(u"quit_bnt")
        self.quit_bnt.setFont(font)

        self.verticalLayout.addWidget(self.quit_bnt)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#55aa00;\">\ub124\uc774\ubc84 \uc9c0\uc2dd\uc778 \ud06c\ub864\ub9c1</span></p></body></html>", None))
        self.keyword_label.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.page_label.setText(QCoreApplication.translate("Form", u"\ud398\uc774\uc9c0 \uc218", None))
        self.start_bnt.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c \uc2dc\uc791", None))
        self.reset_bnt.setText(QCoreApplication.translate("Form", u"\ub9ac\uc14b", None))
        self.save_bnt.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
        self.quit_bnt.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

