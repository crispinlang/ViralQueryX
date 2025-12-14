-- MySQL dump 10.13  Distrib 9.4.0, for macos15 (arm64)
--
-- Host: localhost    Database: viral_db
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `enzyme_annotation`
--

DROP TABLE IF EXISTS `enzyme_annotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enzyme_annotation` (
  `enzyme_annotation_id` int NOT NULL AUTO_INCREMENT,
  `uniprot_id` varchar(50) NOT NULL,
  `ec_number` varchar(20) DEFAULT NULL,
  `enzyme_name` varchar(255) DEFAULT NULL,
  `source_db` varchar(100) DEFAULT 'BRENDA',
  PRIMARY KEY (`enzyme_annotation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genome_sequence`
--

DROP TABLE IF EXISTS `genome_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genome_sequence` (
  `sequence_id` int NOT NULL AUTO_INCREMENT,
  `virus_id` int DEFAULT NULL,
  `accession` varchar(50) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `sequence` longtext,
  `ncbi_nuccore_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sequence_id`),
  KEY `virus_id` (`virus_id`),
  CONSTRAINT `genome_sequence_ibfk_1` FOREIGN KEY (`virus_id`) REFERENCES `virus` (`virus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `protein_sequence`
--

DROP TABLE IF EXISTS `protein_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `protein_sequence` (
  `protein_id` int NOT NULL AUTO_INCREMENT,
  `virus_id` int DEFAULT NULL,
  `uniprot_id` varchar(50) DEFAULT NULL,
  `protein_name` varchar(255) DEFAULT NULL,
  `sequence` text,
  `uniprot_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`protein_id`),
  KEY `virus_id` (`virus_id`),
  CONSTRAINT `protein_sequence_ibfk_1` FOREIGN KEY (`virus_id`) REFERENCES `virus` (`virus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `virus`
--

DROP TABLE IF EXISTS `virus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `virus` (
  `virus_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `genome_type` varchar(50) DEFAULT NULL,
  `baltimore_group` varchar(5) DEFAULT NULL,
  `enveloped` tinyint(1) DEFAULT NULL,
  `genome_size_kb` float DEFAULT NULL,
  `segments` int DEFAULT NULL,
  `capsid_symmetry` varchar(50) DEFAULT NULL,
  `typical_virion_diameter_nm` int DEFAULT NULL,
  `primary_hosts` text,
  `transmission_route` text,
  `associated_diseases` text,
  `ncbi_taxid` varchar(32) DEFAULT NULL,
  `ncbi_tax_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`virus_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-14 17:59:16
