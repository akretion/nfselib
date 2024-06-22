from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

__NAMESPACE__ = "http://www.publica.inf.br"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 14,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 2,
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "total_digits": 8,
        },
    )
    CodigoPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 4,
        },
    )
    Municipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 7,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Tipo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    NfseSubstituidora: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcParcelas:
    class Meta:
        name = "tcParcelas"

    condicao: Optional[int] = field(
        default=None,
        metadata={
            "name": "Condicao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    Parcela: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    Valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DataVencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.publica.inf.br"

    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TcCondicoesPagamentos:
    class Meta:
        name = "tcCondicoesPagamentos"

    Parcelas: List[TcParcelas] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    Valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
        },
    )
    InformacoesComplementares: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 7,
        },
    )
    CodigoPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"

    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    MotivoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "max_length": 255,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 50,
        },
    )


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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

    @dataclass
    class Faixa:
        NumeroNfseInicial: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
            },
        )
        NumeroNfseFinal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
            },
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 50,
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 10,
        },
    )
    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"1|2|3|4",
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
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 10,
        },
    )
    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
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
class TcConsultaNfseRecebida:
    class Meta:
        name = "tcConsultaNfseRecebida"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    DataNfse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    DataRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultaNfseRecebidaEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    ConsultaNfseRecebida: Optional[TcConsultaNfseRecebida] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class TcCartaCorrecao:
    class Meta:
        name = "tcCartaCorrecao"

    NumeroCartaCorrecao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        },
    )
    Oficial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    DataDeclaracao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
            },
        )
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    DataHoraCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    DataEmissaoRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    Competencia: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    NfseSubstituida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    CondicaoPagamento: Optional[TcCondicoesPagamentos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcInfPedidoCartaCorrecao:
    class Meta:
        name = "tcInfPedidoCartaCorrecao"

    IdentificacaoNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
            },
        )
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    Competencia: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
            },
        )
    )
    CondicaoPagamento: Optional[TcCondicoesPagamentos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    Confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    InfNfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )


@dataclass
class TcPedidoCartaCorrecao:
    class Meta:
        name = "tcPedidoCartaCorrecao"

    InfPedidoCartaCorrecao: Optional[TcInfPedidoCartaCorrecao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"

    InfRps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Cancelamento: Optional[TcCancelamentoNfse] = field(
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
class CartaCorrecaoNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Pedido: Optional[TcPedidoCartaCorrecao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    Rps: Optional[TcRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    SubstituicaoNfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
        Rps: Optional[TcRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "max_length": 255,
            },
        )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    nfseSubstituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )
    ListaCorrecao: Optional["TcCompNfse.ListaCorrecao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        },
    )

    @dataclass
    class ListaCorrecao:
        CartaCorrecao: List[TcCartaCorrecao] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    QuantidadeRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    ListaRps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
        Rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
                "min_occurs": 1,
            },
        )


@dataclass
class CartaCorrecaoNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    compNfse: Optional[TcCompNfse] = field(
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
class ConsultaNfseRecebidaResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    ListaNfse: Optional["ConsultaNfseRecebidaResposta.ListaNfse"] = field(
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
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            },
        )


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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

    @dataclass
    class ListaNfse:
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            },
        )


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
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
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            },
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    ListaNfse: Optional["GerarNfseResposta.ListaNfse"] = field(
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
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            },
        )


@dataclass
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
            compNfse: Optional[TcCompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                },
            )

        @dataclass
        class NfseSubstituidora:
            compNfse: Optional[TcCompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                },
            )
