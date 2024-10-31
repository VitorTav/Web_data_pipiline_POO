CREATE TABLE COMBUSTIVEL_INSUMOS
(
    ID INT(10) NOT NULL AUTO_INCREMENT,
    VIGENCIA VARCHAR(250) NULL,
    UNIDADE_CNPJ VARCHAR(250) NULL,
    UNIDADE_NOME VARCHAR(250) NULL,
    UNIDADE_SAP VARCHAR(250) NULL,
    UNIDADE_TMS VARCHAR(250) NULL,
    UNIDADE_PROMAX_UNB VARCHAR(250) NULL,
    UNIDADE_REGIONAL VARCHAR(250) NULL,
    OPERADOR_CNPJ VARCHAR(250) NULL,
    OPERADOR_NOME VARCHAR(250) NULL,
    OPERADOR_SAP VARCHAR(250) NULL,
    OPERADOR_TMS VARCHAR(250) NULL,
    OPERADOR_PROMAX VARCHAR(250) NULL,
    ORGANIZACAO_DE_COMPRAS VARCHAR(250) NULL,
    PRAZO_PAGAMENTO VARCHAR(250) NULL,
    CREDITOIMPOSTO VARCHAR(250) NULL,
    DESCRICAO VARCHAR(250) NULL,
    INICIATIVA VARCHAR(250) NULL,
    PRECOANP VARCHAR(250) NULL,
    PRECOCREDITOIMPOSTOS VARCHAR(250) NULL,
    PRECOOPERADORA VARCHAR(250) NULL,
    _ID VARCHAR(250) NULL,
    PRIMARY KEY (`ID`)
) ENGINE = InnoDB;
ALTER TABLE `COMBUSTIVEL_INSUMOS` ADD UNIQUE `UNI_ID` (`UNIDADE_NOME`, `_ID`);
ALTER TABLE `COMBUSTIVEL_INSUMOS` ADD INDEX( `UNIDADE_NOME`);
ALTER TABLE `COMBUSTIVEL_INSUMOS` ADD INDEX( `_ID`);