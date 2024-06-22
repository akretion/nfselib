from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe/tipos"


@dataclass
class TpCpfcnpj:
    """
    Tipo que representa um CPF/CNPJ.
    """

    class Meta:
        name = "tpCPFCNPJ"

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
    Chave de identificação da NFS-e.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar NumeroNFe: Número da NFS-e.
    :ivar CodigoVerificacao: Código de verificação da NFS-e.
    """

    class Meta:
        name = "tpChaveNFe"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        },
    )
    NumeroNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 8,
            "max_length": 8,
            "white_space": "collapse",
        },
    )


@dataclass
class TpChaveRps:
    """
    Tipo que define a chave identificadora de um RPS.

    :ivar InscricaoPrestador: Inscrição municipal do prestador de
        serviços.
    :ivar SerieRPS: Série do RPS.
    :ivar NumeroRPS: Número do RPS.
    """

    class Meta:
        name = "tpChaveRPS"

    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        },
    )
    SerieRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    NumeroRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )


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
            "max_length": 3,
            "white_space": "collapse",
        },
    )
    Logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 50,
            "white_space": "collapse",
        },
    )
    NumeroEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    ComplementoEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    Cidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
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
            "pattern": r"[0-9]{7,8}",
        },
    )


class TpOpcaoSimples(Enum):
    """
    Tipo referente às possíveis opções de escolha pelo Simples.

    :cvar VALUE_0: Não-optante pelo Simples Federal nem Municipal.
    :cvar VALUE_1: Optante pelo Simples Federal (Alíquota de 1,0%).
    :cvar VALUE_2: Optante pelo Simples Federal (Alíquota de 0,5%).
    :cvar VALUE_3: Optante pelo Simples Municipal.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TpStatusNfe(Enum):
    """
    Tipo referente aos possíveis status de NFS-e.

    :cvar N: Normal.
    :cvar C: Cancelada.
    :cvar E: Extraviada.
    """

    N = "N"
    C = "C"
    E = "E"


class TpTipoRps(Enum):
    """
    Tipo referente aos possíveis tipos de RPS.

    :cvar RPS: Recibo Provisório de Serviços.
    :cvar RPS_M: Recibo Provisório de Serviços proveniente de Nota
        Fiscal Conjugada (Mista).
    :cvar RPS_C: Cupom.
    """

    RPS = "RPS"
    RPS_M = "RPS-M"
    RPS_C = "RPS-C"


@dataclass
class TpChaveNfeRps:
    """
    Tipo que representa a chave de uma NFS-e e a Chave do RPS que a mesma
    substitui.

    :ivar ChaveNFe: Chave da NFS-e gerada.
    :ivar ChaveRPS: Chave do RPS substituído.
    """

    class Meta:
        name = "tpChaveNFeRPS"

    ChaveNFe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ChaveRPS: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "pattern": r"[0-9]{1,12}",
        },
    )
    InscricaoPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        },
    )
    CPFCNPJRemetente: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
    QtdNotasProcessadas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
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


@dataclass
class TpNfe:
    """
    Tipo que representa uma NFS-e.

    :ivar Assinatura: Assinatura digital da NFS-e.
    :ivar ChaveNFe: Chave de identificação da NFS-e.
    :ivar DataEmissaoNFe: Data de emissão da NFS-e
    :ivar NumeroLote: Número de lote gerador da NFS-e.
    :ivar ChaveRPS: Chave do RPS que originou a NFS-e.
    :ivar TipoRPS: Tipo do RPS emitido.
    :ivar DataEmissaoRPS: Data de emissão do RPS que originou a NFS-e.
    :ivar CPFCNPJPrestador: CPF/CNPJ do Prestador do serviço.
    :ivar RazaoSocialPrestador: Nome/Razão Social do Prestador.
    :ivar EnderecoPrestador: Endereço do Prestador.
    :ivar EmailPrestador: E-mail do Prestador.
    :ivar StatusNFe: Status da NFS-e.
    :ivar DataCancelamento: Data de cancelamento da NFS-e.
    :ivar TributacaoNFe: Tributação da NFS-e.
    :ivar OpcaoSimples: Opção pelo Simples.
    :ivar NumeroGuia: Número da guia vinculada a NFS-e.
    :ivar DataQuitacaoGuia: Data de quitação da guia vinculada a NFS-e.
    :ivar ValorServicos: Valor dos serviços prestados.
    :ivar ValorDeducoes: Valor das deduções.
    :ivar ValorPIS: Valor da retenção do PIS.
    :ivar ValorCOFINS: Valor da retenção do COFINS.
    :ivar ValorINSS: Valor da retenção do INSS.
    :ivar ValorIR: Valor da retenção do IR.
    :ivar ValorCSLL: Valor da retenção do CSLL.
    :ivar CodigoServico: Código do serviço.
    :ivar AliquotaServicos: Valor da alíquota.
    :ivar ValorISS: Valor do ISS.
    :ivar ValorCredito: Valor do crédito gerado.
    :ivar ISSRetido: Retenção do ISS.
    :ivar CPFCNPJTomador: CPF/CNPJ do tomador do serviço.
    :ivar InscricaoMunicipalTomador: Inscrição Municipal do Tomador.
    :ivar InscricaoEstadualTomador: Inscrição Estadual do tomador.
    :ivar RazaoSocialTomador: Nome/Razão Social do tomador.
    :ivar EnderecoTomador: Endereço do tomador.
    :ivar EmailTomador: E-mail do tomador.
    :ivar CPFCNPJIntermediario: CNPJ do intermediário de serviço.
    :ivar InscricaoMunicipalIntermediario: Inscrição Municipal do
        intermediário de serviço.
    :ivar ISSRetidoIntermediario: Retenção do ISS pelo intermediário de
        serviço.
    :ivar EmailIntermediario: E-mail do intermediário de serviço.
    :ivar Discriminacao: Descrição dos serviços.
    :ivar ValorCargaTributaria: Valor da carga tributária total em R$.
    :ivar PercentualCargaTributaria: Valor percentual da carga
        tributária.
    :ivar FonteCargaTributaria: Fonte de informação da carga tributária.
    :ivar CodigoCEI: Código do CEI – Cadastro específico do INSS.
    :ivar MatriculaObra: Código que representa a matrícula da obra no
        sistema de cadastro de obras.
    :ivar MunicipioPrestacao: Código da cidade do município da prestação
        do serviço.
    :ivar NumeroEncapsulamento: Código que representa o número do
        encapsulamento.
    :ivar ValorTotalRecebido: Informe o valor total recebido.
    """

    class Meta:
        name = "tpNFe"

    Assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "format": "base64",
        },
    )
    ChaveNFe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    DataEmissaoNFe: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    ChaveRPS: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    TipoRPS: Optional[TpTipoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    DataEmissaoRPS: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    CPFCNPJPrestador: Optional[TpCpfcnpj] = field(
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
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    EnderecoPrestador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    EmailPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    StatusNFe: Optional[TpStatusNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    DataCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    TributacaoNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "white_space": "collapse",
        },
    )
    OpcaoSimples: Optional[TpOpcaoSimples] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NumeroGuia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    DataQuitacaoGuia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ValorServicos: Optional[str] = field(
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
    ValorDeducoes: Optional[str] = field(
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
    CodigoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        },
    )
    AliquotaServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    ValorISS: Optional[str] = field(
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
    ValorCredito: Optional[str] = field(
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
    ISSRetido: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    CPFCNPJTomador: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    InscricaoMunicipalTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        },
    )
    InscricaoEstadualTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,19}",
        },
    )
    RazaoSocialTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    EnderecoTomador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    EmailTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    CPFCNPJIntermediario: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    InscricaoMunicipalIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        },
    )
    ISSRetidoIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    EmailIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    ValorCargaTributaria: Optional[str] = field(
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
    PercentualCargaTributaria: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 7,
            "fraction_digits": 4,
        },
    )
    FonteCargaTributaria: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    CodigoCEI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    MatriculaObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    MunicipioPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
        },
    )
    NumeroEncapsulamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    ValorTotalRecebido: Optional[str] = field(
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


@dataclass
class TpRps:
    """
    Tipo que representa um RPS.

    :ivar Assinatura: Assinatura digital do RPS.
    :ivar ChaveRPS: Informe a chave do RPS emitido.
    :ivar TipoRPS: Informe o Tipo do RPS emitido.
    :ivar DataEmissao: Informe a Data de emissão do RPS.
    :ivar StatusRPS: Informe o Status do RPS.
    :ivar TributacaoRPS: Informe o tipo de tributação do RPS.
    :ivar ValorServicos: Informe o valor dos serviços prestados.
    :ivar ValorDeducoes: Informe o valor das deduções.
    :ivar ValorPIS: Informe o valor da retenção do PIS.
    :ivar ValorCOFINS: Informe o valor da retenção do COFINS.
    :ivar ValorINSS: Informe o valor da retenção do INSS.
    :ivar ValorIR: Informe o valor da retenção do IR.
    :ivar ValorCSLL: Informe o valor da retenção do CSLL.
    :ivar CodigoServico: Informe o código do serviço do RPS. Este código
        deve pertencer à lista de serviços.
    :ivar AliquotaServicos: Informe o valor da alíquota. Obs. O conteúdo
        deste campo será ignorado caso a tributação ocorra no município
        (Situação do RPS = T ).
    :ivar ISSRetido: Informe a retenção.
    :ivar CPFCNPJTomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar InscricaoMunicipalTomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município de São Paulo (CCM). Quando
        este campo for preenchido, seu conteúdo será considerado como
        prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo
        utilizado para identificar o Tomador e recuperar seus dados da
        base de dados da Prefeitura.
    :ivar InscricaoEstadualTomador: Informe a inscrição estadual do
        tomador. Este campo será ignorado caso seja fornecido um
        CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao
        município de São Paulo.
    :ivar RazaoSocialTomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município de São
        Paulo.
    :ivar EnderecoTomador: Informe o endereço do tomador. Os campos do
        endereço são obrigatórios apenas para tomadores pessoa jurídica
        (CNPJ informado). O conteúdo destes campos será ignorado caso
        seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador
        pertença ao município de São Paulo.
    :ivar EmailTomador: Informe o e-mail do tomador.
    :ivar CPFCNPJIntermediario: CNPJ do intermediário de serviço.
    :ivar InscricaoMunicipalIntermediario: Inscrição Municipal do
        intermediário de serviço.
    :ivar ISSRetidoIntermediario: Retenção do ISS pelo intermediário de
        serviço.
    :ivar EmailIntermediario: E-mail do intermediário de serviço.
    :ivar Discriminacao: Informe a discriminação dos serviços.
    :ivar ValorCargaTributaria: Valor da carga tributária total em R$.
    :ivar PercentualCargaTributaria: Valor percentual da carga
        tributária.
    :ivar FonteCargaTributaria: Fonte de informação da carga tributária.
    :ivar CodigoCEI: Código do CEI – Cadastro específico do INSS.
    :ivar MatriculaObra: Código que representa a matrícula da obra no
        sistema de cadastro de obras.
    :ivar MunicipioPrestacao: Código da cidade do município da prestação
        do serviço.
    :ivar NumeroEncapsulamento: Código que representa o número do
        encapsulamento da obra.
    :ivar ValorTotalRecebido: Informe o valor total recebido.
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
    ChaveRPS: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
    DataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    StatusRPS: Optional[TpStatusNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    TributacaoRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "white_space": "collapse",
        },
    )
    ValorServicos: Optional[str] = field(
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
    ValorDeducoes: Optional[str] = field(
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
    CodigoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        },
    )
    AliquotaServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    ISSRetido: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    CPFCNPJTomador: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    InscricaoMunicipalTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        },
    )
    InscricaoEstadualTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,19}",
        },
    )
    RazaoSocialTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    EnderecoTomador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    EmailTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    CPFCNPJIntermediario: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    InscricaoMunicipalIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        },
    )
    ISSRetidoIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    EmailIntermediario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    ValorCargaTributaria: Optional[str] = field(
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
    PercentualCargaTributaria: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 7,
            "fraction_digits": 4,
        },
    )
    FonteCargaTributaria: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    CodigoCEI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    MatriculaObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    MunicipioPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
        },
    )
    NumeroEncapsulamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        },
    )
    ValorTotalRecebido: Optional[str] = field(
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
