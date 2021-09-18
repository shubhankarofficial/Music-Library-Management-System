-- MariaDB dump 10.19  Distrib 10.5.9-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: musicp
-- ------------------------------------------------------
-- Server version	10.5.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Album`
--

DROP TABLE IF EXISTS `Album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Album` (
  `albumID` int(11) NOT NULL,
  `albumTitle` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `artistID` int(11) NOT NULL,
  `genreName` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tracks` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`albumID`),
  KEY `artistID` (`artistID`),
  KEY `genreName` (`genreName`),
  CONSTRAINT `Album_ibfk_1` FOREIGN KEY (`artistID`) REFERENCES `Artist` (`artistID`),
  CONSTRAINT `Album_ibfk_2` FOREIGN KEY (`genreName`) REFERENCES `Genre` (`genreName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Album`
--

LOCK TABLES `Album` WRITE;
/*!40000 ALTER TABLE `Album` DISABLE KEYS */;
INSERT INTO `Album` VALUES (201,'Whatever',1,'DANCE',13,3750,2014),(202,'1977-10-29 - Evans Field House',2,'Rock',15,2784,2018),(203,'Nostalgia, Ultra.',3,'R&B',14,2207,2011),(204,'SOME OTHER ONES',4,'Indie Rock',14,3992,2015),(205,'Shelter',5,'Pop',15,5771,2010);
/*!40000 ALTER TABLE `Album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Artist`
--

DROP TABLE IF EXISTS `Artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Artist` (
  `artistID` int(11) NOT NULL,
  `artistName` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Description` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`artistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Artist`
--

LOCK TABLES `Artist` WRITE;
/*!40000 ALTER TABLE `Artist` DISABLE KEYS */;
INSERT INTO `Artist` VALUES (1,'Weeknd','Abel Makkonen Tesfaye, aka Weeknd, is a Canadian singer and songwriter'),(2,'Green Day','Green Day is an American band formed in California in 1987'),(3,'R3HAB','Fadil El Ghoul, aka R3hab, is a Moroccan Dutch DJ'),(4,'Coldplay','Coldplay are a British rock band formed in London in 1996.'),(5,'Porter Robinson','Porter Weston Robinson is an American DJ, musician, and singer');
/*!40000 ALTER TABLE `Artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Genre`
--

DROP TABLE IF EXISTS `Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Genre` (
  `genreName` varchar(72) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`genreName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genre`
--

LOCK TABLES `Genre` WRITE;
/*!40000 ALTER TABLE `Genre` DISABLE KEYS */;
INSERT INTO `Genre` VALUES ('DANCE','broad range of electronic music made for nightclubs, and festivals'),('Indie Rock','independent record labels, used interchangeably with alternative rock'),('Pop','describes all music that is popular and includes many disparate styles'),('R&B','soul and funk-influenced pop music originated as disco music'),('Rock','music centered on the electric guitar, with electric bass and drums');
/*!40000 ALTER TABLE `Genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Playlist`
--

DROP TABLE IF EXISTS `Playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Playlist` (
  `playlistID` int(11) NOT NULL,
  `playlistName` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tracks` int(11) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`playlistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Playlist`
--

LOCK TABLES `Playlist` WRITE;
/*!40000 ALTER TABLE `Playlist` DISABLE KEYS */;
INSERT INTO `Playlist` VALUES (1,'PL1',7,1910),(2,'PL2',9,1939),(3,'PL3',5,2088);
/*!40000 ALTER TABLE `Playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PlaylistContent`
--

DROP TABLE IF EXISTS `PlaylistContent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlaylistContent` (
  `playlistID` int(11) DEFAULT NULL,
  `songID` int(11) DEFAULT NULL,
  KEY `playlistID` (`playlistID`),
  KEY `songID` (`songID`),
  CONSTRAINT `PlaylistContent_ibfk_1` FOREIGN KEY (`playlistID`) REFERENCES `Playlist` (`playlistID`),
  CONSTRAINT `PlaylistContent_ibfk_2` FOREIGN KEY (`songID`) REFERENCES `SongFile` (`songID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlaylistContent`
--

LOCK TABLES `PlaylistContent` WRITE;
/*!40000 ALTER TABLE `PlaylistContent` DISABLE KEYS */;
INSERT INTO `PlaylistContent` VALUES (1,1012),(2,1011),(3,1030),(1,1001),(1,1002),(3,1001),(1,1004),(3,1005),(2,1006),(2,1007),(2,1031),(1,1032),(2,1033),(2,1035),(1,1036),(2,1047),(2,1044),(3,1046),(1,1045),(3,1042),(2,1050);
/*!40000 ALTER TABLE `PlaylistContent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SongFile`
--

DROP TABLE IF EXISTS `SongFile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SongFile` (
  `songID` int(11) NOT NULL,
  `songTitle` varchar(72) COLLATE utf8mb4_unicode_ci NOT NULL,
  `artistID` int(11) NOT NULL,
  `albumID` int(11) NOT NULL,
  `trackNo` int(11) DEFAULT NULL,
  `duration` int(11) NOT NULL,
  `format` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `genreName` varchar(72) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`songID`),
  KEY `artistID` (`artistID`),
  KEY `albumID` (`albumID`),
  KEY `genreName` (`genreName`),
  CONSTRAINT `SongFile_ibfk_1` FOREIGN KEY (`artistID`) REFERENCES `Artist` (`artistID`),
  CONSTRAINT `SongFile_ibfk_2` FOREIGN KEY (`albumID`) REFERENCES `Album` (`albumID`),
  CONSTRAINT `SongFile_ibfk_3` FOREIGN KEY (`genreName`) REFERENCES `Genre` (`genreName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SongFile`
--

LOCK TABLES `SongFile` WRITE;
/*!40000 ALTER TABLE `SongFile` DISABLE KEYS */;
INSERT INTO `SongFile` VALUES (1001,'Might As Well',2,202,15,439,'mp3','Rock'),(1002,'Dust',5,205,8,590,'mp3','Pop'),(1003,'epaR Featuring Vince Staples',5,205,15,182,'flac','Pop'),(1004,'Moonlight Featuring Hodgy Beats',5,205,9,95,'ogg','Pop'),(1005,'Loser',2,202,2,582,'mp3','Rock'),(1006,'street fighter',3,203,10,299,'mp3','R&B'),(1007,'Strawberry Swing',3,203,11,80,'mp3','R&B'),(1008,'Novacane',3,203,14,186,'ogg','R&B'),(1009,'We All Try',3,203,12,244,'mp3','R&B'),(1010,'HOSO BOYO',3,203,13,226,'flac','R&B'),(1011,'DON JUAN',3,203,6,247,'mp3','R&B'),(1012,'maybe watson - ps remix instr',1,201,13,199,'mp3','DANCE'),(1013,'YOUNG COCONUT',3,203,3,103,'mp3','R&B'),(1014,'HACHIKO',3,203,4,183,'ogg','R&B'),(1015,'Stapleton',5,205,3,108,'mp3','Pop'),(1016,'TwoFourSix',1,201,9,327,'mp3','DANCE'),(1017,'ONION MAN',3,203,1,563,'mp3','R&B'),(1018,'PETERS PICKLES',3,203,7,132,'flac','R&B'),(1019,'New Minglewood Blues',2,202,1,148,'mp3','Rock'),(1020,'El Paso',2,202,3,283,'mp3','Rock'),(1021,'Ramble On Rose',2,202,14,386,'ogg','Rock'),(1022,'FISH TERRY',3,203,8,254,'flac','R&B'),(1023,'It Must Have Been The Roses',2,202,9,339,'mp3','Rock'),(1024,'Let It Grow',2,202,5,479,'mp3','Rock'),(1025,'Bertha',2,202,13,479,'flac','Rock'),(1026,'bits talkin',4,204,13,150,'mp3','Indie Rock'),(1027,'Pigeons Featuring Wolf Haley',5,205,2,241,'mp3','Pop'),(1028,'LITTLE PEPPER',3,203,9,417,'mp3','R&B'),(1029,'Close to the sun',3,203,2,440,'ogg','R&B'),(1030,'ROOTS - SILENT TREATMENT INTRO',1,201,3,327,'mp3','DANCE'),(1031,'Show Out',1,201,5,276,'mp3','DANCE'),(1032,'Sober Thoughts (w_ Goldlink)',1,201,4,115,'ogg','DANCE'),(1033,'Kill',5,205,6,316,'mp3','Pop'),(1034,'Wake Me Up',5,205,14,289,'mp3','Pop'),(1035,'ALL WE DO RMX (w_ JMSN)',1,201,7,189,'mp3','DANCE'),(1036,'ATM JAM (ALTERNATE MIX)',1,201,6,297,'flac','DANCE'),(1037,'CIARA- BODY PARTY',1,201,12,220,'ogg','DANCE'),(1038,'Songs For Women',4,204,10,196,'mp3','Indie Rock'),(1039,'goldeneye',4,204,1,115,'mp3','Indie Rock'),(1040,'There Will Be Tears',4,204,2,495,'ogg','Indie Rock'),(1041,'Good Lovin\'',2,202,4,514,'mp3','Rock'),(1042,'Friend Of The Devil',2,202,12,593,'ogg','Rock'),(1043,'soul calibur',4,204,3,193,'mp3','Indie Rock'),(1044,'Electric Feel',4,204,7,156,'mp3','Indie Rock'),(1045,'Lovecrimes',4,204,14,175,'ogg','Indie Rock'),(1046,'FOREVER LASTING NIGHT',1,201,9,201,'mp3','DANCE'),(1047,'Blinding Lights',1,201,1,114,'flac','DANCE'),(1048,'Jill Scott - It\'s Love (Kaytranada Edition)',1,201,8,369,'ogg','DANCE'),(1049,'Jupiter',1,201,11,464,'mp3','DANCE'),(1050,'Swim Good',4,204,6,262,'ogg','Indie Rock');
/*!40000 ALTER TABLE `SongFile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-30 11:22:41
