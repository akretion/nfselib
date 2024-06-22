from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://localhost:8080/WsNFe2/tp"


class Nulo(Enum):
    """
    Definição para aceitar dado tipo nulo.
    """

    VALUE = ""


class TpAssincrono(Enum):
    """
    Tipo de processamento.

    :cvar S: Processamento Assíncrono
    :cvar N: Processamento Síncrono
    """

    S = "S"
    N = "N"


@dataclass
class TpBairroCompleto:
    """
    Informações do Bairro com o seu Tipo.

    :ivar TipoBairro: Tipo do Bairro (Bairro, Vila etc)
    :ivar NomeBairro: Nome do Bairro.
    """

    class Meta:
        name = "tpBairroCompleto"

    TipoBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    NomeBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )


@dataclass
class TpCpfcnpj2:
    """
    Tipo que representa um CPF/CNPJ.
    """

    class Meta:
        name = "tpCPFCNPJ2"

    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0}|[0-9]{11}",
        },
    )
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{14}",
        },
    )


@dataclass
class TpChaveNfe:
    """
    Chave de identificação da NF-e.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar NumeroNFe: Número da NF-e.
    :ivar CodigoVerificacao: Código de verificação da NF-e.
    :ivar RazaoSocialPrestador: Razão Social do Prestador do RPS.
    """

    class Meta:
        name = "tpChaveNFe"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    NumeroNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    RazaoSocialPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )


@dataclass
class TpChaveSubstituicaoNfse:
    """
    Chave de identificação para Substituição de uma NFSe.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar CPFCNPJTomador: CPF/CNPJ do Tomador.
    :ivar NumeroNFSeSubstituida: Número da NFSe a ser substituida.
    :ivar DataEmissaoNFSeSubstituida: Data da Emissão da NFSe a ser
        substituida.
    """

    class Meta:
        name = "tpChaveSubstituicaoNFSe"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    CPFCNPJTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    NumeroNFSeSubstituida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoNFSeSubstituida: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "white_space": "collapse",
        },
    )


class TpDeducaoPor(Enum):
    """
    Tipo que representa o modo de Dedução.

    :cvar VALOR: Dedução por valor em R$
    :cvar PERCENTUAL: Dedução por percentual do valor total de serviços
    """

    VALOR = "Valor"
    PERCENTUAL = "Percentual"


@dataclass
class TpEndereco:
    """
    Tipo Endereço.
    """

    class Meta:
        name = "tpEndereco"

    TipoLogradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    Logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    NumeroEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
        },
    )
    ComplementoEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        },
    )
    TipoBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    Cidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]",
        },
    )
    UF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 2,
            "white_space": "collapse",
        },
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,8}",
        },
    )


@dataclass
class TpInformacoesLote:
    """
    Informações do lote processado.

    :ivar NumeroLote: Número de lote.
    :ivar InscricaoPrestador: Inscrição municipal do prestador dos RPS
        contidos no lote.
    :ivar CPFCNPJRemetente: CNPJ do remetente autorizado a transmitir a
        mensagem XML.
    :ivar DataEnvioLote: Data/hora de envio do lote.
    :ivar QtdNotasProcessadas: Quantidade de RPS do lote.
    :ivar TempoProcessamento: Tempo de processamento do lote.
    :ivar ValorTotalServicos: Valor total dos serviços dos RPS contidos
        na mensagem XML.
    :ivar ValorTotalDeducoes: Valor total das deduções dos RPS contidos
        na mensagem XML.
    """

    class Meta:
        name = "tpInformacoesLote"

    NumeroLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    CPFCNPJRemetente: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    DataEnvioLote: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    QtdNotasProcessadas: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    TempoProcessamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ValorTotalServicos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorTotalDeducoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )


class TpItemTributavel(Enum):
    """
    Informa se o Item de serviço é tributavel ou nao.

    :cvar S: Sim - Item tributável
    :cvar N: Item não tributável
    """

    S = "S"
    N = "N"


@dataclass
class TpLogradouroCompleto:
    """
    Informações do Logradouro com o seu Tipo.

    :ivar TipoLogradouro: Tipo do Logradouro (Rua, Avenida etc)
    :ivar NomeLogradouro: Nome do Logradouro.
    """

    class Meta:
        name = "tpLogradouroCompleto"

    TipoLogradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    NomeLogradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )


class TpMetodoEnvio(Enum):
    """
    Metodo de Envio.

    :cvar WS: Web Service
    :cvar DLL: Componente RPS - DLL.
    :cvar DMS: Sistema DMS.
    """

    WS = "WS"
    DLL = "DLL"
    DMS = "DMS"


@dataclass
class TpNotaCancelamentoNfse:
    """
    Tipo Detalhes do Cancelamento de NFSe.

    :ivar InscricaoMunicipalPrestador: Inscrição municipal do prestador
        de serviços.
    :ivar NumeroNota: Número da NF-e.
    :ivar CodigoVerificacao: Código de verificação da NF-e.
    :ivar MotivoCancelamento: Motivo do Cancelamento da Nota Fiscal.
    :ivar Id:
    """

    class Meta:
        name = "tpNotaCancelamentoNFSe"

    InscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    MotivoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TpNotaConsultaNfse:
    """
    Tipo Detalhes da Nota da Consulta de NFSe.

    :ivar InscricaoMunicipalPrestador: Inscrição municipal do prestador
        de serviços.
    :ivar NumeroNota: Número da NF-e.
    :ivar CodigoVerificacao: Código de verificação da NF-e.
    :ivar Id:
    """

    class Meta:
        name = "tpNotaConsultaNFSe"

    InscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TpOperacao(Enum):
    """
    Tipo Operação.

    :cvar A: Sem Dedução.
    :cvar B: Com Dedução/Materiais.
    :cvar C: Imune/Isenta de ISSQN
    :cvar D: Devolução/Simples Remessa.
    :cvar J: Intermediação.
    """

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    J = "J"


@dataclass
class TpRpsconsultaNfse:
    """
    Tipo Detalhes do RPSSe.

    :ivar InscricaoMunicipalPrestador: Inscrição municipal do prestador
        de serviços.
    :ivar NumeroRPS: Número RPS.
    :ivar SeriePrestacao: Serie RPS.
    :ivar Id:
    """

    class Meta:
        name = "tpRPSConsultaNFSe"

    InscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    SeriePrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TpSerieRps(Enum):
    """
    Tipo série de documento.

    :cvar NF: Nota Fiscal de Servicos
    """

    NF = "NF"


class TpSerieRpssubstituido(Enum):
    """
    Tipo série de documento.

    :cvar NF: Nota Fiscal de Servicos
    :cvar VALUE:
    """

    NF = "NF"
    VALUE = ""


class TpSituacaoRps(Enum):
    """
    Tipo referente aos possíveis status de RPS.

    :cvar N: Normal.
    :cvar C: Cancelado.
    """

    N = "N"
    C = "C"


class TpTipoDeducao(Enum):
    """
    Tipo que representa as descrições das deduções permitidas.

    :cvar DESPESAS_COM_MATERIAIS: Despesas com Materiais.
    :cvar DESPESAS_COM_SUBEMPREITADA: Despesas com Subempreitada.
    :cvar DESPESAS_COM_MERCADORIAS: Despesas com Mercadorias.
    :cvar SERVICOS_DE_VEICULACAO_E_DIVULGACAO: Servicos de Veiculacao e
        Divulgacao
    :cvar SERVICOS: Outros Servicos que permitem dedução. Ex.
        Intermediação de Serviços, quando em uma nota existe um
        intermediário.
    :cvar MAPA_DE_CONST_CIVIL: Mapa de construção civil.
    :cvar VALUE:
    """

    DESPESAS_COM_MATERIAIS = "Despesas com Materiais"
    DESPESAS_COM_SUBEMPREITADA = "Despesas com Subempreitada"
    DESPESAS_COM_MERCADORIAS = "Despesas com Mercadorias"
    SERVICOS_DE_VEICULACAO_E_DIVULGACAO = "Servicos de Veiculacao e Divulgacao"
    SERVICOS = "Servicos"
    MAPA_DE_CONST_CIVIL = "Mapa de Const. Civil"
    VALUE = ""


class TpTipoRps(Enum):
    """
    Tipo referente aos possíveis tipos de RPS.

    :cvar RPS: Recibo Provisório de Serviços.
    """

    RPS = "RPS"


class TpTipoRecolhimento(Enum):
    """
    Tipo referente ao recolhimento.

    :cvar A: A Recolher.
    :cvar R: Retido na Fonte.
    """

    A = "A"
    R = "R"


class TpTributacao(Enum):
    """
    Tipo referente aos modos de tributação.

    :cvar C: Isenta de ISS.
    :cvar F: Imune.
    :cvar K: Depósito em Juízo.
    :cvar E: Não Incidente no Município.
    :cvar T: Tributável
    :cvar H: Tributável Simples Nacional.
    :cvar G: Tributável Fixo.
    :cvar N: Não Tributável.
    :cvar M: Tributação Microempresário Individual (MEI)
    """

    C = "C"
    F = "F"
    K = "K"
    E = "E"
    T = "T"
    H = "H"
    G = "G"
    N = "N"
    M = "M"


@dataclass
class TpChaveRps:
    """
    Tipo que define a chave identificadora de um RPS.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar SerieRPS: Série do RPS.
    :ivar NumeroRPS: Número do RPS.
    :ivar DataEmissaoRPS: Data de Emissao do RPS.
    :ivar RazaoSocialPrestador: Razão Social do Prestador do RPS.
    """

    class Meta:
        name = "tpChaveRPS"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    SerieRPS: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoRPS: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    RazaoSocialPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )


@dataclass
class TpConsultaNfse:
    """
    NFSe de retorno de consulta.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar NumeroNFe: Número da NF-e.
    :ivar CodigoVerificacao: Código de verificação da NF-e.
    :ivar SerieRPS: Série do RPS.
    :ivar NumeroRPS: Número do RPS.
    :ivar DataEmissaoRPS: Data de Emissão do RPS.
    :ivar RazaoSocialPrestador: Razão Social do Prestador do Serviço.
    :ivar TipoRecolhimento: Tipo do Recolhimento do Serviço.
    :ivar ValorDeduzir: Valor total de deduções.
    :ivar ValorTotal: Valor total de Itens de Nota.
    :ivar Aliquota: Valor total de Itens de Nota.
    """

    class Meta:
        name = "tpConsultaNFSe"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    NumeroNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    SerieRPS: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoRPS: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    RazaoSocialPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )
    TipoRecolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ValorDeduzir: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorTotal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )


@dataclass
class TpDeducoes:
    """
    Tipo deduções de nota fiscal.
    """

    class Meta:
        name = "tpDeducoes"

    DeducaoPor: Optional[TpDeducaoPor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    TipoDeducao: Optional[TpTipoDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    CPFCNPJReferencia: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    NumeroNFReferencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "pattern": r"[0-9]{1,10}",
        },
    )
    ValorTotalReferencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    PercentualDeduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    ValorDeduzir: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )


@dataclass
class TpDetalhesConsultaRps:
    """
    Tipo Detalhes da Consulta de RPS.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar SerieRPS: Série do RPS.
    :ivar NumeroRPS: Número do RPS.
    """

    class Meta:
        name = "tpDetalhesConsultaRPS"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    SerieRPS: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )


@dataclass
class TpItens:
    """
    Tipo Itens de Nota Fiscal.
    """

    class Meta:
        name = "tpItens"

    DiscriminacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 250,
            "white_space": "preserve",
        },
    )
    Quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    ValorUnitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorTotal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    Tributavel: Optional[TpItemTributavel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpLoteCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """

    class Meta:
        name = "tpLoteCancelamentoNFSe"

    Nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TpNotasCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """

    class Meta:
        name = "tpNotasCancelamentoNFSe"

    Nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )


@dataclass
class TpNotasConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """

    class Meta:
        name = "tpNotasConsultaNFSe"

    Nota: List[TpNotaConsultaNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )


@dataclass
class TpRpssConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """

    class Meta:
        name = "tpRPSsConsultaNFSe"

    RPS: List[TpRpsconsultaNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )


@dataclass
class TpRetornoNotasCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """

    class Meta:
        name = "tpRetornoNotasCancelamentoNFSe"

    Nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpChaveNfeRps:
    """
    Tipo que representa a chave de uma NFSe e a Chave do RPS que a mesma substitui.

    :ivar ChaveNFe: Chave da NFSe gerada.
    :ivar ChaveRPS: Chave do RPS substituído.
    """

    class Meta:
        name = "tpChaveNFeRPS"

    ChaveNFe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ChaveRPS: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpEvento:
    """
    :ivar Codigo: Código do evento.
    :ivar Descricao: Descrição do enveto.
    :ivar ChaveRPS: Chave do RPS.
    :ivar ChaveNFe: Chave da NFe.
    """

    class Meta:
        name = "tpEvento"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{3,4}",
        },
    )
    Descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    ChaveRPS: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ChaveNFe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpListaDeducoes:
    """
    Deduções.
    """

    class Meta:
        name = "tpListaDeducoes"

    Deducao: List[TpDeducoes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 200,
        },
    )


@dataclass
class TpListaDetalhesConsultaRps:
    """
    Lista de Detalhes da Consulta RPS.
    """

    class Meta:
        name = "tpListaDetalhesConsultaRPS"

    Detalhe: List[TpDetalhesConsultaRps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )


@dataclass
class TpListaItens:
    """
    Itens de Serviço.
    """

    class Meta:
        name = "tpListaItens"

    Item: List[TpItens] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 25,
        },
    )


@dataclass
class TpListaNfse:
    """
    Lista de NFSE consultada.
    """

    class Meta:
        name = "tpListaNFSe"

    ConsultaNFSe: List[TpConsultaNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpLoteConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """

    class Meta:
        name = "tpLoteConsultaNFSe"

    NotaConsulta: Optional[TpNotasConsultaNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    RPSConsulta: Optional[TpRpssConsultaNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TpListaAlertas:
    """
    Alertas.
    """

    class Meta:
        name = "tpListaAlertas"

    Alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpListaErros:
    """
    Erros.
    """

    class Meta:
        name = "tpListaErros"

    Erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpListaNfseRps:
    """
    NFSE e seu respectivo RPS.
    """

    class Meta:
        name = "tpListaNFSeRPS"

    ChaveNFSeRPS: List[TpChaveNfeRps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpNfse:
    """
    Tipo que representa uma NFSe.

    :ivar NumeroNota: Número da Nota Fiscal
    :ivar DataProcessamento: Data que a Nota Fiscal foi Processada
    :ivar NumeroLote: Número do Lote
    :ivar CodigoVerificacao: Código de Verificacao
    :ivar Assinatura: Assinatura digital do RPS.
    :ivar InscricaoMunicipalPrestador: Informe a Inscrição Municipal do
        Prestador
    :ivar RazaoSocialPrestador: Informe a Razao Social do Prestador
    :ivar TipoRPS: Informe o Tipo do RPS emitido.
    :ivar SerieRPS: Informe a Série do RPS emitido.
    :ivar NumeroRPS: Informe o Número do RPS emitido.
    :ivar DataEmissaoRPS: Informe a Data de emissão do RPS.
    :ivar SituacaoRPS: Informe o Status do RPS.
    :ivar SerieRPSSubstituido: Informe a Série do RPS substituído.
    :ivar NumeroRPSSubstituido: Informe o Número do RPS substituído.
    :ivar NumeroNFSeSubstituida: Informe o Número da NFSe substituída.
    :ivar DataEmissaoNFSeSubstituida: Informe a Data de Emissão da NFSe
        substituída.
    :ivar SeriePrestacao: Série de prestação
    :ivar InscricaoMunicipalTomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município. Quando este campo for
        preenchido, seu conteúdo será considerado como prioritário com
        relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para
        identificar o Tomador e recuperar seus dados da base de dados da
        Prefeitura.
    :ivar CPFCNPJTomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar RazaoSocialTomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município.
    :ivar DocTomadorEstrangeiro: Informe o Documento de Identificação do
        tomador. Este campo é obrigatório apenas para tomadores
        estrageiros, ou seja quando no CidadeTomador que indica o Codigo
        SIAFI da cidade do tomador for informado 0009999
    :ivar TipoLogradouroTomador: Informe o Tipo do Logradouro do
        Endereço do Tomador.
    :ivar LogradouroTomador: Informe o Logradouro do Endereço do
        Tomador.
    :ivar NumeroEnderecoTomador: Informe o Número do Endereço do
        Tomador.
    :ivar ComplementoEnderecoTomador: Informe o Comlpemento do Endereço
        do Tomador.
    :ivar TipoBairroTomador: Informe o Tipo do Bairro do Endereço do
        Tomador.
    :ivar BairroTomador: Informe o Bairro do Endereço do Tomador.
    :ivar CidadeTomador: Informe a Cidade do Tomador.
    :ivar CidadeTomadorDescricao: Informe a Descricao Cidade do Tomador.
    :ivar CEPTomador: Informe o CEP do Tomador.
    :ivar EmailTomador: Informe o e-mail do tomador.
    :ivar CodigoAtividade: Informe o código da atividade do RPS. Este
        código deve pertencer à lista CNAE.
    :ivar AliquotaAtividade: Informe o valor da alíquota.
    :ivar TipoRecolhimento: Informe a retenção.
    :ivar MunicipioPrestacao: Informe o Município da Prestação do
        Serviço.
    :ivar MunicipioPrestacaoDescricao: Informe o Município da Prestação
        do Serviço.
    :ivar Operacao: Informe a Operação da Prestação do Serviço.
    :ivar Tributacao: Informe o tipo de tributação do RPS.
    :ivar ValorPIS: Informe o valor da retenção do PIS.
    :ivar ValorCOFINS: Informe o valor da retenção do COFINS.
    :ivar ValorINSS: Informe o valor da retenção do INSS.
    :ivar ValorIR: Informe o valor da retenção do IR.
    :ivar ValorCSLL: Informe o valor da retenção do CSLL.
    :ivar AliquotaPIS: Informe a Alíquota da retenção do PIS.
    :ivar AliquotaCOFINS: Informe a Alíquota da retenção do COFINS.
    :ivar AliquotaINSS: Informe a Alíquota da retenção do INSS.
    :ivar AliquotaIR: Informe a Alíquota da retenção do IR.
    :ivar AliquotaCSLL: Informe a Alíquota da retenção do CSLL.
    :ivar DescricaoRPS: Descrição da Nota.
    :ivar DDDPrestador: DDD do Prestador.
    :ivar TelefonePrestador: Telefone do Prestador.
    :ivar DDDTomador: DDD do Tomador.
    :ivar TelefoneTomador: Telefone do Tomador.
    :ivar MotCancelamento: Informe o Motivo do Cancelamento.
    :ivar CPFCNPJIntermediario: CPF/CNPJ do intermediário do serviço.
        Campo não é obrigatório, deve ser informado quando houver um
        intermediário entre o tomador e o prestador.
    :ivar Deducoes: Lista de Deduções.
    :ivar Itens: Lista de Itens.
    """

    class Meta:
        name = "tpNFSe"

    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataProcessamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    NumeroLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "format": "base64",
        },
    )
    InscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    RazaoSocialPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )
    TipoRPS: Optional[TpTipoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SerieRPS: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoRPS: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SituacaoRPS: Optional[TpSituacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SerieRPSSubstituido: Optional[TpSerieRpssubstituido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    NumeroRPSSubstituido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    NumeroNFSeSubstituida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoNFSeSubstituida: Optional[Union[XmlDateTime, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    SeriePrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    InscricaoMunicipalTomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{6,11}",
        },
    )
    CPFCNPJTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    RazaoSocialTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )
    DocTomadorEstrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
            "white_space": "preserve",
        },
    )
    TipoLogradouroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    LogradouroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    NumeroEnderecoTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
        },
    )
    ComplementoEnderecoTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        },
    )
    TipoBairroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    BairroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    CidadeTomador: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        },
    )
    CidadeTomadorDescricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    CEPTomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,8}",
        },
    )
    EmailTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 60,
            "white_space": "preserve",
        },
    )
    CodigoAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{9}",
        },
    )
    AliquotaAtividade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    TipoRecolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    MunicipioPrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        },
    )
    MunicipioPrestacaoDescricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        },
    )
    Operacao: Optional[TpOperacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Tributacao: Optional[TpTributacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ValorPIS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    AliquotaPIS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaCOFINS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaIR: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    DescricaoRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 1500,
            "white_space": "preserve",
        },
    )
    DDDPrestador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,3}",
        },
    )
    TelefonePrestador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_inclusive": 99999999,
        },
    )
    DDDTomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,3}",
        },
    )
    TelefoneTomador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_inclusive": 99999999,
        },
    )
    MotCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        },
    )
    CPFCNPJIntermediario: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    Deducoes: Optional[TpListaDeducoes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Itens: Optional[TpListaItens] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpRps:
    """
    Tipo que representa um RPS.

    :ivar Assinatura: Assinatura digital do RPS.
    :ivar InscricaoMunicipalPrestador: Informe a Inscrição Municipal do
        Prestador
    :ivar RazaoSocialPrestador: Informe a Razao Social do Prestador
    :ivar TipoRPS: Informe o Tipo do RPS emitido.
    :ivar SerieRPS: Informe a Série do RPS emitido.
    :ivar NumeroRPS: Informe o Número do RPS emitido.
    :ivar DataEmissaoRPS: Informe a Data de emissão do RPS.
    :ivar SituacaoRPS: Informe o Status do RPS.
    :ivar SerieRPSSubstituido: Informe a Série do RPS substituído.
    :ivar NumeroRPSSubstituido: Informe o Número do RPS substituído.
    :ivar NumeroNFSeSubstituida: Informe o Número da NFSe substituída.
    :ivar DataEmissaoNFSeSubstituida: Informe a Data de Emissão da NFSe
        substituída.
    :ivar SeriePrestacao: Informe o Documento de Prestação
    :ivar InscricaoMunicipalTomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município. Quando este campo for
        preenchido, seu conteúdo será considerado como prioritário com
        relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para
        identificar o Tomador e recuperar seus dados da base de dados da
        Prefeitura.
    :ivar CPFCNPJTomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar RazaoSocialTomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município.
    :ivar DocTomadorEstrangeiro: Informe o Documento de Identificação do
        tomador. Este campo é obrigatório apenas para tomadores
        estrageiros, ou seja quando no CidadeTomador que indica o Codigo
        SIAFI da cidade do tomador for informado 0009999
    :ivar TipoLogradouroTomador: Informe o Tipo do Logradouro do
        Endereço do Tomador.
    :ivar LogradouroTomador: Informe o Logradouro do Endereço do
        Tomador.
    :ivar NumeroEnderecoTomador: Informe o Número do Endereço do
        Tomador.
    :ivar ComplementoEnderecoTomador: Informe o Comlpemento do Endereço
        do Tomador.
    :ivar TipoBairroTomador: Informe o Tipo do Bairro do Endereço do
        Tomador.
    :ivar BairroTomador: Informe o Bairro do Endereço do Tomador.
    :ivar CidadeTomador: Informe a Cidade do Tomador.
    :ivar CidadeTomadorDescricao: Informe a Descricao da Cidade do
        Tomador.
    :ivar CEPTomador: Informe o CEP do Tomador.
    :ivar EmailTomador: Informe o e-mail do tomador.
    :ivar CodigoAtividade: Informe o código da atividade do RPS. Este
        código deve pertencer à lista CNAE.
    :ivar AliquotaAtividade: Informe o valor da alíquota.
    :ivar TipoRecolhimento: Informe a retenção.
    :ivar MunicipioPrestacao: Informe o Município da Prestação do
        Serviço.
    :ivar MunicipioPrestacaoDescricao: Informe o Município da Prestação
        do Serviço.
    :ivar Operacao: Informe a Operação da Prestação do Serviço.
    :ivar Tributacao: Informe o tipo de tributação do RPS.
    :ivar ValorPIS: Informe o valor da retenção do PIS.
    :ivar ValorCOFINS: Informe o valor da retenção do COFINS.
    :ivar ValorINSS: Informe o valor da retenção do INSS.
    :ivar ValorIR: Informe o valor da retenção do IR.
    :ivar ValorCSLL: Informe o valor da retenção do CSLL.
    :ivar AliquotaPIS: Informe a Alíquota da retenção do PIS.
    :ivar AliquotaCOFINS: Informe a Alíquota da retenção do COFINS.
    :ivar AliquotaINSS: Informe a Alíquota da retenção do INSS.
    :ivar AliquotaIR: Informe a Alíquota da retenção do IR.
    :ivar AliquotaCSLL: Informe a Alíquota da retenção do CSLL.
    :ivar DescricaoRPS: Descrição da Nota.
    :ivar DDDPrestador: DDD do Prestador.
    :ivar TelefonePrestador: Telefone do Prestador.
    :ivar DDDTomador: DDD do Tomador.
    :ivar TelefoneTomador: Telefone do Tomador.
    :ivar MotCancelamento: Informe o Motivo do Cancelamento.
    :ivar CPFCNPJIntermediario: Informe o CPF/CNPJ do intermediário do
        serviço. Campo não é obrigatório, deve ser informado quando
        houver um intermediário entre o tomador e o prestador.
    :ivar Deducoes: Lista de Deduções.
    :ivar Itens: Lista de Itens.
    :ivar Id:
    """

    class Meta:
        name = "tpRPS"

    Assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "format": "base64",
        },
    )
    InscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    RazaoSocialPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )
    TipoRPS: Optional[TpTipoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SerieRPS: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoRPS: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SituacaoRPS: Optional[TpSituacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    SerieRPSSubstituido: Optional[TpSerieRpssubstituido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    NumeroRPSSubstituido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    NumeroNFSeSubstituida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataEmissaoNFSeSubstituida: Optional[Union[XmlDate, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "white_space": "collapse",
        },
    )
    SeriePrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    InscricaoMunicipalTomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        },
    )
    CPFCNPJTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    RazaoSocialTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        },
    )
    DocTomadorEstrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
            "white_space": "preserve",
        },
    )
    TipoLogradouroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    LogradouroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    NumeroEnderecoTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
        },
    )
    ComplementoEnderecoTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        },
    )
    TipoBairroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        },
    )
    BairroTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    CidadeTomador: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        },
    )
    CidadeTomadorDescricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        },
    )
    CEPTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,8}",
        },
    )
    EmailTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 60,
            "white_space": "preserve",
        },
    )
    CodigoAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{9}",
        },
    )
    AliquotaAtividade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    TipoRecolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    MunicipioPrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        },
    )
    MunicipioPrestacaoDescricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        },
    )
    Operacao: Optional[TpOperacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Tributacao: Optional[TpTributacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ValorPIS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    ValorCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        },
    )
    AliquotaPIS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaCOFINS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaIR: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    AliquotaCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    DescricaoRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 1500,
            "white_space": "preserve",
        },
    )
    DDDPrestador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,3}",
        },
    )
    TelefonePrestador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": 99999999,
        },
    )
    DDDTomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,3}",
        },
    )
    TelefoneTomador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": 99999999,
        },
    )
    MotCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        },
    )
    CPFCNPJIntermediario: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        },
    )
    Deducoes: Optional[TpListaDeducoes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Itens: Optional[TpListaItens] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TpListaNfseConsultaNota:
    """
    Lista de NFSE consultada.
    """

    class Meta:
        name = "tpListaNFSeConsultaNota"

    Nota: List[TpNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TpLote:
    """
    Lote de RPS.
    """

    class Meta:
        name = "tpLote"

    RPS: List[TpRps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
