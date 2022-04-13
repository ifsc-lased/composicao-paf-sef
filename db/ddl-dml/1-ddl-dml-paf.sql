CREATE USER IF NOT EXISTS 'dafpaf'@'%' IDENTIFIED WITH mysql_native_password BY 'E37vEB3dnm';
CREATE SCHEMA IF NOT EXISTS `daf-paf`;
GRANT ALL PRIVILEGES ON `daf-paf`.* TO 'dafpaf'@'%';

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "-03:00";

USE `daf-paf` ;
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
-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: daf-paf-1
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `pessoa_fisica_fk_id` int NOT NULL,
  PRIMARY KEY (`pessoa_fisica_fk_id`),
  KEY `fk_cliente_pessoa_fisica1_idx` (`pessoa_fisica_fk_id`),
  CONSTRAINT `fk_cliente_pessoa_fisica1` FOREIGN KEY (`pessoa_fisica_fk_id`) REFERENCES `pessoa_fisica` (`pessoa_fk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (4),(5),(6);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daf`
--

DROP TABLE IF EXISTS `daf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daf` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_daf` varchar(22) NOT NULL,
  `modo_operacao` tinyint(1) DEFAULT NULL,
  `versao_sb` int DEFAULT NULL,
  `hash_sb` varchar(43) DEFAULT NULL,
  `cnpj_fabricante` varchar(14) DEFAULT NULL,
  `modelo` varchar(20) DEFAULT NULL,
  `contador` int DEFAULT NULL,
  `certificado_sef` longtext,
  `estado` varchar(10) DEFAULT NULL,
  `ultimo_token` varchar(255) DEFAULT NULL,
  `max_dfe` int DEFAULT NULL,
  `num_dfe` int DEFAULT NULL,
  `porta` varchar(255) DEFAULT NULL,
  `data_extravio` datetime DEFAULT NULL,
  `data_registro` datetime DEFAULT NULL,
  `chave_paf` varchar(86) DEFAULT NULL,
  `situacao` int DEFAULT NULL,
  `data_insercao` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `daf_id_daf_uindex` (`id_daf`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daf`
--

LOCK TABLES `daf` WRITE;
/*!40000 ALTER TABLE `daf` DISABLE KEYS */;
INSERT INTO `daf` VALUES (1,'k6sWojUlSvKCKJsBOr3jtA',0,2,'MoxgVDBf9MdYEQtb97TGchVvA8mh3gkjBE-C2-mzviU','86096781000185','daf-pi-ec',0,'-----BEGIN CERTIFICATE-----\nMIICJjCCAaugAwIBAgIUaS3sIKXSF6A7DJbWAJefB3sn95gwCgYIKoZIzj0EAwIw\ndDEMMAoGA1UECgwDU0VGMQ4wDAYDVQQLDAVHRVNBQzELMAkGA1UEBhMCQlIxFzAV\nBgNVBAgMDlNhbnRhIENhdGFyaW5hMRYwFAYDVQQHDA1GbG9yaWFub3BvbGlzMRYw\nFAYDVQQDDA1zZWYuc2MuZ292LmJyMB4XDTIxMDUyODE0MzUxOFoXDTMxMDUyNzE0\nMzUxOFowdDEMMAoGA1UECgwDU0VGMQ4wDAYDVQQLDAVHRVNBQzELMAkGA1UEBhMC\nQlIxFzAVBgNVBAgMDlNhbnRhIENhdGFyaW5hMRYwFAYDVQQHDA1GbG9yaWFub3Bv\nbGlzMRYwFAYDVQQDDA1zZWYuc2MuZ292LmJyMHYwEAYHKoZIzj0CAQYFK4EEACID\nYgAEJ2NZpBT8RNKxVuJoPDtRyHZwATAQCPLZJLpHBEfHYw34oqkoxa8rhWvHbkz0\nrEDO2U+aVEwtOGxChZqFtUTQ2a92sDuNtEscv8Kiq63A38vsBrdkEoXHQmAe5HU1\nPVwcMAoGCCqGSM49BAMCA2kAMGYCMQDpSFdJD8/VGq/yXYEEUoxr0AB8rjcwdL3S\nTQ3ZtdW4j6sam5CSdFhkUKSuvW17UMkCMQC+O8Srmy4sZVBlb1gCOxxEmmwxVxEc\nLPHYbf1rpnfzuq44vqAI8MnRcAnLgtQNmr8=\n-----END CERTIFICATE-----\n','inativo','jau',1000,0,'',NULL,'2021-07-02 00:00:00','OMxOFIhiKw_EIyC3m-C3TnU-1_R5YTLY9zSyfJrxPg2mCMoCodU5QJaXGyFNi72W6eUnGpR9nlAMudvP3yGNgg',0,'2021-05-27 16:36:20');
/*!40000 ALTER TABLE `daf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `pessoa_juridica_fk_id` int NOT NULL,
  `csc_id` int NOT NULL,
  `csc` varchar(36) NOT NULL,
  `ambiente` int NOT NULL,
  `id_paf` varchar(43) NOT NULL,
  `endereco_sefaz` varchar(255) NOT NULL,
  `tp_emis` int NOT NULL DEFAULT '1',
  `nome_certificado` varchar(255),
  `senha_certificado` varchar(255),
  PRIMARY KEY (`pessoa_juridica_fk_id`),
  KEY `fk_empresa_pessoa_juridica1_idx` (`pessoa_juridica_fk_id`),
  CONSTRAINT `fk_empresa_pessoa_juridica1` FOREIGN KEY (`pessoa_juridica_fk_id`) REFERENCES `pessoa_juridica` (`pessoa_fk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,1,'OMW1ZLGWUJH8QNLJDAZ46I3J2Q08E2G4P6NT',1,'mmOnLd8Z75MpeOtFILOkweFYOFit4ZvM8nk5GjDrGuE','svrs',1,'contribuinteRegular28572444000110.pkcs12','123456');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `endereco`
--

DROP TABLE IF EXISTS `endereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `endereco` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pessoa_fk_id` int NOT NULL,
  `endereco` varchar(60) NOT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `bairro` varchar(60) DEFAULT NULL,
  `complemento` varchar(60) DEFAULT NULL,
  `logradouro` varchar(60) DEFAULT NULL,
  `numero` varchar(60) DEFAULT NULL,
  `municipio_fk_codigo_ibge` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_endereco_municipio1_idx` (`municipio_fk_codigo_ibge`),
  KEY `fk_endereco_pessoa1_idx` (`pessoa_fk_id`),
  CONSTRAINT `fk_endereco_municipio1` FOREIGN KEY (`municipio_fk_codigo_ibge`) REFERENCES `municipio` (`codigo_ibge`),
  CONSTRAINT `fk_endereco_pessoa1` FOREIGN KEY (`pessoa_fk_id`) REFERENCES `pessoa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `endereco`
--

LOCK TABLES `endereco` WRITE;
/*!40000 ALTER TABLE `endereco` DISABLE KEYS */;
INSERT INTO `endereco` VALUES (1,3,'Luqeeeba ebov','93348423','Bidoe','Sala 318','Rua','119',4202081),(2,4,'Leaikawe efapu','40470407','Canaxena','Sala 416','Rodovia','482',4310207),(3,5,'Reauae ezola','45025408','Mobucal','Sala 506','Via','293',4304614),(4,6,'Nazazupic uaokiaa','17202201','Nijuta','Sala 296','Rodovia','538',4317301);
/*!40000 ALTER TABLE `endereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedor_sistema`
--

DROP TABLE IF EXISTS `fornecedor_sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedor_sistema` (
  `pessoa_juridica_fk_id` int NOT NULL,
  `id_csrt` int DEFAULT NULL,
  PRIMARY KEY (`pessoa_juridica_fk_id`),
  CONSTRAINT `fk_fornecedor_pessoa_juridica` FOREIGN KEY (`pessoa_juridica_fk_id`) REFERENCES `pessoa_juridica` (`pessoa_fk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedor_sistema`
--

LOCK TABLES `fornecedor_sistema` WRITE;
/*!40000 ALTER TABLE `fornecedor_sistema` DISABLE KEYS */;
INSERT INTO `fornecedor_sistema` VALUES (2,1);
/*!40000 ALTER TABLE `fornecedor_sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `pessoa_fisica_fk_id` int NOT NULL,
  `login` varchar(15) NOT NULL,
  `senha` varchar(8) NOT NULL,
  `empresa_fk_id` int NOT NULL,
  PRIMARY KEY (`pessoa_fisica_fk_id`),
  KEY `fk_funcionario_empresa1_idx` (`empresa_fk_id`),
  CONSTRAINT `fk_funcionario_empresa1` FOREIGN KEY (`empresa_fk_id`) REFERENCES `empresa` (`pessoa_juridica_fk_id`),
  CONSTRAINT `fk_funcionario_pessoa_fisica1` FOREIGN KEY (`pessoa_fisica_fk_id`) REFERENCES `pessoa_fisica` (`pessoa_fk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (3,'mahono','1234',1);
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario_pdv`
--

DROP TABLE IF EXISTS `funcionario_pdv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario_pdv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ponto_venda_fk_id` int NOT NULL,
  `funcionario_fk_id` int NOT NULL,
  `data_hora_login` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ponto_venda_has_funcionario_funcionario1_idx` (`funcionario_fk_id`),
  KEY `fk_ponto_venda_has_funcionario_ponto_venda1_idx` (`ponto_venda_fk_id`),
  CONSTRAINT `fk_ponto_venda_has_funcionario_funcionario1` FOREIGN KEY (`funcionario_fk_id`) REFERENCES `funcionario` (`pessoa_fisica_fk_id`),
  CONSTRAINT `fk_ponto_venda_has_funcionario_ponto_venda1` FOREIGN KEY (`ponto_venda_fk_id`) REFERENCES `ponto_venda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario_pdv`
--

LOCK TABLES `funcionario_pdv` WRITE;
/*!40000 ALTER TABLE `funcionario_pdv` DISABLE KEYS */;
INSERT INTO `funcionario_pdv` VALUES (1,1,3,'2021-07-19 11:43:16');
/*!40000 ALTER TABLE `funcionario_pdv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `municipio`
--

DROP TABLE IF EXISTS `municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `municipio` (
  `codigo_ibge` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `uf_codigo_ibge` int NOT NULL,
  PRIMARY KEY (`codigo_ibge`),
  KEY `fk_municipio_uf_idx` (`uf_codigo_ibge`),
  CONSTRAINT `fk_municipio_uf` FOREIGN KEY (`uf_codigo_ibge`) REFERENCES `uf` (`codigo_ibge`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipio`
--

LOCK TABLES `municipio` WRITE;
/*!40000 ALTER TABLE `municipio` DISABLE KEYS */;
INSERT INTO `municipio` VALUES (4100103,'Abatia',41),(4100202,'Adrianopolis',41),(4100301,'Agudos do Sul',41),(4100400,'Almirante Tamandare',41),(4100459,'Altamira do Parana',41),(4100509,'Altonia',41),(4100608,'Alto Parana',41),(4100707,'Alto Piquiri',41),(4100806,'Alvorada do Sul',41),(4100905,'Amapora',41),(4101002,'Ampere',41),(4101051,'Anahy',41),(4101101,'Andira',41),(4101150,'angulo',41),(4101200,'Antonina',41),(4101309,'Antonio Olinto',41),(4101408,'Apucarana',41),(4101507,'Arapongas',41),(4101606,'Arapoti',41),(4101655,'Arapua',41),(4101705,'Araruna',41),(4101804,'Araucaria',41),(4101853,'Ariranha do Ivai',41),(4101903,'Assai',41),(4102000,'Assis Chateaubriand',41),(4102109,'Astorga',41),(4102208,'Atalaia',41),(4102307,'Balsa Nova',41),(4102406,'Bandeirantes',41),(4102505,'Barbosa Ferraz',41),(4102604,'Barracao',41),(4102703,'Barra do Jacare',41),(4102752,'Bela Vista da Caroba',41),(4102802,'Bela Vista do Paraiso',41),(4102901,'Bituruna',41),(4103008,'Boa Esperanca',41),(4103024,'Boa Esperanca do Iguacu',41),(4103040,'Boa Ventura de Sao Roque',41),(4103057,'Boa Vista da Aparecida',41),(4103107,'Bocaiuva do Sul',41),(4103156,'Bom Jesus do Sul',41),(4103206,'Bom Sucesso',41),(4103222,'Bom Sucesso do Sul',41),(4103305,'Borrazopolis',41),(4103354,'Braganey',41),(4103370,'Brasilandia do Sul',41),(4103404,'Cafeara',41),(4103453,'Cafelandia',41),(4103479,'Cafezal do Sul',41),(4103503,'California',41),(4103602,'Cambara',41),(4103701,'Cambe',41),(4103800,'Cambira',41),(4103909,'Campina da Lagoa',41),(4103958,'Campina do Simao',41),(4104006,'Campina Grande do Sul',41),(4104055,'Campo Bonito',41),(4104105,'Campo do Tenente',41),(4104204,'Campo Largo',41),(4104253,'Campo Magro',41),(4104303,'Campo Mourao',41),(4104402,'Candido de Abreu',41),(4104428,'Candoi',41),(4104451,'Cantagalo',41),(4104501,'Capanema',41),(4104600,'Capitao Leonidas Marques',41),(4104659,'Carambei',41),(4104709,'Carlopolis',41),(4104808,'Cascavel',41),(4104907,'Castro',41),(4105003,'Catanduvas',41),(4105102,'Centenario do Sul',41),(4105201,'Cerro Azul',41),(4105300,'Ceu Azul',41),(4105409,'Chopinzinho',41),(4105508,'Cianorte',41),(4105607,'Cidade Gaucha',41),(4105706,'Clevelandia',41),(4105805,'Colombo',41),(4105904,'Colorado',41),(4106001,'Congonhinhas',41),(4106100,'Conselheiro Mairinck',41),(4106209,'Contenda',41),(4106308,'Corbelia',41),(4106407,'Cornelio Procopio',41),(4106456,'Coronel Domingos Soares',41),(4106506,'Coronel Vivida',41),(4106555,'Corumbatai do Sul',41),(4106571,'Cruzeiro do Iguacu',41),(4106605,'Cruzeiro do Oeste',41),(4106704,'Cruzeiro do Sul',41),(4106803,'Cruz Machado',41),(4106852,'Cruzmaltina',41),(4106902,'Curitiba',41),(4107009,'Curiuva',41),(4107108,'Diamante do Norte',41),(4107124,'Diamante do Sul',41),(4107157,'Diamante DOeste',41),(4107207,'Dois Vizinhos',41),(4107256,'Douradina',41),(4107306,'Doutor Camargo',41),(4107405,'Eneas Marques',41),(4107504,'Engenheiro Beltrao',41),(4107520,'Esperanca Nova',41),(4107538,'Entre Rios do Oeste',41),(4107546,'Espigao Alto do Iguacu',41),(4107553,'Farol',41),(4107603,'Faxinal',41),(4107652,'Fazenda Rio Grande',41),(4107702,'Fenix',41),(4107736,'Fernandes Pinheiro',41),(4107751,'Figueira',41),(4107801,'Florai',41),(4107850,'Flor da Serra do Sul',41),(4107900,'Floresta',41),(4108007,'Florestopolis',41),(4108106,'Florida',41),(4108205,'Formosa do Oeste',41),(4108304,'Foz do Iguacu',41),(4108320,'Francisco Alves',41),(4108403,'Francisco Beltrao',41),(4108452,'Foz do Jordao',41),(4108502,'General Carneiro',41),(4108551,'Godoy Moreira',41),(4108601,'Goioere',41),(4108650,'Goioxim',41),(4108700,'Grandes Rios',41),(4108809,'Guaira',41),(4108908,'Guairaca',41),(4108957,'Guamiranga',41),(4109005,'Guapirama',41),(4109104,'Guaporema',41),(4109203,'Guaraci',41),(4109302,'Guaraniacu',41),(4109401,'Guarapuava',41),(4109500,'Guaraquecaba',41),(4109609,'Guaratuba',41),(4109658,'Honorio Serpa',41),(4109708,'Ibaiti',41),(4109757,'Ibema',41),(4109807,'Ibipora',41),(4109906,'Icaraima',41),(4110003,'Iguaracu',41),(4110052,'Iguatu',41),(4110078,'Imbau',41),(4110102,'Imbituva',41),(4110201,'Inacio Martins',41),(4110300,'Inaja',41),(4110409,'Indianopolis',41),(4110508,'Ipiranga',41),(4110607,'Ipora',41),(4110656,'Iracema do Oeste',41),(4110706,'Irati',41),(4110805,'Iretama',41),(4110904,'Itaguaje',41),(4110953,'Itaipulandia',41),(4111001,'Itambaraca',41),(4111100,'Itambe',41),(4111209,'Itapejara dOeste',41),(4111258,'Itaperucu',41),(4111308,'Itauna do Sul',41),(4111407,'Ivai',41),(4111506,'Ivaipora',41),(4111555,'Ivate',41),(4111605,'Ivatuba',41),(4111704,'Jaboti',41),(4111803,'Jacarezinho',41),(4111902,'Jaguapita',41),(4112009,'Jaguariaiva',41),(4112108,'Jandaia do Sul',41),(4112207,'Janiopolis',41),(4112306,'Japira',41),(4112405,'Japura',41),(4112504,'Jardim Alegre',41),(4112603,'Jardim Olinda',41),(4112702,'Jataizinho',41),(4112751,'Jesuitas',41),(4112801,'Joaquim Tavora',41),(4112900,'Jundiai do Sul',41),(4112959,'Juranda',41),(4113007,'Jussara',41),(4113106,'Kalore',41),(4113205,'Lapa',41),(4113254,'Laranjal',41),(4113304,'Laranjeiras do Sul',41),(4113403,'Leopolis',41),(4113429,'Lidianopolis',41),(4113452,'Lindoeste',41),(4113502,'Loanda',41),(4113601,'Lobato',41),(4113700,'Londrina',41),(4113734,'Luiziana',41),(4113759,'Lunardelli',41),(4113809,'Lupionopolis',41),(4113908,'Mallet',41),(4114005,'Mambore',41),(4114104,'Mandaguacu',41),(4114203,'Mandaguari',41),(4114302,'Mandirituba',41),(4114351,'Manfrinopolis',41),(4114401,'Mangueirinha',41),(4114500,'Manoel Ribas',41),(4114609,'Marechal Candido Rondon',41),(4114708,'Maria Helena',41),(4114807,'Marialva',41),(4114906,'Marilandia do Sul',41),(4115002,'Marilena',41),(4115101,'Mariluz',41),(4115200,'Maringa',41),(4115309,'Mariopolis',41),(4115358,'Maripa',41),(4115408,'Marmeleiro',41),(4115457,'Marquinho',41),(4115507,'Marumbi',41),(4115606,'Matelandia',41),(4115705,'Matinhos',41),(4115739,'Mato Rico',41),(4115754,'Maua da Serra',41),(4115804,'Medianeira',41),(4115853,'Mercedes',41),(4115903,'Mirador',41),(4116000,'Miraselva',41),(4116059,'Missal',41),(4116109,'Moreira Sales',41),(4116208,'Morretes',41),(4116307,'Munhoz de Melo',41),(4116406,'Nossa Senhora das Gracas',41),(4116505,'Nova Alianca do Ivai',41),(4116604,'Nova America da Colina',41),(4116703,'Nova Aurora',41),(4116802,'Nova Cantu',41),(4116901,'Nova Esperanca',41),(4116950,'Nova Esperanca do Sudoeste',41),(4117008,'Nova Fatima',41),(4117057,'Nova Laranjeiras',41),(4117107,'Nova Londrina',41),(4117206,'Nova Olimpia',41),(4117214,'Nova Santa Barbara',41),(4117222,'Nova Santa Rosa',41),(4117255,'Nova Prata do Iguacu',41),(4117271,'Nova Tebas',41),(4117297,'Novo Itacolomi',41),(4117305,'Ortigueira',41),(4117404,'Ourizona',41),(4117453,'Ouro Verde do Oeste',41),(4117503,'Paicandu',41),(4117602,'Palmas',41),(4117701,'Palmeira',41),(4117800,'Palmital',41),(4117909,'Palotina',41),(4118006,'Paraiso do Norte',41),(4118105,'Paranacity',41),(4118204,'Paranagua',41),(4118303,'Paranapoema',41),(4118402,'Paranavai',41),(4118451,'Pato Bragado',41),(4118501,'Pato Branco',41),(4118600,'Paula Freitas',41),(4118709,'Paulo Frontin',41),(4118808,'Peabiru',41),(4118857,'Perobal',41),(4118907,'Perola',41),(4119004,'Perola dOeste',41),(4119103,'Pien',41),(4119152,'Pinhais',41),(4119202,'Pinhalao',41),(4119251,'Pinhal de Sao Bento',41),(4119301,'Pinhao',41),(4119400,'Pirai do Sul',41),(4119509,'Piraquara',41),(4119608,'Pitanga',41),(4119657,'Pitangueiras',41),(4119707,'Planaltina do Parana',41),(4119806,'Planalto',41),(4119905,'Ponta Grossa',41),(4119954,'Pontal do Parana',41),(4120002,'Porecatu',41),(4120101,'Porto Amazonas',41),(4120150,'Porto Barreiro',41),(4120200,'Porto Rico',41),(4120309,'Porto Vitoria',41),(4120333,'Prado Ferreira',41),(4120358,'Pranchita',41),(4120408,'Presidente Castelo Branco',41),(4120507,'Primeiro de Maio',41),(4120606,'Prudentopolis',41),(4120655,'Quarto Centenario',41),(4120705,'Quatigua',41),(4120804,'Quatro Barras',41),(4120853,'Quatro Pontes',41),(4120903,'Quedas do Iguacu',41),(4121000,'Querencia do Norte',41),(4121109,'Quinta do Sol',41),(4121208,'Quitandinha',41),(4121257,'Ramilandia',41),(4121307,'Rancho Alegre',41),(4121356,'Rancho Alegre DOeste',41),(4121406,'Realeza',41),(4121505,'Reboucas',41),(4121604,'Renascenca',41),(4121703,'Reserva',41),(4121752,'Reserva do Iguacu',41),(4121802,'Ribeirao Claro',41),(4121901,'Ribeirao do Pinhal',41),(4122008,'Rio Azul',41),(4122107,'Rio Bom',41),(4122156,'Rio Bonito do Iguacu',41),(4122172,'Rio Branco do Ivai',41),(4122206,'Rio Branco do Sul',41),(4122305,'Rio Negro',41),(4122404,'Rolandia',41),(4122503,'Roncador',41),(4122602,'Rondon',41),(4122651,'Rosario do Ivai',41),(4122701,'Sabaudia',41),(4122800,'Salgado Filho',41),(4122909,'Salto do Itarare',41),(4123006,'Salto do Lontra',41),(4123105,'Santa Amelia',41),(4123204,'Santa Cecilia do Pavao',41),(4123303,'Santa Cruz de Monte Castelo',41),(4123402,'Santa Fe',41),(4123501,'Santa Helena',41),(4123600,'Santa Ines',41),(4123709,'Santa Isabel do Ivai',41),(4123808,'Santa Izabel do Oeste',41),(4123824,'Santa Lucia',41),(4123857,'Santa Maria do Oeste',41),(4123907,'Santa Mariana',41),(4123956,'Santa Monica',41),(4124004,'Santana do Itarare',41),(4124020,'Santa Tereza do Oeste',41),(4124053,'Santa Terezinha de Itaipu',41),(4124103,'Santo Antonio da Platina',41),(4124202,'Santo Antonio do Caiua',41),(4124301,'Santo Antonio do Paraiso',41),(4124400,'Santo Antonio do Sudoeste',41),(4124509,'Santo Inacio',41),(4124608,'Sao Carlos do Ivai',41),(4124707,'Sao Jeronimo da Serra',41),(4124806,'Sao Joao',41),(4124905,'Sao Joao do Caiua',41),(4125001,'Sao Joao do Ivai',41),(4125100,'Sao Joao do Triunfo',41),(4125209,'Sao Jorge dOeste',41),(4125308,'Sao Jorge do Ivai',41),(4125357,'Sao Jorge do Patrocinio',41),(4125407,'Sao Jose da Boa Vista',41),(4125456,'Sao Jose das Palmeiras',41),(4125506,'Sao Jose dos Pinhais',41),(4125555,'Sao Manoel do Parana',41),(4125605,'Sao Mateus do Sul',41),(4125704,'Sao Miguel do Iguacu',41),(4125753,'Sao Pedro do Iguacu',41),(4125803,'Sao Pedro do Ivai',41),(4125902,'Sao Pedro do Parana',41),(4126009,'Sao Sebastiao da Amoreira',41),(4126108,'Sao Tome',41),(4126207,'Sapopema',41),(4126256,'Sarandi',41),(4126272,'Saudade do Iguacu',41),(4126306,'Senges',41),(4126355,'Serranopolis do Iguacu',41),(4126405,'Sertaneja',41),(4126504,'Sertanopolis',41),(4126603,'Siqueira Campos',41),(4126652,'Sulina',41),(4126678,'Tamarana',41),(4126702,'Tamboara',41),(4126801,'Tapejara',41),(4126900,'Tapira',41),(4127007,'Teixeira Soares',41),(4127106,'Telemaco Borba',41),(4127205,'Terra Boa',41),(4127304,'Terra Rica',41),(4127403,'Terra Roxa',41),(4127502,'Tibagi',41),(4127601,'Tijucas do Sul',41),(4127700,'Toledo',41),(4127809,'Tomazina',41),(4127858,'Tres Barras do Parana',41),(4127882,'Tunas do Parana',41),(4127908,'Tuneiras do Oeste',41),(4127957,'Tupassi',41),(4127965,'Turvo',41),(4128005,'Ubirata',41),(4128104,'Umuarama',41),(4128203,'Uniao da Vitoria',41),(4128302,'Uniflor',41),(4128401,'Urai',41),(4128500,'Wenceslau Braz',41),(4128534,'Ventania',41),(4128559,'Vera Cruz do Oeste',41),(4128609,'Vere',41),(4128625,'Alto Paraiso',41),(4128633,'Doutor Ulysses',41),(4128658,'Virmond',41),(4128708,'Vitorino',41),(4128807,'Xambre',41),(4200051,'Abdon Batista',42),(4200101,'Abelardo Luz',42),(4200200,'Agrolandia',42),(4200309,'Agronomica',42),(4200408,'agua Doce',42),(4200507,'aguas de Chapeco',42),(4200556,'aguas Frias',42),(4200606,'aguas Mornas',42),(4200705,'Alfredo Wagner',42),(4200754,'Alto Bela Vista',42),(4200804,'Anchieta',42),(4200903,'Angelina',42),(4201000,'Anita Garibaldi',42),(4201109,'Anitapolis',42),(4201208,'Antonio Carlos',42),(4201257,'Apiuna',42),(4201273,'Arabuta',42),(4201307,'Araquari',42),(4201406,'Ararangua',42),(4201505,'Armazem',42),(4201604,'Arroio Trinta',42),(4201653,'Arvoredo',42),(4201703,'Ascurra',42),(4201802,'Atalanta',42),(4201901,'Aurora',42),(4201950,'Balneario Arroio do Silva',42),(4202008,'Balneario Camboriu',42),(4202057,'Balneario Barra do Sul',42),(4202073,'Balneario Gaivota',42),(4202081,'Bandeirante',42),(4202099,'Barra Bonita',42),(4202107,'Barra Velha',42),(4202131,'Bela Vista do Toldo',42),(4202156,'Belmonte',42),(4202206,'Benedito Novo',42),(4202305,'Biguacu',42),(4202404,'Blumenau',42),(4202438,'Bocaina do Sul',42),(4202453,'Bombinhas',42),(4202503,'Bom Jardim da Serra',42),(4202537,'Bom Jesus',42),(4202578,'Bom Jesus do Oeste',42),(4202602,'Bom Retiro',42),(4202701,'Botuvera',42),(4202800,'Braco do Norte',42),(4202859,'Braco do Trombudo',42),(4202875,'Brunopolis',42),(4202909,'Brusque',42),(4203006,'Cacador',42),(4203105,'Caibi',42),(4203154,'Calmon',42),(4203204,'Camboriu',42),(4203253,'Capao Alto',42),(4203303,'Campo Alegre',42),(4203402,'Campo Belo do Sul',42),(4203501,'Campo Ere',42),(4203600,'Campos Novos',42),(4203709,'Canelinha',42),(4203808,'Canoinhas',42),(4203907,'Capinzal',42),(4203956,'Capivari de Baixo',42),(4204004,'Catanduvas',42),(4204103,'Caxambu do Sul',42),(4204152,'Celso Ramos',42),(4204178,'Cerro Negro',42),(4204194,'Chapadao do Lageado',42),(4204202,'Chapeco',42),(4204251,'Cocal do Sul',42),(4204301,'Concordia',42),(4204350,'Cordilheira Alta',42),(4204400,'Coronel Freitas',42),(4204459,'Coronel Martins',42),(4204509,'Corupa',42),(4204558,'Correia Pinto',42),(4204608,'Criciuma',42),(4204707,'Cunha Pora',42),(4204756,'Cunhatai',42),(4204806,'Curitibanos',42),(4204905,'Descanso',42),(4205001,'Dionisio Cerqueira',42),(4205100,'Dona Emma',42),(4205159,'Doutor Pedrinho',42),(4205175,'Entre Rios',42),(4205191,'Ermo',42),(4205209,'Erval Velho',42),(4205308,'Faxinal dos Guedes',42),(4205357,'Flor do Sertao',42),(4205407,'Florianopolis',42),(4205431,'Formosa do Sul',42),(4205456,'Forquilhinha',42),(4205506,'Fraiburgo',42),(4205555,'Frei Rogerio',42),(4205605,'Galvao',42),(4205704,'Garopaba',42),(4205803,'Garuva',42),(4205902,'Gaspar',42),(4206009,'Governador Celso Ramos',42),(4206108,'Grao Para',42),(4206207,'Gravatal',42),(4206306,'Guabiruba',42),(4206405,'Guaraciaba',42),(4206504,'Guaramirim',42),(4206603,'Guaruja do Sul',42),(4206652,'Guatambu',42),(4206702,'Herval dOeste',42),(4206751,'Ibiam',42),(4206801,'Ibicare',42),(4206900,'Ibirama',42),(4207007,'Icara',42),(4207106,'Ilhota',42),(4207205,'Imarui',42),(4207304,'Imbituba',42),(4207403,'Imbuia',42),(4207502,'Indaial',42),(4207577,'Iomere',42),(4207601,'Ipira',42),(4207650,'Ipora do Oeste',42),(4207684,'Ipuacu',42),(4207700,'Ipumirim',42),(4207759,'Iraceminha',42),(4207809,'Irani',42),(4207858,'Irati',42),(4207908,'Irineopolis',42),(4208005,'Ita',42),(4208104,'Itaiopolis',42),(4208203,'Itajai',42),(4208302,'Itapema',42),(4208401,'Itapiranga',42),(4208450,'Itapoa',42),(4208500,'Ituporanga',42),(4208609,'Jabora',42),(4208708,'Jacinto Machado',42),(4208807,'Jaguaruna',42),(4208906,'Jaragua do Sul',42),(4208955,'Jardinopolis',42),(4209003,'Joacaba',42),(4209102,'Joinville',42),(4209151,'Jose Boiteux',42),(4209177,'Jupia',42),(4209201,'Lacerdopolis',42),(4209300,'Lages',42),(4209409,'Laguna',42),(4209458,'Lajeado Grande',42),(4209508,'Laurentino',42),(4209607,'Lauro Muller',42),(4209706,'Lebon Regis',42),(4209805,'Leoberto Leal',42),(4209854,'Lindoia do Sul',42),(4209904,'Lontras',42),(4210001,'Luiz Alves',42),(4210035,'Luzerna',42),(4210050,'Macieira',42),(4210100,'Mafra',42),(4210209,'Major Gercino',42),(4210308,'Major Vieira',42),(4210407,'Maracaja',42),(4210506,'Maravilha',42),(4210555,'Marema',42),(4210605,'Massaranduba',42),(4210704,'Matos Costa',42),(4210803,'Meleiro',42),(4210852,'Mirim Doce',42),(4210902,'Modelo',42),(4211009,'Mondai',42),(4211058,'Monte Carlo',42),(4211108,'Monte Castelo',42),(4211207,'Morro da Fumaca',42),(4211256,'Morro Grande',42),(4211306,'Navegantes',42),(4211405,'Nova Erechim',42),(4211454,'Nova Itaberaba',42),(4211504,'Nova Trento',42),(4211603,'Nova Veneza',42),(4211652,'Novo Horizonte',42),(4211702,'Orleans',42),(4211751,'Otacilio Costa',42),(4211801,'Ouro',42),(4211850,'Ouro Verde',42),(4211876,'Paial',42),(4211892,'Painel',42),(4211900,'Palhoca',42),(4212007,'Palma Sola',42),(4212056,'Palmeira',42),(4212106,'Palmitos',42),(4212205,'Papanduva',42),(4212239,'Paraiso',42),(4212254,'Passo de Torres',42),(4212270,'Passos Maia',42),(4212304,'Paulo Lopes',42),(4212403,'Pedras Grandes',42),(4212502,'Penha',42),(4212601,'Peritiba',42),(4212650,'Pescaria Brava',42),(4212700,'Petrolandia',42),(4212809,'Balneario Picarras',42),(4212908,'Pinhalzinho',42),(4213005,'Pinheiro Preto',42),(4213104,'Piratuba',42),(4213153,'Planalto Alegre',42),(4213203,'Pomerode',42),(4213302,'Ponte Alta',42),(4213351,'Ponte Alta do Norte',42),(4213401,'Ponte Serrada',42),(4213500,'Porto Belo',42),(4213609,'Porto Uniao',42),(4213708,'Pouso Redondo',42),(4213807,'Praia Grande',42),(4213906,'Presidente Castello Branco',42),(4214003,'Presidente Getulio',42),(4214102,'Presidente Nereu',42),(4214151,'Princesa',42),(4214201,'Quilombo',42),(4214300,'Rancho Queimado',42),(4214409,'Rio das Antas',42),(4214508,'Rio do Campo',42),(4214607,'Rio do Oeste',42),(4214706,'Rio dos Cedros',42),(4214805,'Rio do Sul',42),(4214904,'Rio Fortuna',42),(4215000,'Rio Negrinho',42),(4215059,'Rio Rufino',42),(4215075,'Riqueza',42),(4215109,'Rodeio',42),(4215208,'Romelandia',42),(4215307,'Salete',42),(4215356,'Saltinho',42),(4215406,'Salto Veloso',42),(4215455,'Sangao',42),(4215505,'Santa Cecilia',42),(4215554,'Santa Helena',42),(4215604,'Santa Rosa de Lima',42),(4215653,'Santa Rosa do Sul',42),(4215679,'Santa Terezinha',42),(4215687,'Santa Terezinha do Progresso',42),(4215695,'Santiago do Sul',42),(4215703,'Santo Amaro da Imperatriz',42),(4215752,'Sao Bernardino',42),(4215802,'Sao Bento do Sul',42),(4215901,'Sao Bonifacio',42),(4216008,'Sao Carlos',42),(4216057,'Sao Cristovao do Sul',42),(4216107,'Sao Domingos',42),(4216206,'Sao Francisco do Sul',42),(4216255,'Sao Joao do Oeste',42),(4216305,'Sao Joao Batista',42),(4216354,'Sao Joao do Itaperiu',42),(4216404,'Sao Joao do Sul',42),(4216503,'Sao Joaquim',42),(4216602,'Sao Jose',42),(4216701,'Sao Jose do Cedro',42),(4216800,'Sao Jose do Cerrito',42),(4216909,'Sao Lourenco do Oeste',42),(4217006,'Sao Ludgero',42),(4217105,'Sao Martinho',42),(4217154,'Sao Miguel da Boa Vista',42),(4217204,'Sao Miguel do Oeste',42),(4217253,'Sao Pedro de Alcantara',42),(4217303,'Saudades',42),(4217402,'Schroeder',42),(4217501,'Seara',42),(4217550,'Serra Alta',42),(4217600,'Sideropolis',42),(4217709,'Sombrio',42),(4217758,'Sul Brasil',42),(4217808,'Taio',42),(4217907,'Tangara',42),(4217956,'Tigrinhos',42),(4218004,'Tijucas',42),(4218103,'Timbe do Sul',42),(4218202,'Timbo',42),(4218251,'Timbo Grande',42),(4218301,'Tres Barras',42),(4218350,'Treviso',42),(4218400,'Treze de Maio',42),(4218509,'Treze Tilias',42),(4218608,'Trombudo Central',42),(4218707,'Tubarao',42),(4218756,'Tunapolis',42),(4218806,'Turvo',42),(4218855,'Uniao do Oeste',42),(4218905,'Urubici',42),(4218954,'Urupema',42),(4219002,'Urussanga',42),(4219101,'Vargeao',42),(4219150,'Vargem',42),(4219176,'Vargem Bonita',42),(4219200,'Vidal Ramos',42),(4219309,'Videira',42),(4219358,'Vitor Meireles',42),(4219408,'Witmarsum',42),(4219507,'Xanxere',42),(4219606,'Xavantina',42),(4219705,'Xaxim',42),(4219853,'Zortea',42),(4220000,'Balneario Rincao',42),(4300034,'Acegua',43),(4300059,'agua Santa',43),(4300109,'Agudo',43),(4300208,'Ajuricaba',43),(4300307,'Alecrim',43),(4300406,'Alegrete',43),(4300455,'Alegria',43),(4300471,'Almirante Tamandare do Sul',43),(4300505,'Alpestre',43),(4300554,'Alto Alegre',43),(4300570,'Alto Feliz',43),(4300604,'Alvorada',43),(4300638,'Amaral Ferrador',43),(4300646,'Ametista do Sul',43),(4300661,'Andre da Rocha',43),(4300703,'Anta Gorda',43),(4300802,'Antonio Prado',43),(4300851,'Arambare',43),(4300877,'Ararica',43),(4300901,'Aratiba',43),(4301008,'Arroio do Meio',43),(4301057,'Arroio do Sal',43),(4301073,'Arroio do Padre',43),(4301107,'Arroio dos Ratos',43),(4301206,'Arroio do Tigre',43),(4301305,'Arroio Grande',43),(4301404,'Arvorezinha',43),(4301503,'Augusto Pestana',43),(4301552,'aurea',43),(4301602,'Bage',43),(4301636,'Balneario Pinhal',43),(4301651,'Barao',43),(4301701,'Barao de Cotegipe',43),(4301750,'Barao do Triunfo',43),(4301800,'Barracao',43),(4301859,'Barra do Guarita',43),(4301875,'Barra do Quarai',43),(4301909,'Barra do Ribeiro',43),(4301925,'Barra do Rio Azul',43),(4301958,'Barra Funda',43),(4302006,'Barros Cassal',43),(4302055,'Benjamin Constant do Sul',43),(4302105,'Bento Goncalves',43),(4302154,'Boa Vista das Missues',43),(4302204,'Boa Vista do Burica',43),(4302220,'Boa Vista do Cadeado',43),(4302238,'Boa Vista do Incra',43),(4302253,'Boa Vista do Sul',43),(4302303,'Bom Jesus',43),(4302352,'Bom Principio',43),(4302378,'Bom Progresso',43),(4302402,'Bom Retiro do Sul',43),(4302451,'Boqueirao do Leao',43),(4302501,'Bossoroca',43),(4302584,'Bozano',43),(4302600,'Braga',43),(4302659,'Brochier',43),(4302709,'Butia',43),(4302808,'Cacapava do Sul',43),(4302907,'Cacequi',43),(4303004,'Cachoeira do Sul',43),(4303103,'Cachoeirinha',43),(4303202,'Cacique Doble',43),(4303301,'Caibate',43),(4303400,'Caicara',43),(4303509,'Camaqua',43),(4303558,'Camargo',43),(4303608,'Cambara do Sul',43),(4303673,'Campestre da Serra',43),(4303707,'Campina das Missues',43),(4303806,'Campinas do Sul',43),(4303905,'Campo Bom',43),(4304002,'Campo Novo',43),(4304101,'Campos Borges',43),(4304200,'Candelaria',43),(4304309,'Candido Godoi',43),(4304358,'Candiota',43),(4304408,'Canela',43),(4304507,'Cangucu',43),(4304606,'Canoas',43),(4304614,'Canudos do Vale',43),(4304622,'Capao Bonito do Sul',43),(4304630,'Capao da Canoa',43),(4304655,'Capao do Cipo',43),(4304663,'Capao do Leao',43),(4304671,'Capivari do Sul',43),(4304689,'Capela de Santana',43),(4304697,'Capitao',43),(4304705,'Carazinho',43),(4304713,'Caraa',43),(4304804,'Carlos Barbosa',43),(4304853,'Carlos Gomes',43),(4304903,'Casca',43),(4304952,'Caseiros',43),(4305009,'Catuipe',43),(4305108,'Caxias do Sul',43),(4305116,'Centenario',43),(4305124,'Cerrito',43),(4305132,'Cerro Branco',43),(4305157,'Cerro Grande',43),(4305173,'Cerro Grande do Sul',43),(4305207,'Cerro Largo',43),(4305306,'Chapada',43),(4305355,'Charqueadas',43),(4305371,'Charrua',43),(4305405,'Chiapetta',43),(4305439,'Chui',43),(4305447,'Chuvisca',43),(4305454,'Cidreira',43),(4305504,'Ciriaco',43),(4305587,'Colinas',43),(4305603,'Colorado',43),(4305702,'Condor',43),(4305801,'Constantina',43),(4305835,'Coqueiro Baixo',43),(4305850,'Coqueiros do Sul',43),(4305871,'Coronel Barros',43),(4305900,'Coronel Bicaco',43),(4305934,'Coronel Pilar',43),(4305959,'Cotipora',43),(4305975,'Coxilha',43),(4306007,'Crissiumal',43),(4306056,'Cristal',43),(4306072,'Cristal do Sul',43),(4306106,'Cruz Alta',43),(4306130,'Cruzaltense',43),(4306205,'Cruzeiro do Sul',43),(4306304,'David Canabarro',43),(4306320,'Derrubadas',43),(4306353,'Dezesseis de Novembro',43),(4306379,'Dilermando de Aguiar',43),(4306403,'Dois Irmaos',43),(4306429,'Dois Irmaos das Missues',43),(4306452,'Dois Lajeados',43),(4306502,'Dom Feliciano',43),(4306551,'Dom Pedro de Alcantara',43),(4306601,'Dom Pedrito',43),(4306700,'Dona Francisca',43),(4306734,'Doutor Mauricio Cardoso',43),(4306759,'Doutor Ricardo',43),(4306767,'Eldorado do Sul',43),(4306809,'Encantado',43),(4306908,'Encruzilhada do Sul',43),(4306924,'Engenho Velho',43),(4306932,'Entre-Ijuis',43),(4306957,'Entre Rios do Sul',43),(4306973,'Erebango',43),(4307005,'Erechim',43),(4307054,'Ernestina',43),(4307104,'Herval',43),(4307203,'Erval Grande',43),(4307302,'Erval Seco',43),(4307401,'Esmeralda',43),(4307450,'Esperanca do Sul',43),(4307500,'Espumoso',43),(4307559,'Estacao',43),(4307609,'Estancia Velha',43),(4307708,'Esteio',43),(4307807,'Estrela',43),(4307815,'Estrela Velha',43),(4307831,'Eugenio de Castro',43),(4307864,'Fagundes Varela',43),(4307906,'Farroupilha',43),(4308003,'Faxinal do Soturno',43),(4308052,'Faxinalzinho',43),(4308078,'Fazenda Vilanova',43),(4308102,'Feliz',43),(4308201,'Flores da Cunha',43),(4308250,'Floriano Peixoto',43),(4308300,'Fontoura Xavier',43),(4308409,'Formigueiro',43),(4308433,'Forquetinha',43),(4308458,'Fortaleza dos Valos',43),(4308508,'Frederico Westphalen',43),(4308607,'Garibaldi',43),(4308656,'Garruchos',43),(4308706,'Gaurama',43),(4308805,'General Camara',43),(4308854,'Gentil',43),(4308904,'Getulio Vargas',43),(4309001,'Girua',43),(4309050,'Glorinha',43),(4309100,'Gramado',43),(4309126,'Gramado dos Loureiros',43),(4309159,'Gramado Xavier',43),(4309209,'Gravatai',43),(4309258,'Guabiju',43),(4309308,'Guaiba',43),(4309407,'Guapore',43),(4309506,'Guarani das Missues',43),(4309555,'Harmonia',43),(4309571,'Herveiras',43),(4309605,'Horizontina',43),(4309654,'Hulha Negra',43),(4309704,'Humaita',43),(4309753,'Ibarama',43),(4309803,'Ibiaca',43),(4309902,'Ibiraiaras',43),(4309951,'Ibirapuita',43),(4310009,'Ibiruba',43),(4310108,'Igrejinha',43),(4310207,'Ijui',43),(4310306,'Ilopolis',43),(4310330,'Imbe',43),(4310363,'Imigrante',43),(4310405,'Independencia',43),(4310413,'Inhacora',43),(4310439,'Ipe',43),(4310462,'Ipiranga do Sul',43),(4310504,'Irai',43),(4310538,'Itaara',43),(4310553,'Itacurubi',43),(4310579,'Itapuca',43),(4310603,'Itaqui',43),(4310652,'Itati',43),(4310702,'Itatiba do Sul',43),(4310751,'Ivora',43),(4310801,'Ivoti',43),(4310850,'Jaboticaba',43),(4310876,'Jacuizinho',43),(4310900,'Jacutinga',43),(4311007,'Jaguarao',43),(4311106,'Jaguari',43),(4311122,'Jaquirana',43),(4311130,'Jari',43),(4311155,'Joia',43),(4311205,'Julio de Castilhos',43),(4311239,'Lagoa Bonita do Sul',43),(4311254,'Lagoao',43),(4311270,'Lagoa dos Tres Cantos',43),(4311304,'Lagoa Vermelha',43),(4311403,'Lajeado',43),(4311429,'Lajeado do Bugre',43),(4311502,'Lavras do Sul',43),(4311601,'Liberato Salzano',43),(4311627,'Lindolfo Collor',43),(4311643,'Linha Nova',43),(4311700,'Machadinho',43),(4311718,'Macambara',43),(4311734,'Mampituba',43),(4311759,'Manoel Viana',43),(4311775,'Maquine',43),(4311791,'Marata',43),(4311809,'Marau',43),(4311908,'Marcelino Ramos',43),(4311981,'Mariana Pimentel',43),(4312005,'Mariano Moro',43),(4312054,'Marques de Souza',43),(4312104,'Mata',43),(4312138,'Mato Castelhano',43),(4312153,'Mato Leitao',43),(4312179,'Mato Queimado',43),(4312203,'Maximiliano de Almeida',43),(4312252,'Minas do Leao',43),(4312302,'Miraguai',43),(4312351,'Montauri',43),(4312377,'Monte Alegre dos Campos',43),(4312385,'Monte Belo do Sul',43),(4312401,'Montenegro',43),(4312427,'Mormaco',43),(4312443,'Morrinhos do Sul',43),(4312450,'Morro Redondo',43),(4312476,'Morro Reuter',43),(4312500,'Mostardas',43),(4312609,'Mucum',43),(4312617,'Muitos Capues',43),(4312625,'Muliterno',43),(4312658,'Nao-Me-Toque',43),(4312674,'Nicolau Vergueiro',43),(4312708,'Nonoai',43),(4312757,'Nova Alvorada',43),(4312807,'Nova Araca',43),(4312906,'Nova Bassano',43),(4312955,'Nova Boa Vista',43),(4313003,'Nova Brescia',43),(4313011,'Nova Candelaria',43),(4313037,'Nova Esperanca do Sul',43),(4313060,'Nova Hartz',43),(4313086,'Nova Padua',43),(4313102,'Nova Palma',43),(4313201,'Nova Petropolis',43),(4313300,'Nova Prata',43),(4313334,'Nova Ramada',43),(4313359,'Nova Roma do Sul',43),(4313375,'Nova Santa Rita',43),(4313391,'Novo Cabrais',43),(4313409,'Novo Hamburgo',43),(4313425,'Novo Machado',43),(4313441,'Novo Tiradentes',43),(4313466,'Novo Xingu',43),(4313490,'Novo Barreiro',43),(4313508,'Osorio',43),(4313607,'Paim Filho',43),(4313656,'Palmares do Sul',43),(4313706,'Palmeira das Missues',43),(4313805,'Palmitinho',43),(4313904,'Panambi',43),(4313953,'Pantano Grande',43),(4314001,'Parai',43),(4314027,'Paraiso do Sul',43),(4314035,'Pareci Novo',43),(4314050,'Parobe',43),(4314068,'Passa Sete',43),(4314076,'Passo do Sobrado',43),(4314100,'Passo Fundo',43),(4314134,'Paulo Bento',43),(4314159,'Paverama',43),(4314175,'Pedras Altas',43),(4314209,'Pedro Osorio',43),(4314308,'Pejucara',43),(4314407,'Pelotas',43),(4314423,'Picada Cafe',43),(4314456,'Pinhal',43),(4314464,'Pinhal da Serra',43),(4314472,'Pinhal Grande',43),(4314498,'Pinheirinho do Vale',43),(4314506,'Pinheiro Machado',43),(4314548,'Pinto Bandeira',43),(4314555,'Pirapo',43),(4314605,'Piratini',43),(4314704,'Planalto',43),(4314753,'Poco das Antas',43),(4314779,'Pontao',43),(4314787,'Ponte Preta',43),(4314803,'Portao',43),(4314902,'Porto Alegre',43),(4315008,'Porto Lucena',43),(4315057,'Porto Maua',43),(4315073,'Porto Vera Cruz',43),(4315107,'Porto Xavier',43),(4315131,'Pouso Novo',43),(4315149,'Presidente Lucena',43),(4315156,'Progresso',43),(4315172,'Protasio Alves',43),(4315206,'Putinga',43),(4315305,'Quarai',43),(4315313,'Quatro Irmaos',43),(4315321,'Quevedos',43),(4315354,'Quinze de Novembro',43),(4315404,'Redentora',43),(4315453,'Relvado',43),(4315503,'Restinga Seca',43),(4315552,'Rio dos indios',43),(4315602,'Rio Grande',43),(4315701,'Rio Pardo',43),(4315750,'Riozinho',43),(4315800,'Roca Sales',43),(4315909,'Rodeio Bonito',43),(4315958,'Rolador',43),(4316006,'Rolante',43),(4316105,'Ronda Alta',43),(4316204,'Rondinha',43),(4316303,'Roque Gonzales',43),(4316402,'Rosario do Sul',43),(4316428,'Sagrada Familia',43),(4316436,'Saldanha Marinho',43),(4316451,'Salto do Jacui',43),(4316477,'Salvador das Missues',43),(4316501,'Salvador do Sul',43),(4316600,'Sananduva',43),(4316709,'Santa Barbara do Sul',43),(4316733,'Santa Cecilia do Sul',43),(4316758,'Santa Clara do Sul',43),(4316808,'Santa Cruz do Sul',43),(4316907,'Santa Maria',43),(4316956,'Santa Maria do Herval',43),(4316972,'Santa Margarida do Sul',43),(4317004,'Santana da Boa Vista',43),(4317103,'SantAna do Livramento',43),(4317202,'Santa Rosa',43),(4317251,'Santa Tereza',43),(4317301,'Santa Vitoria do Palmar',43),(4317400,'Santiago',43),(4317509,'Santo angelo',43),(4317558,'Santo Antonio do Palma',43),(4317608,'Santo Antonio da Patrulha',43),(4317707,'Santo Antonio das Missues',43),(4317756,'Santo Antonio do Planalto',43),(4317806,'Santo Augusto',43),(4317905,'Santo Cristo',43),(4317954,'Santo Expedito do Sul',43),(4318002,'Sao Borja',43),(4318051,'Sao Domingos do Sul',43),(4318101,'Sao Francisco de Assis',43),(4318200,'Sao Francisco de Paula',43),(4318309,'Sao Gabriel',43),(4318408,'Sao Jeronimo',43),(4318424,'Sao Joao da Urtiga',43),(4318432,'Sao Joao do Polesine',43),(4318440,'Sao Jorge',43),(4318457,'Sao Jose das Missues',43),(4318465,'Sao Jose do Herval',43),(4318481,'Sao Jose do Hortencio',43),(4318499,'Sao Jose do Inhacora',43),(4318507,'Sao Jose do Norte',43),(4318606,'Sao Jose do Ouro',43),(4318614,'Sao Jose do Sul',43),(4318622,'Sao Jose dos Ausentes',43),(4318705,'Sao Leopoldo',43),(4318804,'Sao Lourenco do Sul',43),(4318903,'Sao Luiz Gonzaga',43),(4319000,'Sao Marcos',43),(4319109,'Sao Martinho',43),(4319125,'Sao Martinho da Serra',43),(4319158,'Sao Miguel das Missues',43),(4319208,'Sao Nicolau',43),(4319307,'Sao Paulo das Missues',43),(4319356,'Sao Pedro da Serra',43),(4319364,'Sao Pedro das Missues',43),(4319372,'Sao Pedro do Butia',43),(4319406,'Sao Pedro do Sul',43),(4319505,'Sao Sebastiao do Cai',43),(4319604,'Sao Sepe',43),(4319703,'Sao Valentim',43),(4319711,'Sao Valentim do Sul',43),(4319737,'Sao Valerio do Sul',43),(4319752,'Sao Vendelino',43),(4319802,'Sao Vicente do Sul',43),(4319901,'Sapiranga',43),(4320008,'Sapucaia do Sul',43),(4320107,'Sarandi',43),(4320206,'Seberi',43),(4320230,'Sede Nova',43),(4320263,'Segredo',43),(4320305,'Selbach',43),(4320321,'Senador Salgado Filho',43),(4320354,'Sentinela do Sul',43),(4320404,'Serafina Correa',43),(4320453,'Serio',43),(4320503,'Sertao',43),(4320552,'Sertao Santana',43),(4320578,'Sete de Setembro',43),(4320602,'Severiano de Almeida',43),(4320651,'Silveira Martins',43),(4320677,'Sinimbu',43),(4320701,'Sobradinho',43),(4320800,'Soledade',43),(4320859,'Tabai',43),(4320909,'Tapejara',43),(4321006,'Tapera',43),(4321105,'Tapes',43),(4321204,'Taquara',43),(4321303,'Taquari',43),(4321329,'Taquarucu do Sul',43),(4321352,'Tavares',43),(4321402,'Tenente Portela',43),(4321436,'Terra de Areia',43),(4321451,'Teutonia',43),(4321469,'Tio Hugo',43),(4321477,'Tiradentes do Sul',43),(4321493,'Toropi',43),(4321501,'Torres',43),(4321600,'Tramandai',43),(4321626,'Travesseiro',43),(4321634,'Tres Arroios',43),(4321667,'Tres Cachoeiras',43),(4321709,'Tres Coroas',43),(4321808,'Tres de Maio',43),(4321832,'Tres Forquilhas',43),(4321857,'Tres Palmeiras',43),(4321907,'Tres Passos',43),(4321956,'Trindade do Sul',43),(4322004,'Triunfo',43),(4322103,'Tucunduva',43),(4322152,'Tunas',43),(4322186,'Tupanci do Sul',43),(4322202,'Tupancireta',43),(4322251,'Tupandi',43),(4322301,'Tuparendi',43),(4322327,'Turucu',43),(4322343,'Ubiretama',43),(4322350,'Uniao da Serra',43),(4322376,'Unistalda',43),(4322400,'Uruguaiana',43),(4322509,'Vacaria',43),(4322525,'Vale Verde',43),(4322533,'Vale do Sol',43),(4322541,'Vale Real',43),(4322558,'Vanini',43),(4322608,'Venancio Aires',43),(4322707,'Vera Cruz',43),(4322806,'Veranopolis',43),(4322855,'Vespasiano Correa',43),(4322905,'Viadutos',43),(4323002,'Viamao',43),(4323101,'Vicente Dutra',43),(4323200,'Victor Graeff',43),(4323309,'Vila Flores',43),(4323358,'Vila Langaro',43),(4323408,'Vila Maria',43),(4323457,'Vila Nova do Sul',43),(4323507,'Vista Alegre',43),(4323606,'Vista Alegre do Prata',43),(4323705,'Vista Gaucha',43),(4323754,'Vitoria das Missues',43),(4323804,'Xangri-la',43);
/*!40000 ALTER TABLE `municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nfce`
--

DROP TABLE IF EXISTS `nfce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nfce` (
  `id` int NOT NULL AUTO_INCREMENT,
  `xml_distribuicao` longtext,
  `chave_acesso` varchar(45) NOT NULL,
  `venda_fk_id` int NOT NULL,
  `dh_emi` datetime NOT NULL,
  `nnf` int NOT NULL,
  `tp_emis` int NOT NULL,
  `tp_amb` int NOT NULL,
  `xml` longtext NOT NULL,
  `ret_sefaz` longtext,
  `situacao` int DEFAULT NULL,
  `protocolo` varchar(15) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `resultado_aut_daf` int DEFAULT NULL,
  `id_aut_daf` varchar(600) DEFAULT NULL,
  `aut_apg_daf` varchar(600) DEFAULT NULL,
  `retida_daf` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_nfce_chave` (`chave_acesso`),
  KEY `fk_nfce_venda1_idx` (`venda_fk_id`),
  KEY `uk_nfce_chave_idx` (`chave_acesso`),
  CONSTRAINT `fk_nfce_venda1` FOREIGN KEY (`venda_fk_id`) REFERENCES `venda` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nfce`
--

LOCK TABLES `nfce` WRITE;
/*!40000 ALTER TABLE `nfce` DISABLE KEYS */;
/*!40000 ALTER TABLE `nfce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa`
--

DROP TABLE IF EXISTS `pessoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `telefone_principal` varchar(225) DEFAULT NULL,
  `email` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa`
--

LOCK TABLES `pessoa` WRITE;
/*!40000 ALTER TABLE `pessoa` DISABLE KEYS */;
INSERT INTO `pessoa` VALUES (1,'Ryfax Xizapovazu Wucukumoxapa','(48) 22513-5350','contato@kudeae.com.br'),(2,'Mobaga','(48) 99913-0491','contato@mobaga.com.br'),(3,'Mahonouab eheheio igafute','(48) 99744-5956','contato@mahono.com.br'),(4,'Gebi umim oao','(48) 97997-4456','contato@gebium.com.br'),(5,'Forapof oqexov emaqaour','(48) 98894-3878','contato@forapo.com.br'),(6,'Saraja aueh aounijub','(48) 97950-4813','contato@saraja.com.br');
/*!40000 ALTER TABLE `pessoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa_fisica`
--

DROP TABLE IF EXISTS `pessoa_fisica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa_fisica` (
  `pessoa_fk_id` int NOT NULL,
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`pessoa_fk_id`),
  UNIQUE KEY `cpf_UNIQUE` (`cpf`),
  KEY `fk_pessoa_fisica_pessoa1_idx` (`pessoa_fk_id`),
  CONSTRAINT `fk_pessoa_fisica_pessoa1` FOREIGN KEY (`pessoa_fk_id`) REFERENCES `pessoa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa_fisica`
--

LOCK TABLES `pessoa_fisica` WRITE;
/*!40000 ALTER TABLE `pessoa_fisica` DISABLE KEYS */;
INSERT INTO `pessoa_fisica` VALUES (6,'54192931451'),(5,'58106333744'),(3,'66952583688'),(4,'99623852886');
/*!40000 ALTER TABLE `pessoa_fisica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pessoa_juridica`
--

DROP TABLE IF EXISTS `pessoa_juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pessoa_juridica` (
  `pessoa_fk_id` int NOT NULL,
  `cnpj` varchar(14) NOT NULL,
  `nome_fantasia` varchar(225) NOT NULL,
  `inscricao_estadual_sc` varchar(9) NOT NULL,
  PRIMARY KEY (`pessoa_fk_id`),
  UNIQUE KEY `cnpj_UNIQUE` (`cnpj`),
  KEY `fk_pessoa_juridica_pessoa1_idx` (`pessoa_fk_id`),
  CONSTRAINT `fk_pessoa_juridica_pessoa1` FOREIGN KEY (`pessoa_fk_id`) REFERENCES `pessoa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pessoa_juridica`
--

LOCK TABLES `pessoa_juridica` WRITE;
/*!40000 ALTER TABLE `pessoa_juridica` DISABLE KEYS */;
INSERT INTO `pessoa_juridica` VALUES (1,'28572444000110','Wazumanaji Kybu','752271637'),(2,'75519779000155','Gote uoe','409137980');
/*!40000 ALTER TABLE `pessoa_juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ponto_venda`
--

DROP TABLE IF EXISTS `ponto_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ponto_venda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `serial` varchar(80) DEFAULT NULL,
  `id_pdv` varchar(10) NOT NULL,
  `empresa_fk_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ponto_venda_empresa1_idx` (`empresa_fk_id`),
  CONSTRAINT `fk_ponto_venda_empresa1` FOREIGN KEY (`empresa_fk_id`) REFERENCES `empresa` (`pessoa_juridica_fk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ponto_venda`
--

LOCK TABLES `ponto_venda` WRITE;
/*!40000 ALTER TABLE `ponto_venda` DISABLE KEYS */;
INSERT INTO `ponto_venda` VALUES (1,'Daqeoaja','125488','2QPS3jJ8Eb',1);
/*!40000 ALTER TABLE `ponto_venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(120) NOT NULL,
  `marca` varchar(120) DEFAULT NULL,
  `valor_unitario` double NOT NULL,
  `cfop` varchar(60) NOT NULL,
  `cean` varchar(14) NOT NULL,
  `ncm` int NOT NULL,
  `icms_modalidade` varchar(10) NOT NULL,
  `icms_csosn` varchar(10) NOT NULL,
  `icms_cst` varchar(10) NOT NULL,
  `unidade` varchar(10) NOT NULL,
  `perc_trib` decimal(10,3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'Zahoteya eeiv','Pobugix',1.99,'5102','SEM GTIN',51795137,'102','400','07','UN',0.450),(2,'Pekuqaio ayala','Rauizex',1.99,'5102','SEM GTIN',64662492,'102','400','07','UN',0.360),(3,'Tohiyopey oiut','Deuime',1.99,'5102','SEM GTIN',98608701,'102','400','07','UN',0.190),(4,'Nudulube aiageg','Viwirudue',1.99,'5102','SEM GTIN',79702978,'102','400','07','UN',0.150),(5,'Darofuuu apuqiy','Kizabo',1.99,'5102','SEM GTIN',28648102,'102','400','07','UN',0.260),(6,'Lepeoi ieiz','Kefihilef',1.99,'5102','SEM GTIN',53889174,'102','400','07','UN',0.010),(7,'Sewadixed oaimeeeb','Beboheb',1.99,'5102','SEM GTIN',83566068,'102','400','07','UN',0.450),(8,'Vehami aoueapa','Rilirudu',1.99,'5102','SEM GTIN',84061792,'102','400','07','UN',0.480),(9,'Koioiitut uqej','Gilaoiia',1.99,'5102','SEM GTIN',45508429,'102','400','07','UN',0.400),(10,'Vowig eje','Temefemu',1.99,'5102','SEM GTIN',45324892,'102','400','07','UN',0.390),(11,'Kotahow utuwiqud','Mipetudi',1.99,'5102','SEM GTIN',53966284,'102','400','07','UN',0.090),(12,'Leui awipa','Covecexaq',1.99,'5102','SEM GTIN',13479585,'102','400','07','UN',0.170),(13,'Lecogixal ouecih','Fegemaxu',1.99,'5102','SEM GTIN',64520996,'102','400','07','UN',0.150),(14,'Vamooeae onuaoe','Jaieya',1.99,'5102','SEM GTIN',14919621,'102','400','07','UN',0.140),(15,'Rekau ueua','Domauad',1.99,'5102','SEM GTIN',43277319,'102','400','07','UN',0.280);
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requisicoes`
--

DROP TABLE IF EXISTS `requisicoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requisicoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pedido` longtext NOT NULL,
  `resposta` longtext,
  `servico` varchar(255) NOT NULL,
  `nfce_fk_id` int DEFAULT NULL,
  `data_hora` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_requisicoes_nfce1_idx` (`nfce_fk_id`),
  CONSTRAINT `fk_requisicoes_nfce1` FOREIGN KEY (`nfce_fk_id`) REFERENCES `nfce` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requisicoes`
--

LOCK TABLES `requisicoes` WRITE;
/*!40000 ALTER TABLE `requisicoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `requisicoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uf`
--

DROP TABLE IF EXISTS `uf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uf` (
  `codigo_ibge` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `sigla` varchar(2) NOT NULL,
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
-- Table structure for table `venda`
--

DROP TABLE IF EXISTS `venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_hora` datetime NOT NULL,
  `desconto` decimal(2,2) DEFAULT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  `cliente_fk_id` int DEFAULT NULL,
  `funcionario_pdv_fk_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_venda_cliente1_idx` (`cliente_fk_id`),
  KEY `fk_venda_funcionario_pdv1_idx` (`funcionario_pdv_fk_id`),
  CONSTRAINT `fk_venda_cliente1` FOREIGN KEY (`cliente_fk_id`) REFERENCES `cliente` (`pessoa_fisica_fk_id`),
  CONSTRAINT `fk_venda_funcionario_pdv1` FOREIGN KEY (`funcionario_pdv_fk_id`) REFERENCES `funcionario_pdv` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda`
--

LOCK TABLES `venda` WRITE;
/*!40000 ALTER TABLE `venda` DISABLE KEYS */;
/*!40000 ALTER TABLE `venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venda_item`
--

DROP TABLE IF EXISTS `venda_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda_item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `venda_fk_id` int NOT NULL,
  `produto_fk_id` int NOT NULL,
  `quantidade` int NOT NULL,
  `valor_item` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_venda_has_produto_produto1_idx` (`produto_fk_id`),
  KEY `fk_venda_has_produto_venda1_idx` (`venda_fk_id`),
  CONSTRAINT `fk_venda_has_produto_produto1` FOREIGN KEY (`produto_fk_id`) REFERENCES `produto` (`id`),
  CONSTRAINT `fk_venda_has_produto_venda1` FOREIGN KEY (`venda_fk_id`) REFERENCES `venda` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda_item`
--

LOCK TABLES `venda_item` WRITE;
/*!40000 ALTER TABLE `venda_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `venda_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;