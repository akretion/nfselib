from enum import Enum

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


class Tamb(Enum):
    """
    Tipo Ambiente.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class Tboolean(Enum):
    """Confirmacao 1- Sim, 2 - Nao"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class TcodigoImpostoFederal(Enum):
    """
    Codigo do imposto 1-PIS, 2-COFINS, 3-INSS, 4-IR, 5-CSLL.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class Tnota(Enum):
    """Tipo Nota 1- NFSe; 2 - NFSe-a"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class TtipoDeducao(Enum):
    """Tipo recolhimento 1 - SEM DEDUÇÃO, 2 - MAPA DE MATERIAIS, 3 - PERCENTUAL, 4 - POR VALOR, 5 - PERCENTUAL / MAPA DE MATERIAIS, 6 - PUBLICIDADE, 7 - MAPA DE DEDUÇÕES PARA INTERMEDIAÇÃO"""
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"


class TtipoItemDeducao(Enum):
    """Tipo recolhimento 1 - DESPESAS COM MATERIAIS, 2 - DESPESAS COM SUBEMPREITADA, 3 - VEICULAÇÃO E PUBLICIDADE, 4 - SERVIÇOS"""
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TtipoPessoa(Enum):
    """1- Pessoa Fisica, 2 - Juridica"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class TtipoRecolhimento(Enum):
    """Tipo recolhimento 1 - PRÓPRIO, 2 - RETIDO, 3 - ISENTO DE RECOLHIMENTO"""
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TtipoTributacao(Enum):
    """Tipo tributacao 1 - Isento de ISSQN, 2 - IMUNE, 3 - EXIGIBILIDADE SUSPENSA, 4 - TRIBUTÁVEL, 5 - NÃO INCIDENTE NO MUNICÍPIO, 6 - TRIBUTÁVEL S.N., 7 - TRIBUTÁVEL FIXO, 8 - NÃO TRIBUTÁVEL, 9 - TRIBUTÁVEL MEI"""
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"


class TtipoValorDeducao(Enum):
    """Tipo recolhimento 1 - Valor, 2 - Percentual"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class TtipoValorImpostos(Enum):
    """Tipo recolhimento 1 - Valor, 2 - Aliquota"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class Tuf(Enum):
    """
    Tipo Sigla da UF // acrescentado em 24/10/08.
    """
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"
