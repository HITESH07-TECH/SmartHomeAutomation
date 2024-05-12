-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: smarthomeautomation
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `scheduledtasks`
--

DROP TABLE IF EXISTS `scheduledtasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduledtasks` (
  `TaskID` int NOT NULL,
  `TaskName` varchar(255) DEFAULT NULL,
  `UserID` int DEFAULT NULL,
  `DevicesInvolved` text,
  `ExecutionTime` datetime DEFAULT NULL,
  `RecurrencePattern` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`TaskID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `scheduledtasks_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduledtasks`
--

LOCK TABLES `scheduledtasks` WRITE;
/*!40000 ALTER TABLE `scheduledtasks` DISABLE KEYS */;
INSERT INTO `scheduledtasks` VALUES (1,'Update Devices',1,'[1,2,3]','2022-04-11 00:00:00','Daily'),(2,'Check Sensors',2,'[1,3]','2022-04-11 09:00:00','Weekly'),(3,'Energy Report',5,'[1,5,7]','2022-04-12 08:00:00','Monthly'),(4,'Security Audit',3,'[2,3,4]','2022-04-12 14:00:00','Bi-weekly'),(5,'Maintenance Check',1,'[1,2,5]','2022-04-13 10:00:00','Quarterly');
/*!40000 ALTER TABLE `scheduledtasks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-12 18:48:31
