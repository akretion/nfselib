from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from nfselib.ginfes.bindings.xmldsig_core_schema_v02 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/tipos_v03.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "length": 11,
            "white_space": "collapse",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "total_digits": 7,
            "white_space": "collapse",
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "length": 2,
            "white_space": "collapse",
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "total_digits": 8,
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 7,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 7,
            "white_space": "collapse",
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "length": 2,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2|3",
        },
    )


@dataclass
class TcInfConfirmacaoCancelamento:
    class Meta:
        name = "tcInfConfirmacaoCancelamento"

    Sucesso: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
            "white_space": "collapse",
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.ginfes.com.br/tipos_v03.xsd"

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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "total_digits": 7,
            "white_space": "collapse",
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 7,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    InfConfirmacaoCancelamento: Optional[TcInfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    DataEmissaoRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    NaturezaOperacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "white_space": "collapse",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    Competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    NfseSubstituida: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    ValorCredito: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
            "white_space": "collapse",
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    ConstrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "white_space": "collapse",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"1|2",
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            },
        )
    )
    ConstrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
    nfseSubstituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
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
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
            "total_digits": 4,
            "white_space": "collapse",
        },
    )
    ListaRps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
        },
    )

    @dataclass
    class ListaRps:
        Rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
                "min_occurs": 1,
            },
        )
