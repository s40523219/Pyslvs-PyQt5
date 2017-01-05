# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/panel/run_Path_Solving.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(475, 588)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(475, 588))
        Dialog.setMaximumSize(QtCore.QSize(475, 588))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bezier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.algorithmPanel = QtWidgets.QWidget(Dialog)
        self.algorithmPanel.setObjectName("algorithmPanel")
        self.algorithmPanelLayout = QtWidgets.QHBoxLayout(self.algorithmPanel)
        self.algorithmPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.algorithmPanelLayout.setObjectName("algorithmPanelLayout")
        self.label_6 = QtWidgets.QLabel(self.algorithmPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.algorithmPanelLayout.addWidget(self.label_6)
        self.type0 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type0.setChecked(True)
        self.type0.setObjectName("type0")
        self.algorithmPanelLayout.addWidget(self.type0)
        self.type1 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type1.setObjectName("type1")
        self.algorithmPanelLayout.addWidget(self.type1)
        self.type2 = QtWidgets.QRadioButton(self.algorithmPanel)
        self.type2.setObjectName("type2")
        self.algorithmPanelLayout.addWidget(self.type2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.algorithmPanelLayout.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.algorithmPanel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.mainPanel = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPanel.sizePolicy().hasHeightForWidth())
        self.mainPanel.setSizePolicy(sizePolicy)
        self.mainPanel.setObjectName("mainPanel")
        self.mainPanelLayout = QtWidgets.QHBoxLayout(self.mainPanel)
        self.mainPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPanelLayout.setObjectName("mainPanelLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pointNum = QtWidgets.QLabel(self.mainPanel)
        self.pointNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pointNum.setObjectName("pointNum")
        self.horizontalLayout_2.addWidget(self.pointNum)
        self.label_5 = QtWidgets.QLabel(self.mainPanel)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Point_list = QtWidgets.QListWidget(self.mainPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Point_list.sizePolicy().hasHeightForWidth())
        self.Point_list.setSizePolicy(sizePolicy)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.mainPanel)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.X_coordinate = QtWidgets.QLineEdit(self.mainPanel)
        self.X_coordinate.setObjectName("X_coordinate")
        self.horizontalLayout_3.addWidget(self.X_coordinate)
        self.label_4 = QtWidgets.QLabel(self.mainPanel)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Y_coordinate = QtWidgets.QLineEdit(self.mainPanel)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.horizontalLayout_3.addWidget(self.Y_coordinate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.mainPanelLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.clearAll = QtWidgets.QPushButton(self.mainPanel)
        self.clearAll.setAutoDefault(False)
        self.clearAll.setObjectName("clearAll")
        self.verticalLayout.addWidget(self.clearAll)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.moveUp = QtWidgets.QPushButton(self.mainPanel)
        self.moveUp.setAutoDefault(False)
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.mainPanel)
        self.moveDown.setAutoDefault(False)
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout.addWidget(self.moveDown)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.remove = QtWidgets.QPushButton(self.mainPanel)
        self.remove.setAutoDefault(False)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.add = QtWidgets.QPushButton(self.mainPanel)
        self.add.setAutoDefault(False)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.mainPanelLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.mainPanel)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainPanelLayout.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.isCustomize = QtWidgets.QCheckBox(self.mainPanel)
        self.isCustomize.setObjectName("isCustomize")
        self.verticalLayout_3.addWidget(self.isCustomize)
        self.limitPanel = QtWidgets.QWidget(self.mainPanel)
        self.limitPanel.setEnabled(False)
        self.limitPanel.setObjectName("limitPanel")
        self.gridLayout = QtWidgets.QGridLayout(self.limitPanel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.limitPanel)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.AxMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AxMax.setMinimum(-999.0)
        self.AxMax.setMaximum(999.0)
        self.AxMax.setProperty("value", 50.0)
        self.AxMax.setObjectName("AxMax")
        self.gridLayout.addWidget(self.AxMax, 1, 1, 1, 1)
        self.AyMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AyMax.setMinimum(-999.0)
        self.AyMax.setMaximum(999.0)
        self.AyMax.setProperty("value", 50.0)
        self.AyMax.setObjectName("AyMax")
        self.gridLayout.addWidget(self.AyMax, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.limitPanel)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.DxMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DxMax.setMinimum(-999.0)
        self.DxMax.setMaximum(999.0)
        self.DxMax.setProperty("value", 50.0)
        self.DxMax.setObjectName("DxMax")
        self.gridLayout.addWidget(self.DxMax, 3, 1, 1, 1)
        self.AxMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AxMin.setMinimum(-999.0)
        self.AxMin.setMaximum(999.0)
        self.AxMin.setProperty("value", -50.0)
        self.AxMin.setObjectName("AxMin")
        self.gridLayout.addWidget(self.AxMin, 1, 2, 1, 1)
        self.DxMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DxMin.setMinimum(-99.99)
        self.DxMin.setProperty("value", -50.0)
        self.DxMin.setObjectName("DxMin")
        self.gridLayout.addWidget(self.DxMin, 3, 2, 1, 1)
        self.AyMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.AyMin.setMinimum(-999.0)
        self.AyMin.setMaximum(999.0)
        self.AyMin.setProperty("value", -50.0)
        self.AyMin.setObjectName("AyMin")
        self.gridLayout.addWidget(self.AyMin, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.limitPanel)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.limitPanel)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.DyMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DyMin.setMinimum(-999.0)
        self.DyMin.setMaximum(999.0)
        self.DyMin.setProperty("value", -50.0)
        self.DyMin.setObjectName("DyMin")
        self.gridLayout.addWidget(self.DyMin, 4, 2, 1, 1)
        self.DyMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.DyMax.setMinimum(-999.0)
        self.DyMax.setMaximum(999.0)
        self.DyMax.setProperty("value", 50.0)
        self.DyMax.setObjectName("DyMax")
        self.gridLayout.addWidget(self.DyMax, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.limitPanel)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.LMax = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.LMax.setMinimum(0.01)
        self.LMax.setMaximum(999.0)
        self.LMax.setProperty("value", 50.0)
        self.LMax.setObjectName("LMax")
        self.gridLayout.addWidget(self.LMax, 5, 1, 1, 1)
        self.LMin = QtWidgets.QDoubleSpinBox(self.limitPanel)
        self.LMin.setMinimum(0.01)
        self.LMin.setMaximum(999.0)
        self.LMin.setProperty("value", 5.0)
        self.LMin.setObjectName("LMin")
        self.gridLayout.addWidget(self.LMin, 5, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.limitPanel)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.limitPanel)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.limitPanel)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.mainPanelLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.mainPanel)
        self.startPanel = QtWidgets.QWidget(Dialog)
        self.startPanel.setObjectName("startPanel")
        self.startPanelLayout = QtWidgets.QHBoxLayout(self.startPanel)
        self.startPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.startPanelLayout.setObjectName("startPanelLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startPanelLayout.addItem(spacerItem7)
        self.Generate = QtWidgets.QPushButton(self.startPanel)
        self.Generate.setObjectName("Generate")
        self.startPanelLayout.addWidget(self.Generate)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startPanelLayout.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.startPanel)
        self.timePanel = QtWidgets.QWidget(Dialog)
        self.timePanel.setObjectName("timePanel")
        self.timePanelLayout = QtWidgets.QHBoxLayout(self.timePanel)
        self.timePanelLayout.setContentsMargins(0, 0, 0, 0)
        self.timePanelLayout.setObjectName("timePanelLayout")
        self.label_7 = QtWidgets.QLabel(self.timePanel)
        self.label_7.setObjectName("label_7")
        self.timePanelLayout.addWidget(self.label_7)
        self.timeShow = QtWidgets.QLabel(self.timePanel)
        self.timeShow.setObjectName("timeShow")
        self.timePanelLayout.addWidget(self.timeShow)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timePanelLayout.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.timePanel)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Path Solving"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose the points in the path as you want.</span></p><p><span style=\" font-size:12pt;\">This generator will design a crank rocker to meet this path requirement.</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "Algorithm: "))
        self.type0.setText(_translate("Dialog", "Genetic"))
        self.type1.setText(_translate("Dialog", "Firefly"))
        self.type2.setText(_translate("Dialog", "Differtial Evolution"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Point(s):</span></p></body></html>"))
        self.pointNum.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">Point(s)</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "x: "))
        self.X_coordinate.setPlaceholderText(_translate("Dialog", "0.0"))
        self.label_4.setText(_translate("Dialog", "y: "))
        self.Y_coordinate.setPlaceholderText(_translate("Dialog", "0.0"))
        self.clearAll.setText(_translate("Dialog", "Clear All"))
        self.moveUp.setText(_translate("Dialog", "Move up"))
        self.moveDown.setText(_translate("Dialog", "Move down"))
        self.remove.setText(_translate("Dialog", "-"))
        self.add.setText(_translate("Dialog", "+"))
        self.isCustomize.setText(_translate("Dialog", "Customize:"))
        self.label_8.setText(_translate("Dialog", "Ax: "))
        self.label_9.setText(_translate("Dialog", "Ay: "))
        self.label_10.setText(_translate("Dialog", "Dx: "))
        self.label_11.setText(_translate("Dialog", "Dy: "))
        self.label_12.setText(_translate("Dialog", "Links: "))
        self.label_13.setText(_translate("Dialog", "Max"))
        self.label_14.setText(_translate("Dialog", "Min"))
        self.Generate.setText(_translate("Dialog", "Generate"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Time spent: </span></p></body></html>"))
        self.timeShow.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt\">[No record]</span></p></body></html>"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
