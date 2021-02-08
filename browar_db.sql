CREATE DATABASE `browar_db`;
use browar_db;


CREATE TABLE `browary` (
  `id` int(11) NOT NULL,
  `typ` varchar(30) CHARACTER SET latin2 NOT NULL,
  `alkohol` varchar(5) CHARACTER SET latin2 NOT NULL,
  `browar` varchar(30) CHARACTER SET latin2 NOT NULL,
  `ocena` int(11) DEFAULT 0,
  `grafika` varchar(250) CHARACTER SET latin2 NOT NULL DEFAULT 'defaultBottle.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `browary` (`id`, `typ`, `alkohol`, `browar`, `ocena`, `grafika`) VALUES
(1, 'Piwo Jasne', '5%', 'Namysłów', 14, 'namyslow-butelka.png'),
(2, 'Piwo Jasne', '5%', 'Carlsberg', 1, 'carlsberg-butelka.png'),
(3, 'Piwo Jasne', '6%', 'Harnaś', 10, 'harnas-butelka.png'),
(4, 'Piwo Jasne', '4.5%', 'Żywiec', -2, 'zywiec-butelka.png'),
(5, 'Piwo Jasne', '5%', 'Łomża', 0, 'lomza-butelka.png'),
(33, 'ddd', '7%', 'ddd', -1, 'defaultBottle.png');
