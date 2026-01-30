-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: bi-project-saraasljivo-bi.l.aivencloud.com    Database: students_dw
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '7025306c-f467-11f0-8440-862ccfb07042:1-917,
c229e06b-f533-11f0-bf90-862ccfb05325:1-30077';

--
-- Table structure for table `dim_department`
--

DROP TABLE IF EXISTS `dim_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_department` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE KEY `department_name` (`department_name`)
) ENGINE=InnoDB AUTO_INCREMENT=10024 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dim_lifestyle`
--

DROP TABLE IF EXISTS `dim_lifestyle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_lifestyle` (
  `lifestyle_id` int NOT NULL AUTO_INCREMENT,
  `study_hours_per_week` int DEFAULT NULL,
  `sleep_hours_per_night` decimal(4,2) DEFAULT NULL,
  `stress_level` int DEFAULT NULL,
  `extracurricular_activities` varchar(5) DEFAULT NULL,
  `internet_access_at_home` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`lifestyle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10267 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dim_student`
--

DROP TABLE IF EXISTS `dim_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_student` (
  `student_key` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`student_key`)
) ENGINE=InnoDB AUTO_INCREMENT=18458 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fact_student_performance`
--

DROP TABLE IF EXISTS `fact_student_performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fact_student_performance` (
  `fact_id` int NOT NULL AUTO_INCREMENT,
  `student_key` int DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `lifestyle_id` int DEFAULT NULL,
  `attendance` decimal(5,2) DEFAULT NULL,
  `total_score` decimal(6,2) DEFAULT NULL,
  `midterm_score` decimal(6,2) DEFAULT NULL,
  `final_score` decimal(6,2) DEFAULT NULL,
  `assignments_avg` decimal(6,2) DEFAULT NULL,
  `quizzes_avg` decimal(6,2) DEFAULT NULL,
  `participation_score` decimal(6,2) DEFAULT NULL,
  `projects_score` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`fact_id`),
  KEY `student_key` (`student_key`),
  KEY `department_id` (`department_id`),
  KEY `lifestyle_id` (`lifestyle_id`),
  CONSTRAINT `fact_student_performance_ibfk_1` FOREIGN KEY (`student_key`) REFERENCES `dim_student` (`student_key`),
  CONSTRAINT `fact_student_performance_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `dim_department` (`department_id`),
  CONSTRAINT `fact_student_performance_ibfk_3` FOREIGN KEY (`lifestyle_id`) REFERENCES `dim_lifestyle` (`lifestyle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=504 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-30 20:28:22
