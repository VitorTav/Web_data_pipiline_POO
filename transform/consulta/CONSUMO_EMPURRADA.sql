CREATE TABLE dbfreightech.CONSUMO_EMPURRADA
    ( ID INT(10) NOT NULL AUTO_INCREMENT , 
    Vigencia VARCHAR(250) NULL,
    Unidade_CNPJ VARCHAR(250) NULL,
    Unidade_Nome VARCHAR(250) NULL,
    Unidade_SAP VARCHAR(250) NULL,
    Unidade_TMS VARCHAR(250) NULL,
    Unidade_Promax_UNB VARCHAR(250) NULL,
    Unidade_Regional VARCHAR(250) NULL,
    Operador_CNPJ VARCHAR(250) NULL,
    Operador_Nome VARCHAR(250) NULL,
    Operador_SAP VARCHAR(250) NULL,
    Operador_TMS VARCHAR(250) NULL,
    Operador_Promax VARCHAR(250) NULL,
    Organizacao_de_Compras VARCHAR(250) NULL,
    Prazo_Pagamento VARCHAR(250) NULL,
    Capacidade_Empurrada VARCHAR(250) NULL,
    Consumo VARCHAR(250) NULL,
    Ford VARCHAR(250) NULL,
    Iveco VARCHAR(250) NULL,
    Mercedes VARCHAR(250) NULL,
    Scania VARCHAR(250) NULL,
    Volks VARCHAR(250) NULL,
    Volvo VARCHAR(250) NULL,
    _ID VARCHAR(250) NULL ,
 PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `dbfreightech`.`CONSUMO_EMPURRADA` ADD UNIQUE `UNI_ID` (`Unidade_Nome`, `_ID`); 
ALTER TABLE `CONSUMO_EMPURRADA` ADD INDEX( `Unidade_Nome`);
ALTER TABLE `CONSUMO_EMPURRADA` ADD INDEX( `_ID`);
