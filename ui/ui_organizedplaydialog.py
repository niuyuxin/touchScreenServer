# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'organizedplaydialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_organizedPlayDialog(object):
    def setupUi(self, organizedPlayDialog):
        organizedPlayDialog.setObjectName("organizedPlayDialog")
        organizedPlayDialog.resize(687, 503)
        self.verticalLayout = QtWidgets.QVBoxLayout(organizedPlayDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tipsLabel = QtWidgets.QLabel(organizedPlayDialog)
        self.tipsLabel.setObjectName("tipsLabel")
        self.verticalLayout.addWidget(self.tipsLabel)
        self.contentFrame = QtWidgets.QFrame(organizedPlayDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.verticalLayout.addWidget(self.contentFrame)
        self.groupBox = QtWidgets.QGroupBox(organizedPlayDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sceneQuantityLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.sceneQuantityLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneQuantityLineEdit.sizePolicy().hasHeightForWidth())
        self.sceneQuantityLineEdit.setSizePolicy(sizePolicy)
        self.sceneQuantityLineEdit.setObjectName("sceneQuantityLineEdit")
        self.horizontalLayout_2.addWidget(self.sceneQuantityLineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lastModifiedTimeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lastModifiedTimeLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastModifiedTimeLineEdit.sizePolicy().hasHeightForWidth())
        self.lastModifiedTimeLineEdit.setSizePolicy(sizePolicy)
        self.lastModifiedTimeLineEdit.setText("")
        self.lastModifiedTimeLineEdit.setObjectName("lastModifiedTimeLineEdit")
        self.horizontalLayout_2.addWidget(self.lastModifiedTimeLineEdit)
        spacerItem = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.playsIdLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.playsIdLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playsIdLineEdit.sizePolicy().hasHeightForWidth())
        self.playsIdLineEdit.setSizePolicy(sizePolicy)
        self.playsIdLineEdit.setObjectName("playsIdLineEdit")
        self.horizontalLayout_2.addWidget(self.playsIdLineEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editingPushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.editingPushButton.setAutoDefault(False)
        self.editingPushButton.setDefault(False)
        self.editingPushButton.setObjectName("editingPushButton")
        self.horizontalLayout.addWidget(self.editingPushButton)
        self.newPushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.newPushButton.setAutoDefault(False)
        self.newPushButton.setDefault(False)
        self.newPushButton.setObjectName("newPushButton")
        self.horizontalLayout.addWidget(self.newPushButton)
        self.renamePushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.renamePushButton.setAutoDefault(False)
        self.renamePushButton.setDefault(False)
        self.renamePushButton.setObjectName("renamePushButton")
        self.horizontalLayout.addWidget(self.renamePushButton)
        self.deletePushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.deletePushButton.setAutoDefault(False)
        self.deletePushButton.setDefault(False)
        self.deletePushButton.setObjectName("deletePushButton")
        self.horizontalLayout.addWidget(self.deletePushButton)
        self.exportPushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.exportPushButton.setAutoDefault(False)
        self.exportPushButton.setDefault(False)
        self.exportPushButton.setObjectName("exportPushButton")
        self.horizontalLayout.addWidget(self.exportPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.returnPushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.returnPushButton.setAutoDefault(True)
        self.returnPushButton.setDefault(True)
        self.returnPushButton.setObjectName("returnPushButton")
        self.horizontalLayout.addWidget(self.returnPushButton)
        self.activePushButton = QtWidgets.QPushButton(organizedPlayDialog)
        self.activePushButton.setAutoDefault(False)
        self.activePushButton.setDefault(False)
        self.activePushButton.setObjectName("activePushButton")
        self.horizontalLayout.addWidget(self.activePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(organizedPlayDialog)
        self.returnPushButton.clicked.connect(organizedPlayDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(organizedPlayDialog)

    def retranslateUi(self, organizedPlayDialog):
        _translate = QtCore.QCoreApplication.translate
        organizedPlayDialog.setWindowTitle(_translate("organizedPlayDialog", "Dialog"))
        self.tipsLabel.setText(_translate("organizedPlayDialog", "tips ..."))
        self.groupBox.setTitle(_translate("organizedPlayDialog", "GroupBox"))
        self.label.setText(_translate("organizedPlayDialog", "场景数量："))
        self.label_2.setText(_translate("organizedPlayDialog", "上次修改时间："))
        self.label_3.setText(_translate("organizedPlayDialog", "剧幕特征码："))
        self.playsIdLineEdit.setText(_translate("organizedPlayDialog", "123"))
        self.editingPushButton.setText(_translate("organizedPlayDialog", "编辑剧目"))
        self.newPushButton.setText(_translate("organizedPlayDialog", "新建剧目"))
        self.renamePushButton.setText(_translate("organizedPlayDialog", "重命名剧目"))
        self.deletePushButton.setText(_translate("organizedPlayDialog", "删除剧目"))
        self.exportPushButton.setText(_translate("organizedPlayDialog", "导出剧目..."))
        self.returnPushButton.setText(_translate("organizedPlayDialog", "返回"))
        self.activePushButton.setText(_translate("organizedPlayDialog", "设为活动剧目"))

