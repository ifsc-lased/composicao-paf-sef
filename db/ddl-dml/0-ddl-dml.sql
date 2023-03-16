USE `daf-ws` ;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "-03:00";

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
-- Table structure for table `algoritmo`
--

DROP TABLE IF EXISTS `algoritmo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `algoritmo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ativo` bit(1) NOT NULL,
  `nome` varchar(5) DEFAULT NULL,
  `tam_chave` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algoritmo`
--

LOCK TABLES `algoritmo` WRITE;
/*!40000 ALTER TABLE `algoritmo` DISABLE KEYS */;
INSERT INTO `algoritmo` VALUES (1,_binary '','RS256',4096),(2,_binary '','ES384',384),(3,_binary '','ES512',512),(4,_binary '\0','RS256',1024),(5,_binary '','ES256',256),(6,_binary '','RS256',2048);
/*!40000 ALTER TABLE `algoritmo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anexo`
--

DROP TABLE IF EXISTS `anexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anexo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `arquivo` tinyblob,
  `descricao` varchar(255) DEFAULT NULL,
  `log_fk_processo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1fd16p898okwsfl57333k64cd` (`log_fk_processo_id`),
  CONSTRAINT `FK1fd16p898okwsfl57333k64cd` FOREIGN KEY (`log_fk_processo_id`) REFERENCES `log_processo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anexo`
--

LOCK TABLES `anexo` WRITE;
/*!40000 ALTER TABLE `anexo` DISABLE KEYS */;
/*!40000 ALTER TABLE `anexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aut_daf`
--

DROP TABLE IF EXISTS `aut_daf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aut_daf` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contador` int NOT NULL,
  `data_validacao` datetime(6) DEFAULT NULL,
  `id_aut` varchar(255) DEFAULT NULL,
  `daf_fk_id_daf` varchar(255) DEFAULT NULL,
  `dfe_fk_chdfe` varchar(44) DEFAULT NULL,
  `resultado_fk_cstat` int DEFAULT NULL,
  `software_basico_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK_1li72uib419ny680krbysop3b` (`id_aut`),
  KEY `FKdnlc4hleh5giq0af2xechdjex` (`daf_fk_id_daf`),
  KEY `FK6iaxgtv45y8kml9e1s7cbkt9y` (`dfe_fk_chdfe`),
  KEY `FKa7mvvrnrm3sobd1p5hlp5fifx` (`resultado_fk_cstat`),
  KEY `FKt8625p7onnnjanm5sv4a3s9ji` (`software_basico_id`),
  CONSTRAINT `FK6iaxgtv45y8kml9e1s7cbkt9y` FOREIGN KEY (`dfe_fk_chdfe`) REFERENCES `dfe` (`chdfe`),
  CONSTRAINT `FKa7mvvrnrm3sobd1p5hlp5fifx` FOREIGN KEY (`resultado_fk_cstat`) REFERENCES `resultado` (`cstat`),
  CONSTRAINT `FKdnlc4hleh5giq0af2xechdjex` FOREIGN KEY (`daf_fk_id_daf`) REFERENCES `daf` (`id_daf`),
  CONSTRAINT `FKt8625p7onnnjanm5sv4a3s9ji` FOREIGN KEY (`software_basico_id`) REFERENCES `software_basico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aut_daf`
--

LOCK TABLES `aut_daf` WRITE;
/*!40000 ALTER TABLE `aut_daf` DISABLE KEYS */;
INSERT INTO `aut_daf` VALUES (1,2,'2021-07-19 13:13:09.243000','BgefRedevu-hzECnG_lvJFgpu-poAmAL85pAAn7YDB0','ChAgT4LGSbKXo4UO8m6Cbg','42210728572444000110650017360564201332439096',1005,1),(2,0,'2021-07-19 13:13:09.390000',NULL,NULL,'42210728572444000110650012644207201448711551',2003,NULL),(3,0,'2021-07-19 13:13:09.494000',NULL,NULL,'42210728572444000110650018589717231454046760',2003,NULL);
/*!40000 ALTER TABLE `aut_daf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_EXECUTION`
--

DROP TABLE IF EXISTS `BATCH_JOB_EXECUTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_EXECUTION` (
  `JOB_EXECUTION_ID` bigint NOT NULL,
  `VERSION` bigint DEFAULT NULL,
  `JOB_INSTANCE_ID` bigint NOT NULL,
  `CREATE_TIME` datetime NOT NULL,
  `START_TIME` datetime DEFAULT NULL,
  `END_TIME` datetime DEFAULT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  `EXIT_CODE` varchar(2500) DEFAULT NULL,
  `EXIT_MESSAGE` varchar(2500) DEFAULT NULL,
  `LAST_UPDATED` datetime DEFAULT NULL,
  `JOB_CONFIGURATION_LOCATION` varchar(2500) DEFAULT NULL,
  PRIMARY KEY (`JOB_EXECUTION_ID`),
  KEY `JOB_INST_EXEC_FK` (`JOB_INSTANCE_ID`),
  CONSTRAINT `JOB_INST_EXEC_FK` FOREIGN KEY (`JOB_INSTANCE_ID`) REFERENCES `BATCH_JOB_INSTANCE` (`JOB_INSTANCE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_EXECUTION`
--

LOCK TABLES `BATCH_JOB_EXECUTION` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_EXECUTION` VALUES (1,2,1,'2021-07-19 13:12:52','2021-07-19 13:12:52','2021-07-19 13:12:53','COMPLETED','COMPLETED','','2021-07-19 13:12:53',NULL);
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_EXECUTION_CONTEXT`
--

DROP TABLE IF EXISTS `BATCH_JOB_EXECUTION_CONTEXT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_EXECUTION_CONTEXT` (
  `JOB_EXECUTION_ID` bigint NOT NULL,
  `SHORT_CONTEXT` varchar(2500) NOT NULL,
  `SERIALIZED_CONTEXT` text,
  PRIMARY KEY (`JOB_EXECUTION_ID`),
  CONSTRAINT `JOB_EXEC_CTX_FK` FOREIGN KEY (`JOB_EXECUTION_ID`) REFERENCES `BATCH_JOB_EXECUTION` (`JOB_EXECUTION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_EXECUTION_CONTEXT`
--

LOCK TABLES `BATCH_JOB_EXECUTION_CONTEXT` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_CONTEXT` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_EXECUTION_CONTEXT` VALUES (1,'{\"@class\":\"java.util.HashMap\"}',NULL);
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_CONTEXT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_EXECUTION_PARAMS`
--

DROP TABLE IF EXISTS `BATCH_JOB_EXECUTION_PARAMS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_EXECUTION_PARAMS` (
  `JOB_EXECUTION_ID` bigint NOT NULL,
  `TYPE_CD` varchar(6) NOT NULL,
  `KEY_NAME` varchar(100) NOT NULL,
  `STRING_VAL` varchar(250) DEFAULT NULL,
  `DATE_VAL` datetime DEFAULT NULL,
  `LONG_VAL` bigint DEFAULT NULL,
  `DOUBLE_VAL` double DEFAULT NULL,
  `IDENTIFYING` char(1) NOT NULL,
  KEY `JOB_EXEC_PARAMS_FK` (`JOB_EXECUTION_ID`),
  CONSTRAINT `JOB_EXEC_PARAMS_FK` FOREIGN KEY (`JOB_EXECUTION_ID`) REFERENCES `BATCH_JOB_EXECUTION` (`JOB_EXECUTION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_EXECUTION_PARAMS`
--

LOCK TABLES `BATCH_JOB_EXECUTION_PARAMS` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_PARAMS` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_EXECUTION_PARAMS` VALUES (1,'LONG','run.id','','1970-01-01 00:00:00',1,0,'Y');
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_PARAMS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_EXECUTION_SEQ`
--

DROP TABLE IF EXISTS `BATCH_JOB_EXECUTION_SEQ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_EXECUTION_SEQ` (
  `ID` bigint NOT NULL,
  `UNIQUE_KEY` char(1) NOT NULL,
  UNIQUE KEY `UNIQUE_KEY_UN` (`UNIQUE_KEY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_EXECUTION_SEQ`
--

LOCK TABLES `BATCH_JOB_EXECUTION_SEQ` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_SEQ` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_EXECUTION_SEQ` VALUES (1,'0');
/*!40000 ALTER TABLE `BATCH_JOB_EXECUTION_SEQ` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_INSTANCE`
--

DROP TABLE IF EXISTS `BATCH_JOB_INSTANCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_INSTANCE` (
  `JOB_INSTANCE_ID` bigint NOT NULL,
  `VERSION` bigint DEFAULT NULL,
  `JOB_NAME` varchar(100) NOT NULL,
  `JOB_KEY` varchar(32) NOT NULL,
  PRIMARY KEY (`JOB_INSTANCE_ID`),
  UNIQUE KEY `JOB_INST_UN` (`JOB_NAME`,`JOB_KEY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_INSTANCE`
--

LOCK TABLES `BATCH_JOB_INSTANCE` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_INSTANCE` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_INSTANCE` VALUES (1,0,'jobQuartz','853d3449e311f40366811cbefb3d93d7');
/*!40000 ALTER TABLE `BATCH_JOB_INSTANCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_JOB_SEQ`
--

DROP TABLE IF EXISTS `BATCH_JOB_SEQ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_JOB_SEQ` (
  `ID` bigint NOT NULL,
  `UNIQUE_KEY` char(1) NOT NULL,
  UNIQUE KEY `UNIQUE_KEY_UN` (`UNIQUE_KEY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_JOB_SEQ`
--

LOCK TABLES `BATCH_JOB_SEQ` WRITE;
/*!40000 ALTER TABLE `BATCH_JOB_SEQ` DISABLE KEYS */;
INSERT INTO `BATCH_JOB_SEQ` VALUES (1,'0');
/*!40000 ALTER TABLE `BATCH_JOB_SEQ` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_STEP_EXECUTION`
--

DROP TABLE IF EXISTS `BATCH_STEP_EXECUTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_STEP_EXECUTION` (
  `STEP_EXECUTION_ID` bigint NOT NULL,
  `VERSION` bigint NOT NULL,
  `STEP_NAME` varchar(100) NOT NULL,
  `JOB_EXECUTION_ID` bigint NOT NULL,
  `START_TIME` datetime NOT NULL,
  `END_TIME` datetime DEFAULT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  `COMMIT_COUNT` bigint DEFAULT NULL,
  `READ_COUNT` bigint DEFAULT NULL,
  `FILTER_COUNT` bigint DEFAULT NULL,
  `WRITE_COUNT` bigint DEFAULT NULL,
  `READ_SKIP_COUNT` bigint DEFAULT NULL,
  `WRITE_SKIP_COUNT` bigint DEFAULT NULL,
  `PROCESS_SKIP_COUNT` bigint DEFAULT NULL,
  `ROLLBACK_COUNT` bigint DEFAULT NULL,
  `EXIT_CODE` varchar(2500) DEFAULT NULL,
  `EXIT_MESSAGE` varchar(2500) DEFAULT NULL,
  `LAST_UPDATED` datetime DEFAULT NULL,
  PRIMARY KEY (`STEP_EXECUTION_ID`),
  KEY `JOB_EXEC_STEP_FK` (`JOB_EXECUTION_ID`),
  CONSTRAINT `JOB_EXEC_STEP_FK` FOREIGN KEY (`JOB_EXECUTION_ID`) REFERENCES `BATCH_JOB_EXECUTION` (`JOB_EXECUTION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_STEP_EXECUTION`
--

LOCK TABLES `BATCH_STEP_EXECUTION` WRITE;
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION` DISABLE KEYS */;
INSERT INTO `BATCH_STEP_EXECUTION` VALUES (1,3,'processarImportadosSVRS',1,'2021-07-19 13:12:52','2021-07-19 13:12:53','COMPLETED',1,0,0,0,0,0,0,0,'COMPLETED','','2021-07-19 13:12:53');
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_STEP_EXECUTION_CONTEXT`
--

DROP TABLE IF EXISTS `BATCH_STEP_EXECUTION_CONTEXT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_STEP_EXECUTION_CONTEXT` (
  `STEP_EXECUTION_ID` bigint NOT NULL,
  `SHORT_CONTEXT` varchar(2500) NOT NULL,
  `SERIALIZED_CONTEXT` text,
  PRIMARY KEY (`STEP_EXECUTION_ID`),
  CONSTRAINT `STEP_EXEC_CTX_FK` FOREIGN KEY (`STEP_EXECUTION_ID`) REFERENCES `BATCH_STEP_EXECUTION` (`STEP_EXECUTION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_STEP_EXECUTION_CONTEXT`
--

LOCK TABLES `BATCH_STEP_EXECUTION_CONTEXT` WRITE;
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION_CONTEXT` DISABLE KEYS */;
INSERT INTO `BATCH_STEP_EXECUTION_CONTEXT` VALUES (1,'{\"@class\":\"java.util.HashMap\",\"batch.taskletType\":\"br.edu.ifsc.lased.daf.jobs.Jobs$$Lambda$842/836077337\",\"batch.stepType\":\"org.springframework.batch.core.step.tasklet.TaskletStep\"}',NULL);
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION_CONTEXT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATCH_STEP_EXECUTION_SEQ`
--

DROP TABLE IF EXISTS `BATCH_STEP_EXECUTION_SEQ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATCH_STEP_EXECUTION_SEQ` (
  `ID` bigint NOT NULL,
  `UNIQUE_KEY` char(1) NOT NULL,
  UNIQUE KEY `UNIQUE_KEY_UN` (`UNIQUE_KEY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATCH_STEP_EXECUTION_SEQ`
--

LOCK TABLES `BATCH_STEP_EXECUTION_SEQ` WRITE;
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION_SEQ` DISABLE KEYS */;
INSERT INTO `BATCH_STEP_EXECUTION_SEQ` VALUES (1,'0');
/*!40000 ALTER TABLE `BATCH_STEP_EXECUTION_SEQ` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `certificacao`
--

DROP TABLE IF EXISTS `certificacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certificacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aviso_vigencia` datetime(6) DEFAULT NULL,
  `fim_vigencia` datetime(6) DEFAULT NULL,
  `inicio_vigencia` datetime(6) DEFAULT NULL,
  `processo_certificacao_fk_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKi5kv7hcpe0vitpe6jh23bqjud` (`processo_certificacao_fk_id`),
  CONSTRAINT `FKi5kv7hcpe0vitpe6jh23bqjud` FOREIGN KEY (`processo_certificacao_fk_id`) REFERENCES `processo_certificacao` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `certificacao`
--

LOCK TABLES `certificacao` WRITE;
/*!40000 ALTER TABLE `certificacao` DISABLE KEYS */;
INSERT INTO `certificacao` VALUES (1,NULL,'2021-07-11 13:12:55.533000','2020-07-11 13:12:55.533000',1),(2,NULL,'2021-07-11 13:12:55.533000','2020-07-11 13:12:55.533000',2),(3,NULL,'2021-07-11 13:12:55.533000','2020-07-11 13:12:55.533000',3),(4,NULL,'2022-07-11 13:12:55.533000','2021-07-11 13:12:55.533000',4),(5,NULL,NULL,'2021-07-11 13:12:55.533000',5),(6,NULL,'2022-07-11 13:12:55.533000','2021-07-11 13:12:55.533000',6),(7,NULL,NULL,'2021-07-12 13:13:09.527000',7),(8,NULL,NULL,'2021-07-12 13:13:09.527000',8);
/*!40000 ALTER TABLE `certificacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `certificado_sef`
--

DROP TABLE IF EXISTS `certificado_sef`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certificado_sef` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cfp` varchar(255) NOT NULL,
  `ca_cfp` varchar(255) NOT NULL,
  `aviso_vigencia` datetime(6) DEFAULT NULL,
  `fim_vigencia` datetime(6) DEFAULT NULL,
  `inicio_vigencia` datetime(6) DEFAULT NULL,
  `keystore_file` varchar(255) DEFAULT NULL,
  `keystore_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `certificado_sef`
--

LOCK TABLES `certificado_sef` WRITE;
/*!40000 ALTER TABLE `certificado_sef` DISABLE KEYS */;
INSERT INTO `certificado_sef` VALUES (1,'J33D3Kr4R0TKyHYm3TYtUIhvOjAFmOg86x63ndD-bAU','J33D3Kr4R0TKyHYm3TYtUIhvOjAFmOg86x63ndD-bAU',NULL,NULL,'2021-07-11 13:12:55.533000','sef-rsa-2048.pkcs12','PKCS12'),(2,'utBtrlaIFV_zKR6oZMtV0oXARqlSfCa0pT2uHaDJLe8','utBtrlaIFV_zKR6oZMtV0oXARqlSfCa0pT2uHaDJLe8',NULL,NULL,'2021-07-12 13:13:09.527000','sef-rsa-4096.pkcs12','PKCS12'),(3,'SdFcN6lp3DImbcsgZBOPvXc2HMdBC3juLkD6ee4Fz5w','SdFcN6lp3DImbcsgZBOPvXc2HMdBC3juLkD6ee4Fz5w',NULL,NULL,'2021-07-12 13:13:09.527000','sef-ec-384.pkcs12','PKCS12');
/*!40000 ALTER TABLE `certificado_sef` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `certificado_sef_algoritmo`
--

DROP TABLE IF EXISTS `certificado_sef_algoritmo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certificado_sef_algoritmo` (
  `certificado_sef_fk_id` int NOT NULL,
  `algoritmo_fk_id` int NOT NULL,
  PRIMARY KEY (`certificado_sef_fk_id`,`algoritmo_fk_id`),
  KEY `FKrmxupoi4htkput0fr2s5ngfoq` (`algoritmo_fk_id`),
  CONSTRAINT `FKd3warr0r3209kf4po1wgoeicp` FOREIGN KEY (`certificado_sef_fk_id`) REFERENCES `certificado_sef` (`id`),
  CONSTRAINT `FKrmxupoi4htkput0fr2s5ngfoq` FOREIGN KEY (`algoritmo_fk_id`) REFERENCES `algoritmo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `certificado_sef_algoritmo`
--

LOCK TABLES `certificado_sef_algoritmo` WRITE;
/*!40000 ALTER TABLE `certificado_sef_algoritmo` DISABLE KEYS */;
INSERT INTO `certificado_sef_algoritmo` VALUES (2,1),(3,2),(1,6);
/*!40000 ALTER TABLE `certificado_sef_algoritmo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `certificadora`
--

DROP TABLE IF EXISTS `certificadora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certificadora` (
  `pessoa_juridica_fk_cnpj` varchar(14) NOT NULL,
  PRIMARY KEY (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FK50bshy76e2sejjfwbuj7ki5cs` FOREIGN KEY (`pessoa_juridica_fk_cnpj`) REFERENCES `pessoa_juridica` (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `certificadora`
--

LOCK TABLES `certificadora` WRITE;
/*!40000 ALTER TABLE `certificadora` DISABLE KEYS */;
INSERT INTO `certificadora` VALUES ('67321567000130'),('77830710000173');
/*!40000 ALTER TABLE `certificadora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribuinte`
--

DROP TABLE IF EXISTS `contribuinte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contribuinte` (
  `credenciado_nfe` int NOT NULL,
  `situacao` int NOT NULL,
  `pessoa_juridica_fk_cnpj` varchar(14) NOT NULL,
  PRIMARY KEY (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FKesdcthljr4c6o0sn1v5wn98wo` FOREIGN KEY (`pessoa_juridica_fk_cnpj`) REFERENCES `pessoa_juridica` (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribuinte`
--

LOCK TABLES `contribuinte` WRITE;
/*!40000 ALTER TABLE `contribuinte` DISABLE KEYS */;
INSERT INTO `contribuinte` VALUES (1,1,'28572444000110'),(1,0,'66380626000189'),(1,1,'89340307000145');
/*!40000 ALTER TABLE `contribuinte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `csrt`
--

DROP TABLE IF EXISTS `csrt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `csrt` (
  `id_csrt` int NOT NULL,
  `csrt` varchar(36) DEFAULT NULL,
  `revogado` bit(1) NOT NULL,
  `fabricante_fk_cnpj` varchar(14) NOT NULL,
  PRIMARY KEY (`fabricante_fk_cnpj`,`id_csrt`),
  UNIQUE KEY `UKqv2kg9rkur8yqnis5udg7vxvv` (`id_csrt`,`fabricante_fk_cnpj`,`csrt`),
  CONSTRAINT `FKew99na6je21flmffxwa03i9jm` FOREIGN KEY (`fabricante_fk_cnpj`) REFERENCES `fabricante` (`pessoa_juridica_fk_cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `csrt`
--

LOCK TABLES `csrt` WRITE;
/*!40000 ALTER TABLE `csrt` DISABLE KEYS */;
INSERT INTO `csrt` VALUES (1,'S6FP4DHL6RZW8A2BYBXM2XJV0ECTGQJSTUJD',_binary '\0','87528541000175'),(2,'YKQFGV4KJXG3Q994M6WJZ6THXIQO2FJH1YDP',_binary '','87528541000175');
/*!40000 ALTER TABLE `csrt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daf`
--

DROP TABLE IF EXISTS `daf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daf` (
  `id_daf` varchar(255) NOT NULL,
  `contador_atual` int NOT NULL,
  `cfp_atual` varchar(255) DEFAULT NULL,
  `data_extravio` datetime(6) DEFAULT NULL,
  `justificativa_extravio` varchar(255) DEFAULT NULL,
  `situacao` int NOT NULL,
  `modelo_daf_fk_id` int DEFAULT NULL,
  PRIMARY KEY (`id_daf`),
  KEY `FKq4y5q6vj13xtvrb1egrostuf4` (`modelo_daf_fk_id`),
  CONSTRAINT `FKq4y5q6vj13xtvrb1egrostuf4` FOREIGN KEY (`modelo_daf_fk_id`) REFERENCES `modelo_daf` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daf`
--

LOCK TABLES `daf` WRITE;
/*!40000 ALTER TABLE `daf` DISABLE KEYS */;
INSERT INTO `daf` VALUES ('ChAgT4LGSbKXo4UO8m6Cbg',2,'SdFcN6lp3DImbcsgZBOPvXc2HMdBC3juLkD6ee4Fz5w',NULL,NULL,1,2);
/*!40000 ALTER TABLE `daf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dfe`
--

DROP TABLE IF EXISTS `dfe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dfe` (
  `chdfe` varchar(44) NOT NULL,
  `autorizacao_daf` varchar(300) DEFAULT NULL,
  `data_emissao` datetime(6) DEFAULT NULL,
  `modelo` int NOT NULL,
  `protocolo_autorizacao` varchar(15) DEFAULT NULL,
  `status_resposta` varchar(4) DEFAULT NULL,
  `tp_amb` int NOT NULL,
  `xml_dfe_distribuicao` longtext,
  `contribuinte_fk_cnpj` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`chdfe`),
  KEY `FKtpiw0i65oqakg9232ycyr6hj2` (`contribuinte_fk_cnpj`),
  CONSTRAINT `FKtpiw0i65oqakg9232ycyr6hj2` FOREIGN KEY (`contribuinte_fk_cnpj`) REFERENCES `contribuinte` (`pessoa_juridica_fk_cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dfe`
--

LOCK TABLES `dfe` WRITE;
/*!40000 ALTER TABLE `dfe` DISABLE KEYS */;
INSERT INTO `dfe` VALUES ('42210728572444000110650012644207201448711551','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6ImdpQTRQYzA3OTN2ZEE3YTdMVkhuZkRYSmpxZWxId28yZ1cta3NTOGVtX00ifQ.FQmxSr9n2HBalq2UQdQo_yTKtK0z5bZDObY4xOdKEvw','2021-07-20 15:01:02.000000',65,'727439425308376','100',1,'<nfeProc xmlns=\"http://www.portalfiscal.inf.br/nfe\" versao=\"4.00\"><NFe><infNFe Id=\"NFe42210728572444000110650012644207201448711551\" versao=\"4.00\"><ide><cUF>42</cUF><cNF>44871155</cNF><natOp>VENDA DE MERCADORIA CONFORME CFOP</natOp><mod>65</mod><serie>1</serie><nNF>264420720</nNF><dhEmi>2021-7-20T12:01:02-03:00</dhEmi><tpNF>1</tpNF><idDest>1</idDest><cMunFG>4205407</cMunFG><tpImp>5</tpImp><tpEmis>1</tpEmis><cDV>1</cDV><tpAmb>1</tpAmb><finNFe>1</finNFe><indFinal>1</indFinal><indPres>1</indPres><procEmi>0</procEmi><verProc>NFC-e93</verProc></ide><total><ICMSTot><vBC>0.00</vBC><vICMS>0.00</vICMS><vICMSDeson>0.00</vICMSDeson><vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST><vFCPST>0.00</vFCPST><vFCPSTRet>0.00</vFCPSTRet><vProd>0.00</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc><vII>0.00</vII><vIPI>0.00</vIPI><vIPIDevol>0.00</vIPIDevol><vPIS>0.00</vPIS><vCOFINS>0.00</vCOFINS><vOutro>0.00</vOutro><vNF>0.00</vNF><vTotTrib>0.00</vTotTrib></ICMSTot></total><infRespTec><CNPJ>36675777000101</CNPJ><xContato>4450482106</xContato></infRespTec><infAdic><infAdFisco>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6ImdpQTRQYzA3OTN2ZEE3YTdMVkhuZkRYSmpxZWxId28yZ1cta3NTOGVtX00ifQ.FQmxSr9n2HBalq2UQdQo_yTKtK0z5bZDObY4xOdKEvw</infAdFisco></infAdic></infNFe></NFe><protNFe versao=\"4.00\"><infProt Id=\"ID727439425308376\"><tpAmb>1</tpAmb><verAplic>1</verAplic><chNFe>42210728572444000110650012644207201448711551</chNFe><dhRecbto>2021-7-20T13:01:02-03:00</dhRecbto><nProt>727439425308376</nProt><digVal>UThSTUZGU0pZSEkwM0lFRFpXODA=</digVal><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe></nfeProc>','28572444000110'),('42210728572444000110650017360564201332439096','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6IkJnZWZSZWRldnUtaHpFQ25HX2x2SkZncHUtcG9BbUFMODVwQUFuN1lEQjAifQ.nj-tJEzlqLqfvP5SMXiISTefZBIMYfhyTCG-xvRZlug','2021-07-20 15:01:02.000000',65,'346641684802574','100',1,'<nfeProc xmlns=\"http://www.portalfiscal.inf.br/nfe\" versao=\"4.00\"><NFe><infNFe Id=\"NFe42210728572444000110650017360564201332439096\" versao=\"4.00\"><ide><cUF>42</cUF><cNF>33243909</cNF><natOp>VENDA DE MERCADORIA CONFORME CFOP</natOp><mod>65</mod><serie>1</serie><nNF>736056420</nNF><dhEmi>2021-7-20T12:01:02-03:00</dhEmi><tpNF>1</tpNF><idDest>1</idDest><cMunFG>4205407</cMunFG><tpImp>5</tpImp><tpEmis>1</tpEmis><cDV>6</cDV><tpAmb>1</tpAmb><finNFe>1</finNFe><indFinal>1</indFinal><indPres>1</indPres><procEmi>0</procEmi><verProc>NFC-e25</verProc></ide><total><ICMSTot><vBC>0.00</vBC><vICMS>0.00</vICMS><vICMSDeson>0.00</vICMSDeson><vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST><vFCPST>0.00</vFCPST><vFCPSTRet>0.00</vFCPSTRet><vProd>0.00</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc><vII>0.00</vII><vIPI>0.00</vIPI><vIPIDevol>0.00</vIPIDevol><vPIS>0.00</vPIS><vCOFINS>0.00</vCOFINS><vOutro>0.00</vOutro><vNF>0.00</vNF><vTotTrib>0.00</vTotTrib></ICMSTot></total><infRespTec><CNPJ>15054433000105</CNPJ><xContato>5453035597</xContato></infRespTec><infAdic><infAdFisco>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6IkJnZWZSZWRldnUtaHpFQ25HX2x2SkZncHUtcG9BbUFMODVwQUFuN1lEQjAifQ.nj-tJEzlqLqfvP5SMXiISTefZBIMYfhyTCG-xvRZlug</infAdFisco></infAdic></infNFe></NFe><protNFe versao=\"4.00\"><infProt Id=\"ID346641684802574\"><tpAmb>1</tpAmb><verAplic>1</verAplic><chNFe>42210728572444000110650017360564201332439096</chNFe><dhRecbto>2021-7-20T13:01:02-03:00</dhRecbto><nProt>346641684802574</nProt><digVal>OEZOTUNUVzFZTVdJTk1KR0xaS1E=</digVal><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe></nfeProc>','28572444000110'),('42210728572444000110650018589717231454046760','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6ImtoRkplaC1aUWNHRUFTRUNNLU9lcHVyelpUZU1YUGxpRldrLXZPeHV3WEkifQ.Dgcy-dJmvzlYn4ziaIxuXF-wynwtNf_dIDi2xiSJ8TA','2021-07-20 15:01:02.000000',65,'575438839822543','100',1,'<nfeProc xmlns=\"http://www.portalfiscal.inf.br/nfe\" versao=\"4.00\"><NFe><infNFe Id=\"NFe42210728572444000110650018589717231454046760\" versao=\"4.00\"><ide><cUF>42</cUF><cNF>45404676</cNF><natOp>VENDA DE MERCADORIA CONFORME CFOP</natOp><mod>65</mod><serie>1</serie><nNF>858971723</nNF><dhEmi>2021-7-20T12:01:02-03:00</dhEmi><tpNF>1</tpNF><idDest>1</idDest><cMunFG>4205407</cMunFG><tpImp>5</tpImp><tpEmis>1</tpEmis><cDV>0</cDV><tpAmb>1</tpAmb><finNFe>1</finNFe><indFinal>1</indFinal><indPres>1</indPres><procEmi>0</procEmi><verProc>NFC-e29</verProc></ide><total><ICMSTot><vBC>0.00</vBC><vICMS>0.00</vICMS><vICMSDeson>0.00</vICMSDeson><vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST><vFCPST>0.00</vFCPST><vFCPSTRet>0.00</vFCPSTRet><vProd>0.00</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc><vII>0.00</vII><vIPI>0.00</vIPI><vIPIDevol>0.00</vIPIDevol><vPIS>0.00</vPIS><vCOFINS>0.00</vCOFINS><vOutro>0.00</vOutro><vNF>0.00</vNF><vTotTrib>0.00</vTotTrib></ICMSTot></total><infRespTec><CNPJ>89734149000108</CNPJ><xContato>2847541759</xContato></infRespTec><infAdic><infAdFisco>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYWYiOiJDaEFnVDRMR1NiS1hvNFVPOG02Q2JnIiwibW9wIjowLCJ2c2IiOjEsInBkdiI6Ing0WW93Sm82WHMiLCJjbnQiOjIsImF1dCI6ImtoRkplaC1aUWNHRUFTRUNNLU9lcHVyelpUZU1YUGxpRldrLXZPeHV3WEkifQ.Dgcy-dJmvzlYn4ziaIxuXF-wynwtNf_dIDi2xiSJ8TA</infAdFisco></infAdic></infNFe></NFe><protNFe versao=\"4.00\"><infProt Id=\"ID575438839822543\"><tpAmb>1</tpAmb><verAplic>1</verAplic><chNFe>42210728572444000110650018589717231454046760</chNFe><dhRecbto>2021-7-20T13:01:02-03:00</dhRecbto><nProt>575438839822543</nProt><digVal>RlhUUlVMOTdUWTRTNVNXMFIxRUs=</digVal><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe></nfeProc>','28572444000110');
/*!40000 ALTER TABLE `dfe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `endereco`
--

DROP TABLE IF EXISTS `endereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `endereco` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bairro` varchar(255) DEFAULT NULL,
  `cep` varchar(255) DEFAULT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `logradouro` varchar(255) DEFAULT NULL,
  `numero` varchar(255) DEFAULT NULL,
  `municipio_fk_codigo_ibge` int DEFAULT NULL,
  `pessoa_juridica_fk_cnpj` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK1teclgh0syag80fomj530gsag` (`municipio_fk_codigo_ibge`),
  KEY `FKd5tfvvmt2p9ooyjcwq6l6vbsu` (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FK1teclgh0syag80fomj530gsag` FOREIGN KEY (`municipio_fk_codigo_ibge`) REFERENCES `municipio` (`codigo_ibge`),
  CONSTRAINT `FKd5tfvvmt2p9ooyjcwq6l6vbsu` FOREIGN KEY (`pessoa_juridica_fk_cnpj`) REFERENCES `pessoa_juridica` (`cnpj`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `endereco`
--

LOCK TABLES `endereco` WRITE;
/*!40000 ALTER TABLE `endereco` DISABLE KEYS */;
INSERT INTO `endereco` VALUES (1,'Moxosazelus','98629518','Sala ','Rajacaqix Zyjecaze','Quadra','',4216503,'28572444000110'),(2,'Bewupalex','47004560','Sala 8','Degewe Maroxop','sarela','3',4206108,'28572444000110'),(3,'Vegebanupoju','97737339','Sala 3','Hituhu Pavytex','Estrada','',4203808,'66380626000189'),(4,'Sonynemi','18348308','Sala 8','Wuwygezil Ricyqokutada','Vereda','',4202602,'87528541000175'),(5,'Mycalehu','05003554','Sala 20','Dyhavofupez Cequgik','Parque','',4205506,'86096781000185'),(6,'Bevor','92430028','Sala 64','Fofeha Jelykabucem','sarela','2',4200705,'67321567000130'),(7,'Bedikykunux','05155899','Sala ','Syxu Cenuvomo','Loteamento','',4203253,'77830710000173');
/*!40000 ALTER TABLE `endereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etapa`
--

DROP TABLE IF EXISTS `etapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `etapa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `ordem` int NOT NULL,
  `tipo` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etapa`
--

LOCK TABLES `etapa` WRITE;
/*!40000 ALTER TABLE `etapa` DISABLE KEYS */;
INSERT INTO `etapa` VALUES (1,'Início',1,1),(2,'Análise da Documentaçao',2,1),(3,'Análise dos fontes',3,1),(4,'Geraçao da certificaçao',4,1),(5,'Finalizaçao',5,1),(6,'Início',1,2),(7,'Análise da Documentaçao',2,2),(8,'Análise dos fontes do firmeware',3,2),(9,'Análise do hardware',4,2),(10,'Análise dos fontes',5,2),(11,'Geraçao da certificaçao',6,2),(12,'Finalizaçao',7,2),(13,'Início',1,3),(14,'Análise da Documentaçao',2,3),(15,'Análise dos fontes',3,3),(16,'Geraçao da certificaçao',4,3),(17,'Finalizaçao',5,3);
/*!40000 ALTER TABLE `etapa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fabricante`
--

DROP TABLE IF EXISTS `fabricante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fabricante` (
  `daf` bit(1) NOT NULL,
  `paf` bit(1) NOT NULL,
  `pessoa_juridica_fk_cnpj` varchar(14) NOT NULL,
  PRIMARY KEY (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FK8oxdv6ev9vd96mhvoilnhotve` FOREIGN KEY (`pessoa_juridica_fk_cnpj`) REFERENCES `pessoa_juridica` (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fabricante`
--

LOCK TABLES `fabricante` WRITE;
/*!40000 ALTER TABLE `fabricante` DISABLE KEYS */;
INSERT INTO `fabricante` VALUES (_binary '',_binary '\0','86096781000185'),(_binary '\0',_binary '','87528541000175');
/*!40000 ALTER TABLE `fabricante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_processo`
--

DROP TABLE IF EXISTS `log_processo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_processo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comentario` varchar(255) DEFAULT NULL,
  `etapa_fk_id` int DEFAULT NULL,
  `processo_fk_certificacao_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKsarec7cjoxy564mapk2yn8m51` (`etapa_fk_id`),
  KEY `FKg2wcocgklysro2yu9o0qtuyif` (`processo_fk_certificacao_id`),
  CONSTRAINT `FKg2wcocgklysro2yu9o0qtuyif` FOREIGN KEY (`processo_fk_certificacao_id`) REFERENCES `processo_certificacao` (`id`),
  CONSTRAINT `FKsarec7cjoxy564mapk2yn8m51` FOREIGN KEY (`etapa_fk_id`) REFERENCES `etapa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_processo`
--

LOCK TABLES `log_processo` WRITE;
/*!40000 ALTER TABLE `log_processo` DISABLE KEYS */;
INSERT INTO `log_processo` VALUES (1,'início',1,1),(2,'fim',5,1),(3,'início',6,2),(4,'fim',12,2),(5,'início',13,3),(6,'fim',17,3),(7,'início',1,4),(8,'fim',5,4),(9,'início',6,5),(10,'fim',12,5),(11,'início',13,6),(12,'fim',17,6),(13,'início',6,7),(14,'fim',12,7),(15,'início',13,8),(16,'fim',17,8);
/*!40000 ALTER TABLE `log_processo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelo_daf`
--

DROP TABLE IF EXISTS `modelo_daf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelo_daf` (
  `id` int NOT NULL AUTO_INCREMENT,
  `chave_ateste` varchar(2000) DEFAULT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `algoritmo_fk_id` int DEFAULT NULL,
  `certificacao_fk_id` int DEFAULT NULL,
  `fabricante_fk_cnpj` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_modelo_nome_cnpj` (`nome`,`fabricante_fk_cnpj`),
  KEY `FKoakhwdwwbcd1xaqf2fo2fo7wd` (`algoritmo_fk_id`),
  KEY `FKh20e9wdtkft39h6y4s4j8djhy` (`certificacao_fk_id`),
  KEY `FKen4kle8ij88n9waf7yrxv27wo` (`fabricante_fk_cnpj`),
  CONSTRAINT `FKen4kle8ij88n9waf7yrxv27wo` FOREIGN KEY (`fabricante_fk_cnpj`) REFERENCES `fabricante` (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FKh20e9wdtkft39h6y4s4j8djhy` FOREIGN KEY (`certificacao_fk_id`) REFERENCES `certificacao` (`id`),
  CONSTRAINT `FKoakhwdwwbcd1xaqf2fo2fo7wd` FOREIGN KEY (`algoritmo_fk_id`) REFERENCES `algoritmo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelo_daf`
--

LOCK TABLES `modelo_daf` WRITE;
/*!40000 ALTER TABLE `modelo_daf` DISABLE KEYS */;
INSERT INTO `modelo_daf` VALUES (1,'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApM31Ezbk1IU+gKc32kKVng0MC6iRux8BpjzFqyefC7mxEZGHowuJk5HHqYFNj8GM0U5+QvxGHw/Ug/a/MlFS6FiVWq65+5PJCFqKuda8UMn7ArnE2U6Y6ZlbS8CtrdtLSigIa8hzL1XnY2OUPCITFBKjPJ6xO1isGfZUjBAYqnqwG367ugoHQZYCYhJzzHBMuiRFqxXu73evK0gQc1iiY3LDqwiGzVbOZq3ZYXPk3F406/rse7+K/JA39DrePLbvs8W4pR2A7JJ9sLlITP6stRqPE2ufsuUM252C50SqK/fhg/JwtPsU/54J2iFVGmIldGgeXnvzOqWgh0SxENLG9h455MHqLTLXIdC5VNa3h48St77pPlOb2nBgj3ElA3PtM0u60H8u6VFgkDBGcZAI5r6y2F7fDLKuC82kt6aUO6Y8AFKvNJ7LiYsqvhU5cWHLt497jb6GrsTrMc8HE2RUQ0Q/+CNMZQkpP4m3YzpxxbTuv03XYuYnAIXKgp1B21IKVS1zxFPZJBWg88UtQKqc+HvSuAYk8FFGjMPktdyFlgka/F9xWK5Fu1wb2EUZGg+wzDxNndhnre9S4F66iv+4XjuMdTRhlu9AUKv6fT2a+lLPvxkuQ6nbF6fYTsAhN73bhmXiNsFCgpaH6hDWbSMm0a8MZSbhLNA5dagdsupZ3DkCAwEAAQ==','modelo-vencido',1,2,'86096781000185'),(2,'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAnbCa7Pv3JAm0J3aZ5CzkPiNijVPPONCp663JdajQGSMRbPFEPBUOpY78hKA3tKMeJKQNmsYelJ/IqnAffQiWUNKbcGU65TI77grjpD+ZsFQ3qnR4LyRi68tXu+dX5wMAp7DEfo/CP0pzfV8WxyRKNFtTj64PwSPz5I4EVzA/trdSDokhC8czfI4lI7XaJHEhLC4mnJadGpB47nZVM8vISsjaBO3Fg118zX1zHbognSOdmsNzeB8GuULUotM46SFIu91aoGxiDhrWwYBIhaUwNAyi0vkgJhW7qg981AFwyL66sk1LZB7sVy2usbOLf/T8rmRcLvr5hlQ9g/ySMzYZT1GDM0wJEFZ6xBpYRKyxU+jtVAPIaiNMT4l7EBqUK0D1qoDn5vblzwtCUcWR+2eamvb/Xkv0V9tGjyHDhSukFUyVqvlKfXYY4jlscQiXwAHCXL5+HR0gSGM5uSzmhAdEDpXJdtDBO3OGx9szYkOPDGFUVkZWNTpnTPrlHtsWuJLCW3g0hM/IDYPMdtrts62ZEh6gPEKMOjoyir3zHD5RHwh+B09MR60bsw4Up2BGhPLyplmLAXTuV+rFUt/IXatYF7RR5rSPjycmJR0Mfg8skxQb9E6J0oqc4KgDhFLC95+TWPCvAPs7DGoupZdPdYj8zDIfhy3VFsUCX2LodF9M+ocCAwEAAQ==','modelo-ok',1,5,'86096781000185'),(3,'MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAElNXZ/NYjXC0NbsDrsSEQptfGDiwKzr3KK/Pndzt7dOVx70jITvLB5Zf9f2oA5+egrpMGIq/NFw8noDRPaz/CZn02kM0yAa4wXRlpuPz1Ph4ihqWH+2qFFiOqdjp22S/0','daf-pi',2,7,'86096781000185');
/*!40000 ALTER TABLE `modelo_daf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelo_daf_certificados_sef`
--

DROP TABLE IF EXISTS `modelo_daf_certificados_sef`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelo_daf_certificados_sef` (
  `alias_certificado_sef` varchar(255) DEFAULT NULL,
  `aviso_vigencia` datetime(6) DEFAULT NULL,
  `fim_vigencia` datetime(6) DEFAULT NULL,
  `inicio_vigencia` datetime(6) DEFAULT NULL,
  `certificado_sef_fk_id` int NOT NULL,
  `modelo_daf_fk_id` int NOT NULL,
  PRIMARY KEY (`certificado_sef_fk_id`,`modelo_daf_fk_id`),
  KEY `FKhs4vh8yj1fp9aoig587c4sye4` (`modelo_daf_fk_id`),
  CONSTRAINT `FKhs4vh8yj1fp9aoig587c4sye4` FOREIGN KEY (`modelo_daf_fk_id`) REFERENCES `modelo_daf` (`id`),
  CONSTRAINT `FKkrb8gf17kt7xvr5erh3t8lt48` FOREIGN KEY (`certificado_sef_fk_id`) REFERENCES `certificado_sef` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelo_daf_certificados_sef`
--

LOCK TABLES `modelo_daf_certificados_sef` WRITE;
/*!40000 ALTER TABLE `modelo_daf_certificados_sef` DISABLE KEYS */;
INSERT INTO `modelo_daf_certificados_sef` VALUES ('1',NULL,NULL,'2021-07-11 13:12:55.533000',1,1),('1',NULL,NULL,'2021-07-11 13:12:55.533000',1,2),('1',NULL,NULL,'2021-07-12 13:13:09.527000',2,4),('1',NULL,NULL,'2021-07-12 13:13:09.527000',3,3);
/*!40000 ALTER TABLE `modelo_daf_certificados_sef` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelo_daf_software_basico`
--

DROP TABLE IF EXISTS `modelo_daf_software_basico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelo_daf_software_basico` (
  `software_basico_fk_id` int NOT NULL,
  `modelo_daf_fk_id` int NOT NULL,
  PRIMARY KEY (`modelo_daf_fk_id`,`software_basico_fk_id`),
  KEY `FKhojsqurrpjr7y8g7qf6w7ej6h` (`software_basico_fk_id`),
  CONSTRAINT `FKhojsqurrpjr7y8g7qf6w7ej6h` FOREIGN KEY (`software_basico_fk_id`) REFERENCES `software_basico` (`id`),
  CONSTRAINT `FKqmoe7r4r301uqtp3pnhone75g` FOREIGN KEY (`modelo_daf_fk_id`) REFERENCES `modelo_daf` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelo_daf_software_basico`
--

LOCK TABLES `modelo_daf_software_basico` WRITE;
/*!40000 ALTER TABLE `modelo_daf_software_basico` DISABLE KEYS */;
INSERT INTO `modelo_daf_software_basico` VALUES (1,1),(1,2),(2,1),(2,2),(3,3),(3,4);
/*!40000 ALTER TABLE `modelo_daf_software_basico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `municipio`
--

DROP TABLE IF EXISTS `municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `municipio` (
  `codigo_ibge` int NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `uf_fk_codigo_ibge` int DEFAULT NULL,
  PRIMARY KEY (`codigo_ibge`),
  KEY `FKh21ndo0wwx8k10d178kao8asp` (`uf_fk_codigo_ibge`),
  CONSTRAINT `FKh21ndo0wwx8k10d178kao8asp` FOREIGN KEY (`uf_fk_codigo_ibge`) REFERENCES `uf` (`codigo_ibge`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipio`
--

LOCK TABLES `municipio` WRITE;
/*!40000 ALTER TABLE `municipio` DISABLE KEYS */;
INSERT INTO `municipio` VALUES (4200051,'Abdon Batista',42),(4200101,'Abelardo Luz',42),(4200200,'Agrolândia',42),(4200309,'Agronomica',42),(4200408,'Agua Doce',42),(4200507,'Aguas de Chapeco',42),(4200556,'Aguas Frias',42),(4200606,'Aguas Mornas',42),(4200705,'Alfredo Wagner',42),(4200754,'Alto Bela Vista',42),(4200804,'Anchieta',42),(4200903,'Angelina',42),(4201000,'Anita Garibaldi',42),(4201109,'Anitapolis',42),(4201208,'Antonio Carlos',42),(4201257,'Apiuna',42),(4201273,'Arabuta',42),(4201307,'Araquari',42),(4201406,'Ararangua',42),(4201505,'Armazem',42),(4201604,'Arroio Trinta',42),(4201653,'Arvoredo',42),(4201703,'Ascurra',42),(4201802,'Atalanta',42),(4201901,'Aurora',42),(4201950,'Balneario Arroio do Silva',42),(4202008,'Balneario Camboriu',42),(4202057,'Balneario Barra do Sul',42),(4202073,'Balneario Gaivota',42),(4202081,'Bandeirante',42),(4202099,'Barra Bonita',42),(4202107,'Barra Velha',42),(4202131,'Bela Vista do Toldo',42),(4202156,'Belmonte',42),(4202206,'Benedito Novo',42),(4202305,'Biguacu',42),(4202404,'Blumenau',42),(4202438,'Bocaina do Sul',42),(4202453,'Bombinhas',42),(4202503,'Bom Jardim da Serra',42),(4202537,'Bom Jesus',42),(4202578,'Bom Jesus do Oeste',42),(4202602,'Bom Retiro',42),(4202701,'Botuvera',42),(4202800,'Braco do Norte',42),(4202859,'Braco do Trombudo',42),(4202875,'Brunopolis',42),(4202909,'Brusque',42),(4203006,'Cacador',42),(4203105,'Caibi',42),(4203154,'Calmon',42),(4203204,'Camboriu',42),(4203253,'Capao Alto',42),(4203303,'Campo Alegre',42),(4203402,'Campo Belo do Sul',42),(4203501,'Campo Ere',42),(4203600,'Campos Novos',42),(4203709,'Canelinha',42),(4203808,'Canoinhas',42),(4203907,'Capinzal',42),(4203956,'Capivari de Baixo',42),(4204004,'Catanduvas',42),(4204103,'Caxambu do Sul',42),(4204152,'Celso Ramos',42),(4204178,'Cerro Negro',42),(4204194,'Chapadao do Lageado',42),(4204202,'Chapeco',42),(4204251,'Cocal do Sul',42),(4204301,'Concordia',42),(4204350,'Cordilheira Alta',42),(4204400,'Coronel Freitas',42),(4204459,'Coronel Martins',42),(4204509,'Corupa',42),(4204558,'Correia Pinto',42),(4204608,'Criciuma',42),(4204707,'Cunha Pora',42),(4204756,'Cunhatai',42),(4204806,'Curitibanos',42),(4204905,'Descanso',42),(4205001,'Dionisio Cerqueira',42),(4205100,'Dona Emma',42),(4205159,'Doutor Pedrinho',42),(4205175,'Entre Rios',42),(4205191,'Ermo',42),(4205209,'Erval Velho',42),(4205308,'Faxinal dos Guedes',42),(4205357,'Flor do Sertao',42),(4205407,'Florianopolis',42),(4205431,'Formosa do Sul',42),(4205456,'Forquilhinha',42),(4205506,'Fraiburgo',42),(4205555,'Frei Rogerio',42),(4205605,'Galvao',42),(4205704,'Garopaba',42),(4205803,'Garuva',42),(4205902,'Gaspar',42),(4206009,'Governador Celso Ramos',42),(4206108,'Grao Para',42),(4206207,'Gravatal',42),(4206306,'Guabiruba',42),(4206405,'Guaraciaba',42),(4206504,'Guaramirim',42),(4206603,'Guaruja do Sul',42),(4206652,'Guatambu',42),(4206702,'Herval dOeste',42),(4206751,'Ibiam',42),(4206801,'Ibicare',42),(4206900,'Ibirama',42),(4207007,'Icara',42),(4207106,'Ilhota',42),(4207205,'Imarui',42),(4207304,'Imbituba',42),(4207403,'Imbuia',42),(4207502,'Indaial',42),(4207577,'Iomere',42),(4207601,'Ipira',42),(4207650,'Ipora do Oeste',42),(4207684,'Ipuacu',42),(4207700,'Ipumirim',42),(4207759,'Iraceminha',42),(4207809,'Irani',42),(4207858,'Irati',42),(4207908,'Irineopolis',42),(4208005,'Ita',42),(4208104,'Itaiopolis',42),(4208203,'Itajai',42),(4208302,'Itapema',42),(4208401,'Itapiranga',42),(4208450,'Itapoa',42),(4208500,'Ituporanga',42),(4208609,'Jabora',42),(4208708,'Jacinto Machado',42),(4208807,'Jaguaruna',42),(4208906,'Jaragua do Sul',42),(4208955,'Jardinopolis',42),(4209003,'Joacaba',42),(4209102,'Joinville',42),(4209151,'Jose Boiteux',42),(4209177,'Jupia',42),(4209201,'Lacerdopolis',42),(4209300,'Lages',42),(4209409,'Laguna',42),(4209458,'Lajeado Grande',42),(4209508,'Laurentino',42),(4209607,'Lauro Muller',42),(4209706,'Lebon Regis',42),(4209805,'Leoberto Leal',42),(4209854,'Lindoia do Sul',42),(4209904,'Lontras',42),(4210001,'Luiz Alves',42),(4210035,'Luzerna',42),(4210050,'Macieira',42),(4210100,'Mafra',42),(4210209,'Major Gercino',42),(4210308,'Major Vieira',42),(4210407,'Maracaja',42),(4210506,'Maravilha',42),(4210555,'Marema',42),(4210605,'Massaranduba',42),(4210704,'Matos Costa',42),(4210803,'Meleiro',42),(4210852,'Mirim Doce',42),(4210902,'Modelo',42),(4211009,'Mondai',42),(4211058,'Monte Carlo',42),(4211108,'Monte Castelo',42),(4211207,'Morro da Fumaca',42),(4211256,'Morro Grande',42),(4211306,'Navegantes',42),(4211405,'Nova Erechim',42),(4211454,'Nova Itaberaba',42),(4211504,'Nova Trento',42),(4211603,'Nova Veneza',42),(4211652,'Novo Horizonte',42),(4211702,'Orleans',42),(4211751,'Otacilio Costa',42),(4211801,'Ouro',42),(4211850,'Ouro Verde',42),(4211876,'Paial',42),(4211892,'Painel',42),(4211900,'Palhoca',42),(4212007,'Palma Sola',42),(4212056,'Palmeira',42),(4212106,'Palmitos',42),(4212205,'Papanduva',42),(4212239,'Paraiso',42),(4212254,'Passo de Torres',42),(4212270,'Passos Maia',42),(4212304,'Paulo Lopes',42),(4212403,'Pedras Grandes',42),(4212502,'Penha',42),(4212601,'Peritiba',42),(4212650,'Pescaria Brava',42),(4212700,'Petrolândia',42),(4212809,'Balneario Picarras',42),(4212908,'Pinhalzinho',42),(4213005,'Pinheiro Preto',42),(4213104,'Piratuba',42),(4213153,'Planalto Alegre',42),(4213203,'Pomerode',42),(4213302,'Ponte Alta',42),(4213351,'Ponte Alta do Norte',42),(4213401,'Ponte Serrada',42),(4213500,'Porto Belo',42),(4213609,'Porto Uniao',42),(4213708,'Pouso Redondo',42),(4213807,'Praia Grande',42),(4213906,'Presidente Castello Branco',42),(4214003,'Presidente Getulio',42),(4214102,'Presidente Nereu',42),(4214151,'Princesa',42),(4214201,'Quilombo',42),(4214300,'Rancho Queimado',42),(4214409,'Rio das Antas',42),(4214508,'Rio do Campo',42),(4214607,'Rio do Oeste',42),(4214706,'Rio dos Cedros',42),(4214805,'Rio do Sul',42),(4214904,'Rio Fortuna',42),(4215000,'Rio Negrinho',42),(4215059,'Rio Rufino',42),(4215075,'Riqueza',42),(4215109,'Rodeio',42),(4215208,'Romelândia',42),(4215307,'Salete',42),(4215356,'Saltinho',42),(4215406,'Salto Veloso',42),(4215455,'Sangao',42),(4215505,'Santa Cecilia',42),(4215554,'Santa Helena',42),(4215604,'Santa Rosa de Lima',42),(4215653,'Santa Rosa do Sul',42),(4215679,'Santa Terezinha',42),(4215687,'Santa Terezinha do Progresso',42),(4215695,'Santiago do Sul',42),(4215703,'Santo Amaro da Imperatriz',42),(4215752,'Sao Bernardino',42),(4215802,'Sao Bento do Sul',42),(4215901,'Sao Bonifacio',42),(4216008,'Sao Carlos',42),(4216057,'Sao Cristovao do Sul',42),(4216107,'Sao Domingos',42),(4216206,'Sao Francisco do Sul',42),(4216255,'Sao Joao do Oeste',42),(4216305,'Sao Joao Batista',42),(4216354,'Sao Joao do Itaperiu',42),(4216404,'Sao Joao do Sul',42),(4216503,'Sao Joaquim',42),(4216602,'Sao Jose',42),(4216701,'Sao Jose do Cedro',42),(4216800,'Sao Jose do Cerrito',42),(4216909,'Sao Lourenco do Oeste',42),(4217006,'Sao Ludgero',42),(4217105,'Sao Martinho',42),(4217154,'Sao Miguel da Boa Vista',42),(4217204,'Sao Miguel do Oeste',42),(4217253,'Sao Pedro de Alcântara',42),(4217303,'Saudades',42),(4217402,'Schroeder',42),(4217501,'Seara',42),(4217550,'Serra Alta',42),(4217600,'Sideropolis',42),(4217709,'Sombrio',42),(4217758,'Sul Brasil',42),(4217808,'Taio',42),(4217907,'Tangara',42),(4217956,'Tigrinhos',42),(4218004,'Tijucas',42),(4218103,'Timbe do Sul',42),(4218202,'Timbo',42),(4218251,'Timbo Grande',42),(4218301,'Tres Barras',42),(4218350,'Treviso',42),(4218400,'Treze de Maio',42),(4218509,'Treze Tilias',42),(4218608,'Trombudo Central',42),(4218707,'Tubarao',42),(4218756,'Tunapolis',42),(4218806,'Turvo',42),(4218855,'Uniao do Oeste',42),(4218905,'Urubici',42),(4218954,'Urupema',42),(4219002,'Urussanga',42),(4219101,'Vargeao',42),(4219150,'Vargem',42),(4219176,'Vargem Bonita',42),(4219200,'Vidal Ramos',42),(4219309,'Videira',42),(4219358,'Vitor Meireles',42),(4219408,'Witmarsum',42),(4219507,'Xanxere',42),(4219606,'Xavantina',42),(4219705,'Xaxim',42),(4219853,'Zortea',42),(4220000,'Balneario Rincao',42);
/*!40000 ALTER TABLE `municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paf_contribuinte`
--

DROP TABLE IF EXISTS `paf_contribuinte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paf_contribuinte` (
  `id_paf` varchar(43) NOT NULL,
  `ativo` bit(1) NOT NULL,
  `contribuinte_fk_cnpj` varchar(14) DEFAULT NULL,
  `versao_paf_fk_nome_versao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_paf`),
  KEY `FKs08ac9se2gvoo5xwec8372muu` (`contribuinte_fk_cnpj`),
  KEY `FK1tgo8gw003ploh6349gvw4rx3` (`versao_paf_fk_nome_versao`),
  CONSTRAINT `FK1tgo8gw003ploh6349gvw4rx3` FOREIGN KEY (`versao_paf_fk_nome_versao`) REFERENCES `versao_paf` (`nome_versao`),
  CONSTRAINT `FKs08ac9se2gvoo5xwec8372muu` FOREIGN KEY (`contribuinte_fk_cnpj`) REFERENCES `contribuinte` (`pessoa_juridica_fk_cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paf_contribuinte`
--

LOCK TABLES `paf_contribuinte` WRITE;
/*!40000 ALTER TABLE `paf_contribuinte` DISABLE KEYS */;
INSERT INTO `paf_contribuinte` VALUES ('Cp9EbMr_auscbxT_h3Pl2TR_TnNs32wKQF-rn1Cnw7c',_binary '','89340307000145','paf_001'),('FMbbaF036j7IGDjsKbgzCRIBcMgxCQ4Srpqi3QfFkI8',_binary '\0','28572444000110','paf_001'),('HBfwWemnHXq3PexXuXzFMPIgrFHeVfDY3tp4noVqn5E',_binary '','28572444000110','paf_002'),('U9Q715d_WssK1XulT_1GvhkSmF9GZtg6qoNziHC_7VU',_binary '','66380626000189','paf_002');
/*!40000 ALTER TABLE `paf_contribuinte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa_juridica`
--

DROP TABLE IF EXISTS `pessoa_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa_juridica` (
  `cnpj` varchar(14) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `inscricao_estadual_sc` varchar(9) DEFAULT NULL,
  `nome_fantasia` varchar(255) DEFAULT NULL,
  `razao_social` varchar(255) DEFAULT NULL,
  `telefone_principal` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa_juridica`
--

LOCK TABLES `pessoa_juridica` WRITE;
/*!40000 ALTER TABLE `pessoa_juridica` DISABLE KEYS */;
INSERT INTO `pessoa_juridica` VALUES ('28572444000110','contato@fafe.com.br','569107148','Fafe Zopuhul','Lecelapekyk Hitudagu Kedez','+5548286328891'),('66380626000189','contato@ginipej.com.br','415773842','Ginipej Hyrobubeduf','Tafoqabanur Hevagu Wugadeledox','+5548541873418'),('67321567000130','contato@womexywuqery.com.br','335906781','Womexywuqery Kelav','Savuqocoka Hubipaga Vibaqafedup','+5548334669570'),('77830710000173','contato@qero.com.br','781237779','Qero Jalij','Qasa Pifuw Hetoso','+5548269784349'),('86096781000185','contato@honovy.com.br','137843597','Honovy Hepytasyhyj','Pumawucom Wotofonazufo Siwu','+5548651888991'),('87528541000175','contato@wudebamyk.com.br','783504419','Wudebamyk Zixatotajeq','Vysobubuhal Wymarocujov Hysa','+5548953296606'),('89340307000145','contato@fomogeripiq.com.br','404638186','Fomogeripiq Zanybodop','Konov Limil Waqot','+5548478838058');
/*!40000 ALTER TABLE `pessoa_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processo_certificacao`
--

DROP TABLE IF EXISTS `processo_certificacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processo_certificacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` int NOT NULL,
  `certificadora_fk_cnpj` varchar(14) DEFAULT NULL,
  `fabricante_fk_cnpj` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK8dtmljlcxk6nlaf4nvym83eup` (`certificadora_fk_cnpj`),
  KEY `FKeub9wauh0owtgyh8njtfco1v0` (`fabricante_fk_cnpj`),
  CONSTRAINT `FK8dtmljlcxk6nlaf4nvym83eup` FOREIGN KEY (`certificadora_fk_cnpj`) REFERENCES `certificadora` (`pessoa_juridica_fk_cnpj`),
  CONSTRAINT `FKeub9wauh0owtgyh8njtfco1v0` FOREIGN KEY (`fabricante_fk_cnpj`) REFERENCES `fabricante` (`pessoa_juridica_fk_cnpj`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processo_certificacao`
--

LOCK TABLES `processo_certificacao` WRITE;
/*!40000 ALTER TABLE `processo_certificacao` DISABLE KEYS */;
INSERT INTO `processo_certificacao` VALUES (1,1,'67321567000130','87528541000175'),(2,2,'77830710000173','86096781000185'),(3,3,'77830710000173','86096781000185'),(4,1,'67321567000130','87528541000175'),(5,2,'77830710000173','86096781000185'),(6,3,'77830710000173','86096781000185'),(7,2,'77830710000173','86096781000185'),(8,2,'77830710000173','86096781000185');
/*!40000 ALTER TABLE `processo_certificacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_daf`
--

DROP TABLE IF EXISTS `registro_daf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro_daf` (
  `id` int NOT NULL AUTO_INCREMENT,
  `chave_daf` varchar(2000) DEFAULT NULL,
  `chave_paf` varchar(86) DEFAULT NULL,
  `chave_sef` varchar(86) DEFAULT NULL,
  `contador_registro` int NOT NULL,
  `data_registro` datetime(6) DEFAULT NULL,
  `data_remocao` datetime(6) DEFAULT NULL,
  `just_ultima_alt_modo_op` varchar(255) DEFAULT NULL,
  `justificativa_remocao` varchar(255) DEFAULT NULL,
  `modo_operacao` bit(1) NOT NULL,
  `daf_fk_id_daf` varchar(255) DEFAULT NULL,
  `paf_contribuinte_fk_id_paf` varchar(43) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UK245gw2gug7xgrqf4evkh56bhf` (`chave_sef`),
  UNIQUE KEY `UKnjt8e4vr81raeb2ocg2yjs51c` (`chave_paf`),
  KEY `FKc2v0r6m6kc754y87dvcipuq0b` (`daf_fk_id_daf`),
  KEY `FKgvglgjo1aw9rj10xbgmxm6wq6` (`paf_contribuinte_fk_id_paf`),
  CONSTRAINT `FKc2v0r6m6kc754y87dvcipuq0b` FOREIGN KEY (`daf_fk_id_daf`) REFERENCES `daf` (`id_daf`),
  CONSTRAINT `FKgvglgjo1aw9rj10xbgmxm6wq6` FOREIGN KEY (`paf_contribuinte_fk_id_paf`) REFERENCES `paf_contribuinte` (`id_paf`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_daf`
--

LOCK TABLES `registro_daf` WRITE;
/*!40000 ALTER TABLE `registro_daf` DISABLE KEYS */;
INSERT INTO `registro_daf` VALUES (1,'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnt+jQlRs4gbHOR820Vhk6NnW8w3U4A5lkR8J0g9kYSLgXbipWBsT77Odgkg+NFHRxSGBJQzuA+tUQHQyd/wiaKDQY82tNqbAKFSKYjBQwtVX2R6BzV9vu7CwUZwq7jEGRTDR1xYRW9B/Ykd7+nHXyeWId1AjbyjrryMFo4qWDnmrOxrqdhBa802DUF1G0/kLLFF9JLgZilFE++vU6o0ITzTJK5qh/se1wgbnQsbPEbSA0bUKdO1UCR3ZEqrGJGsH9DDNzZLUQNFCYISa+aXKrHH0cfsjetlzNR1bZ7cAKXb/TqXN3fApiramloCGSmFwSnUDiPBmgnGJq+03hxEXJwIDAQAB','5n5iI6TdSWFpkO1_fu4i5mxa2QjbI5q30CbzqWl1wMdMR2tMUq1-BBIY4v1TY3nqyIhEj_GHXRpfEOaW2_0Rhw','glgU1cEj6SkZrLpcs21x02IAJfUMfthhwCkUVG5DO6CWXH8Io1ECk8affm5cJV4e6s7Ynfk1YMjCnySxUjbRKA',1,'2021-07-19 13:13:08.416000',NULL,NULL,NULL,_binary '\0','ChAgT4LGSbKXo4UO8m6Cbg','HBfwWemnHXq3PexXuXzFMPIgrFHeVfDY3tp4noVqn5E');
/*!40000 ALTER TABLE `registro_daf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resultado`
--

DROP TABLE IF EXISTS `resultado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultado` (
  `cstat` int NOT NULL,
  `apagar_retido` bit(1) NOT NULL,
  `rejeicao` bit(1) NOT NULL,
  `xmotivo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cstat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultado`
--

LOCK TABLES `resultado` WRITE;
/*!40000 ALTER TABLE `resultado` DISABLE KEYS */;
INSERT INTO `resultado` VALUES (1000,_binary '',_binary '\0','Solicitação recebida com sucesso'),(1001,_binary '',_binary '\0','Dispositivo registrado com sucesso'),(1002,_binary '',_binary '\0','Registro de dispositivo removido'),(1003,_binary '',_binary '\0','Consulta de Software Basico efetuada com sucesso'),(1004,_binary '',_binary '\0','Notificacao de extravio efetuada com sucesso'),(1005,_binary '',_binary '\0','Validacao do fragmento DAF realizada com sucesso'),(1006,_binary '',_binary '\0','Modo de operação alterado com sucesso'),(2000,_binary '\0',_binary '','registro do idDaf não encontrado'),(2001,_binary '\0',_binary '','idpaf não corresponde ao registro do DAF'),(2002,_binary '\0',_binary '','nonce não corresponde ao informado pela SEF'),(2003,_binary '\0',_binary '','valor do mcounter inválido'),(2004,_binary '\0',_binary '','assinatura de token inválida'),(2005,_binary '\0',_binary '','CNPJ do contribuinte diverge do CNPJ da assinatura'),(2006,_binary '\0',_binary '','idpaf não registrado'),(2007,_binary '\0',_binary '','DAF extraviado'),(2008,_binary '\0',_binary '','idDaf do token não corresponde ao IdDAF informado'),(2009,_binary '\0',_binary '','DAF em situação irregular'),(2010,_binary '\0',_binary '','justificativa inválida. A justificativa deve conter entre 15 e 255 caracteres'),(2011,_binary '\0',_binary '','consumo indevido pelo aplicativo da empresa. Permitido no máximo 40 requisições por hora'),(2012,_binary '\0',_binary '','CNPJ do fabricante DAF inválido'),(2013,_binary '\0',_binary '','modelo DAF inválido'),(2014,_binary '\0',_binary '','impressão digital do certificado digital da SEF informada não é reconhecida'),(2015,_binary '\0',_binary '','versão do Software Básico informada não é reconhecida'),(2100,_binary '\0',_binary '','hash do idpaf diverge do calculado'),(2101,_binary '\0',_binary '','assinatura gerada pela attestationkey não corresponde a um modelo de DAF certificado'),(2102,_binary '\0',_binary '','CNPJ do responsável técnico inválido'),(2103,_binary '\0',_binary '','identificador do CSRT (tag:idCSRT) não cadastrado na SEF'),(2104,_binary '\0',_binary '','identificador do CSRT (tag:idCSRT) revogado'),(2105,_binary '\0',_binary '','CNPJ do contribuinte não cadastrado'),(2108,_binary '\0',_binary '','CNPJ do responsável técnico não cadastrado'),(2300,_binary '\0',_binary '','IdDAF do requerente não corresponde ao IdDAF de autorização do DFe'),(2301,_binary '\0',_binary '','chave DFe não encontrada'),(2302,_binary '\0',_binary '','DAF deve atualizar a versão do software básico'),(2303,_binary '\0',_binary '','versão do software básico do DAF está desatualizada'),(2304,_binary '\0',_binary '','token de autorização inválido'),(2305,_binary '\0',_binary '','DAF deve atualizar o certificado digital da SEF'),(2400,_binary '\0',_binary '','remoção extraordinária de autorização retida indisponível para o contribuinte'),(2401,_binary '\0',_binary '','número de recibo não encontrado'),(2402,_binary '\0',_binary '','lote em processamento'),(2403,_binary '\0',_binary '','a rejeição informada para o DF-e é inválida'),(2404,_binary '\0',_binary '','as informações essenciais do DF-e são inválidas'),(2500,_binary '\0',_binary '','notificação de extravio do DAF já foi realizada'),(2600,_binary '\0',_binary '','o modo de operação já informado anteriormente'),(9999,_binary '\0',_binary '','Erro não catalogado');
/*!40000 ALTER TABLE `resultado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software_basico`
--

DROP TABLE IF EXISTS `software_basico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software_basico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_lancamento` datetime(6) DEFAULT NULL,
  `resumo_criptografico` varchar(43) DEFAULT NULL,
  `sig_sef` varchar(2000) DEFAULT NULL,
  `cfp_sig_sef` varchar(2000) DEFAULT NULL,
  `url` varchar(2000) DEFAULT NULL,
  `versao` int NOT NULL,
  `certificacao_fk_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKmsa9fafrr8fh8tk0wp2bm9vqv` (`certificacao_fk_id`),
  CONSTRAINT `FKmsa9fafrr8fh8tk0wp2bm9vqv` FOREIGN KEY (`certificacao_fk_id`) REFERENCES `certificacao` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software_basico`
--

LOCK TABLES `software_basico` WRITE;
/*!40000 ALTER TABLE `software_basico` DISABLE KEYS */;
INSERT INTO `software_basico` VALUES (1,'2021-07-18 13:12:55.533000','aQ3SJz-S4Sd0rTHKPeht0JDHdGoMcbv6FrtofvxWwzg','MGUCMQCo6EID9wl4l0F8r4fnBfgGiLckVsqgoFd0zL00DC03Ny3e57X3f3l19r35L-XJFPoCMGRFJKIl399mDp7yH-4oyuy4VJ0kkaGOPt4AkXQ4zZF4aRQKzKzN4yuhBx48L705Sg','J33D3Kr4R0TKyHYm3TYtUIhvOjAFmOg86x63ndD-bAU','http://sb860967810001851.com.br',1,6),(2,'2020-07-11 13:12:55.533000','CsS3YJ6VOR0lslPrYmppUoTFwO5AwAih_lyy5jzurY8','MGUCMQCo6EID9wl4l0F8r4fnBfgGiLckVsqgoFd0zL00DC03Ny3e57X3f3l19r35L-XJFPoCMGRFJKIl399mDp7yH-4oyuy4VJ0kkaGOPt4AkXQ4zZF4aRQKzKzN4yuhBx48L705Sg','J33D3Kr4R0TKyHYm3TYtUIhvOjAFmOg86x63ndD-bAU','http://sb860967810001852.com.br',2,3),(3,'2021-07-12 13:13:09.527000','2WPyJbsrfOTaKbFOVyoMnUGzKMk8ljtc3dJpNQLrvFI','MGUCMQCo6EID9wl4l0F8r4fnBfgGiLckVsqgoFd0zL00DC03Ny3e57X3f3l19r35L-XJFPoCMGRFJKIl399mDp7yH-4oyuy4VJ0kkaGOPt4AkXQ4zZF4aRQKzKzN4yuhBx48L705Sg','SdFcN6lp3DImbcsgZBOPvXc2HMdBC3juLkD6ee4Fz5w','http://versaodaflase1.0.br',2,8);
/*!40000 ALTER TABLE `software_basico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uf`
--

DROP TABLE IF EXISTS `uf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uf` (
  `codigo_ibge` int NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `sigla` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`codigo_ibge`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uf`
--

LOCK TABLES `uf` WRITE;
/*!40000 ALTER TABLE `uf` DISABLE KEYS */;
INSERT INTO `uf` VALUES (11,'Rondonia','RO'),(12,'Acre','AC'),(13,'Amazonas','AM'),(14,'Roraima','RR'),(15,'Para','PA'),(16,'Amapa','AP'),(17,'Tocantins','TO'),(21,'Maranhao','MA'),(22,'Piaui','PI'),(23,'Ceara','CE'),(24,'Rio Grande do Norte','RN'),(25,'Paraiba','PB'),(26,'Pernambuco','PE'),(27,'Alagoas','AL'),(28,'Sergipe','SE'),(29,'Bahia','BA'),(31,'Minas Gerais','MG'),(32,'Espirito Santo','ES'),(33,'Rio de Janeiro','RJ'),(35,'Sao Paulo','SP'),(41,'Parana','PR'),(42,'Santa Catarina','SC'),(43,'Rio Grande do Sul','RS'),(50,'Mato Grosso do Sul','MS'),(51,'Mato Grosso','MT'),(52,'Goias','GO'),(53,'Distrito Federal','DF');
/*!40000 ALTER TABLE `uf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `versao_paf`
--

DROP TABLE IF EXISTS `versao_paf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `versao_paf` (
  `nome_versao` varchar(20) NOT NULL,
  `certificacao_fk_id` int DEFAULT NULL,
  `csrt_fk_cnpj` varchar(14) DEFAULT NULL,
  `csrt_fk_id_csrt` int DEFAULT NULL,
  PRIMARY KEY (`nome_versao`),
  KEY `FKsj8r8xp8smbu36c3fquymp75b` (`certificacao_fk_id`),
  KEY `FKnege917ufiunen9k754b4q1ub` (`csrt_fk_cnpj`,`csrt_fk_id_csrt`),
  CONSTRAINT `FKnege917ufiunen9k754b4q1ub` FOREIGN KEY (`csrt_fk_cnpj`, `csrt_fk_id_csrt`) REFERENCES `csrt` (`fabricante_fk_cnpj`, `id_csrt`),
  CONSTRAINT `FKsj8r8xp8smbu36c3fquymp75b` FOREIGN KEY (`certificacao_fk_id`) REFERENCES `certificacao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `versao_paf`
--

LOCK TABLES `versao_paf` WRITE;
/*!40000 ALTER TABLE `versao_paf` DISABLE KEYS */;
INSERT INTO `versao_paf` VALUES ('paf_001',4,'87528541000175',2),('paf_002',4,'87528541000175',1);
/*!40000 ALTER TABLE `versao_paf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xml_distribuicao`
--

DROP TABLE IF EXISTS `xml_distribuicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xml_distribuicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_inclusao` datetime(6) DEFAULT NULL,
  `data_processamento` datetime(6) DEFAULT NULL,
  `protocolo_autorizacao` varchar(255) DEFAULT NULL,
  `xml` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xml_distribuicao`
--

LOCK TABLES `xml_distribuicao` WRITE;
/*!40000 ALTER TABLE `xml_distribuicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `xml_distribuicao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;