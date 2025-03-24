-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2025 at 05:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gecaf`
--

-- --------------------------------------------------------

--
-- Table structure for table `cnp_data`
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
-- Dumping data for table `cnp_data`
--

INSERT INTO `cnp_data` (`cnp`, `situacao`, `cnpj`, `razao_social`, `cc`, `telefone`, `telefone_proprietario`, `email`, `endereco`, `bairro`, `cidade`, `uf`, `cep`, `latitude`, `longitude`, `observacao`) VALUES
(703, 1, '12.300.137/0001-40', 'MD Biju Comércio de Bijuterias LTDA ME', '043/038.882-9', '3047-9530', '98586-6602 (Denilson) / 98593-4775 (Marckson)', 'md.negabijubrb@gmail.com', 'QNN 23 Conjunto F Lote 02', 'Ceilândia Norte', 'Ceilândia', 'DF', '72.225-236', -158.070880, -481.224670, ''),
(704, 1, '12.029.475/0001-90', 'Nolasco & Lima Utilidades do Lar LTDA ME', '053/053.916-0 ', '3358-8880 ', '99975-0113 Rogéria / Rosangela: 99643-7863', 'r_rogeria@hotmail.com', 'QS 116, Conjunto 06, Lote 03, Loja 02', 'Samambaia Sul', 'Samambaia', 'DF', '72.302-566', -158.711900, -480.655770, ''),
(711, 1, '10.776.784/0001-06', 'Comercial de Alimentos Cristal Araguari LTDA-ME', '105/021.241-7', '3605-4054 - Ramal 22', '3625-3272 / 99967-7456/ 99967-5839 Antônio', 'convenienciabrb711@gmail.com; fiscal.cristalsupermercados@gmail.com;', 'Quadra 08 Lote 08 S/N ', 'Recreio Mossoró', 'Cidade Ocidental', 'GO', '72.880-000', -161.023190, -479.488930, ''),
(712, 1, '32.954.165/0001-99', 'MR Serviços de Lanchonete e Financeiros Eireli', '086.007.585-0', '61 3060-1221 ', '(61) 98511-0016 - Maria José', 'pointgourmetcafeteria@gmail.com', 'Quadra 203 Conjunto 9 quiosque 32', 'Setor Residencial Oeste', 'São Sebastião', 'DF', '71.692-625', NULL, NULL, ''),
(713, 1, '16.578.121/0001-55', 'Point 13 Conveniência e Revistaria LTDA ME', '107/036.450-6', '98589-8017 / 9 9551-', 'Maria Clara - 61 99210-1665', 'servicoconveniencia@gmail.com', 'AR 13 Conjunto 18 Lote 30 Loja 03', 'Sobradinho II', 'Sobradinho II', 'DF', '73.062-318', -156.460760, -478.211570, ''),
(714, 1, '18.198.129/0001-11', 'C&L Papelaria e Cosméticos EIRELI ME', '240/046.015-3', '3046-6687', '98592-9026/99251-6499', 'elenibatista10@gmail.com', 'ADE Quadra 400 Conjunto 4 Lote 28', 'Recanto das Emas', 'Recanto das Emas', 'DF', '72.625-004', -159.079800, -480.528780, ''),
(715, 1, '12.875.569/0001-80', 'BRB SERVIÇOS S/A (Na Hora Riacho Mall)', '100.024.400-5', '61-3027-8722', 'Marcos Nunes (61)993139333/ Sarah Rodrigues (61)998536773/Christiane de Oliveira (61)994164421', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; christiane.nunes@brbservicos.co', 'QN 7 Area especial 1 - Na Hora Riacho Mall', 'Riacho Fundo I', 'Riacho Fundo I', 'DF', '71.805-731', NULL, NULL, ''),
(718, 1, '20.168.708/0001-63', 'Aliança Avante Empreendimentos LTDA - ME', '268/000.250-9', '99265-8658', '8423-4465 Lacerles', 'larceleselias@gmail.com; larceles.menezes@gmail.com', 'QA 04 MC s/n Lote 09 a 11, Loja 09 ', 'Setor Leste', 'Planaltina de Goiás', 'GO', '73.752-058', -154.544320, -476.091750, ''),
(719, 1, '03.367.856/0001-98', 'Central Import\'s Utilidades LTDA - ME', '053/033.459-3', '3458-2964 ', '98369-3856 (Necy)', 'necypereira@gmail.com', 'QN 504 Conjunto 01 Lote 01 Loja 01', 'Samambaia Sul', 'Samambaia', 'DF', '72.310-601', -158.823270, -480.804900, ''),
(721, 1, '12.875.569/0001-80', 'BRB SERVICOS S/A - UNIÃO DOS PALMARES', '100.024.400-5', '61 3027-8725', '', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'RUA DOMINGOS DE PINO N° 99, LETRA B', 'CENTRO', 'UNIAO DOS PALMARES', 'AL', '57.800-000', NULL, NULL, ''),
(722, 1, '07.089.904/0001-84', 'B2 SERVICOS DE INTERNET LTDA', '209/023.326-0', '3032-2139', '(61) 9 9439-9507 Ana; (61) 9 9216-9479 Francisco', 'mamutecafe504.brb@gmail.com', 'SEPN 504 Bloco C nº 31 Loja 28 1º pavimento ', 'Asa Norte', 'Brasília', 'DF', '70.730-520', -157.763860, -478.874850, ''),
(723, 1, '33.503.863/0001-30', 'José dos Reis de Oliveira Comércio de Alimentos ', '057/601.377-3', '3369-7000 / 3369-249', '3369-8685 / 9984-8438 e 61 99258-2542 Reis / 9176-3993 Jardene', 'comercialreisdf@hotmail.com', 'Avenida Paranoá, Quadra 29 Conjunto 21 Lotes 04/07 Lojas 01/02', 'Paranoá', 'Paranoá', 'DF', '71.573-017', -157.642260, -477.804380, ''),
(724, 1, '08.268.568/0001-08', 'Helder Morato - Artes Modas LTDA - ME', '084/000.597-0', '3723-1900', '9963-8608 Helder', 'heldermorato@gmail.com', 'Quadra 67, Lote 17, Loja 01', 'Jardim Pérola II', 'Águas Lindas de Goiás', 'GO', '72.911-268', -157.407260, -482.606710, ''),
(728, 1, '13.031.567/0001-77', 'Potiguar Materiais Elétricos e Hidráulicos LTDA ME', '081/001.769-5', '3434-8638', '98557 7222 Anibal', 'jpm728brb@hotmail.com; ', 'Quadra 403 Conjunto 20 Lote 13 Loja 01', 'Recanto das Emas', 'Recanto das Emas', 'DF', '72.630-320', -159.102470, -480.641530, ''),
(729, 1, '05.466.879/0002-66', 'C & N Correspondente e Serviços de Informática LTDA ME', '058/021.587-3', '3963-2136', '3033-3587 / 9177-2539 Clayton', 'claytonmalaquiasonofre@gmail.com', 'QNB 01 Lote 20 Lojas 06/07', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.115-010', -158.316900, -480.591500, ''),
(730, 1, '12.875.569/0001-80', 'BRB SERVIÇOS S/A (Feira dos Goianos)', '100.024.400-5', '61-30278739', 'Marcos Nunes (61)993139333/ Sarah Rodrigues (61)998536773/Christiane de Oliveira (61)994164421', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'QI 13 LOTE 01/14 ALA 37 BOX 9, 10, 11A, 11B, 12A, 12B, 13, 14, Pátio da Moda/Feira dos Goianos', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.135-130', NULL, NULL, ''),
(738, 1, '47.719.181/0001-74', 'RASTA PE COMERCIO DE CALCADOS LTDA', '216/032.133-2', '3573-5211', '98527-1211 Marcos Antônio', 'rastape880@hotmail.com', 'QUADRA 41, COMERCIO LOCAL, LOTE 02', 'Setor Leste', 'Gama', 'DF', '72.465-413', NULL, NULL, ''),
(739, 1, '01.614.544/0001-06', 'Retalhão e Confecções Fortaleza LTDA ME', '110/606.483-3', '3389-1808', '9909-1066 Maria Evani / 9909-1064 Lincon', 'linconalbuquerque@yahoo.com.br', 'Quadra 03 Conjunto A Lote 40 Lojas A/B ', 'Setor Residencial Leste', 'Planaltina', 'DF', '73.350-301', -156.182170, -476.479490, ''),
(741, 1, '45.670.142/0001-02', 'Copel Papelaria Ltda', '059.034.137-5', '3964-7040', '99291-3787 - Cláudio', 'papelariacopel@hotmail.com', 'SRTVS Qd 701 Bloco I Lojas 7 e 8 - Edifício Palácio da Imprensa - Térreo', 'Asa Sul', 'Brasília', 'DF', '70.340-905', NULL, NULL, ''),
(745, 1, '08.468.455/0001-48', 'AME Comercial Medicamentos LTDA ME', '084/003.021-5', '3613-7171 ', '98445-9647 Aldenice / 98546-1377 Maciel', 'aldenicesilva73@hotmail.com', 'Quadra 11 Lote 01 Loja 01', 'Jardim da Barragem V', 'Águas Lindas de Goiás', 'GO', '72.920-800', -157.359390, -482.955580, ''),
(748, 1, '00.771.264/0001-49', 'Cariri Comércio de Sandálias Ltda', '216/011.057-9', '3384-3758', '8421-3616 / 99612-1821 Rosecleide', 'roselrm@hotmail.com', 'Quadra 06, Loja 11', 'Setor Oeste', 'Gama', 'DF', '72.425-060', -160.089740, -480.715090, ''),
(749, 1, '11.077.121/0001-58', 'Frandelle Comércio de Alimentos EIRELI - ME', '026/050.446-7', ' 61-98404-7622', '61-984047622 JOSE NAUTO/ 61-991590860 WILSON/ 61-992952897  Michelle', 'frandellealimentos1@gmail.com ', 'CNM 02, Lote B, Loja 01', 'Ceilândia Centro', 'Ceilândia', 'DF', '72.215-500', -158.153680, -481.040840, ''),
(752, 1, '04.291.697/0001-58', 'Potência Administradora Imobiliária LTDA - ME', '054/013.918-1', '3382-7002', '7811-0595 / 9985-3416 Paulo Cézar / 98319-5082 Jairo', 'paulo@guaraveiculos.com.br;jairobrb@gmail.com', 'QE 13 Conjunto E Lote 02 Loja 04 Parte', 'Guará II', 'Guará', 'DF', '71.050-050', -158.257760, -479.800930, ''),
(753, 1, '05.381.373/0001-73', 'Gonçalves & Souza Mercado LTDA - ME', '110/056.742-6', '3488-4492', '(61) 9 991109007 José Gonçalves', 'manoel.netomoraes@hotmail.com', 'Estância 1, Módulo M, Lote 02, Loja A', 'Setor Residencial Mestre D\'Armas', 'Planaltina', 'DF', '73.301-970', -156.186940, -476.760030, ''),
(756, 1, '12.875.569/0001-80', 'BRB SERVIÇOS S/A (Feira do Guará) ', '100.024.400-5', '61-3027-8756', 'Marcos Nunes (61)993139333/ Sarah Rodrigues (61)998536773/Christiane de Oliveira (61)994164421 \n', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'Área Especial do CAVE Feira Permanente do Guará - Prédio da Administração da Feira', 'Guará II', 'Guará', 'DF', '71.025-900', -1582.413860, -4797.568870, 'Correspondente Contratado pela BRB Serviços Feira do Guará'),
(764, 0, '00.967.364/0001-45', 'Magazine Art & Paz LTDA EPP', '268/000.159-6', '61 - 99334-0680', '8423 4465 Larceles // 9611-8283 Larceles', 'larceleselias@gmail.com;larceles.menezes@gmail.com', 'Av B Quadra 01 MC Lote 07 Loja A', 'Setor Sul', 'Planaltina de Goiás', 'GO', '73.753-101', -154.567020, -476.138440, ''),
(767, 1, '17.349.434/0001-02', 'Joel Empório LTDA - ME', '209.024.790-2', '3273-8887', '98430-8702', 'liliribeiro20@gmail.com', 'SCLRN 706 Bl B Loja 29 Parte', 'Asa Norte', 'Brasília', 'DF', '70.740-702', -157.710840, -478.891370, 'Em reforma do dia 18/12 a 29/12/2023'),
(769, 1, '03.400.663/0001-91', 'Led Variedades e Equipamentos de Comunicação LTDA', '110/052.100-0', '61 - 3388-0301', '(61) 99167-8606 - Alcineis', 'alcineischarlesbsb@gmail.com; deribamar097@gmail.com', 'Rua Eugênio Jardim Q 32 Lote 18A Loja 04', 'Setor Tradicional', 'Planaltina', 'DF', '73.330-073', -156.184760, -476.573930, ''),
(771, 0, '40.973.476/0001-23', 'LOJAS TREND PLANALTINA GOIAS LTDA', '268.004973-4', '3639-2824 ', '8423-4465 Larceles / 9611-7741 Larceles', 'larceleselias@gmail.com;larceles.menezes@gmail.com', 'QC 03 MC Lote 09 Lojas 2 e 3', 'Setor Norte', 'Planaltina de Goiás', 'GO', '73.751-250', -154.507650, -476.149130, ''),
(774, 1, '72.596.547/0001-02', 'Campista Materiais para Construção LTDA', '089/000.050-6', '3485-1010 / 3485-366', 'Lucas Pita (61)99107-7544 /Genivaldo 98281 0487', 'campistapita@gmail.com; lucas.pita25@gmail.com', 'QMS 33 lotes 2, 6 e 26', 'Setor de Mansões', 'Sobradinho II', 'DF', '73.080-000', -156.373220, -478.366080, ''),
(776, 1, '12.875.569/0001-80', 'BRB SERVICOS S/A - PENEDO', '100.024.400-5', '61 3027-8729', '', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'TV. CAMPOS TEIXEIRA N° 114', 'CENTRO', 'PENEDO', 'AL', '57.200-000', NULL, NULL, ''),
(777, 1, '18.311.859/0001-87', 'A.R Comércio de Utilidades Eireli', '025/036.135-3', '61 996884251', '99939-5939 / 98529-7159', 'facilutilidades08@gmail.com; annelizesantos@hotmail.com', 'Quadra 08 Lote 06 Loja 02', 'Incra 08', 'Brazlândia', 'DF', '72.760-080', -157.419200, -481.696750, ''),
(779, 1, '14.280.871/0001-10', 'SUPERMERCADO MANIA COMERCIO DE ALIMENTOS LTDA', '283.002.617-3', '61-3060-2933', 'Cristiane Nakamura(61) 99620-8120', 'crisnakamura.bsb@gmail.com', 'Quadra 4 Lote 17 Loja 2', 'Setor Veredas', 'Brazlândia', 'DF', '72.725-400', NULL, NULL, ''),
(783, 1, '19.539.786/0001-48', 'HM - Axhcar LTDA', '084/006.076-9', '99963-8608', '99963-8608 - Helder', 'heldermorato@gmail.com', 'Qd 1 Loja 1', 'Jardim Guaíra I', 'Águas Lindas de Goiás', 'GO', '72.912-672', -157.529750, -482.615590, ''),
(784, 1, '12.875.569/0001-80', 'BRB SERVICOS S/A - PORTO CALVO', '100.024.400-5', '61 3027-8726', '', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'RUA SÃO BENTO N° 6', 'CENTRO', 'PORTO CALVO', 'AL', '57.900-000', NULL, NULL, ''),
(785, 1, '14.402.486/0001-07', 'Mimos e Encantos Comércio de Presentes LTDA - EPP', '078/009.482-4', '3567-8236', '99803-4258 Melissa / 99971-8181 Marli', 'mimoseencantospresentes@gmail.com', 'Av. Araucárias Lote 1525 Loja 74 Pavimento 01, Shopping Metrópole', 'Águas Claras', 'Águas Claras', 'DF', '71.936-250', -158.402360, -480.205730, 'Antigo CNP 672'),
(791, 1, '12.875.569/0001-80', 'BRB SERVICOS S/A - SANTANA DO IPANEMA', '100.024.400-5', '61 3027-8728', '', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'AVENIDA NOSSA SENHORA DE FÁTIMA N° 156', '', 'SANTANA DO IPANEMA', 'AL', '57.500-000', NULL, NULL, ''),
(792, 1, '13.128.415/0001-97', 'DL - Comércio Varejista de Sandálias LTDA EPP', '058/027.732-1', '3357-1286', '3244-8917 /99964-3316 Sandra', 'conveniencia792@hotmail.com', 'QR 406 Conj 07 Lote 24', 'Samambaia Norte', 'Samambaia', 'DF', '72.321-007', -158.629060, -480.816300, ''),
(797, 1, '22.963.922/0001-37', 'MN Plus Calçados e Assessórios LTDA', '104.064.278-8', '(61)9.9867-7070 ', '(61)9.8172-8571', 'parperfeito.calcados23@gmail.com', 'Avenida Comercial 15 de Junho, Quadra 08 Lote 13 Loja 03', 'Parque Rio Branco', 'Valparaíso de Goiás', 'GO', '72.870-083', -160.753850, -479.903840, ''),
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
(850, 1, '41.198.828/0001-83', 'Araújo Bombonieri LTDA', '201/046256-9 ', '61-3978-5117', '(61)99643-7863 (Rosangela)', 'araujo2021bombonieri@gmail.com', 'Avenida Contorno, Área Especial Lote 03 Sala 14 (situado na unidade do DETRAN do Gama)', 'Cidade Nova', 'Gama', 'DF', '72.490-010', -159.979740, -480.610630, ''),
(851, 1, '05.540.602/0001-55', 'RAMOS E RAMALHO LTDA', '107/040.171-1', '3970-7872 ', ' 99100-9173 Nadja ', 'cnp851@gmail.com', 'Quadra 14 Áreas especiais 29 e 30 Parte A (situado na unidade do DETRAN de Sobradinho)', 'Sobradinho', 'Sobradinho', 'DF', '72.350-110', -156.519390, -477.808350, ''),
(853, 1, '37.084.647/0001-59', 'SILAS SARAIVA COMERCIO DE FERRAGENS LTDA', '241/021.293-4', '(61) 3525-7685', '98559-5977 Silas', 'silassaraiva@gmail.com; saraiva.cnp853@gmail.com; caixas.cnp853@gmail.com; acsasaraiva@gmail.com', 'SHRF II QS 14, Bloco B, Lote 01', 'Riacho Fundo II', 'Riacho Fundo II', 'DF', '71.884-546', -159.439550, -480.367380, ''),
(855, 1, '03.771.149/0001-62', 'Look Video LTDA ME', '201/016.739-7', '3395-2063 ', 'Rosângela Maria: 996437863\nVinícius Campos: 985952205\nGeane Santos:995049330\n', 'euvicristo@hotmail.com', 'QR 316 Conjunto P Casa 23 Lojas 01 e 02', 'Santa Maria', 'Santa Maria', 'DF', '72.505-260', -160.086780, -479.930390, ''),
(858, 1, '12.875.569/0001-80', 'BRB SERVICOS S/A - DELMIRO GOUVEIA', '100.024.400-5', '61 3027-8740', '', 'marcos.siqueira@brbservicos.com.br; sarah.santos@brbservicos.com.br; Christiane.nunes@brbservicos.co', 'RUA VER. JOÃO DANTAS FEITOSA', '', 'DELMIRO GOUVEIA', 'AL', '57.200-000', NULL, NULL, ''),
(860, 1, '05.386.426/0001-49', 'NC Correspondente Comércio de Chinelos Ltda - ME', '047/010.042-7', '3264-5905', '99177-2539', 'cmonofre07@gmail.com', 'CSD 05, Lote 07, Loja 01', 'Taguatinga Sul', 'Taguatinga', 'DF', '72.020-055', -158.486990, -480.467530, ''),
(861, 1, '07.847.440/0001-28', 'Quales Comercio e Serviços LTDA ME', '201/031.236-2', '3202-5511 / 3202-441', '8417-5889 / 8312-2323 Carlos', 'carlos.lopes@convenienciabsb.com.br', 'SCS Quadra 06 Bloco A Loja 131 - Edifício Presidente', 'Asa Sul', 'Brasília', 'DF', '70.327-900', -157.967490, -478.902550, ''),
(863, 1, '05.330.191/0001-73', 'TIARLES LOURENCO DOS SANTOS EIRELI', '110/020.269-0', '9 9912-4131', '9 9912-4131 Tiarles / Operadora Juliane 61 99629-0582.', 'tiarleslourenco@gmail.com', 'Rua Café Goiano Quadra 11 Lote 06 Loja 01', 'Vila Vicentina', 'Planaltina', 'DF', '73.320-110', -156.288500, -476.539630, ''),
(866, 1, '07.994.316/0001-95', 'Valéria da Silva Vasques Magalhães ME', '087/000.553-7', '3606-1840', '9913-3603 / 98522-8267 Júnior (gerente )/ 9694-2617 Valéria', 'brbconv866@gmail.com', 'QD 54, lote 13 loja 4\n', 'Centro', 'Santo Antônio do Descoberto', 'GO', '72.900-362', -159.439340, -4826.415610, ''),
(869, 0, '05.382.984/0001-36', 'M C Leite Martins Utilidades do Lar ME', '043/016.183-2', '(61) 3377 - 7253', '8634-0606 Milane', 'mcmilane@yahoo.com.br', 'EQNP 15/19 Bloco F Lote 04 Loja 04', 'P Norte', 'Ceilândia', 'DF', '72.241-566', -158.079280, -481.334470, ''),
(870, 1, '07.393.450/0001-30', 'LM Cunha Cafeteria LTDA ME', '105/010.084-8', '3877-7393 / 3386 739', 'Moises (61) 99224-0516 /Tatiana (61) 98412-3841', 'lmcunha870@gmail.com', '3ª Avenida, Lotes 294A e 300A Loja 02', 'Núcleo Bandeirante', 'Núcleo Bandeirante', 'DF', '71.720-505', -158.679160, -479.625310, ''),
(871, 1, '02.451.423/0001-53', 'Centro de Formação de Condutores A B Educativo LTDA EPP', '201.039.911-5', '3225-0469', 'Fabiano 3321-2066/ 98193-2455  Luciene - 3369-1000/ 98260-1100', 'autoescola.saocristovao@outlook.com', 'Setor de Diversões Sul, Bloco G Loja 01 Térreo', 'Asa Sul', 'Brasília', 'DF', '70.392-900', -157.966140, -478.846020, ''),
(874, 1, '05.520.248/0001-05', '4M - Comércio e Serviços LTDA ME', '174/009.253-5', '3377-5832 ', '8404-7584 / 2108-8894 Gildean', 'loja874@gmail.com', 'EQNP 26/30 Bloco E Lojas 01 e 02', 'Ceilândia Sul', 'Ceilândia', 'DF', '72.235-545', -158.436180, -481.197450, ''),
(875, 1, '05.515.605/0001-39', 'Via Bella Bijoux - Comércio e Confecção de Bijouterias LTDA ME', '058/013.681-7', '3355-1469', '3244-8917 / 99964-3316 Sandra ', 'conveniencia875@yahoo.com.br', 'QND 20 Lote 01 Lojas 02 e 03', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.120-200', -158.105660, -480.612660, ''),
(878, 1, '07.946.315/0001-75', 'C. Serra Comércio de Armarinho LTDA ME', '264/001.306-2', '3624-3515', '3385-1550 /98476-9508 / 98158-5841', 'c.serra878@gmail.com', 'Quadra 163 Lote 27 Loja 01', 'Jardim Céu Azul', 'Valparaíso de Goiás', 'GO', '72.871-110', -160.549160, -480.130800, ''),
(882, 1, '08.332.146/0001-46', 'FERC Utilidades e Armarinho LTDA ME', '053/038.911-8', '99321-0390 / 9823898', '98223-5093 Eduardo / 98173-8401 /61981738401 Maria de Fátima', 'fercutilidadesearmarinho@hotmail.com; gestor_eduardo@hotmail.com; loja882@hotmail.com;', 'QN 208 Conjunto E Lote 01 Loja 01', 'Samambaia Norte', 'Samambaia', 'DF', '72.316-515', -158.646000, -480.787610, ''),
(885, 1, '41.553.265/0001-02', 'RSL Serviço e Comércio LTDA', '280/010.582-2', '(61) 3968-7557', '61 98199 - 6576 /61 93968 - 7557 - Rogério', 'pontoarte885@gmail.com', 'QS 104 Conjunto 06 Lotes 05/06 Loja 02', 'Samambaia Sul', 'Samambaia', 'DF', '72.302-500', -158.758410, -480.809340, 'Loja foi vendida. Quando o contrato venceu, o novo sócio alterou a Razão Social e CNPJ e a loja foi contratada como nova empresa. A Gecor decidu por manter a mesma numeração.'),
(887, 1, '06.317.789/0001-95', 'Multimix Comércio de Utilidades LTDA', '103/028.308-4', '3352-3955', '61983332115 - Gabriela', 'brb887@gmail.com', 'CSE 03 Lote 16 Loja 01', 'Taguatinga Sul', 'Taguatinga', 'DF', '72.025-035', -158.578400, -480.432830, ''),
(888, 1, '06.994.363/0001-76', 'Coelho & Rabelo Comércio, Representações e Serviços LTDA ME', '082/000.010-8', '(61) 99187-1962', '(61) 99653-7308 / (11) 98989-9882 Naiara\n', 'santaterezinharosas@gmail.com', 'QNA 04, Lote 30, Loa 01/B', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.110-060', -158.279960, -480.578670, ''),
(889, 1, '15.596.030/0001-80', 'LM Papelaria e Copiadora LTDA - ME', '107/035.724-0', '61 99113-3398', '61 99113-3398 Wanessa', 'papelariapremium@gmail.com; wanessambcruz@gmail.com', 'Quadra 02 conjunto C/D bloco A lote A loja 18', 'Sobradinho', 'Sobradinho', 'DF', '73.015-383', -156.549270, -477.940630, 'Antigo CNP 657'),
(894, 1, '07.415.898/0001-08', 'Araújo Barreto Logística de Documentos Brasília LTDA ME', '082.003.373-1', '3336-8823', '99972 6195 Igor / 99820 6195 Elisabete', 'igor_desp@hotmail.com; elisabete.kelly19@gmail.com', 'SIG - Área Especial N° 2, Sala 19-A (situado na unidade do DETRAN de Taguatinga)', 'Taguatinga Norte', 'Taguatinga', 'DF', '72.152-500', -158.339700, -480.856810, 'Contrato de renovação automática, fim da vigência em 30.06.2022. Estando próximo a essa data efetuar o ajuste onde for necessário (Planilha Projeto, CNB, Contrato SAP)'),
(895, 1, '07.409.153/0001-36', 'Araguaia Comércio e Serviços LTDA ME', '079/001.544-7', '3373-9506', '61-99962-0800 - Waldinir', 'araguaia895@gmail.com', 'QNM 11 Lote 03 - AE S/N 1º andar Parte \"C\" - Shopping Popular (situado na unidade do \"Na Hora\" de Ceilândia)', 'Ceilândia Sul', 'Ceilândia', 'DF', '72.215-110', -158.197760, -481.022030, 'Contrato de renovação automática, fim da vigência em 30.06.2022. Estando próximo a essa data efetuar o ajuste onde for necessário (Planilha Projeto, CNB, Contrato SAP). Reforma 3 meses Na hora a partir do dia 08/11/21.'),
(896, 1, '19.727.649/0001-37', 'A C P Magazines e Informática Eireli', '060/041.445-0', '3967-5585', '(61)984383078', 'rastapechinelossitiodogama@gmail.com; uniconthec@gmail.com', 'QC 05 Lote 28 Loja 02 Residencial Santos Dumont', 'Santa Maria', 'Santa Maria', 'DF', '72.593-305', -159.947290, -479.958340, ''),
(898, 1, '10.448.220/0001-36', 'Comercial Opaspin LTDA', '024/022.513-9', '3568-9535', '(61) 99902-7747 Jonh Diego', 'johnaspin@gmail.com', 'Rua 08 Chácara 207 Lote 01 Loja 02/03', 'Vicente Pires', 'Vicente Pires', 'DF', '72.110-800', NULL, NULL, 'Recontratada através da NE 2024/033 aprovada em 18/07/2024;');

-- --------------------------------------------------------

--
-- Table structure for table `cnp_historico`
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
-- Dumping data for table `cnp_historico`
--

INSERT INTO `cnp_historico` (`cnp`, `dez_23`, `jan_24`, `fev_24`, `mar_24`, `abr_24`, `mai_24`, `jun_24`, `jul_24`, `ago_24`, `set_24`, `out_24`, `nov_24`, `dez_24`, `jan_25`, `fev_25`, `mar_25`, `abr_25`, `mai_25`, `jun_25`, `jul_25`, `ago_25`, `set_25`, `out_25`, `nov_25`, `dez_25`) VALUES
(703, 80432.51, 104970.68, 96671.44, 91076.85, 91076.85, 91765.43, 91765.43, 103059.26, 64751.45, 64751.45, 82535.68, 39906.56, 71638.84, 77562.73, 69558.27, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(704, 56470.38, 125574.73, 63024.24, 56004.20, 56004.20, 52279.06, 52279.06, 60113.92, 53751.53, 53751.53, 56399.92, 51403.27, 57006.24, 51730.52, 73810.09, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(711, 21990.52, 97676.22, 62026.02, 66268.67, 66268.67, 60138.02, 60138.02, 70713.99, 58935.03, 58935.03, 61021.41, 55686.84, 60988.69, 69170.92, 59844.69, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(712, 87316.95, 0.00, 79844.59, 83401.15, 83401.15, 81430.44, 81430.44, 90117.39, 81208.68, 81208.68, 83446.89, 68367.78, 73370.10, 76717.06, 82182.93, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(713, 54454.81, 58155.78, 51316.37, 51408.97, 51408.97, 46764.08, 46764.08, 50580.57, 48190.71, 48190.71, 47815.52, 45233.71, 39367.86, 42980.22, 42657.71, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(714, 91088.80, 179984.41, 96054.06, 96340.71, 96340.71, 77219.65, 77219.65, 97841.87, 84752.07, 84752.07, 93414.68, 80861.45, 86917.92, 83873.84, 82935.90, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(715, 21708.83, 0.00, 16766.91, 16163.25, 16163.25, 18527.12, 18527.12, 21615.40, 23089.58, 23089.58, 27702.14, 26448.02, 25730.67, 35761.10, 32244.17, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(718, 121704.59, 139847.18, 97039.57, 106580.80, 106580.80, 81102.63, 81102.63, 104146.20, 83544.35, 83544.35, 79842.87, 72093.14, 122114.85, 146411.07, 131583.84, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(719, 33152.06, 84592.02, 30684.32, 32477.13, 32477.13, 31462.00, 31462.00, 37122.65, 32393.41, 32393.41, 29700.45, 27312.22, 32406.25, 25379.48, 27316.78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(721, 2008.73, 100061.77, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 857.77, 903.54, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(722, 20346.22, 55059.81, 21108.99, 17121.86, 17121.86, 16184.46, 16184.46, 15904.86, 13774.68, 13774.68, 16146.98, 15078.72, 15522.88, 17845.70, 20513.23, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(723, 68170.07, 169483.68, 71005.97, 72084.19, 72084.19, 58826.42, 58826.42, 66414.06, 60808.45, 60808.45, 61774.24, 55976.37, 52991.22, 59739.04, 61322.27, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(724, 102482.56, 169056.52, 115715.49, 112346.59, 112346.59, 100029.03, 100029.03, 117594.75, 95970.87, 95970.87, 99532.78, 91401.04, 97049.93, 107952.99, 114658.08, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(728, 57643.63, 126855.58, 61408.31, 54953.01, 54953.01, 50626.78, 50626.78, 54678.90, 36081.46, 36081.46, 48980.26, 39257.99, 22787.49, 42483.68, 45124.37, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(729, 34469.24, 53755.87, 44403.31, 35059.01, 35059.01, 29084.27, 29084.27, 28020.10, 22168.71, 22168.71, 21318.10, 25634.92, 18062.04, 22177.37, 22109.13, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(730, 20367.85, 166858.30, 10654.20, 13862.02, 13862.02, 10796.92, 10796.92, 15701.60, 15409.71, 15409.71, 16481.67, 17479.61, 26056.18, 20292.86, 16779.24, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(738, 0.00, 0.00, 125.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 24160.09, 71027.49, 84276.39, 91176.60, 96052.71, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(739, 129129.85, 174911.70, 141951.22, 141531.63, 141531.63, 119791.84, 119791.84, 134076.42, 107009.23, 107009.23, 121858.55, 118377.93, 110696.87, 113643.72, 116779.87, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(741, 12190.14, 0.00, 8825.45, 7389.61, 7389.61, 7951.05, 7951.05, 9797.27, 6326.23, 6326.23, 8033.77, 4984.65, 5580.59, 6555.14, 8621.82, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(745, 57582.68, 0.00, 59143.34, 72244.14, 72244.14, 66516.97, 66516.97, 77593.47, 64224.07, 64224.07, 60421.45, 55343.53, 62960.52, 55345.99, 56886.02, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(748, 43648.83, 78219.92, 47606.76, 47909.57, 47909.57, 49286.26, 49286.26, 44423.54, 34682.92, 34682.92, 46491.78, 44852.07, 55987.42, 50030.43, 72333.49, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(749, 74619.56, 127349.50, 67936.96, 81817.25, 81817.25, 72357.26, 72357.26, 73985.16, 65583.97, 65583.97, 65661.02, 63882.63, 62091.14, 70460.64, 75434.40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(752, 34047.38, 58740.24, 49934.14, 49786.02, 49786.02, 43451.11, 43451.11, 48448.72, 44586.29, 44586.29, 49230.77, 42915.62, 42743.47, 49542.63, 52664.52, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(753, 86484.70, 163651.11, 86659.56, 71663.41, 71663.41, 79252.91, 79252.91, 88827.87, 82444.83, 82444.83, 82808.40, 72678.96, 74036.42, 71619.13, 75028.37, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(756, 20819.58, 35458.13, 14143.11, 16225.20, 16225.20, 20822.49, 20822.49, 22067.54, 14358.46, 14358.46, 15752.87, 14606.33, 14291.55, 17502.39, 17383.53, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(764, 65558.76, 157589.90, 68738.13, 67822.12, 67822.12, 58226.90, 58226.90, 67149.45, 65276.86, 65276.86, 60591.89, 54284.62, 11041.65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(767, 23508.81, 79831.73, 43889.73, 34947.04, 34947.04, 32266.64, 32266.64, 30749.78, 31822.05, 31822.05, 34242.27, 32231.14, 26828.06, 32660.25, 39264.48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(769, 92716.09, 140811.00, 96453.17, 107858.46, 107858.46, 94887.90, 94887.90, 88490.69, 72516.45, 72516.45, 73011.22, 69154.26, 64888.89, 61599.36, 74868.43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(771, 85352.55, 112505.17, 76603.73, 83702.44, 83702.44, 81428.08, 81428.08, 83026.61, 82050.49, 82050.49, 106896138.54, 77669.59, 60233.41, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(774, 47181.60, 65347.40, 49670.86, 47494.98, 47494.98, 40734.72, 40734.72, 42241.84, 41091.83, 41091.83, 41027.99, 34606.16, 39085.82, 41508.66, 42737.35, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(776, 41019.24, 125258.15, 41403.49, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 159.27, 1441.31, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(777, 58741.81, 84846.25, 64638.86, 60389.53, 60389.53, 56828.76, 56828.76, 58543.61, 54220.62, 54220.62, 52082.46, 53605.39, 55467.57, 51610.30, 57484.53, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(779, 60762.51, 97327.73, 79496.82, 75544.86, 75544.86, 75738.65, 75738.65, 78666.28, 70140.05, 70140.05, 75100.49, 62460.88, 59962.77, 60429.05, 66899.43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(783, 62587.63, 93039.97, 61523.30, 70240.84, 70240.84, 49660.18, 49660.18, 4670.52, 36214.44, 36214.44, 37541.30, 36054.09, 34982.82, 40529.78, 36905.74, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(784, 52321.19, 77341.89, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 651.29, 846.08, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(785, 27128.92, 0.00, 42947.48, 37344.74, 37344.74, 35857.03, 35857.03, 34602.19, 33873.22, 33873.22, 34577.55, 27971.51, 33799.13, 28782.28, 39049.48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(791, 0.00, 96447.56, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -10.46, 86.71, 169.07, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(792, 70148.20, 124002.76, 75474.33, 63853.35, 63853.35, 56292.12, 56292.12, 54603.51, 54030.35, 54030.35, 46637.76, 44543.84, 49761.82, 65598.15, 61444.46, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(797, 52523.12, 149584.66, 51144.30, 55391.58, 55391.58, 42974.06, 42974.06, 47845.77, 40652.52, 40652.52, 41197.70, 37562.73, 36518.97, 42115.55, 44145.90, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
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
(850, 14310.19, 28366.93, 22855.45, 17582.74, 17582.74, 15598.23, 15598.23, 15548.81, 16242.09, 16242.09, 17732.68, 17315.16, 19036.34, 21059.20, 21358.76, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(851, 28224.56, 69290.91, 39909.09, 29910.96, 29910.96, 26226.11, 26226.11, 32726.16, 26084.05, 26084.05, 28699.04, 26278.62, 28184.56, 30396.77, 32376.18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(853, 52454.41, 86781.12, 51055.41, 54865.91, 54865.91, 45361.77, 45361.77, 50288.45, 46409.27, 46409.27, 48163.00, 39002.41, 39329.28, 44586.36, 44969.77, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(855, 40760.43, 157384.21, 61176.13, 54521.02, 54521.02, 49546.51, 49546.51, 49123.75, 40571.78, 40571.78, 47196.80, 43575.08, 36514.96, 41389.93, 41379.58, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(858, 40252.57, 92571.85, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 8.30, 1216.97, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(860, 23936.32, 72718.30, 39513.64, 34650.01, 34650.01, 32543.65, 32543.65, 33021.21, 26429.63, 26429.63, 29796.77, 24732.74, 30047.96, 28985.81, 32342.78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(861, 40587.65, 76736.55, 45048.19, 44020.63, 44020.63, 38727.59, 38727.59, 40809.74, 37439.77, 37439.77, 35853.96, 31550.22, 36852.71, 40100.92, 41725.42, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(863, 60689.17, 74102.47, 60099.50, 58689.83, 58689.83, 56255.66, 56255.66, 60941.84, 51412.80, 51412.80, 55266.00, 44693.19, 45489.20, 58069.37, 51033.68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(866, 126748.99, 252787.80, 118439.01, 120545.61, 120545.61, 109079.71, 109079.71, 106613.51, 106074.59, 106074.59, 114322.44, 101003.87, 108149.98, 101039.96, 107513.01, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(869, 77625.46, 135725.22, 83460.28, 74275.44, 74275.44, 69029.43, 69029.43, 61650.02, 59734.31, 59734.31, 56950.92, 53893.41, 51417.36, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(870, 51630.69, 123911.02, 69119.51, 51423.74, 51423.74, 44204.88, 44204.88, 57960.86, 42213.97, 42213.97, 56123.57, 52791.55, 45853.19, 61074.40, 64807.18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(871, 27175.70, 52133.67, 26744.21, 28078.67, 28078.67, 26841.05, 26841.05, 26017.07, 24200.05, 24200.05, 24063.20, 22057.43, 21267.74, 22178.71, 26177.89, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(874, 107141.87, 199400.32, 115342.99, 105711.32, 105711.32, 102769.10, 102769.10, 99131.05, 92128.01, 92128.01, 81251.68, 76720.80, 76982.74, 87535.10, 92249.48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(875, 58396.11, 117265.94, 66277.40, 65384.84, 65384.84, 73591.23, 73591.23, 81724.76, 87615.58, 87615.58, 67447.05, 56206.26, 57062.76, 39448.99, 60789.21, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(878, 37792.74, 107250.08, 33866.32, 38178.67, 38178.67, 33740.47, 33740.47, 33647.93, 29011.95, 29011.95, 32339.43, 28740.75, 28819.15, 30970.23, 34207.47, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(882, 68898.70, 171642.18, 80275.24, 73097.40, 73097.40, 66303.99, 66303.99, 74886.53, 51935.23, 51935.23, 56595.36, 61498.15, 61202.25, 61292.05, 51821.91, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(885, 93028.18, 150752.55, 85141.42, 86718.78, 86718.78, 105023.59, 105023.59, 116591.06, 94415.08, 94415.08, 110395.91, 94197.94, 68640.96, 98970.82, 83221.53, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(887, 27403.81, 75878.06, 36497.20, 30879.81, 30879.81, 31908.71, 31908.71, 29386.59, 31867.12, 31867.12, 29902.37, 27650.20, 24074.81, 31095.45, 32854.87, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(888, 43286.64, 66192.86, 45406.01, 39889.95, 39889.95, 32086.65, 32086.65, 40038.73, 38129.65, 38129.65, 27944.41, 30301.16, 28490.55, 33045.78, 36613.88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(889, 40809.15, 0.00, 41729.98, 39611.01, 39611.01, 34209.72, 34209.72, 32641.53, 29236.94, 29236.94, 28508.27, 22437.66, 21670.61, 23548.14, 26130.06, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(894, 18685.68, 45150.58, 44477.45, 41883.39, 41883.39, 41106.09, 41106.09, 36813.77, 34042.64, 34042.64, 32675.17, 32897.59, 35947.71, 40187.03, 39092.40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(895, 84288.36, 122066.20, 88566.07, 85850.48, 85850.48, 90929.33, 90929.33, 87807.64, 83625.35, 83625.35, 85254.81, 75989.58, 75314.61, 91515.51, 97765.97, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(896, 16894.42, 43076.53, 22312.44, 20343.71, 20343.71, 20412.13, 20412.13, 23413.97, 17520.76, 17520.76, 19438.78, 16830.82, 19148.05, 17997.98, 20658.68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(898, 79618.81, 56935.13, 76081.58, 71795.23, 71795.23, 41520.09, 41520.09, 0.00, 0.00, 0.00, 39572.63, 49561.87, 61606.21, 69143.74, 82676.75, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `seguradora`
--

CREATE TABLE `seguradora` (
  `id` int(11) NOT NULL,
  `cnp` int(11) NOT NULL,
  `inicio_vigencia_seguro` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `valor_cobertura` decimal(15,2) DEFAULT NULL,
  `valor_parcela` decimal(15,2) DEFAULT NULL,
  `debito1` varchar(50) DEFAULT NULL,
  `debito2` varchar(50) DEFAULT NULL,
  `debito3` varchar(50) DEFAULT NULL,
  `debito4` varchar(50) DEFAULT NULL,
  `debito5` varchar(50) DEFAULT NULL,
  `forma_de_pgt` varchar(20) DEFAULT NULL,
  `situacao_proposta` varchar(50) DEFAULT NULL,
  `obs` text DEFAULT NULL,
  `apolice` varchar(50) DEFAULT NULL,
  `multiseguros` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `seguradora`
--

INSERT INTO `seguradora` (`id`, `cnp`, `inicio_vigencia_seguro`, `vencimento`, `valor_cobertura`, `valor_parcela`, `debito1`, `debito2`, `debito3`, `debito4`, `debito5`, `forma_de_pgt`, `situacao_proposta`, `obs`, `apolice`, `multiseguros`) VALUES
(76, 885, '2025-02-01', '2025-02-01', 100000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', '1351000320371', NULL),
(77, 728, '2024-02-27', '2025-02-27', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(78, 756, '2024-02-16', '2025-02-16', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', '1351000319871', NULL),
(79, 875, '2024-02-27', '2025-02-27', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(80, 822, '2024-07-31', '2025-07-31', 70000.00, 629.89, '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', '15/11/2024 BAIXADO', '15/12/2024 PENDENTE', '15/01/2025 PENDENTE', 'B', 'A', 'APÓLICE CANCELADA POR FALTA DE PGTO', '1351000315871', NULL),
(81, 848, '2024-07-31', '2025-07-31', 70000.00, 629.89, '15/09/2024 BAIXADO', '15/10/2024 PENDENTE', '15/11/2024 PENDENTE', '15/12/2024 PENDENTE', '15/01/2025 PENDENTE', 'B', 'A', 'APÓLICE CANCELADA POR FALTA DE PGTO', '1351000315671', NULL),
(82, 748, '2024-07-31', '2025-07-31', 70000.00, 629.89, '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 PENDENTE', 'B', 'A', '1ª REPROGRAMAÇÃO DE BOLETO', '1351000315771', NULL),
(83, 898, '2024-09-05', '2025-09-05', 70000.00, 809.86, '27/10/2024 BAIXADO', '27/11/2024 BAIXADO', '27/12/2024 BAIXADO', '27/01/2025 BAIXADO', '2025-02-27 00:00:00', 'B', '0', 'Sem pendência ', '1351000316471', NULL),
(84, 704, '2023-12-01', '2024-12-01', 70000.00, 809.86, '15/01/2024 BAIXADO', '15/02/2024 BAIXADO', '15/03/2024 BAIXADO', '15/04/2024 BAIXADO', '2024-05-15 00:00:00', 'B', 'A', 'CONFIRMAR O STATUS DO CNP.', '1351000308971', NULL),
(85, 703, '2024-08-22', '2025-08-22', 90000.00, 809.86, '15/10/2024 BAIXADO', '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 PENDENTE', '2025-02-15 00:00:00', 'B', 'A', '2ª Reprogramação de boleto.', '1351000316371', NULL),
(86, 896, '2024-02-01', '2025-02-01', 70000.00, 0.00, NULL, NULL, NULL, NULL, NULL, 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(87, 809, '2024-01-11', '2025-01-11', 70000.00, 0.00, NULL, NULL, NULL, NULL, NULL, 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(88, 711, '2024-01-04', '2025-01-04', 70000.00, 0.00, NULL, NULL, NULL, NULL, NULL, 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(89, 712, '2024-02-27', '2025-02-27', 90000.00, 0.00, NULL, NULL, NULL, NULL, NULL, 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(90, 713, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318671', 'CADASTRAR'),
(91, 714, '2024-12-01', '2025-12-01', 90000.00, 809.86, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000317371', 'CADASTRAR'),
(92, 719, '2024-05-15', '2025-05-15', 70000.00, 629.89, '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000315071', NULL),
(93, 715, '2024-12-26', '2025-12-26', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318971', 'CADASTRAR'),
(94, 718, '2024-12-01', '2025-12-01', 100000.00, 899.84, '15/01/2025 PENDENTE', '15/02/2025 PENDENTE', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', '1ª REPROGRAMAÇÃO DE BOLETO', '1351000317271', 'CADASTRAR'),
(95, 722, '2025-01-11', '2026-01-11', 70000.00, 629.89, '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', '2025-06-15 00:00:00', '2025-07-15 00:00:00', 'B', 'A', 'Sem pendência', '1351000319171', 'CADASTRAR'),
(96, 723, '2025-02-01', '2026-02-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', '1351000320171', NULL),
(97, 724, '2024-12-01', '2025-12-01', 120000.00, 1079.81, '15/02/2025 BAIXADO', '15/03/2025 BAIXADO', '2025-04-15 00:00:00', '2025-05-15 00:00:00', '2025-06-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318471', 'CADASTRAR'),
(98, 730, '2025-02-16', '2026-02-16', 70000.00, 629.89, '2024-03-15 00:00:00', '2024-04-15 00:00:00', '2024-04-15 00:00:00', '2024-05-15 00:00:00', '2024-06-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000319871', 'CADASTRAR'),
(99, 729, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '15/03/2025 BAIXADO', '15/04/2025 BAIXADO', '15/05/2025 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000317771', 'CADASTRAR'),
(100, 745, '2024-02-21', '2025-02-21', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(101, 784, '2024-02-06', '2025-02-06', 70000.00, 629.89, '-', '-', '-', '-', '-', 'B', 'A', 'CNP encerrada', NULL, NULL),
(102, 739, '2025-12-01', '2026-12-01', 150000.00, 1349.77, '29/01/2025 BAIXADO', '2025-03-01 00:00:00', '2025-04-01 00:00:00', '2025-05-01 00:00:00', '2025-06-01 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318271', NULL),
(103, 741, '2024-06-21', '2025-06-21', 70000.00, 629.89, '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', 'B', 'A', 'Sem pendência', '1351000316971', 'CADASTRAR'),
(104, 791, '0000-00-00', '0000-00-00', 70000.00, 0.00, '-', '-', '-', '-', '-', 'B', 'A', 'CNP encerrada', NULL, NULL),
(105, 753, '2024-04-02', '2025-04-02', 90000.00, 1079.81, '20/04/2024 BAIXADO', '15/05/2024 BAIXADO', '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000314371', 'CADASTRAR'),
(106, 749, '2025-02-21', '2026-02-21', 90000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(107, 752, '2024-02-27', '2025-02-27', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(108, 764, '2024-12-07', '2025-12-07', 70000.00, 629.89, '15/01/2025 PENDENTE', '15/02/2025 PENDENTE', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', '1ª REPROGRAMAÇÃO DE BOLETO', '1351000318571', NULL),
(109, 767, '2024-09-11', '2025-09-11', 70000.00, 629.89, '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', 'B', 'A', 'Sem pendência', '1351000316671', NULL),
(110, 771, '2025-02-21', '2026-02-21', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(111, 776, '2023-12-01', '2024-12-01', 70000.00, 629.89, '15/01/2024 BAIXADO', '15/02/2024 BAIXADO', '15/03/2024 PENDENTE', '2024-04-15 00:00:00', '2024-05-15 00:00:00', 'B', 'A', 'CNP encerrada: cancelar apólice ', '1351000307571', NULL),
(112, 769, '2024-12-01', '2025-12-01', 90000.00, 809.86, '15/01/2025 PENDENTE', '15/02/2025 PENDENTE', '2025-03-15 00:00:00', '15/04/2025', '2025-05-15 00:00:00', 'B', 'A', '1ª REPROGRAMAÇÃO DE BOLETO', '1351000318771', NULL),
(113, 774, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000317971', NULL),
(114, 777, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '2025-02-15 00:00:00', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '15/05/2025', 'B', 'A', 'Sem pendência', '1351000318871', NULL),
(115, 779, '2024-09-29', '0000-00-00', 90000.00, 629.89, '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', 'B', 'A', 'Sem pendência', '1351000316571', NULL),
(116, 783, '2025-02-01', '2026-02-01', 70000.00, 0.00, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(117, 785, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000317171', NULL),
(118, 792, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000317571', 'CADASTRAR'),
(119, 797, '2025-01-04', '2026-01-04', 70000.00, 629.89, '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', '2025-06-15 00:00:00', '2025-07-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000319671', 'CADASTRAR'),
(120, 858, '2023-12-01', '2024-12-01', 70000.00, 629.89, '-', '-', '-', '-', '-', 'B', 'A', 'CNP encerrada', NULL, NULL),
(121, 805, '2024-04-15', '2025-04-15', 70000.00, 629.89, '15/05/2024 BAIXADO', '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000314771', 'CADASTRAR'),
(122, 803, '2024-12-01', '2025-12-01', 70000.00, 629.89, '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', '2025-06-15 00:00:00', '2025-07-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000320271', 'CADASTRAR'),
(123, 811, '2025-02-06', '2026-02-06', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(124, 813, '2025-02-01', '2026-02-01', 90000.00, 899.84, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(125, 818, '2024-04-15', '2025-04-15', 70000.00, 629.89, '15/05/2024 BAIXADO', '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000314571', NULL),
(126, 817, '2024-01-04', '2025-01-04', 70000.00, 809.86, '16/01/2024 BAIXADO', '15/02/2024 BAIXADO', '15/03/2024 BAIXADO', '15/04/2024 BAIXADO', '15/05/2024 BAIXADO', 'B', 'A', 'CONFIRMAR O STATUS DO CNP.', '1351000310271', NULL),
(127, 824, '2024-12-01', '2025-12-01', 70000.00, 809.86, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000319071', NULL),
(128, 829, '2025-02-01', '2026-02-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(129, 839, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2024 BAIXADO', '15/02/2024 BAIXADO', '2024-03-15 00:00:00', '2024-04-15 00:00:00', '2024-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318071', NULL),
(130, 846, '2024-04-15', '2025-04-15', 70000.00, 629.89, '25/05/2024 PENDENTE', '2024-06-25 00:00:00', '2024-07-25 00:00:00', '2024-08-25 00:00:00', '2024-09-25 00:00:00', 'B', 'A', 'CONFIRMAR O STATUS DO CNP.', '1351000314671', NULL),
(131, 850, '2024-04-15', '2025-04-15', 70000.00, 629.89, '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000314871', 'CADASTRAR'),
(132, 851, '2024-05-15', '2025-05-15', 70000.00, 629.89, '15/06/2024 BAIXADO', '15/07/2024 BAIXADO', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000315171', 'CADASTRAR'),
(133, 845, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318171', 'CADASTRAR'),
(134, 853, '2025-01-11', '2026-01-11', 70000.00, 629.89, '2024-03-15 00:00:00', '2024-04-15 00:00:00', '2024-05-15 00:00:00', '2024-06-15 00:00:00', '2024-07-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000319471', 'CADASTRAR'),
(135, 855, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 PENDENTE', '15/02/2025 PENDENTE', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', '1ª REPROGRAMAÇÃO DE BOLETO', '1351000317471', 'CADASTRAR'),
(136, 860, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000318371', NULL),
(137, 861, '2024-12-01', '2025-12-01', 70000.00, 629.89, '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000317871', NULL),
(138, 863, '2025-02-26', '2026-02-26', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(139, 866, '2024-12-01', '2025-12-01', 120000.00, 1349.77, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(140, 869, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(141, 870, '2025-02-27', '2026-02-27', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(142, 871, '2025-01-23', '2026-01-23', 70000.00, 629.89, '2025-03-15 00:00:00', '2025-04-15 00:00:00', '2025-05-15 00:00:00', '2025-06-15 00:00:00', '2025-07-15 00:00:00', 'B', 'A', 'Sem pendência ', '1351000319571', 'CADASTRAR'),
(143, 874, '2024-12-01', '2025-12-01', 100000.00, 1349.77, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(144, 878, '2024-08-08', '2025-08-08', 70000.00, 629.89, '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000316071', NULL),
(145, 882, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(146, 887, '2024-10-07', '2025-10-07', 70000.00, 629.89, '15/11/2024 BAIXADO', '15/12/2024 BAIXADO', '15/01/2025 BAIXADO', '15/02/2025 BAIXADO', '2025-03-15 00:00:00', 'B', 'A', 'Sem pendência', '1351000316871', NULL),
(147, 888, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(148, 889, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(149, 894, '2024-12-01', '2025-12-01', 70000.00, 629.89, 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'AGUARDANDO EMISSÃO DOS BOLETOS', 'B', 'A', 'Aguardando emissão da apólice', NULL, NULL),
(150, 895, '2024-05-15', '2025-05-15', 90000.00, 809.86, '15/06/2024 BAIXADA', '15/07/2024 BAIXADA', '15/08/2024 BAIXADO', '15/09/2024 BAIXADO', '15/10/2024 BAIXADO', 'B', 'A', 'Sem pendência ', '1351000314971', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cnp_data`
--
ALTER TABLE `cnp_data`
  ADD PRIMARY KEY (`cnp`);

--
-- Indexes for table `cnp_historico`
--
ALTER TABLE `cnp_historico`
  ADD PRIMARY KEY (`cnp`);

--
-- Indexes for table `seguradora`
--
ALTER TABLE `seguradora`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_seguradora_cnp` (`cnp`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `seguradora`
--
ALTER TABLE `seguradora`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=151;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cnp_historico`
--
ALTER TABLE `cnp_historico`
  ADD CONSTRAINT `fk_cnp_historico` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `seguradora`
--
ALTER TABLE `seguradora`
  ADD CONSTRAINT `fk_seguradora_cnp` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
