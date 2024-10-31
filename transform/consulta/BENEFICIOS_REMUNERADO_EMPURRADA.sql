CREATE TABLE dbfreightech.BENEFICIOS_REMUNERADO_EMPURRADA
    ( ID INT(10) NOT NULL AUTO_INCREMENT , 
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
    CARGO_BENEFICIO VARCHAR(250) NULL,
    ITEM_BENEFICIO VARCHAR(250) NULL,
    PARTICIPACAO_EMPRESA VARCHAR(250) NULL,
    QUANTIDADE VARCHAR(250) NULL,
    QUANTIDADE_DE_DIAS_UTEIS VARCHAR(250) NULL,
    RESSARCIMENTO_FUNCIONARIO VARCHAR(250) NULL,
    TOTAL VARCHAR(250) NULL,
    TURNO_EMPURRADA VARCHAR(250) NULL,
    VALOR VARCHAR(250) NULL,
    _ID VARCHAR(250) NULL ,
 PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `dbfreightech`.`BENEFICIOS_REMUNERADO_EMPURRADA` ADD UNIQUE `UNI_ID` (`UNIDADE_NOME`, `_ID`); 
ALTER TABLE `BENEFICIOS_REMUNERADO_EMPURRADA` ADD INDEX( `UNIDADE_NOME`);
ALTER TABLE `BENEFICIOS_REMUNERADO_EMPURRADA` ADD INDEX( `_ID`);