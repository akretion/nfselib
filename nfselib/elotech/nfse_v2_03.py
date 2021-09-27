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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    numero_alvara_construcao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroAlvaraConstrucao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    incorporacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Incorporacao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )


@dataclass
class TcDadosDeducao:
    class Meta:
        name = "tcDadosDeducao"

    tipo_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoDeducao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "pattern": r"M|S",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 14,
            "white_space": "collapse",
        }
    )
    numero_nota_fiscal_referencia: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNotaFiscalReferencia",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        }
    )
    valor_total_nota_fiscal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorTotalNotaFiscal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    percentual_adeduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PercentualADeduzir",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    valor_adeduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorADeduzir",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 2,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaPis",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoPis",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCofins",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoCofins",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaInss",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoInss",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaIr",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoIr",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCsll",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoCsll",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota_cpp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCpp",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    retido_cpp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoCpp",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    valor_cpp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCpp",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    retido_outras_retencoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetidoOutrasRetencoes",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    aliquota_tot_tributos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaTotTributos",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    val_tot_tributos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValTotTributos",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoRequerente:
    class Meta:
        name = "tcIdentificacaoRequerente"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": " ",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    senha: Optional[str] = field(
        default=None,
        metadata={
            "name": "Senha",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 6,
            "max_length": 30,
        }
    )
    homologa: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Homologa",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )


@dataclass
class TcItemServico:
    class Meta:
        name = "tcItemServico"

    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "collapse",
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    unidade: Optional[TsUnidade] = field(
        default=None,
        metadata={
            "name": "Unidade",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    tributavel: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tributavel",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Quantidade",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        }
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorUnitario",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        }
    )
    valor_desconto: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDesconto",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    valor_liquido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquido",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    dados_deducao: Optional[TcDadosDeducao] = field(
        default=None,
        metadata={
            "name": "DadosDeducao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )
    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "required": True,
            "total_digits": 15,
        }
    )


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "required": True,
        }
    )
    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarNfseServicoPrestadoEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
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
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    mensagem_retorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class NfseSubstituicao(TcSubstituicaoNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    identificacao_intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "IdentificacaoIntermediario",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    responsavel_retencao: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponsavelRetencao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    codigo_nbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoNbs",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    exigibilidade_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExigibilidadeISS",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6|7",
        }
    )
    municipio_incidencia: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioIncidencia",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    numero_processo: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        }
    )
    lista_itens_servico: Optional["TcDadosServico.ListaItensServico"] = field(
        default=None,
        metadata={
            "name": "ListaItensServico",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )

    @dataclass
    class ListaItensServico:
        item_servico: List[TcItemServico] = field(
            default_factory=list,
            metadata={
                "name": "ItemServico",
                "type": "Element",
                "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
                "min_occurs": 1,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    nif_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "NifTomador",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 0,
            "max_length": 40,
            "white_space": "collapse",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoEstadual",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 20,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    chave_acesso: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveAcesso",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{32}",
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    intermediario: Optional[TcDadosIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "pattern": r"1|2|3|4|5|6|7",
        }
    )
    incentivo_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivoFiscal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )


@dataclass
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )
    substituicao_nfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "required": True,
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


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao_cancelamento: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "ConfirmacaoCancelamento",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    declaracao_prestacao_servico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "DeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    chave_acesso: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveAcesso",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{32}",
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
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
                "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )
    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    identificacao_requerente: Optional[TcIdentificacaoRequerente] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRequerente",
            "type": "Element",
            "required": True,
        }
    )
    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class NfseCancelamento(TcCancelamentoNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "required": True,
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    tc_ret_cancelamento: Optional[TcRetCancelamento] = field(
        default=None,
        metadata={
            "name": "tcRetCancelamento",
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
        }
    )
    nfse_cancelamento: Optional[NfseCancelamento] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    nfse_substituicao: Optional[NfseSubstituicao] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
        }
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xml",
            "type": "Element",
            "namespace": "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd",
            "min_length": 1,
            "white_space": "collapse",
        }
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "required": True,
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
            "required": True,
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
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
        namespace = "http://shad.elotech.com.br/schemas/iss/nfse_v2_03.xsd"

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
            lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
                default=None,
                metadata={
                    "name": "ListaMensagemRetorno",
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
