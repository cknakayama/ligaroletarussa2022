-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18-Mar-2022 às 19:51
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `rr2022`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `autenticacao`
--

CREATE TABLE `autenticacao` (
  `cookie` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `autenticacao`
--

INSERT INTO `autenticacao` (`cookie`) VALUES
('1141b282a5a56590081f6c0d304b2836a786671525f507441517872666d6d5544496e5239384e447a7656784a503063476642734e6d75724943796141464e38304836596a797a426455555630556f4972553577736e625f79614c66446f3039726f6c614f4e673d3d3a303a6e616b6179616d615f323030395f35');

-- --------------------------------------------------------

--
-- Estrutura da tabela `leliminatoria_ccap`
--

CREATE TABLE `leliminatoria_ccap` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL,
  `Pts` double DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `leliminatoria_scap`
--

CREATE TABLE `leliminatoria_scap` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL,
  `Pts` double DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lprincipal_ccap`
--

CREATE TABLE `lprincipal_ccap` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL,
  `Pts_total` double DEFAULT 0,
  `Mensal` double DEFAULT 0,
  `Patrimonio` double DEFAULT 0,
  `Mito` double DEFAULT 0,
  `Turno` double DEFAULT 0,
  `Returno` double DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lprincipal_scap`
--

CREATE TABLE `lprincipal_scap` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL,
  `Pts_total` double DEFAULT 0,
  `Mensal` double DEFAULT 0,
  `Patrimonio` double DEFAULT 0,
  `Mito` double DEFAULT 0,
  `Turno` double DEFAULT 0,
  `Returno` double DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mmavulso`
--

CREATE TABLE `mmavulso` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mmliga`
--

CREATE TABLE `mmliga` (
  `ID` int(12) NOT NULL,
  `Nome` tinytext DEFAULT NULL,
  `Cartoleiro` tinytext DEFAULT NULL,
  `Rodada1` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `mmliga`
--

INSERT INTO `mmliga` (`ID`, `Nome`, `Cartoleiro`, `Rodada1`) VALUES
(1352354, 'SC Karate Kid', 'Seu Miagi', 100);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `leliminatoria_ccap`
--
ALTER TABLE `leliminatoria_ccap`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `leliminatoria_scap`
--
ALTER TABLE `leliminatoria_scap`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `lprincipal_ccap`
--
ALTER TABLE `lprincipal_ccap`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `lprincipal_scap`
--
ALTER TABLE `lprincipal_scap`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `mmavulso`
--
ALTER TABLE `mmavulso`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `mmliga`
--
ALTER TABLE `mmliga`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
