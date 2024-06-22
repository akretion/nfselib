from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    versaoDados: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        },
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"

    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 14,
            "white_space": "collapse",
        },
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"

    CodigoObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    NumeroAlvaraConstrucao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    Incorporacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )


@dataclass
class TcDadosDeducao:
    class Meta:
        name = "tcDadosDeducao"

    TipoDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "pattern": r"M|S",
        },
    )
    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 14,
            "white_space": "collapse",
        },
    )
    NumeroNotaFiscalReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        },
    )
    ValorTotalNotaFiscal: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    PercentualADeduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    ValorADeduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    Endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 2,
        },
    )
    CodigoPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 4,
            "white_space": "collapse",
        },
    )
    Cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 8,
        },
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "length": 2,
        },
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Tipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4",
        },
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    NfseSubstituidora: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        },
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )
    Correcao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcValoresDeclaracaoServico:
    class Meta:
        name = "tcValoresDeclaracaoServico"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoInss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoIr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoCsll: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    AliquotaCpp: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    RetidoCpp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    ValorCpp: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    RetidoOutrasRetencoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    AliquotaTotTributos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    ValTotTributos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )


@dataclass
class TcValoresNfse:
    class Meta:
        name = "tcValoresNfse"

    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )


class TsUnidade(Enum):
    """Unidade Media (

    UN - Unidade;
    HS - Horas;
    M2 - Metros Quadrados
    )
    """

    UN = "UN"
    HS = "HS"
    M2 = "M2"


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TcIdentificacaoIntermediario:
    class Meta:
        name = "tcIdentificacaoIntermediario"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoRequerente:
    class Meta:
        name = "tcIdentificacaoRequerente"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    SPACE: Optional[str] = field(
        default=None,
        metadata={
            "name": " ",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Senha: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 6,
            "max_length": 30,
        },
    )
    Homologa: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )


@dataclass
class TcItemServico:
    class Meta:
        name = "tcItemServico"

    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "collapse",
        },
    )
    CodigoCnae: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Unidade: Optional[TsUnidade] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    Tributavel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    Quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    ValorUnitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    ValorDesconto: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    ValorLiquido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    DadosDeducao: Optional[TcDadosDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )


@dataclass
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    SubstituicaoNfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "total_digits": 15,
        },
    )


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Faixa: Optional["ConsultarNfseFaixaEnvio.Faixa"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Pagina: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )

    @dataclass
    class Faixa:
        NumeroNfseInicial: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "total_digits": 15,
            },
        )
        NumeroNfseFinal: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "total_digits": 15,
            },
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    PeriodoEmissao: Optional[
        "ConsultarNfseServicoPrestadoEnvio.PeriodoEmissao"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    PeriodoCompetencia: Optional[
        "ConsultarNfseServicoPrestadoEnvio.PeriodoCompetencia"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Pagina: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )

    @dataclass
    class PeriodoEmissao:
        DataInicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DataFinal: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class PeriodoCompetencia:
        DataInicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DataFinal: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class ConsultarNfseServicoTomadoEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    PeriodoEmissao: Optional[
        "ConsultarNfseServicoTomadoEnvio.PeriodoEmissao"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    PeriodoCompetencia: Optional[
        "ConsultarNfseServicoTomadoEnvio.PeriodoCompetencia"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Pagina: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )

    @dataclass
    class PeriodoEmissao:
        DataInicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DataFinal: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class PeriodoCompetencia:
        DataInicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DataFinal: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    DataRecebimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    MensagemRetorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class NfseSubstituicao(TcSubstituicaoNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    IdentificacaoIntermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    Valores: Optional[TcValoresDeclaracaoServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    ResponsavelRetencao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    CodigoNbs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    CodigoPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 4,
            "white_space": "collapse",
        },
    )
    ExigibilidadeISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6|7",
        },
    )
    MunicipioIncidencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    NumeroProcesso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    ListaItensServico: Optional["TcDadosServico.ListaItensServico"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )

    @dataclass
    class ListaItensServico:
        ItemServico: List[TcItemServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    NifTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 0,
            "max_length": 40,
            "white_space": "collapse",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    InscricaoEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    IdentificacaoNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    ChaveAcesso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{32}",
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5",
        },
    )


@dataclass
class TcInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcInfDeclaracaoPrestacaoServico"

    Rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    Competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    Intermediario: Optional[TcDadosIntermediario] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    ConstrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2|3|4|5|6|7",
        },
    )
    IncentivoFiscal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    InfPedidoCancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )


@dataclass
class TcDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcDeclaracaoPrestacaoServico"

    InfDeclaracaoPrestacaoServico: Optional[
        TcInfDeclaracaoPrestacaoServico
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )


@dataclass
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    SubstituicaoNfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class SubstituicaoNfse:
        Pedido: Optional[TcPedidoCancelamento] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Rps: Optional[TcDeclaracaoPrestacaoServico] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    ConfirmacaoCancelamento: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )
    DataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    NfseSubstituida: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    ValoresNfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    ValorCredito: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    DeclaracaoPrestacaoServico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    ChaveAcesso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{32}",
        },
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    QuantidadeRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    ListaRps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )

    @dataclass
    class ListaRps:
        Rps: List[TcDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    IdentificacaoRequerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NfseCancelamento(TcCancelamentoNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    InfNfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )


@dataclass
class TcRetCancelamento:
    class Meta:
        name = "tcRetCancelamento"
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    tcRetCancelamento: Optional[TcRetCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class Nfse(TcNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[Nfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        },
    )
    nfseCancelamento: Optional[NfseCancelamento] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    nfseSubstituicao: Optional[NfseSubstituicao] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        },
    )
    Xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "white_space": "collapse",
        },
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"1|2|3|4",
        },
    )
    ListaNfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
    listaMensagemRetornoLote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        listaMensagemAlertaRetorno: Optional[ListaMensagemAlertaRetorno] = (
            field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                },
            )
        )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    ListaNfse: Optional["ConsultarNfseFaixaResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        ProximaPagina: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            },
        )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    compNfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    ListaNfse: Optional["ConsultarNfseServicoPrestadoResposta.ListaNfse"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        ProximaPagina: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            },
        )


@dataclass
class ConsultarNfseServicoTomadoResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    ListaNfse: Optional["ConsultarNfseServicoTomadoResposta.ListaNfse"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        ProximaPagina: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            },
        )


@dataclass
class EnviarLoteRpsSincronoResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "total_digits": 15,
        },
    )
    DataRecebimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ListaNfse: Optional["EnviarLoteRpsSincronoResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
    listaMensagemRetornoLote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        listaMensagemAlertaRetorno: Optional[ListaMensagemAlertaRetorno] = (
            field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                },
            )
        )


@dataclass
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    RetSubstituicao: Optional["SubstituirNfseResposta.RetSubstituicao"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )

    @dataclass
    class RetSubstituicao:
        NfseSubstituida: Optional[
            "SubstituirNfseResposta.RetSubstituicao.NfseSubstituida"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        NfseSubstituidora: Optional[
            "SubstituirNfseResposta.RetSubstituicao.NfseSubstituidora"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class NfseSubstituida:
            compNfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                },
            )
            listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
                default=None,
                metadata={
                    "name": "ListaMensagemRetorno",
                    "type": "Element",
                },
            )

        @dataclass
        class NfseSubstituidora:
            compNfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                },
            )
