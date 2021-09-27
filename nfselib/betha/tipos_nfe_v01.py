from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.betha.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws/tipos"


class Condicao(Enum):
    A_VISTA = "A_VISTA"
    A_PRAZO = "A_PRAZO"
    NA_APRESENTACAO = "NA_APRESENTACAO"
    CARTAO_DEBITO = "CARTAO_DEBITO"
    CARTAO_CREDITO = "CARTAO_CREDITO"


@dataclass
class TcContato:
    """
    Representa a forma de contato com a pessoa (física/jurídica)
    """
    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "",
            "min_length": 8,
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r"[0-9]{8,11}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "",
            "min_length": 5,
            "max_length": 80,
            "white_space": "collapse",
            "pattern": r"[A-Za-z0-9\\._-]+@[A-Za-z0-9\\._-]+[.][A-Za-z]+",
        }
    )


@dataclass
class TcCpfCnpj:
    """
    Número de Cpf ou Cnpj.
    """
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0}|[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{14}",
        }
    )


@dataclass
class TcEndereco:
    """
    Representação completa do endereço.
    """
    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,7}",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 2,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7,8}",
        }
    )


@dataclass
class TcValores:
    """
    Representa um conjunto de valores que compõe o documento fiscal.

    :ivar valor_servicos:
    :ivar valor_deducoes:
    :ivar valor_pis:
    :ivar valor_cofins:
    :ivar valor_inss:
    :ivar valor_ir:
    :ivar valor_csll:
    :ivar iss_retido:
    :ivar valor_iss:
    :ivar outras_retencoes:
    :ivar base_calculo: Valor dos serviços - valor das deduções -
        descontos incondicionados
    :ivar aliquota:
    :ivar valor_liquido_nfse: Valor dos serviços - valor do PIS - valor
        COFINS - valor INSS - valor IR  - valor CSLL - outras retenções
        - valor ISS retido - desconto incondicionado - desconto
        condicionado
    :ivar valor_iss_retido:
    :ivar desconto_condicionado:
    :ivar desconto_incondicionado:
    """
    valor_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )
    valor_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    outras_retencoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    base_calculo: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    valor_liquido_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    desconto_condicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    desconto_incondicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    """
    Representa dados para identificação de construção civil.
    """
    class Meta:
        name = "tcDadosConstrucaoCivil"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoNfse:
    """
    Representa dados que identificam uma Nota Fiscal de Serviços Eletrônica.
    """
    class Meta:
        name = "tcIdentificacaoNfse"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,7}",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    """
    Representa dados para identificação do prestador de serviços.
    """
    class Meta:
        name = "tcIdentificacaoPrestador"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoRps:
    """
    Dados de identificação do Rps.
    """
    class Meta:
        name = "tcIdentificacaoRps"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )


@dataclass
class TcParcelas:
    class Meta:
        name = "tcParcelas"

    parcela: Optional[int] = field(
        default=None,
        metadata={
            "name": "Parcela",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_vencimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataVencimento",
            "type": "Element",
            "namespace": "",
        }
    )
    valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Valor",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcDadosServico:
    """
    Representa dados que compõem o serviço prestado.
    """
    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    codigo_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,7}",
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "",
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
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,7}",
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    """
    Representa dados para identificação do intermediário de serviços.
    """
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcCondicoesPagamentos:
    class Meta:
        name = "tcCondicoesPagamentos"

    condicao: Optional[Condicao] = field(
        default=None,
        metadata={
            "name": "Condicao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    qtd_parcela: Optional[int] = field(
        default=None,
        metadata={
            "name": "QtdParcela",
            "type": "Element",
            "namespace": "",
        }
    )
    parcelas: List[TcParcelas] = field(
        default_factory=list,
        metadata={
            "name": "Parcelas",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    """
    Representa dados para identificação do tomador de serviços.
    """
    class Meta:
        name = "tcIdentificacaoTomador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
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
            "namespace": "",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TcDadosTomador:
    """
    Representa dados do tomador de serviços.
    """
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcPedidoCancelamento:
    """
    Representa dados para o pedido de cancelamento de uma nota fiscal.
    """
    class Meta:
        name = "tcPedidoCancelamento"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "",
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
class TcInfRps:
    """
    Representa a estrutura de recibo provisório de serviços (Rps)
    """
    class Meta:
        name = "tcInfRps"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-7]{1}",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[1-6]{1}",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-2]{1}",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "",
        }
    )
    condicao_pagamento: List[TcCondicoesPagamentos] = field(
        default_factory=list,
        metadata={
            "name": "CondicaoPagamento",
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TcRps:
    """
    Representação do RPS.
    """
    class Meta:
        name = "tcRps"

    inf_rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "",
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
class TcLoteRps:
    """
    Lote dp RPS.
    """
    class Meta:
        name = "tcLoteRps"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    quantidade_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,4}",
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )

    @dataclass
    class ListaRps:
        rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
