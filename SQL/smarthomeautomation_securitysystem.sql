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
-- Table structure for table `securitysystem`
--

DROP TABLE IF EXISTS `securitysystem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `securitysystem` (
  `SystemID` int NOT NULL,
  `DeviceIDs` int DEFAULT NULL,
  `ArmStatus` varchar(50) DEFAULT NULL,
  `SecurityMode` varchar(50) DEFAULT NULL,
  `AlarmTriggerConditions` text,
  PRIMARY KEY (`SystemID`),
  KEY `DeviceIDs` (`DeviceIDs`),
  CONSTRAINT `securitysystem_ibfk_1` FOREIGN KEY (`DeviceIDs`) REFERENCES `device` (`DeviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `securitysystem`
--

LOCK TABLES `securitysystem` WRITE;
/*!40000 ALTER TABLE `securitysystem` DISABLE KEYS */;
INSERT INTO `securitysystem` VALUES (1,3,'Disarmed','Home','Motion detected'),(2,4,'Armed','Away','Door opened'),(3,2,'Disarmed','Home','Light sensor detects darkness'),(4,1,'Armed','Night','Temperature drops below 18°C'),(5,6,'Disarmed','Home','Sound level above 70 dB'),(6,5,'Armed','Away','Motion and door opened');
/*!40000 ALTER TABLE `securitysystem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-12 18:48:33
