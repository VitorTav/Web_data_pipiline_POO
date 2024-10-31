CREATE TABLE dbfreightech.EQP_FAD_AS
    ( id INT(10) NOT NULL AUTO_INCREMENT , 
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
    Beneficios VARCHAR(250) NULL,
    Cargo VARCHAR(250) NULL,
    Percentual_Encargos_e_Provisoes VARCHAR(250) NULL,
    Quantidade VARCHAR(250) NULL,
    Valor_Total VARCHAR(250) NULL,
    Valor_Unitario VARCHAR(250) NULL,
    _ID VARCHAR(250) NULL ,
 PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `dbfreightech`.`EQP_FAD_AS` ADD UNIQUE `UNI_ID` (`UNIDADE_NOME`, `_ID`); 
ALTER TABLE `EQP_FAD_AS` ADD INDEX( `UNIDADE_NOME`);
ALTER TABLE `EQP_FAD_AS` ADD INDEX( `_ID`);