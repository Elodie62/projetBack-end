-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le :  mer. 17 mai 2023 à 10:41
-- Version du serveur :  5.7.26
-- Version de PHP :  7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `plannings`
--

-- --------------------------------------------------------

--
-- Structure de la table `activities`
--

CREATE TABLE `activities` (
  `id` int(11) NOT NULL,
  `nameActivity` varchar(255) NOT NULL,
  `startDate` date NOT NULL,
  `duration` int(11) NOT NULL,
  `idPlanning` int(11) NOT NULL,
  `idCompany` int(11) NOT NULL,
  `nbInscription` int(11) NOT NULL,
  `ownerEmail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `activities`
--

INSERT INTO `activities` (`id`, `nameActivity`, `startDate`, `duration`, `idPlanning`, `idCompany`, `nbInscription`, `ownerEmail`) VALUES
(1, 'Archivage', '2023-05-18', 2, 1, 1, 3, 'elodie@leclercq.com'),
(2, 'AfterWork', '2023-05-12', 3, 2, 2, 30, 'admin@disney.com'),
(4, 'youhou', '2023-05-17', 0, 1, 1, 0, 'elodie@leclercq.com');

-- --------------------------------------------------------

--
-- Structure de la table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `nameCompany` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `company`
--

INSERT INTO `company` (`id`, `nameCompany`) VALUES
(1, 'RealLife'),
(2, 'Disney'),
(3, 'Alstom');

-- --------------------------------------------------------

--
-- Structure de la table `planning`
--

CREATE TABLE `planning` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `idCompany` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `planning`
--

INSERT INTO `planning` (`id`, `name`, `idCompany`) VALUES
(1, 'Plannning1', 1),
(2, 'planning 2', 2),
(3, 'planning3', 3);

-- --------------------------------------------------------

--
-- Structure de la table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `nameStatus` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `status`
--

INSERT INTO `status` (`id`, `nameStatus`) VALUES
(1, 'admin'),
(2, 'user'),
(3, 'maintainer');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `idStatus` int(10) NOT NULL,
  `idCompany` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`, `password`, `idStatus`, `idCompany`) VALUES
(13, 'Loic', 'Poisot', 'loic@poisot.com', '0666666666', '$2b$12$7BHWtJmR/T0i4dx2qGUK5.GoIT0m3YkprugqicdsOt67ySnJny3hO', 3, 0),
(14, 'Elodie', 'Leclercq', 'elodie@leclercq.com', '0666666666', '$2b$12$e87/ppwuc4NLlXw1hluBB.lpUiHvHCVD.3iC4Sz/gkUQ1YIk9SYr6', 2, 1),
(15, 'Estelle', 'Casu', 'admin@disney.com', '0666666666', '$2b$12$A/J4OaEBgpGWacsvvYeGYOrnN/.Mc.ZRFTQH/yf6g8JESd8Z7UFwa', 1, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `activities`
--
ALTER TABLE `activities`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `planning`
--
ALTER TABLE `planning`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `activities`
--
ALTER TABLE `activities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `planning`
--
ALTER TABLE `planning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
