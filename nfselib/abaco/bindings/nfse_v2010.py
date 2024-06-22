from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from nfselib.abaco.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "length": 2,
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "total_digits": 8,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "length": 2,
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2|3",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 15,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
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
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
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
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    CodigoCnae: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "total_digits": 7,
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 7,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
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
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
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
    PeriodoEmissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
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
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
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
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
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
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
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
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    DataHoraCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    DataEmissaoRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    NaturezaOperacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "collapse",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    Competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    NfseSubstituida: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "total_digits": 15,
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    ValorCredito: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    ContrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "collapse",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
    )
    ContrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "max_occurs": 2,
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
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
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )
    nfseSubstituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            "required": True,
        },
    )
    ListaRps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
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
    class ListaRps:
        Rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

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
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
