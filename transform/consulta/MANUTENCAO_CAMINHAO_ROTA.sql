CREATE TABLE dbfreightech.MANUTENCAO_CAMINHAO_ROTA 
( id INT(10) NOT NULL AUTO_INCREMENT , 
UNIDADE_CNPJ VARCHAR(250) NULL ,
UNIDADE_NOME VARCHAR(250) NULL ,
UNIDADE_SAP VARCHAR(250) NULL ,
UNIDADE_TMS VARCHAR(250) NULL ,
UNIDADE_PROMAX_UNB VARCHAR(250) NULL ,
UNIDADE_REGIONAL VARCHAR(250) NULL ,
OPERADOR_CNPJ VARCHAR(250) NULL ,
OPERADOR_NOME VARCHAR(250) NULL ,
OPERADOR_SAP VARCHAR(250) NULL ,
OPERADOR_TMS VARCHAR(250) NULL ,
OPERADOR_PROMAX VARCHAR(250) NULL ,
ORGANIZACAO_DE_COMPRAS VARCHAR(250) NULL ,
PRAZO_PAGAMENTO VARCHAR(250) NULL ,
ANO VARCHAR(250) NULL ,
CAPACIDADE_CAMINHAO VARCHAR(250) NULL ,
KM_1000 VARCHAR(250) NULL ,
KM_1250 VARCHAR(250) NULL ,
KM_1500 VARCHAR(250) NULL ,
KM_1750 VARCHAR(250) NULL ,
KM_2000 VARCHAR(250) NULL ,
KM_2250 VARCHAR(250) NULL ,
KM_2500 VARCHAR(250) NULL ,
KM_2750 VARCHAR(250) NULL ,
KM_3000 VARCHAR(250) NULL ,
KM_3250 VARCHAR(250) NULL ,
KM_3500 VARCHAR(250) NULL ,
_ID VARCHAR(250) NULL ,
 PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `dbfreightech`.`MANUTENCAO_CAMINHAO_ROTA` ADD UNIQUE `UNI_ID` (`UNIDADE_NOME`, `_ID`); 
ALTER TABLE `MANUTENCAO_CAMINHAO_ROTA` ADD INDEX( `UNIDADE_NOME`);
ALTER TABLE `MANUTENCAO_CAMINHAO_ROTA` ADD INDEX( `_ID`);