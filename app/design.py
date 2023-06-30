# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 480)
        MainWindow.setMinimumSize(QSize(300, 480))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #1a1a28;\n"
"    font-family: Rubik;\n"
"    font-size: 20pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.lb_temp = QLabel(self.centralwidget)
        self.lb_temp.setObjectName(u"lb_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_temp.sizePolicy().hasHeightForWidth())
        self.lb_temp.setSizePolicy(sizePolicy)
        self.lb_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lb_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setSpacing(10)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setContentsMargins(0, 0, -1, -1)
        self.btn_backspase = QPushButton(self.centralwidget)
        self.btn_backspase.setObjectName(u"btn_backspase")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_backspase.sizePolicy().hasHeightForWidth())
        self.btn_backspase.setSizePolicy(sizePolicy2)
        self.btn_backspase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backspase.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace_FILL1_wght400_GRAD0_opsz481.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspase.setIcon(icon1)
        self.btn_backspase.setIconSize(QSize(40, 40))

        self.layout_buttons.addWidget(self.btn_backspase, 0, 2, 1, 1)

        self.btn_CE = QPushButton(self.centralwidget)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy2.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy2)
        self.btn_CE.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_CE.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_CE, 0, 0, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)
        self.btn_C.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_C.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_C, 0, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_0.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calc.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_calc, 4, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_point.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_point, 4, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #1e2434;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #51c9dc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3db5c8;\n"
"}")

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_div.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_div, 1, 3, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sub.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_sub, 3, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mul.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")
        self.btn_mul.setIconSize(QSize(20, 20))
        self.btn_mul.setCheckable(False)

        self.layout_buttons.addWidget(self.btn_mul, 2, 3, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_plus, 4, 3, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_neg.setStyleSheet(u"QPushButton {\n"
"    background-color: #51c9dc;\n"
"    border-radius: 10px;\n"
"	border: none\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e2434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #282e3e;\n"
"}")

        self.layout_buttons.addWidget(self.btn_neg, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.btn_backspase.setText("")
#if QT_CONFIG(shortcut)
        self.btn_backspase.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_CE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)

        for sc in ('=', 'Enter', 'Return'):
                QShortcut(sc, self.btn_calc).activated.connect(self.btn_calc.animateClick)

#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)

        for sc in (',', '.'):
                QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)

#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
    # retranslateUi

