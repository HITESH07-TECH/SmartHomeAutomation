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
-- Table structure for table `automationscenario`
--

DROP TABLE IF EXISTS `automationscenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `automationscenario` (
  `ScenarioID` int NOT NULL,
  `ScenarioName` varchar(255) DEFAULT NULL,
  `Description` text,
  `ActivationCondition` text,
  `DevicesInvolved` text,
  `Actions` text,
  `ActivationStatus` varchar(50) DEFAULT NULL,
  `UserID` int DEFAULT NULL,
  PRIMARY KEY (`ScenarioID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `automationscenario_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `automationscenario`
--

LOCK TABLES `automationscenario` WRITE;
/*!40000 ALTER TABLE `automationscenario` DISABLE KEYS */;
INSERT INTO `automationscenario` VALUES (1,'Home Lighting','Turn on lights','Time-based','[2]','Turn on Smart Bulb','Active',1),(2,'Security Alert','Notify on motion','Event-based','[3]','Send notification','Active',2),(3,'Door Lock','Lock at 10 PM','Time-based','[4]','Lock Smart Lock','Active',3),(4,'Energy Saving Mode','Reduce power usage','Time-based','[1,5]','Set thermostat to eco mode','Active',1);
/*!40000 ALTER TABLE `automationscenario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-12 18:48:32
