from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.el.com.br/nfse/xsd/el-nfse.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    logradouro_tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogradouroTipo",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    logradouro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Logradouro",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 130,
            "white_space": "collapse",
        }
    )
    logradouro_numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogradouroNumero",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    logradouro_complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogradouroComplemento",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
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
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 70,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "Municipio",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "length": 2,
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "total_digits": 10,
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"

    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        }
    )
    cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )
    indicacao_cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicacaoCpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )
    indicacao_cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicacaoCpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 11,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 0,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )
    indicacao_cpf_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicacaoCpfCnpj",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcRpsSubstituido:
    class Meta:
        name = "tcRpsSubstituido"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        }
    )


@dataclass
class TcServico:
    class Meta:
        name = "tcServico"

    codigo_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "max_length": 10,
        }
    )
    codigo_servico116: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoServico116",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    codigo_servico_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoServicoMunicipal",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Quantidade",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0.01"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    unidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unidade",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "max_length": 20,
        }
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    valor_servico: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServico",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_issqn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssqn",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_desconto: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDesconto",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    numero_alvara: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroAlvara",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorOutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_iss_retido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    outros_descontos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrosDescontos",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
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
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 2,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 2,
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
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
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcServicos:
    class Meta:
        name = "tcServicos"

    servico: List[TcServico] = field(
        default_factory=list,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        }
    )
    local_prestacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalPrestacao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    dados_prestador: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "DadosPrestador",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    dados_tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "DadosTomador",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    identificacao_intermediario: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IdentificacaoIntermediario",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        }
    )
    servicos: Optional[TcServicos] = field(
        default=None,
        metadata={
            "name": "Servicos",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    rps_substituido: Optional[TcRpsSubstituido] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        }
    )
    observacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Observacao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 1000,
            "white_space": "collapse",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4",
        }
    )
    codigo_municipio_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipioPrestacao",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "total_digits": 7,
        }
    )


@dataclass
class TcListaRps:
    class Meta:
        name = "tcListaRps"

    rps: List[TcRps] = field(
        default_factory=list,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        }
    )
    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 11,
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 5,
        }
    )
    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )
    lista_rps: Optional[TcListaRps] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        }
    )


@dataclass
class LoteRps(TcLoteRps):
    class Meta:
        namespace = "http://www.el.com.br/nfse/xsd/el-nfse.xsd"
