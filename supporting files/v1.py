# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 160, 1831, 821))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 1831, 43))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button1_show_Songs = QtWidgets.QPushButton(self.layoutWidget)
        self.button1_show_Songs.setObjectName("button1_show_Songs")
        self.horizontalLayout.addWidget(self.button1_show_Songs)
        self.button2_show_Artists = QtWidgets.QPushButton(self.layoutWidget)
        self.button2_show_Artists.setObjectName("button2_show_Artists")
        self.horizontalLayout.addWidget(self.button2_show_Artists)
        self.button3_show_Albums = QtWidgets.QPushButton(self.layoutWidget)
        self.button3_show_Albums.setObjectName("button3_show_Albums")
        self.horizontalLayout.addWidget(self.button3_show_Albums)
        self.button4_show_Genres = QtWidgets.QPushButton(self.layoutWidget)
        self.button4_show_Genres.setObjectName("button4_show_Genres")
        self.horizontalLayout.addWidget(self.button4_show_Genres)
        self.button5_show_Playlists = QtWidgets.QPushButton(self.layoutWidget)
        self.button5_show_Playlists.setObjectName("button5_show_Playlists")
        self.horizontalLayout.addWidget(self.button5_show_Playlists)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 100, 361, 43))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_select_Playlist = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_select_Playlist.setObjectName("comboBox_select_Playlist")
        self.comboBox_select_Playlist.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_select_Playlist)
        self.button_go_playlist = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_go_playlist.setObjectName("button_go_playlist")
        self.horizontalLayout_2.addWidget(self.button_go_playlist)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 121, 22))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menuFile)
        self.menuAdd.setObjectName("menuAdd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAddSong = QtWidgets.QAction(MainWindow)
        self.actionAddSong.setObjectName("actionAddSong")
        self.actionAddArtist = QtWidgets.QAction(MainWindow)
        self.actionAddArtist.setObjectName("actionAddArtist")
        self.actionAddAlbum = QtWidgets.QAction(MainWindow)
        self.actionAddAlbum.setObjectName("actionAddAlbum")
        self.actionAddPlaylist = QtWidgets.QAction(MainWindow)
        self.actionAddPlaylist.setObjectName("actionAddPlaylist")
        self.actionAddSong_To_Playlist = QtWidgets.QAction(MainWindow)
        self.actionAddSong_To_Playlist.setObjectName("actionAddSong_To_Playlist")
        self.menuAdd.addAction(self.actionAddSong)
        self.menuAdd.addAction(self.actionAddArtist)
        self.menuAdd.addAction(self.actionAddAlbum)
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music DB GUI"))
        self.button1_show_Songs.setToolTip(_translate("MainWindow", "Show Songs"))
        self.button1_show_Songs.setText(_translate("MainWindow", "&Songs"))
        self.button2_show_Artists.setToolTip(_translate("MainWindow", "Show Artists"))
        self.button2_show_Artists.setText(_translate("MainWindow", "&Artists"))
        self.button3_show_Albums.setToolTip(_translate("MainWindow", "Show Albums"))
        self.button3_show_Albums.setText(_translate("MainWindow", "A&lbums"))
        self.button4_show_Genres.setToolTip(_translate("MainWindow", "Show Genres"))
        self.button4_show_Genres.setText(_translate("MainWindow", "&Genres"))
        self.button5_show_Playlists.setToolTip(_translate("MainWindow", "Show Playlists"))
        self.button5_show_Playlists.setText(_translate("MainWindow", "&Playlists"))
        self.label.setText(_translate("MainWindow", "Songs in "))
        self.comboBox_select_Playlist.setItemText(0, _translate("MainWindow", "-- Select Playlist --"))
        self.button_go_playlist.setToolTip(_translate("MainWindow", "Show Playlist Contents"))
        self.button_go_playlist.setText(_translate("MainWindow", "G&o"))
        self.label_2.setText(_translate("MainWindow", "Show data from"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit the program."))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAddSong.setText(_translate("MainWindow", "Song"))
        self.actionAddSong.setStatusTip(_translate("MainWindow", "Add a new Song to the Database"))
        self.actionAddSong.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAddArtist.setText(_translate("MainWindow", "Artist"))
        self.actionAddArtist.setStatusTip(_translate("MainWindow", "Add a new Artist to the Database"))
        self.actionAddArtist.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionAddAlbum.setText(_translate("MainWindow", "Album"))
        self.actionAddAlbum.setStatusTip(_translate("MainWindow", "Add a new Album to the Database"))
        self.actionAddAlbum.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionAddPlaylist.setText(_translate("MainWindow", "Playlist"))
        self.actionAddPlaylist.setStatusTip(_translate("MainWindow", "Add a new Playlist to the Database"))
        self.actionAddSong_To_Playlist.setText(_translate("MainWindow", "Song To Playlist"))
        self.actionAddSong_To_Playlist.setStatusTip(_translate("MainWindow", "Manage Playlists"))
