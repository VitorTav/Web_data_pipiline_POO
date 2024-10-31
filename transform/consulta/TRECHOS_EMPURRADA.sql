CREATE TABLE dbfreightech.TRECHOS_EMPURRADA
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
    Capacidade VARCHAR(250) NULL,
    Destino VARCHAR(250) NULL,
    destino_SAP VARCHAR(250) NULL,
    destino_TMS VARCHAR(250) NULL,
    F_MOV VARCHAR(250) NULL,
    Origem VARCHAR(250) NULL,
    origem_SAP VARCHAR(250) NULL,
    origem_TMS VARCHAR(250) NULL,
    cargaHorariaMotoristaPuxadaMensal VARCHAR(250) NULL,
    cargaHorariaPorTrajetoMinuto VARCHAR(250) NULL,
    cargaHorariaPorTrajetoMinutoLucro VARCHAR(250) NULL,
    cargaHorarioTrajetoDia VARCHAR(250) NULL,
    cargaHorarioTrajetoMes VARCHAR(250) NULL,
    chaveTrecho VARCHAR(250) NULL,
    cnpjIda VARCHAR(250) NULL,
    cnpjVolta VARCHAR(250) NULL,
    consumoDieselAjustado VARCHAR(250) NULL,
    custoDaDiaria VARCHAR(250) NULL,
    custoDoTr VARCHAR(250) NULL,
    diasMes VARCHAR(250) NULL,
    dieselConsumoDieselReaisKM VARCHAR(250) NULL,
    dieselConsumoKmL VARCHAR(250) NULL,
    fatorMotoristaAjustado VARCHAR(250) NULL,
    fatorMotoristaIndicado VARCHAR(250) NULL,
    faturamentoDestinoObrigatorio VARCHAR(250) NULL,
    freteComCprb VARCHAR(250) NULL,
    freteCtrc VARCHAR(250) NULL,
    freteLiquido VARCHAR(250) NULL,
    fretePTms VARCHAR(250) NULL,
    fretePisCofins VARCHAR(250) NULL,
    freteReaisKMDiesel VARCHAR(250) NULL,
    freteReaisKMLavagem VARCHAR(250) NULL,
    freteReaisKMLucroVariavel VARCHAR(250) NULL,
    freteReaisKMManutencaoCarreta VARCHAR(250) NULL,
    freteReaisKMManutencaoCavalo VARCHAR(250) NULL,
    freteReaisKMPedagio VARCHAR(250) NULL,
    freteReaisKMPneu VARCHAR(250) NULL,
    freteReaisKMSalarioVariavel VARCHAR(250) NULL,
    freteReaisKMSeguro VARCHAR(250) NULL,
    freteReaisViagemDiesel VARCHAR(250) NULL,
    freteReaisViagemLavagem VARCHAR(250) NULL,
    freteReaisViagemLucroVariavel VARCHAR(250) NULL,
    freteReaisViagemManutencaoCarreta VARCHAR(250) NULL,
    freteReaisViagemManutencaoCavalo VARCHAR(250) NULL,
    freteReaisViagemPedagio VARCHAR(250) NULL,
    freteReaisViagemPneus VARCHAR(250) NULL,
    freteReaisViagemSalarioVariavel VARCHAR(250) NULL,
    freteReaisViagemSeguro VARCHAR(250) NULL,
    frotaNoMunicipio VARCHAR(250) NULL,
    gradeCarregamento VARCHAR(250) NULL,
    icmsIss VARCHAR(250) NULL,
    impostosIcmsIss VARCHAR(250) NULL,
    kmIda VARCHAR(250) NULL,
    kmRodado VARCHAR(250) NULL,
    kmRodadoMesPorEquipe VARCHAR(250) NULL,
    kmRodadoMesPorEquipeLucro VARCHAR(250) NULL,
    kmVolta VARCHAR(250) NULL,
    lavagemReaisKm VARCHAR(250) NULL,
    lucroVariavelReaisKm VARCHAR(250) NULL,
    manutencaoCavalo VARCHAR(250) NULL,
    manutencaoImplementoReaiskm VARCHAR(250) NULL,
    observacao VARCHAR(250) NULL,
    pedagio VARCHAR(250) NULL,
    pedagioPorEixoIdaVolta VARCHAR(250) NULL,
    pedagioReaisKM VARCHAR(250) NULL,
    percentualIcmsIss VARCHAR(250) NULL,
    percentualPerdaDescartavel VARCHAR(250) NULL,
    percentualPerdaKm VARCHAR(250) NULL,
    percentualPerdaRegiao VARCHAR(250) NULL,
    pneuCustoPneusCamarasReaisKm VARCHAR(250) NULL,
    pneuQuantidadeDePneus VARCHAR(250) NULL,
    pneuValorDeVendaDaCarcaca VARCHAR(250) NULL,
    pneuValorMedioDaRecapagem VARCHAR(250) NULL,
    pneuValorMedioPneus VARCHAR(250) NULL,
    pneuVidautilPneu VARCHAR(250) NULL,
    premioProdutividadeFatorMotorista VARCHAR(250) NULL,
    premioProdutividadeKmRodado VARCHAR(250) NULL,
    premioProdutividadeSalarioVariavel VARCHAR(250) NULL,
    premioProdutividadeSalarioVariavelReaisKm VARCHAR(250) NULL,
    previsaoViagens VARCHAR(250) NULL,
    regiaoEmpurrada VARCHAR(250) NULL,
    seguro VARCHAR(250) NULL,
    seguroReaiskm VARCHAR(250) NULL,
    tempoInternoDestino VARCHAR(250) NULL,
    tempoInternoDestinoLucro VARCHAR(250) NULL,
    tempoInternoOrigem VARCHAR(250) NULL,
    tempoInternoOrigemLucro VARCHAR(250) NULL,
    tempoRefeicaoMinuto VARCHAR(250) NULL,
    tempoTrajetoFabricaCDMinuto VARCHAR(250) NULL,
    trechoComDiaria VARCHAR(250) NULL,
    trechoComVr VARCHAR(250) NULL,
    turnoEmpurrada VARCHAR(250) NULL,
    turnosFabrica VARCHAR(250) NULL,
    velocidadeMediaKmH VARCHAR(250) NULL,
    vidautilAjustadaPneu VARCHAR(250) NULL,
    _id VARCHAR(250) NULL ,
 PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `dbfreightech`.`TRECHOS_EMPURRADA` ADD UNIQUE `UNI_ID` (`Unidade_Nome`, `_id`); 
ALTER TABLE `TRECHOS_EMPURRADA` ADD INDEX( `Unidade_Nome`);
ALTER TABLE `TRECHOS_EMPURRADA` ADD INDEX( `_id`);