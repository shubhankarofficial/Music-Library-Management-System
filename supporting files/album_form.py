# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'album_form_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Album_add(object):
    def setupUi(self, Album_add):
        Album_add.setObjectName("Album_add")
        Album_add.resize(440, 345)
        self.button2_Add_Artist = QtWidgets.QPushButton(Album_add)
        self.button2_Add_Artist.setGeometry(QtCore.QRect(270, 100, 148, 31))
        self.button2_Add_Artist.setObjectName("button2_Add_Artist")
        self.widget = QtWidgets.QWidget(Album_add)
        self.widget.setGeometry(QtCore.QRect(30, 30, 236, 281))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit1_albumID = QtWidgets.QLineEdit(self.widget)
        self.lineEdit1_albumID.setObjectName("lineEdit1_albumID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit1_albumID)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit2_albumTitle = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2_albumTitle.setObjectName("lineEdit2_albumTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit2_albumTitle)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox1_select_Artist = QtWidgets.QComboBox(self.widget)
        self.comboBox1_select_Artist.setObjectName("comboBox1_select_Artist")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox1_select_Artist)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox2_select_Genre = QtWidgets.QComboBox(self.widget)
        self.comboBox2_select_Genre.setObjectName("comboBox2_select_Genre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox2_select_Genre)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit3_tracks = QtWidgets.QLineEdit(self.widget)
        self.lineEdit3_tracks.setObjectName("lineEdit3_tracks")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit3_tracks)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit4_duration = QtWidgets.QLineEdit(self.widget)
        self.lineEdit4_duration.setObjectName("lineEdit4_duration")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit4_duration)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit5_year = QtWidgets.QLineEdit(self.widget)
        self.lineEdit5_year.setObjectName("lineEdit5_year")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit5_year)
        self.button1_Submit = QtWidgets.QPushButton(self.widget)
        self.button1_Submit.setObjectName("button1_Submit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.button1_Submit)

        self.retranslateUi(Album_add)
        QtCore.QMetaObject.connectSlotsByName(Album_add)

    def retranslateUi(self, Album_add):
        _translate = QtCore.QCoreApplication.translate
        Album_add.setWindowTitle(_translate("Album_add", "Add Album"))
        self.button2_Add_Artist.setText(_translate("Album_add", "Add &Artist"))
        self.label.setText(_translate("Album_add", "Album ID"))
        self.lineEdit1_albumID.setPlaceholderText(_translate("Album_add", "1234"))
        self.label_2.setText(_translate("Album_add", "Album Title"))
        self.lineEdit2_albumTitle.setPlaceholderText(_translate("Album_add", "XYZ"))
        self.label_3.setText(_translate("Album_add", "Artist"))
        self.label_4.setText(_translate("Album_add", "Genre"))
        self.label_5.setText(_translate("Album_add", "Tracks"))
        self.lineEdit3_tracks.setPlaceholderText(_translate("Album_add", "01"))
        self.label_6.setText(_translate("Album_add", "Duration"))
        self.lineEdit4_duration.setPlaceholderText(_translate("Album_add", "In Seconds"))
        self.label_7.setText(_translate("Album_add", "Year"))
        self.lineEdit5_year.setPlaceholderText(_translate("Album_add", "1234"))
        self.button1_Submit.setText(_translate("Album_add", "&Submit"))
