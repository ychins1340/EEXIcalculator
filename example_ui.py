# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1258, 883)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(1240, 825))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1221, 806))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 40, 311, 771))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(160, 650, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.MCR_ME = QtWidgets.QLineEdit(self.widget)
        self.MCR_ME.setGeometry(QtCore.QRect(190, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.MCR_ME.setFont(font)
        self.MCR_ME.setObjectName("MCR_ME")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.DWT = QtWidgets.QLineEdit(self.widget)
        self.DWT.setGeometry(QtCore.QRect(190, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.DWT.setFont(font)
        self.DWT.setObjectName("DWT")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(0, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.LWT = QtWidgets.QLineEdit(self.widget)
        self.LWT.setGeometry(QtCore.QRect(190, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.LWT.setFont(font)
        self.LWT.setObjectName("LWT")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.VS_EEDI = QtWidgets.QLineEdit(self.widget)
        self.VS_EEDI.setGeometry(QtCore.QRect(190, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.VS_EEDI.setFont(font)
        self.VS_EEDI.setText("")
        self.VS_EEDI.setObjectName("VS_EEDI")
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setGeometry(QtCore.QRect(10, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.PS_EEDI = QtWidgets.QLineEdit(self.widget)
        self.PS_EEDI.setGeometry(QtCore.QRect(190, 260, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.PS_EEDI.setFont(font)
        self.PS_EEDI.setText("")
        self.PS_EEDI.setObjectName("PS_EEDI")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(10, 300, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setGeometry(QtCore.QRect(10, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.SFC_ME_in = QtWidgets.QLineEdit(self.widget)
        self.SFC_ME_in.setGeometry(QtCore.QRect(190, 310, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.SFC_ME_in.setFont(font)
        self.SFC_ME_in.setText("")
        self.SFC_ME_in.setObjectName("SFC_ME_in")
        self.SFC_AE_in = QtWidgets.QLineEdit(self.widget)
        self.SFC_AE_in.setGeometry(QtCore.QRect(190, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.SFC_AE_in.setFont(font)
        self.SFC_AE_in.setText("")
        self.SFC_AE_in.setObjectName("SFC_AE_in")
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setGeometry(QtCore.QRect(10, 400, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.PTO_in = QtWidgets.QLineEdit(self.widget)
        self.PTO_in.setGeometry(QtCore.QRect(190, 410, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.PTO_in.setFont(font)
        self.PTO_in.setText("")
        self.PTO_in.setObjectName("PTO_in")
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setGeometry(QtCore.QRect(10, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.CF_ME_in = QtWidgets.QLineEdit(self.widget)
        self.CF_ME_in.setGeometry(QtCore.QRect(190, 460, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.CF_ME_in.setFont(font)
        self.CF_ME_in.setText("")
        self.CF_ME_in.setObjectName("CF_ME_in")
        self.CF_AE_in = QtWidgets.QLineEdit(self.widget)
        self.CF_AE_in.setGeometry(QtCore.QRect(190, 510, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.CF_AE_in.setFont(font)
        self.CF_AE_in.setText("")
        self.CF_AE_in.setObjectName("CF_AE_in")
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setGeometry(QtCore.QRect(10, 500, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setGeometry(QtCore.QRect(10, 550, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.OEPL_in = QtWidgets.QLineEdit(self.widget)
        self.OEPL_in.setGeometry(QtCore.QRect(190, 560, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.OEPL_in.setFont(font)
        self.OEPL_in.setText("")
        self.OEPL_in.setObjectName("OEPL_in")
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setGeometry(QtCore.QRect(10, 600, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.nonOEPL_in = QtWidgets.QLineEdit(self.widget)
        self.nonOEPL_in.setGeometry(QtCore.QRect(190, 610, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.nonOEPL_in.setFont(font)
        self.nonOEPL_in.setText("")
        self.nonOEPL_in.setObjectName("nonOEPL_in")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setGeometry(QtCore.QRect(10, 0, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(380, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(380, 30, 411, 451))
        self.widget_2.setObjectName("widget_2")
        self.Vappt = QtWidgets.QTextBrowser(self.widget_2)
        self.Vappt.setGeometry(QtCore.QRect(280, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Vappt.setFont(font)
        self.Vappt.setObjectName("Vappt")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Vavgt = QtWidgets.QTextBrowser(self.widget_2)
        self.Vavgt.setGeometry(QtCore.QRect(280, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Vavgt.setFont(font)
        self.Vavgt.setObjectName("Vavgt")
        self.MCR_avgt = QtWidgets.QTextBrowser(self.widget_2)
        self.MCR_avgt.setGeometry(QtCore.QRect(280, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.MCR_avgt.setFont(font)
        self.MCR_avgt.setObjectName("MCR_avgt")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(20, 170, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(20, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(20, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.PMEt = QtWidgets.QTextBrowser(self.widget_2)
        self.PMEt.setGeometry(QtCore.QRect(280, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PMEt.setFont(font)
        self.PMEt.setObjectName("PMEt")
        self.PAEt = QtWidgets.QTextBrowser(self.widget_2)
        self.PAEt.setGeometry(QtCore.QRect(280, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PAEt.setFont(font)
        self.PAEt.setObjectName("PAEt")
        self.margint = QtWidgets.QTextBrowser(self.widget_2)
        self.margint.setGeometry(QtCore.QRect(280, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.margint.setFont(font)
        self.margint.setObjectName("margint")
        self.reqEEXI = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.reqEEXI.setGeometry(QtCore.QRect(670, 630, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.reqEEXI.setFont(font)
        self.reqEEXI.setObjectName("reqEEXI")
        self.EEXI = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.EEXI.setGeometry(QtCore.QRect(670, 560, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.EEXI.setFont(font)
        self.EEXI.setObjectName("EEXI")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(340, 560, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(340, 630, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setGeometry(QtCore.QRect(800, 20, 411, 701))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setGeometry(QtCore.QRect(10, 570, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.EEXI_2 = QtWidgets.QTextBrowser(self.widget_3)
        self.EEXI_2.setGeometry(QtCore.QRect(290, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.EEXI_2.setFont(font)
        self.EEXI_2.setObjectName("EEXI_2")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.MCR_lim = QtWidgets.QTextBrowser(self.widget_3)
        self.MCR_lim.setGeometry(QtCore.QRect(290, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.MCR_lim.setFont(font)
        self.MCR_lim.setObjectName("MCR_lim")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.PME_lim = QtWidgets.QTextBrowser(self.widget_3)
        self.PME_lim.setGeometry(QtCore.QRect(290, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PME_lim.setFont(font)
        self.PME_lim.setObjectName("PME_lim")
        self.label_19 = QtWidgets.QLabel(self.widget_3)
        self.label_19.setGeometry(QtCore.QRect(10, 170, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.Vappt_lim = QtWidgets.QTextBrowser(self.widget_3)
        self.Vappt_lim.setGeometry(QtCore.QRect(290, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Vappt_lim.setFont(font)
        self.Vappt_lim.setObjectName("Vappt_lim")
        self.label_20 = QtWidgets.QLabel(self.widget_3)
        self.label_20.setGeometry(QtCore.QRect(10, 230, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.reduction = QtWidgets.QTextBrowser(self.widget_3)
        self.reduction.setGeometry(QtCore.QRect(290, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.reduction.setFont(font)
        self.reduction.setObjectName("reduction")
        self.label_24 = QtWidgets.QLabel(self.widget_3)
        self.label_24.setGeometry(QtCore.QRect(110, 640, 291, 41))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("../CR EEXI Calcuation_Bulk.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_30 = QtWidgets.QLabel(self.widget_3)
        self.label_30.setGeometry(QtCore.QRect(10, 290, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.Vapp_reduction = QtWidgets.QTextBrowser(self.widget_3)
        self.Vapp_reduction.setGeometry(QtCore.QRect(290, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Vapp_reduction.setFont(font)
        self.Vapp_reduction.setObjectName("Vapp_reduction")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(800, 0, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Calculation"))
        self.label_2.setText(_translate("MainWindow", "MCR ME *(kW)"))
        self.label.setText(_translate("MainWindow", "DWT *(tonne)"))
        self.label_9.setText(_translate("MainWindow", "LWT (CSR)(tonne)"))
        self.label_10.setText(_translate("MainWindow", "VS EEDI(knot)"))
        self.label_22.setText(_translate("MainWindow", "PS EEDI(kW)"))
        self.label_25.setText(_translate("MainWindow", "SFC ME(g/kWh)"))
        self.label_26.setText(_translate("MainWindow", "SFC AE(g/kWh)"))
        self.label_27.setText(_translate("MainWindow", "PTO(kW)"))
        self.label_28.setText(_translate("MainWindow", "CF ME(tCO2/t-fuel)"))
        self.label_29.setText(_translate("MainWindow", "CF AE(tCO2/t-fuel)"))
        self.label_31.setText(_translate("MainWindow", "Overridable EPL"))
        self.label_32.setText(_translate("MainWindow", "nonOverridable EPL"))
        self.label_21.setText(_translate("MainWindow", "Input (* is necessary)"))
        self.label_17.setText(_translate("MainWindow", "Original"))
        self.label_5.setText(_translate("MainWindow", "MCR avg(kW)"))
        self.label_4.setText(_translate("MainWindow", "Vapp(knot)"))
        self.label_6.setText(_translate("MainWindow", "Vavg(knot)"))
        self.label_11.setText(_translate("MainWindow", "margin(knot)"))
        self.label_12.setText(_translate("MainWindow", "PME(kW)"))
        self.label_13.setText(_translate("MainWindow", "PAE(kW)"))
        self.label_3.setText(_translate("MainWindow", "Attained EEXI(g-CO2/t-mile)"))
        self.label_8.setText(_translate("MainWindow", "Required EEXI(g-CO2/t-mile)"))
        self.label_14.setText(_translate("MainWindow", "Attained EEXI(g-CO2/t-mile)"))
        self.label_15.setText(_translate("MainWindow", "MCR lim(kW)"))
        self.label_18.setText(_translate("MainWindow", "PME lim(kW)"))
        self.label_19.setText(_translate("MainWindow", "Vapp lim(knot)"))
        self.label_20.setText(_translate("MainWindow", "%MCR Reduction"))
        self.label_30.setText(_translate("MainWindow", "Vapp Reduction(knot)"))
        self.label_16.setText(_translate("MainWindow", "Recommended"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
