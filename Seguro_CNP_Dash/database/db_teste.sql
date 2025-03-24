-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/03/2025 às 01:24
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `gecaf`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cnp_data`
--

CREATE TABLE `cnp_data` (
  `cnp` int(11) NOT NULL,
  `situacao` tinyint(4) NOT NULL DEFAULT 1,
  `cnpj` varchar(30) DEFAULT NULL,
  `razao_social` varchar(255) DEFAULT NULL,
  `cc` varchar(50) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `telefone_proprietario` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `uf` char(2) DEFAULT NULL,
  `cep` varchar(20) DEFAULT NULL,
  `latitude` decimal(10,6) DEFAULT NULL,
  `longitude` decimal(10,6) DEFAULT NULL,
  `observacao` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cnp_data`
--

INSERT INTO `cnp_data` (`cnp`, `situacao`, `cnpj`, `razao_social`, `cc`, `telefone`, `telefone_proprietario`, `email`, `endereco`, `bairro`, `cidade`, `uf`, `cep`, `latitude`, `longitude`, `observacao`) VALUES
(803, 1, '02.537.999/0001-38', 'Troke Informática Eireli', '043/027.901-9', '3613-7877', '9291-8266 Ernani / 99965-6701 - Jussara', 'ernanicaixeta@hotmail.com; juju.geo10@hotmail.com', 'Avenida JK Quadra 30 Lote 26 Loja 5', 'Jardim Brasília', 'Águas Lindas de Goiás', 'GO', '72915-021', -157.305220, -482.842690, ''),
(805, 1, '41.297.867/0001-38', 'BOMBONIERE S&A LTDA', '201/046.255-0 ', '3703-5280 / 3326-958', '61 - 98498-3237 - Iolanda', 'bombonieresea@gmail.com', 'Rodoviária de Brasília, Plataforma Inferior \"D\", Entrada do Metrô (situado na unidade do \"Na Hora\" da Rodoviária)', 'Zona Cívico-AdministrATIVA', 'Brasília', 'DF', '70.089-000', -157.933520, -478.834820, 'Reforma até Outubro 2022'),
(809, 1, '07.324.372/0001-12', 'Poderosa Cosméticos LTDA', '209/014.871-8', '3033-1806', '8339-3109 Flávia', 'flaviadesouzalima@gmail.com', 'Quadra 28 Loja 15', 'Setor Oeste', 'Gama', 'DF', '72.420-280', -160.180160, -480.752640, ''),
(811, 1, '12.886.239/0001-90', 'Facilita Armarinho e Presentes LTDA ME', '053/057.487-0', '3357-3760', '98530-3841 Marcos / 98530-3830 William', 'facilitaarmarinho@hotmail.com', 'QR 503 Conjunto 01 Lote 01 Loja 02', 'Samambaia Sul', 'Samambaia', 'DF', '72.309-601', -158.868760, -480.907780, 'Antigo 636'),
(813, 1, '08.287.103/0001-96', 'Mercearia Planalto LTDA EPP', '026/035.337-0', '3965-4333', '99876-7232 Valdinor / 8130-7742 - 98407 1860 Cristiano / 3202-5734 / 9118-4676 Rafael / 9655-1002 Jo', 'valdinor.reis@gmail.com; conveniencia813@gmail.com;', 'EQNN 22/24 Bloco A Loja 06', 'Ceilândia Sul', 'Ceilândia', 'DF', '72.220-571', -158.348930, -481.067610, ''),
(817, 0, '07.611.115/0001-61', 'Nilza Candida Rodrigues', '216/010.477-3', '3242-2909', '99871-0408 - Nilza', 'brbcnp817817@gmail.com', 'EQ 55/56 Área Especial 01, Loja 448-A (situado na unidade do \"Na Hora\" do Gama)', 'Setor Central', 'Gama', 'DF', '72.405-902', -160.132250, -480.622150, ''),
(818, 1, '15.787.415/0001-24', 'P&A Armarinho e Utilidades da Família LTDA - ME', '240/044.198-1', '3404-2288 ', '99292-0518 / 99867-5634 Pedro / 99983-7286 Ângela', 'peaarmarinho@gmail.com', 'QC 6 Conjunto 12 Lote 15 Loja 1', 'Riacho Fundo II', 'Riacho Fundo II', 'DF', '71.882-263', -159.225110, -480.444330, 'Antigo 655. Alterou o endereço.'),
(822, 1, '37.862.464/0001-17', 'CVV COMERCIO E SERVICOS LTDA', '024.046.251-3\n ', '61 3967-6568', '61-98260-7050 - Clayson', 'conveniencia822@gmail.com', 'QNG AREA PARA MERCADO BOX 31 32 E 33 LOTE 07', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.130-901', NULL, NULL, ''),
(824, 1, '08.684.922/0001-77', 'CIA da Casa Papelaria e Conveniência  Ltda', '057/039.521-6', '3467-6180', '9275-8701 Rafael', 'raphael.r.gomes@hotmail.com', 'Av. Comercial Del Lago, Quadra 29 Lote 03/05', 'Itapoã', 'Itapoã', 'DF', '71.590-000', -157.500330, -477.749430, ''),
(829, 1, '05.275.333/0001-47', 'Oliveira Mendonça & Cia LTDA - ME', '287/000.072-8', '3397-2454', '(61) 999395939 Annelize \n(61) 999390835 Inácio \n', 'conveniencia829@gmail.com; annelizesantos@hotmail.com', 'R 04 AE 05 MODULO 15 LOJA 02 Feira do Produtor, Quiosque 15, Loja 02', 'Vicente Pires', 'Vicente Pires', 'DF', '72.155-000', -158.140590, -480.158760, ''),
(839, 1, '07.859.761/0001-42', 'Thor Comércio Varejista de Calçados LTDA', '103/032.545-3', '3201-7338', '3201-7338 / 8449-5051 Thiago', 'imobiliariaestrutura@gmail.com', 'QSA 02, Lote 07, Lojas 2 e 3', 'Taguatinga Sul', 'Taguatinga', 'DF', '72.015-020', -158.372600, -480.549340, ''),
(845, 1, '02.451.423/0005-87', 'Centro de Formação de Condutores A B Educativo LTDA EPP', '201.039.916-6', '3387-1043', '98193-2455 Fábio / 98260-1100 Luciene', 'autoescola.saocristovao@outlook.com', 'Quadra 08, Bloco 12, Lote 11, Sobreloja e Subsolo', 'Sobradinho', 'Sobradinho', 'DF', '73.005-512', -156.469330, -478.026120, ''),
(846, 1, '07.140.242/0001-20', 'Akalanto Fashion Modas LTDA', '264.000.390-3', '3614-1964', '61-99989-8439 - Letícia', 'akalanto1@gmail.com', 'Rua Sem Nome, Quadra 73 Lote 20', 'Jardim Lago Azul', 'Novo Gama', 'GO', '72.865-073', NULL, NULL, ''),
(848, 1, '02.077.518/0001-59', 'Elevata Comercial de Calçados Ltda - ME', '011/026.073-2', '98446-9941', '61 9673-1110 Luiz Antonio ', 'luizantoniolima1948@gmail.com', 'SIA Trecho 07 Nº 100 Conjunto A Loja 1 - Feira dos Importados ', 'SIA ', 'SIA ', 'DF', '71.208-900', -157.961920, -479.494210, ''),
(850, 1, '41.198.828/0001-83', 'Araújo Bombonieri LTDA', '201/046256-9 ', '61-3978-5117', '(61)99643-7863 (Rosangela)', 'araujo2021bombonieri@gmail.com', 'Avenida Contorno, Área Especial Lote 03 Sala 14 (situado na unidade do DETRAN do Gama)', 'Cidade Nova', 'Gama', 'DF', '72.490-010', -159.979740, -480.610630, '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cnp_historico`
--

CREATE TABLE `cnp_historico` (
  `cnp` int(11) NOT NULL,
  `dez_23` decimal(15,2) DEFAULT NULL,
  `jan_24` decimal(15,2) DEFAULT NULL,
  `fev_24` decimal(15,2) DEFAULT NULL,
  `mar_24` decimal(15,2) DEFAULT NULL,
  `abr_24` decimal(15,2) DEFAULT NULL,
  `mai_24` decimal(15,2) DEFAULT NULL,
  `jun_24` decimal(15,2) DEFAULT NULL,
  `jul_24` decimal(15,2) DEFAULT NULL,
  `ago_24` decimal(15,2) DEFAULT NULL,
  `set_24` decimal(15,2) DEFAULT NULL,
  `out_24` decimal(15,2) DEFAULT NULL,
  `nov_24` decimal(15,2) DEFAULT NULL,
  `dez_24` decimal(15,2) DEFAULT NULL,
  `jan_25` decimal(15,2) DEFAULT NULL,
  `fev_25` decimal(15,2) DEFAULT NULL,
  `mar_25` decimal(15,2) DEFAULT NULL,
  `abr_25` decimal(15,2) DEFAULT NULL,
  `mai_25` decimal(15,2) DEFAULT NULL,
  `jun_25` decimal(15,2) DEFAULT NULL,
  `jul_25` decimal(15,2) DEFAULT NULL,
  `ago_25` decimal(15,2) DEFAULT NULL,
  `set_25` decimal(15,2) DEFAULT NULL,
  `out_25` decimal(15,2) DEFAULT NULL,
  `nov_25` decimal(15,2) DEFAULT NULL,
  `dez_25` decimal(15,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cnp_historico`
--

INSERT INTO `cnp_historico` (`cnp`, `dez_23`, `jan_24`, `fev_24`, `mar_24`, `abr_24`, `mai_24`, `jun_24`, `jul_24`, `ago_24`, `set_24`, `out_24`, `nov_24`, `dez_24`, `jan_25`, `fev_25`, `mar_25`, `abr_25`, `mai_25`, `jun_25`, `jul_25`, `ago_25`, `set_25`, `out_25`, `nov_25`, `dez_25`) VALUES
(803, 71742.31, 169654.92, 61297.63, 73529.77, 73529.77, 66031.46, 66031.46, 68211.72, 65106.36, 65106.36, 67728.20, 59435.69, 71395.66, 60456.98, 65117.80, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(805, 36570.88, 39841.71, 38322.07, 37724.94, 37724.94, 29909.12, 29909.12, 38451.76, 33220.04, 33220.04, 36328.10, 28250.47, 30579.20, 32590.73, 35616.15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(809, 29622.36, 83973.73, 39577.12, 35630.12, 35630.12, 41824.35, 41824.35, 43281.73, 41402.11, 41402.11, 50448.60, 42580.30, 38742.38, 39476.63, 42790.43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(811, 48831.99, 0.00, 53386.30, 48244.00, 48244.00, 43232.49, 43232.49, 44424.34, 36184.45, 36184.45, 41614.00, 33676.22, 50890.34, 51847.90, 54150.89, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(813, 65795.38, 73092.35, 86595.19, 81245.26, 81245.26, 73814.97, 73814.97, 76971.09, 93641.83, 93641.83, 86446.45, 75188.50, 78047.07, 88523.79, 86604.25, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(817, 44110.57, 57396.28, 25815.25, 41660.23, 41660.23, 49215.62, 49215.62, 53037.41, 44227.53, 44227.53, 2337.95, 0.00, 0.00, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(818, 54977.57, 0.00, 53726.37, 55304.01, 55304.01, 47030.05, 47030.05, 46406.05, 41932.91, 41932.91, 41179.96, 39282.09, 36798.98, 42595.32, 37668.15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(822, 66074.92, 146790.90, 67099.00, 55043.36, 55043.36, 52752.79, 52752.79, 53160.89, 63469.79, 63469.79, 53341.40, 53954.79, 49407.96, 53879.24, 57628.20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(824, 90770.35, 206595.46, 80740.66, 77530.32, 77530.32, 67204.19, 67204.19, 74103.68, 65812.62, 65812.62, 67529.77, 59149.99, 59834.48, 61285.70, 66091.01, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(829, 37859.99, 78045.05, 43688.15, 39166.32, 39166.32, 36360.98, 36360.98, 48070.39, 44262.88, 44262.88, 43247.26, 34054.39, 38364.09, 38608.86, 43725.71, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(839, 32235.77, 88706.10, 38268.16, 32816.63, 32816.63, 27422.98, 27422.98, 27282.24, 28365.64, 28365.64, 25073.57, 20609.16, 25549.71, 30418.44, 36662.33, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(845, 56657.54, 131738.37, 51065.19, 51334.25, 51334.25, 54822.56, 54822.56, 51739.43, 44369.49, 44369.49, 42955.02, 39112.43, 40847.48, 45635.88, 47878.65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(846, 40443.19, 88176.00, 35938.73, 49888.20, 49888.20, 0.00, 0.00, 0.00, 12858.43, 12858.43, 32876.23, 32404.37, 36581.53, 37612.69, 34685.63, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(848, 45823.15, 77511.96, 40724.07, 34483.85, 34483.85, 28525.44, 28525.44, 35099.40, 24131.96, 24131.96, 30785.61, 26106.51, 34489.50, 28956.72, 36001.94, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(850, 14310.19, 28366.93, 22855.45, 17582.74, 17582.74, 15598.23, 15598.23, 15548.81, 16242.09, 16242.09, 17732.68, 17315.16, 19036.34, 21059.20, 21358.76, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pag_seguradora`
--

CREATE TABLE `pag_seguradora` (
  `id` int(11) NOT NULL,
  `cnp` int(11) NOT NULL,
  `numero_parcela` int(11) NOT NULL CHECK (`numero_parcela` > 0),
  `data_vencimento` date DEFAULT NULL,
  `status` enum('PAGO','PENDENTE','EMITIR') DEFAULT NULL,
  `data_pagamento` datetime DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pag_seguradora`
--

INSERT INTO `pag_seguradora` (`id`, `cnp`, `numero_parcela`, `data_vencimento`, `status`, `data_pagamento`, `usuario_id`) VALUES
(1, 822, 1, '2024-09-15', 'PAGO', NULL, NULL),
(2, 822, 2, '2024-10-15', 'PAGO', NULL, NULL),
(3, 822, 3, '2024-11-15', 'PAGO', NULL, NULL),
(4, 822, 4, '2024-12-15', 'PENDENTE', NULL, NULL),
(5, 822, 5, '2025-01-15', 'PENDENTE', NULL, NULL),
(6, 848, 1, '2024-09-15', 'PAGO', NULL, NULL),
(7, 848, 2, '2024-10-15', 'PENDENTE', NULL, NULL),
(8, 848, 3, '2024-11-15', 'PENDENTE', NULL, NULL),
(9, 848, 4, '2024-12-15', 'PENDENTE', NULL, NULL),
(10, 848, 5, '2025-01-15', 'PENDENTE', NULL, NULL),
(11, 809, 1, NULL, 'PENDENTE', NULL, NULL),
(12, 809, 2, NULL, 'PENDENTE', NULL, NULL),
(13, 809, 3, NULL, 'PENDENTE', NULL, NULL),
(14, 809, 4, NULL, 'PENDENTE', NULL, NULL),
(15, 809, 5, NULL, 'PENDENTE', NULL, NULL),
(16, 805, 1, '2024-05-15', 'PAGO', NULL, NULL),
(17, 805, 2, '2024-06-15', 'PAGO', NULL, NULL),
(18, 805, 3, '2024-07-15', 'PAGO', NULL, NULL),
(19, 805, 4, '2024-08-15', 'PAGO', NULL, NULL),
(20, 805, 5, '2024-09-15', 'PAGO', NULL, NULL),
(21, 803, 1, '2025-03-15', 'PENDENTE', NULL, NULL),
(22, 803, 2, '2025-04-15', 'PENDENTE', NULL, NULL),
(23, 803, 3, '2025-05-15', 'PENDENTE', NULL, NULL),
(24, 803, 4, '2025-06-15', 'PENDENTE', NULL, NULL),
(25, 803, 5, '2025-07-15', 'PENDENTE', NULL, NULL),
(26, 811, 1, NULL, 'EMITIR', NULL, NULL),
(27, 811, 2, NULL, 'EMITIR', NULL, NULL),
(28, 811, 3, NULL, 'EMITIR', NULL, NULL),
(29, 811, 4, NULL, 'EMITIR', NULL, NULL),
(30, 811, 5, NULL, 'EMITIR', NULL, NULL),
(31, 813, 1, NULL, 'EMITIR', NULL, NULL),
(32, 813, 2, NULL, 'EMITIR', NULL, NULL),
(33, 813, 3, NULL, 'EMITIR', NULL, NULL),
(34, 813, 4, NULL, 'EMITIR', NULL, NULL),
(35, 813, 5, NULL, 'EMITIR', NULL, NULL),
(36, 818, 1, '2024-05-15', 'PAGO', NULL, NULL),
(37, 818, 2, '2024-06-15', 'PAGO', NULL, NULL),
(38, 818, 3, '2024-07-15', 'PAGO', NULL, NULL),
(39, 818, 4, '2024-08-15', 'PAGO', NULL, NULL),
(40, 818, 5, '2024-09-15', 'PAGO', NULL, NULL),
(41, 817, 1, '2024-01-16', 'PAGO', NULL, NULL),
(42, 817, 2, '2024-02-15', 'PAGO', NULL, NULL),
(43, 817, 3, '2024-03-15', 'PAGO', NULL, NULL),
(44, 817, 4, '2024-04-15', 'PAGO', NULL, NULL),
(45, 817, 5, '2024-05-15', 'PAGO', NULL, NULL),
(46, 824, 1, '2025-01-15', 'PAGO', NULL, NULL),
(47, 824, 2, '2025-02-15', 'PAGO', NULL, NULL),
(48, 824, 3, '2025-03-15', 'PENDENTE', NULL, NULL),
(49, 824, 4, '2025-04-15', 'PENDENTE', NULL, NULL),
(50, 824, 5, '2025-05-15', 'PENDENTE', NULL, NULL),
(51, 829, 1, NULL, 'EMITIR', NULL, NULL),
(52, 829, 2, NULL, 'EMITIR', NULL, NULL),
(53, 829, 3, NULL, 'EMITIR', NULL, NULL),
(54, 829, 4, NULL, 'EMITIR', NULL, NULL),
(55, 829, 5, NULL, 'EMITIR', NULL, NULL),
(56, 839, 1, '2024-01-15', 'PAGO', NULL, NULL),
(57, 839, 2, '2024-02-15', 'PAGO', NULL, NULL),
(58, 839, 3, '2024-03-15', 'PENDENTE', NULL, NULL),
(59, 839, 4, '2024-04-15', 'PENDENTE', NULL, NULL),
(60, 839, 5, '2024-05-15', 'PENDENTE', NULL, NULL),
(61, 846, 1, '2024-05-25', 'PENDENTE', NULL, NULL),
(62, 846, 2, '2024-06-25', 'PENDENTE', NULL, NULL),
(63, 846, 3, '2024-07-25', 'PENDENTE', NULL, NULL),
(64, 846, 4, '2024-08-25', 'PENDENTE', NULL, NULL),
(65, 846, 5, '2024-09-25', 'PENDENTE', NULL, NULL),
(66, 850, 1, '2024-06-15', 'PAGO', NULL, NULL),
(67, 850, 2, '2024-07-15', 'PAGO', NULL, NULL),
(68, 850, 3, '2024-08-15', 'PAGO', NULL, NULL),
(69, 850, 4, '2024-09-15', 'PAGO', NULL, NULL),
(70, 850, 5, '2024-10-15', 'PAGO', NULL, NULL),
(71, 845, 1, '2025-01-15', 'PAGO', NULL, NULL),
(72, 845, 2, '2025-02-15', 'PAGO', NULL, NULL),
(73, 845, 3, '2025-03-15', 'PENDENTE', NULL, NULL),
(74, 845, 4, '2025-04-15', 'PENDENTE', NULL, NULL),
(75, 845, 5, '2025-05-15', 'PENDENTE', NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `seguradora`
--

CREATE TABLE `seguradora` (
  `cnp` int(11) NOT NULL,
  `inicio_vigencia_seguro` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `valor_cobertura` decimal(15,2) DEFAULT NULL,
  `valor_parcela` decimal(15,2) DEFAULT NULL,
  `forma_de_pgt` varchar(20) DEFAULT NULL,
  `situacao_proposta` varchar(50) DEFAULT NULL,
  `obs` text DEFAULT NULL,
  `apolice` varchar(50) DEFAULT NULL,
  `multiseguros` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `seguradora`
--

INSERT INTO `seguradora` (`cnp`, `inicio_vigencia_seguro`, `vencimento`, `valor_cobertura`, `valor_parcela`, `forma_de_pgt`, `situacao_proposta`, `obs`, `apolice`, `multiseguros`) VALUES
(803, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000320271', 'CADASTRAR'),
(805, '2024-04-15', '2025-04-15', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000314771', 'CADASTRAR'),
(809, '2024-01-11', '2025-01-11', 0.00, 0.00, 'boleto', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(811, '2025-02-06', '2026-02-06', 70000.00, 629.89, 'boleto', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(813, '2025-02-01', '2026-02-01', 100000.00, 899.84, 'boleto', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(817, '2024-01-04', '2025-01-04', 90000.00, 809.86, 'boleto', 'A', 'CONFIRMAR O STATUS DO CNP.', '1351000310271', NULL),
(818, '2024-04-15', '2025-04-15', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000314571', NULL),
(822, '2024-07-31', '2025-07-31', 70000.00, 629.89, 'boleto', 'A', 'APÓLICE CANCELADA POR FALTA DE PGTO', '1351000315871', NULL),
(824, '2024-12-01', '2025-12-01', 90000.00, 809.86, 'boleto', 'A', 'Sem pendência ', '1351000319071', NULL),
(829, '2025-02-01', '2026-02-01', 70000.00, 629.89, 'boleto', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(839, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000318071', NULL),
(845, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000318171', 'CADASTRAR'),
(846, '2024-04-15', '2025-04-15', 70000.00, 629.89, 'boleto', 'A', 'CONFIRMAR O STATUS DO CNP.', '1351000314671', NULL),
(848, '2024-07-31', '2025-07-31', 70000.00, 629.89, 'boleto', 'A', 'APÓLICE CANCELADA POR FALTA DE PGTO', '1351000315671', NULL),
(850, '2024-04-15', '2025-04-15', 70000.00, 629.89, 'boleto', 'A', 'Sem pendência ', '1351000314871', 'CADASTRAR');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cnp_data`
--
ALTER TABLE `cnp_data`
  ADD PRIMARY KEY (`cnp`);

--
-- Índices de tabela `cnp_historico`
--
ALTER TABLE `cnp_historico`
  ADD PRIMARY KEY (`cnp`);

--
-- Índices de tabela `pag_seguradora`
--
ALTER TABLE `pag_seguradora`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_cnp_numero_parcela` (`cnp`,`numero_parcela`);

--
-- Índices de tabela `seguradora`
--
ALTER TABLE `seguradora`
  ADD PRIMARY KEY (`cnp`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `pag_seguradora`
--
ALTER TABLE `pag_seguradora`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `cnp_historico`
--
ALTER TABLE `cnp_historico`
  ADD CONSTRAINT `fk_cnp_historico` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `pag_seguradora`
--
ALTER TABLE `pag_seguradora`
  ADD CONSTRAINT `fk_pag_seguradora_cnp` FOREIGN KEY (`cnp`) REFERENCES `seguradora` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `seguradora`
--
ALTER TABLE `seguradora`
  ADD CONSTRAINT `fk_seguradora_cnp` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
