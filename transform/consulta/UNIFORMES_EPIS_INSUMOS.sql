CREATE TABLE TABELA_EXEMPLO
(
    ID INT(10) NOT NULL AUTO_INCREMENT
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
    CUSTO VARCHAR(250) NULL,
    CUSTO_MES VARCHAR(250) NULL,
    ICMS_REGIAO VARCHAR(250) NULL,
    ITEM_EPI VARCHAR(250) NULL,
    QUANTIDADE_ANO VARCHAR(250) NULL,
    TIPO_EQUIPE VARCHAR(250) NULL,
    _ID VARCHAR(250) NULL, 
    PRIMARY KEY (`ID`)
) ENGINE = InnoDB;
ALTER TABLE `UNIFORMES_EPIS_INSUMOS` ADD UNIQUE `UNI_ID` (`Unidade_Nome`, `_id`);
ALTER TABLE `UNIFORMES_EPIS_INSUMOS` ADD INDEX( `Unidade_Nome`);
ALTER TABLE `UNIFORMES_EPIS_INSUMOS` ADD INDEX( `_id`)
);
