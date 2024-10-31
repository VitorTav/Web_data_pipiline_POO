CREATE TABLE PNEU_INSUMOS
(
    ID INT(10) NOT NULL AUTO_INCREMENT,
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
    ano VARCHAR(250) NULL,
    pneuMedidaEmpurrada VARCHAR(250) NULL,
    tipoPneu VARCHAR(250) NULL,
    valor VARCHAR(250) NULL,
    _id VARCHAR(250) NULL,
    PRIMARY KEY (`ID`)
) ENGINE = InnoDB;
ALTER TABLE `PNEU_INSUMOS` ADD UNIQUE `UNI_ID` (`Unidade_Nome`, `_id`);
ALTER TABLE `PNEU_INSUMOS` ADD INDEX( `Unidade_Nome`);
ALTER TABLE `PNEU_INSUMOS` ADD INDEX( `_id`);
