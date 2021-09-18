#!/usr/bin/env python3

from v1 import Ui_MainWindow
from song_form import Ui_Song_add
from artist_form import Ui_Artist_add
from album_form import Ui_Album_add
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


# Connection to the Database
def createConnection():
    global con
    con = QSqlDatabase.addDatabase("QMYSQL")
    ## NOTE: add your username,hostname and password to the database accordingly
    ## Also set the databasename accordingly
    con.setDatabaseName("musicp")
    #con.setHostName("")
    #con.setUserName("")
    #con.setPassword("")
    if not con.open():
        QMessageBox.critical(None,"Error!",
                             "Database Error: %s" % con.lastError().databaseText())
        return False
    return True


# Add Album form window
class AlbumForm(QtWidgets.QDialog, Ui_Album_add):
    def __init__(self, parent=None):
        super(AlbumForm, self).__init__(parent=parent)
        self.setupUi(self)

        # Initialisation of the form
        self.populateCombobox_artist()
        self.populateCombobox_genre()


        # Add connections to event handlers
        self.button1_Submit.clicked.connect(self.submitAlbum)
        self.button2_Add_Artist.clicked.connect(self.createArtist)


        # Validators for input to clean input
        rx_albumID = QtCore.QRegExp("[0-9]{11}")
        val_albumID = QtGui.QRegExpValidator(rx_albumID)
        self.lineEdit1_albumID.setValidator(val_albumID)
        
        rx_albumTitle = QtCore.QRegExp(".{72}")
        val_albumTitle = QtGui.QRegExpValidator(rx_albumTitle)
        self.lineEdit2_albumTitle.setValidator(val_albumTitle)
        
        rx_tracks = QtCore.QRegExp("[0-9]{11}")
        val_tracks = QtGui.QRegExpValidator(rx_tracks)
        self.lineEdit3_tracks.setValidator(val_tracks)
        
        rx_duration = QtCore.QRegExp("[0-9]{11}")
        val_duration = QtGui.QRegExpValidator(rx_duration)
        self.lineEdit4_duration.setValidator(val_duration)
        
        rx_year = QtCore.QRegExp("[0-9]{5}")
        val_year = QtGui.QRegExpValidator(rx_year)
        self.lineEdit5_year.setValidator(val_year)


    # Event Handlers/Initialisation functions
    def populateCombobox_artist(self):
        self.comboBox1_select_Artist.blockSignals(True)
        self.comboBox1_select_Artist.clear()
        query = QSqlQuery()
        result = query.exec_("SELECT artistID,artistName FROM Artist;")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)}: {query.value(1)}")
        ##print(lst)
        self.comboBox1_select_Artist.addItems(lst)
        self.comboBox1_select_Artist.blockSignals(False)
        
    def populateCombobox_genre(self):
        ####self.comboBox2_select_Album.blockSignals(True)
        self.comboBox2_select_Genre.clear()
        query = QSqlQuery()
        result = query.exec_("SELECT genreName FROM Genre;")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)}")
        ##print(lst)
        self.comboBox2_select_Genre.addItems(lst)
        ####self.comboBox2_select_Album.blockSignals(False)
        
    def submitAlbum(self):
        album_id = self.lineEdit1_albumID.text().strip()
        album_title = self.lineEdit2_albumTitle.text().strip()
        artist_id,_ = self.comboBox1_select_Artist.currentText().split(':',1)
        genre = self.comboBox2_select_Genre.currentText()
        tracks = self.lineEdit3_tracks.text().strip()
        duration = self.lineEdit4_duration.text().strip()
        year = self.lineEdit5_year.text().strip()
        row = set([album_id,album_title,artist_id,genre,tracks,duration,year])
        if '' in row:
            QMessageBox.warning(None,"Error!",
                             "Error: Please fill all entries.")
        else:
            query = QSqlQuery()
            result = query.exec_(f"""INSERT INTO Album 
                                    VALUES({album_id},'{album_title}',{artist_id},'{genre}',
                                           {tracks},{duration},{year});""")
            if result:
                self.close()
            else:
                QMessageBox.warning(None,"Error!",
                             f"Error: Please check your input\n{query.lastError().text()}")
        
    def createArtist(self):
        self.artistFormWin = ArtistForm()
        self.artistFormWin.exec()
        self.populateCombobox_artist()


# Add Artist form window
class ArtistForm(QtWidgets.QDialog, Ui_Artist_add):
    def __init__(self, parent=None):
        super(ArtistForm, self).__init__(parent=parent)
        self.setupUi(self)


        # Add connections to event handlers
        self.button1_Submit.clicked.connect(self.submitArtist)


        # Validators for input to clean input
        rx_artistID = QtCore.QRegExp("[0-9]{11}")
        val_artistID = QtGui.QRegExpValidator(rx_artistID)
        self.lineEdit1_artistID.setValidator(val_artistID)
        
        rx_name = QtCore.QRegExp(".{72}")
        val_name = QtGui.QRegExpValidator(rx_name)
        self.lineEdit2_name.setValidator(val_name)
        
        rx_description = QtCore.QRegExp(".{72}")
        val_description = QtGui.QRegExpValidator(rx_description)
        self.lineEdit3_description.setValidator(val_description)


    # Event Handlers/Initialisation functions
    def submitArtist(self):
        artist_id = self.lineEdit1_artistID.text().strip()
        artist_name = self.lineEdit2_name.text().strip()
        artist_description = self.lineEdit3_description.text().strip()
        row = set([artist_id,artist_name,artist_description])
        if '' in row:
            QMessageBox.warning(None,"Error!",
                             "Error: Please fill all entries.")
        else:
            query = QSqlQuery()
            result = query.exec_(f"""INSERT INTO Artist 
                                    VALUES({artist_id},'{artist_name}','{artist_description}');""")
            if result:
                QMessageBox.information(None,"Data Inserted!",
                             f"Please add a new Album for the artist")
                self.albumFormWin = AlbumForm()
                self.albumFormWin.comboBox1_select_Artist.clear()
                self.albumFormWin.comboBox1_select_Artist.addItems([f'{artist_id}: {artist_name}'])
                self.albumFormWin.comboBox1_select_Artist.setCurrentIndex(0)
                self.albumFormWin.exec()
                self.close()
            else:
                QMessageBox.warning(None,"Error!",
                             f"Error: Please check your input\n{query.lastError().text()}")



# Add Song form window
class SongForm(QtWidgets.QDialog, Ui_Song_add):
    def __init__(self, parent=None):
        super(SongForm, self).__init__(parent=parent)
        self.setupUi(self)


        # Initialisation of the form
        self.populateCombobox_artist()
        self.populateCombobox_album()
        self.populateField_genre()


        # Add connections to event handlers
        ##self.button3_Submit.clicked.connect(lambda: self.close())
        self.button3_Submit.clicked.connect(self.submitSong)
        self.comboBox1_select_Artist.currentTextChanged.connect(self.populateCombobox_album)
        self.comboBox2_select_Album.currentTextChanged.connect(self.populateField_genre)
        self.button1_Add_Artist.clicked.connect(self.createArtist)
        self.button2_Add_Album.clicked.connect(self.createAlbum)


        # Validators for input to clean input
        rx_SongID = QtCore.QRegExp("[0-9]{11}")
        val_SongID = QtGui.QRegExpValidator(rx_SongID)
        self.lineEdit1_SongID.setValidator(val_SongID)
        
        rx_Title = QtCore.QRegExp(".{72}")
        val_Title = QtGui.QRegExpValidator(rx_Title)
        self.lineEdit2_Title.setValidator(val_Title)
        
        rx_TrackNo = QtCore.QRegExp("[0-9]{11}")
        val_TrackNo = QtGui.QRegExpValidator(rx_TrackNo)
        self.lineEdit3_TrackNo.setValidator(val_TrackNo)
        
        rx_Duration  = QtCore.QRegExp("[0-9]{11}")
        val_Duration = QtGui.QRegExpValidator(rx_Duration)
        self.lineEdit4_Duration.setValidator(val_Duration)
        
        rx_Format = QtCore.QRegExp(".{6}")
        val_Format = QtGui.QRegExpValidator(rx_Format)
        self.lineEdit5_Format.setValidator(val_Format)

    
    # Event Handlers/Initialisation functions
    def populateCombobox_artist(self):
        self.comboBox1_select_Artist.blockSignals(True)
        self.comboBox1_select_Artist.clear()
        query = QSqlQuery()
        result = query.exec_("SELECT artistID,artistName FROM Artist;")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)}: {query.value(1)}")
        ##print(lst)
        self.comboBox1_select_Artist.addItems(lst)
        self.comboBox1_select_Artist.blockSignals(False)
        
    def populateCombobox_album(self):
        self.comboBox2_select_Album.blockSignals(True)
        self.comboBox2_select_Album.clear()
        artist_id,_ = self.comboBox1_select_Artist.currentText().split(':',1)
        query = QSqlQuery()
        result = query.exec_(f"SELECT albumID,albumTitle FROM Album WHERE artistId = {artist_id};")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)}: {query.value(1)}")
        ##print(lst)
        self.comboBox2_select_Album.addItems(lst)
        self.comboBox2_select_Album.blockSignals(False)
        self.populateField_genre()
        
    def populateField_genre(self):
        album_id,_ = self.comboBox2_select_Album.currentText().split(':',1)
        query = QSqlQuery()
        result = query.exec_(f"SELECT genreName FROM Album WHERE albumID = {album_id};")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)}")
        ##print(lst)
        self.lineEdit6_Genre.setText(lst[0])
        
    def submitSong(self):
        song_id = self.lineEdit1_SongID.text().strip()
        song_title = self.lineEdit2_Title.text().strip()
        artist_id,_ = self.comboBox1_select_Artist.currentText().split(':',1)
        album_id,_ = self.comboBox2_select_Album.currentText().split(':',1)
        track_no = self.lineEdit3_TrackNo.text().strip()
        duration = self.lineEdit4_Duration.text().strip()
        sng_format = self.lineEdit5_Format.text().strip()
        genre = self.lineEdit6_Genre.text().strip()
        row = set([song_id,song_title,artist_id,album_id,track_no,duration,sng_format,genre])
        if '' in row:
            QMessageBox.warning(None,"Error!",
                             "Error: Please fill all entries.")
        else:
            query = QSqlQuery()
            result = query.exec_(f"""INSERT INTO SongFile 
                                    VALUES({song_id},'{song_title}',{artist_id},{album_id},{track_no},
                                        {duration},'{sng_format}','{genre}');""")
            if result:
                self.close()
            else:
                QMessageBox.warning(None,"Error!",
                             f"Error: Please check your input\n{query.lastError().text()}")
        
    def createArtist(self):
        self.artistFormWin = ArtistForm()
        self.artistFormWin.exec()
        self.populateCombobox_artist()
        self.populateCombobox_album()
        
    def createAlbum(self):
        self.albumFormWin = AlbumForm()
        self.albumFormWin.exec()
        self.populateCombobox_artist()
        self.populateCombobox_album()

# Main Form Window Class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


        # Initialisation and connections to event handlers
        self.actionQuit.triggered.connect(QApplication.instance().quit)
        self.actionAddSong.triggered.connect(self.showSongForm)
        self.actionAddArtist.triggered.connect(self.showArtistForm)
        self.actionAddAlbum.triggered.connect(self.showAlbumForm)
        self.button1_show_Songs.clicked.connect(lambda: self.fetchAndDisplayQuery("""SELECT s.songID as Song_ID, s.songTitle as Song_Title,
            ar.artistName as Artist_Name, al.albumTitle as Album_Title, s.trackNo as Tracks, 
            s.duration as Duration, s.format as Format, s.genreName as Genre, al.Year as Release_Year
            FROM SongFile s
            INNER JOIN Artist ar ON s.artistID = ar.artistID
            INNER JOIN Album al ON s.albumID = al.albumID;"""))
        self.button2_show_Artists.clicked.connect(lambda: self.fetchAndDisplayQuery("""SELECT artistID as Artist_ID,artistName as Artist_Name,
            Description FROM Artist;"""))
        self.button3_show_Albums.clicked.connect(lambda: self.fetchAndDisplayQuery("""SELECT al.albumID as Album_ID, al.albumTitle as Album_Title,
            ar.artistName as Artist_Name, al.genreName as Genre, al.tracks as Tracks, 
            al.duration as Duration, al.year as Release_Year
            FROM Album al
            INNER JOIN Artist ar ON al.artistID = ar.artistID;"""))
        self.button4_show_Genres.clicked.connect(lambda: self.fetchAndDisplayQuery("""SELECT * FROM Genre;"""))
        self.button5_show_Playlists.clicked.connect(lambda: self.fetchAndDisplayQuery("""SELECT * FROM Playlist;"""))
        self.populateCombobox()
        self.button_go_playlist.clicked.connect(self.fetchPlaylistQuery)



    # Event handlers/Initialisation functions
    def populateCombobox(self):
        query = QSqlQuery()
        result = query.exec_("SELECT playlistID,playlistName FROM Playlist;")
        lst = []
        while query.next():
            lst.append(f"{query.value(0)} {query.value(1)}")
        ##print(lst)
        self.comboBox_select_Playlist.addItems(lst)

    def fetchAndDisplayQuery(self,qry):
        query = QSqlQuery()
        result = query.exec_(qry)
        ##if result:
            ##print("found")
        tableModel = QSqlTableModel()
        tableModel.setQuery(query)
        self.tableView.setModel(tableModel)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        #self.tableView.show()
        
    def fetchPlaylistQuery(self):
        if self.comboBox_select_Playlist.currentIndex() != 0:
            txt = self.comboBox_select_Playlist.currentText()
            plid,plname = txt.split()
            self.fetchAndDisplayQuery(f"""SELECT * FROM SongFile WHERE songID IN 
                                      (SELECT songID FROM PlaylistContent WHERE playlistId={plid})""")
        else:
            QMessageBox.warning(None,"Error!",
                             "Error: Please select a playlist")
        
    def showSongForm(self):
        self.songFormWin = SongForm()
        self.songFormWin.exec()
        
    def showArtistForm(self):
        self.artistFormWin = ArtistForm()
        self.artistFormWin.exec()
        
    def showAlbumForm(self):
        self.albumFormWin = AlbumForm()
        self.albumFormWin.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
