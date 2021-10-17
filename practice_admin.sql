-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2020 at 08:42 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `practice_admin`
--

-- --------------------------------------------------------

--
-- Table structure for table `practice_admin`
--

CREATE TABLE `practice_admin` (
  `AdminId` int(11) NOT NULL,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `practice_admin`
--

INSERT INTO `practice_admin` (`AdminId`, `Username`, `Password`) VALUES
(1, 'root', 'root');

-- --------------------------------------------------------

--
-- Table structure for table `practice_user`
--

CREATE TABLE `practice_user` (
  `UserId` int(11) NOT NULL,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `practice_user`
--

INSERT INTO `practice_user` (`UserId`, `Username`, `Password`) VALUES
(1, 'piyu', 'piyu'),
(2, 'swarangi', 'swarangi'),
(3, 'simran', 'simran');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `practice_admin`
--
ALTER TABLE `practice_admin`
  ADD PRIMARY KEY (`AdminId`);

--
-- Indexes for table `practice_user`
--
ALTER TABLE `practice_user`
  ADD PRIMARY KEY (`UserId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `practice_admin`
--
ALTER TABLE `practice_admin`
  MODIFY `AdminId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `practice_user`
--
ALTER TABLE `practice_user`
  MODIFY `UserId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
