from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

__NAMESPACE__ = "http://www.publica.inf.br"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 14,
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 2,
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "total_digits": 8,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 4,
        }
    )
    municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "Municipio",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    tipo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    nfse_substituidora: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
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
        }
    )
    parcela: Optional[int] = field(
        default=None,
        metadata={
            "name": "Parcela",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Valor",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    data_vencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataVencimento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_iss_retido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.publica.inf.br"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcCondicoesPagamentos:
    class Meta:
        name = "tcCondicoesPagamentos"

    parcelas: List[TcParcelas] = field(
        default_factory=list,
        metadata={
            "name": "Parcelas",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
        }
    )
    informacoes_complementares: Optional[str] = field(
        default=None,
        metadata={
            "name": "InformacoesComplementares",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 7,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 4,
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
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "length": 14,
            "white_space": "collapse",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    motivo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotivoCancelamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "max_length": 255,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
        namespace = "http://www.publica.inf.br"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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

    @dataclass
    class Faixa:
        numero_nfse_inicial: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroNfseInicial",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
            }
        )
        numero_nfse_final: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroNfseFinal",
                "type": "Element",
                "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
            }
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 10,
        }
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "pattern": r"1|2|3|4",
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
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 10,
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
class TcConsultaNfseRecebida:
    class Meta:
        name = "tcConsultaNfseRecebida"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    data_nfse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataNfse",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    data_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataRps",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    signature: Optional[str] = field(
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
        namespace = "http://www.publica.inf.br"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultaNfseRecebidaEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    consulta_nfse_recebida: Optional[TcConsultaNfseRecebida] = field(
        default=None,
        metadata={
            "name": "ConsultaNfseRecebida",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcCartaCorrecao:
    class Meta:
        name = "tcCartaCorrecao"

    numero_carta_correcao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroCartaCorrecao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        }
    )
    oficial: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oficial",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    data_declaracao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataDeclaracao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    data_hora_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHoraCancelamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    competencia: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    nfse_substituida: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "pattern": r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    condicao_pagamento: Optional[TcCondicoesPagamentos] = field(
        default=None,
        metadata={
            "name": "CondicaoPagamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcInfPedidoCartaCorrecao:
    class Meta:
        name = "tcInfPedidoCartaCorrecao"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "min_length": 1,
            "max_length": 10000,
            "white_space": "collapse",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    competencia: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    condicao_pagamento: Optional[TcCondicoesPagamentos] = field(
        default=None,
        metadata={
            "name": "CondicaoPagamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )


@dataclass
class TcPedidoCartaCorrecao:
    class Meta:
        name = "tcPedidoCartaCorrecao"

    inf_pedido_carta_correcao: Optional[TcInfPedidoCartaCorrecao] = field(
        default=None,
        metadata={
            "name": "InfPedidoCartaCorrecao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"

    inf_rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
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
class CartaCorrecaoNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    pedido: Optional[TcPedidoCartaCorrecao] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    rps: Optional[TcRps] = field(
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
        namespace = "http://www.publica.inf.br"

    substituicao_nfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
        rps: Optional[TcRps] = field(
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
                "type": "Attribute",
                "max_length": 255,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )
    lista_correcao: Optional["TcCompNfse.ListaCorrecao"] = field(
        default=None,
        metadata={
            "name": "ListaCorrecao",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
        }
    )

    @dataclass
    class ListaCorrecao:
        carta_correcao: List[TcCartaCorrecao] = field(
            default_factory=list,
            metadata={
                "name": "CartaCorrecao",
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "total_digits": 10,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
            "length": 14,
            "white_space": "collapse",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
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
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.publica.inf.br",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
        rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://www.publica.inf.br",
                "min_occurs": 1,
            }
        )


@dataclass
class CartaCorrecaoNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    comp_nfse: Optional[TcCompNfse] = field(
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
class ConsultaNfseRecebidaResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    lista_nfse: Optional["ConsultaNfseRecebidaResposta.ListaNfse"] = field(
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
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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

    @dataclass
    class ListaNfse:
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

    lista_nfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
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
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.publica.inf.br"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )


@dataclass
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://www.publica.inf.br"

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
            comp_nfse: Optional[TcCompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class NfseSubstituidora:
            comp_nfse: Optional[TcCompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )
