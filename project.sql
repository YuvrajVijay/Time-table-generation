-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2018 at 01:22 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `aid` int(11) NOT NULL,
  `admin_id` varchar(30) DEFAULT NULL,
  `password` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`aid`, `admin_id`, `password`) VALUES
(1, 'ayush_123', 12345),
(2, 'nivali_123', 123456);

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_number` int(11) DEFAULT NULL,
  `book_name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_number`, `book_name`) VALUES
(4235, 'Data stucture'),
(234162, 'Data stucture'),
(23451, 'Diffrential Equation'),
(2345, 'B.S.Grewal'),
(2315, 'Let us C'),
(12341, 'V.K.Mehta');

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `Roll_Number` bigint(45) NOT NULL,
  `book_name` varchar(35) DEFAULT NULL,
  `book_No` varchar(45) DEFAULT NULL,
  `issue_date` datetime NOT NULL,
  `return_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`Roll_Number`, `book_name`, `book_No`, `issue_date`, `return_date`) VALUES
(17503, 'Operating system', '45261', '2018-06-29 00:00:00', '2018-07-29 00:00:00'),
(17502, 'Avdhanullu', '241321', '2018-06-29 00:00:00', '2018-07-29 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `student_detail`
--

CREATE TABLE `student_detail` (
  `roll_number` bigint(56) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Father_name` varchar(45) DEFAULT NULL,
  `mother_name` varchar(45) DEFAULT NULL,
  `Date_Of_Birth` varchar(45) DEFAULT NULL,
  `Branch` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_detail`
--

INSERT INTO `student_detail` (`roll_number`, `Name`, `Father_name`, `mother_name`, `Date_Of_Birth`, `Branch`) VALUES
(17501, 'Ayush Jain', 'Deepak kumar jain', 'Aruna Jain', 'March06,2000', 'CSE'),
(17502, 'Nivali Yadav', 'Ajay singh yadav', 'Rita rani yadav', 'September15,2000', 'ECE-Dual'),
(17503, 'Akshay singh', 'Mukesh Singh', 'Alka singh', 'May24,1998', 'Mechanical');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`aid`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD UNIQUE KEY `book_number` (`book_number`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD UNIQUE KEY `book_No` (`book_No`);

--
-- Indexes for table `student_detail`
--
ALTER TABLE `student_detail`
  ADD PRIMARY KEY (`roll_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
