from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.megasoft.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    versao_dados: Optional[str] = field(
        default=None,
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        }
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "length": 14,
            "white_space": "collapse",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "length": 8,
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "total_digits": 7,
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    nfse_substituidora: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcValoresDeclaracaoServico:
    class Meta:
        name = "tcValoresDeclaracaoServico"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class TcValoresNfse:
    class Meta:
        name = "tcValoresNfse"

    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    deducao: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Deducao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    valores: Optional[TcValoresDeclaracaoServico] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    inf_adicional: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfAdicional",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )


@dataclass
class TcIdentificacaoConsulente:
    class Meta:
        name = "tcIdentificacaoConsulente"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoIntermediario:
    class Meta:
        name = "tcIdentificacaoIntermediario"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 7,
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoEstadual",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    substituicao_nfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    mensagem_retorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    identificacao_intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "IdentificacaoIntermediario",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "pattern": r"1|2|3|4|5",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcInfDeclaracaoPrestacaoServico"

    rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcNfseMega:
    class Meta:
        name = "tcNfseMega"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    valores_nfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "name": "ValoresNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    codigo_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcDeclaracaoPrestacaoServico"

    inf_declaracao_prestacao_servico: Optional[TcInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "InfDeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
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
        }
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    rps: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcGeraNfseMega:
    class Meta:
        name = "tcGeraNfseMega"

    lista_nfse: Optional[TcListaNfseMega] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    valores_nfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "name": "ValoresNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    declaracao_prestacao_servico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "DeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )

    @dataclass
    class ListaRps:
        rps: List[TcDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class NfseGerada(TcGeraNfseMega):
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcRetCancelamento:
    class Meta:
        name = "tcRetCancelamento"

    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd",
            "required": True,
        }
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
        }
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    comp_nfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://megasoftarrecadanet.com.br/xsd/nfse_v01.xsd"

    lista_nfse: Optional["GerarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: Optional[CompNfse] = field(
            default=None,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "required": True,
            }
        )
        lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemAlertaRetorno",
                "type": "Element",
            }
        )
