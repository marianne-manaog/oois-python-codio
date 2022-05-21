-- MySQL 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: <MY_DATABASE>
-- ------------------------------------------------------
-- Server version       5.7.31-0ubuntu0.18.04.1

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;

CREATE TABLE 'grades' (
  'surname' varchar(30) DEFAULT NULL,
  'forename' varchar(30) DEFAULT NULL,
  'module_code' varchar(8) DEFAULT NULL,
  'scores' int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `modules`;

CREATE TABLE 'modules' (
	'module_code' varchar(8) DEFAULT NULL,
  'module_name' varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `students`;

CREATE TABLE 'students' (
  'student_id' varchar(10) DEFAULT NULL,
  'forename' varchar(30) DEFAULT NULL,
  'surname' varchar(30) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `link_table`;

CREATE TABLE 'link_table' (
  'result_id' varchar(10) DEFAULT NULL,
  'student_id' varchar(10) DEFAULT NULL,
  'module_code' varchar(8) DEFAULT NULL,
  'scores' int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data into the tables above
--

LOCK TABLES 'grades' WRITE;

INSERT INTO 'grades' VALUES ('Smith','John','MATH101',85),('Jones','Dave','COMP101',93),('Bob','Alice','MATH101',50),('Alice','Bob','MATH101',66);

UNLOCK TABLES;

LOCK TABLES 'modules' WRITE;

INSERT INTO 'modules' VALUES ('MATH101','Mathematics'),('COMP101','Computational Modelling');

UNLOCK TABLES;

LOCK TABLES 'students' WRITE;

INSERT INTO 'students' VALUES ('JS01'. 'John','Smith'),('DJ01','Dave','Jones'),('AB01', 'Alice','Bob'),('BA01','Bob','Alice');

UNLOCK TABLES;

LOCK TABLES 'link_table' WRITE;

INSERT INTO 'link_table' VALUES ('RE01','JS01','MATH101',85),('RE02','DJ01','COMP101',93),('RE03','AB01','MATH101',50),('RE04','BA01','MATH101',66);

UNLOCK TABLES;