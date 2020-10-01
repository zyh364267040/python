-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: miniweb
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `miniweb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `miniweb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `miniweb`;

--
-- Table structure for table `tb_books`
--

DROP TABLE IF EXISTS `tb_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_books` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `btitle` varchar(10) NOT NULL,
  `bpubdata` date DEFAULT NULL,
  `bread` int(10) unsigned DEFAULT NULL,
  `bcomment` varchar(20) DEFAULT NULL,
  `isdelete` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_books`
--

LOCK TABLES `tb_books` WRITE;
/*!40000 ALTER TABLE `tb_books` DISABLE KEYS */;
INSERT INTO `tb_books` VALUES (1,'射雕英雄传','1980-05-01',12,'34','\0'),(2,'天龙八部','1986-07-24',36,'40','\0'),(3,'笑傲江湖','1995-12-24',20,'80','\0'),(4,'雪山飞狐','1987-11-11',58,'24','\0');
/*!40000 ALTER TABLE `tb_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_heros`
--

DROP TABLE IF EXISTS `tb_heros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_heros` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `hname` varchar(10) NOT NULL,
  `hgender` bit(1) DEFAULT NULL,
  `hbook_id` int(10) unsigned DEFAULT NULL,
  `hcomment` varchar(20) DEFAULT NULL,
  `isdelete` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `hbook_id` (`hbook_id`),
  CONSTRAINT `tb_heros_ibfk_1` FOREIGN KEY (`hbook_id`) REFERENCES `tb_books` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_heros`
--

LOCK TABLES `tb_heros` WRITE;
/*!40000 ALTER TABLE `tb_heros` DISABLE KEYS */;
INSERT INTO `tb_heros` VALUES (1,'郭靖','',1,'降龙十八掌','\0'),(2,'黄蓉','\0',1,'打狗棍法','\0'),(3,'黄药师','',1,'弹指神通','\0'),(4,'欧阳锋','',1,'蛤蟆功','\0'),(5,'梅超风','\0',1,'九阴白骨爪','\0'),(6,'乔峰','',2,'降龙十八掌','\0'),(7,'段誉','',2,'六脉神剑','\0'),(8,'虚竹','',2,'天山六阳掌','\0'),(9,'王语嫣','\0',2,'神仙姐姐','\0'),(10,'令狐冲','',3,'独孤九剑','\0'),(11,'任盈盈','\0',3,'弹琴','\0'),(12,'岳不群','',3,'华山剑法','\0'),(13,'东方不败','\0',3,'葵花宝典','\0'),(14,'胡斐','',4,'胡家刀法','\0'),(15,'苗若兰','\0',4,'黄衣','\0'),(16,'程灵素','\0',4,'医术','\0'),(17,'袁紫衣','\0',4,'六合拳','\0');
/*!40000 ALTER TABLE `tb_heros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-22 19:46:46
