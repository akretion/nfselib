from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.megasoft.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "length": 8,
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Id: Optional[str] = field(
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Deducao: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    InfAdicional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )


@dataclass
class TcIdentificacaoConsulente:
    class Meta:
        name = "tcIdentificacaoConsulente"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    InscricaoEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
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
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    MensagemRetorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    IdentificacaoIntermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "pattern": r"1|2|3|4|5",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcNfseMega:
    class Meta:
        name = "tcNfseMega"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    ValoresNfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    CodigoTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
class TcListaNfseMega:
    class Meta:
        name = "tcListaNfseMega"

    nfse: List[TcNfseMega] = field(
        default_factory=list,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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

    Confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        },
    )


@dataclass
class TcGeraNfseMega:
    class Meta:
        name = "tcGeraNfseMega"

    ListaNfse: Optional[TcListaNfseMega] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    ValoresNfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    DeclaracaoPrestacaoServico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    QuantidadeRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    ListaRps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
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
        Rps: List[TcDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class NfseGerada(TcGeraNfseMega):
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    InfNfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
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

    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
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
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        },
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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
class GerarNfseResposta:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

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
        compNfse: Optional[CompNfse] = field(
            default=None,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "required": True,
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
