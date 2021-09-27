from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfselib.goiania.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "length": 2,
        }
    )
    codigo_pais: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "total_digits": 7,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "length": 8,
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "pattern": r"1|2|3",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

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
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2",
        }
    )
    responsavel_retencao: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponsavelRetencao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2",
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "total_digits": 7,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    exigibilidade_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExigibilidadeISS",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2|3|4|5|6|7",
        }
    )
    municipio_incidencia: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioIncidencia",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "total_digits": 7,
        }
    )
    numero_processo: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "required": True,
            "max_length": 50,
        }
    )


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    faixa: Optional["ConsultarNfseFaixaEnvio.Faixa"] = field(
        default=None,
        metadata={
            "name": "Faixa",
            "type": "Element",
            "required": True,
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class Faixa:
        numero_nfse_inicial: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseInicial",
                "type": "Element",
                "required": True,
                "total_digits": 15,
            }
        )
        numero_nfse_final: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseFinal",
                "type": "Element",
                "total_digits": 15,
            }
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

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
class ConsultarNfseServicoPrestadoEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    periodo_emissao: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class PeriodoEmissao:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class PeriodoCompetencia:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class ConsultarNfseServicoTomadoEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    consulente: Optional[TcIdentificacaoConsulente] = field(
        default=None,
        metadata={
            "name": "Consulente",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    periodo_emissao: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class PeriodoEmissao:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class PeriodoCompetencia:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
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
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    intermediario: Optional[TcDadosIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2",
        }
    )
    incentivo_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivoFiscal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "pattern": r"1|2",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    rps: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    substituicao_nfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
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
    class SubstituicaoNfse:
        pedido: Optional[TcPedidoCancelamento] = field(
            default=None,
            metadata={
                "name": "Pedido",
                "type": "Element",
                "required": True,
            }
        )
        rps: Optional[TcDeclaracaoPrestacaoServico] = field(
            default=None,
            metadata={
                "name": "Rps",
                "type": "Element",
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
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    endereco_prestador_servico: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "EnderecoPrestadorServico",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    declaracao_prestacao_servico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "DeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
        rps: Optional[TcDeclaracaoPrestacaoServico] = field(
            default=None,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
                "required": True,
            }
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class RetCancelamento:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    nfse_cancelamento: List[TcCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
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
class CancelarNfseResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    ret_cancelamento: Optional[RetCancelamento] = field(
        default=None,
        metadata={
            "name": "RetCancelamento",
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
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd",
        }
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "required": True,
            "pattern": r"1|2|3|4",
        }
    )
    lista_nfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
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
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemAlertaRetorno",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lista_nfse: Optional["ConsultarNfseFaixaResposta.ListaNfse"] = field(
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    comp_nfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "required": True,
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lista_nfse: Optional["ConsultarNfseServicoPrestadoResposta.ListaNfse"] = field(
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseServicoTomadoResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lista_nfse: Optional["ConsultarNfseServicoTomadoResposta.ListaNfse"] = field(
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class EnviarLoteRpsSincronoResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        }
    )
    lista_nfse: Optional["EnviarLoteRpsSincronoResposta.ListaNfse"] = field(
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
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
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


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    lista_nfse: Optional["GerarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
            "required": True,
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "required": True,
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


@dataclass
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://nfse.goiania.go.gov.br/xsd/nfse_gyn_v02.xsd"

    ret_substituicao: Optional["SubstituirNfseResposta.RetSubstituicao"] = field(
        default=None,
        metadata={
            "name": "RetSubstituicao",
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
    class RetSubstituicao:
        nfse_substituida: Optional["SubstituirNfseResposta.RetSubstituicao.NfseSubstituida"] = field(
            default=None,
            metadata={
                "name": "NfseSubstituida",
                "type": "Element",
                "required": True,
            }
        )
        nfse_substituidora: Optional["SubstituirNfseResposta.RetSubstituicao.NfseSubstituidora"] = field(
            default=None,
            metadata={
                "name": "NfseSubstituidora",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class NfseSubstituida:
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

        @dataclass
        class NfseSubstituidora:
            comp_nfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )
