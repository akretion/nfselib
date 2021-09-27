from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "length": 2,
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "total_digits": 8,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
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
class TcItemServico:
    class Meta:
        name = "tcItemServico"

    descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Quantidade",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorUnitario",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    iss_tributavel: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssTributavel",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "pattern": r"1|2",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_length": 1,
            "max_length": 200,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "total_digits": 7,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    itens_servico: List[TcItemServico] = field(
        default_factory=list,
        metadata={
            "name": "ItensServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_occurs": 1,
        }
    )


@dataclass
class TcIdentNovaNfse:
    class Meta:
        name = "tcIdentNovaNfse"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_length": 1,
            "max_length": 200,
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
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"

    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_length": 1,
            "max_length": 20,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
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
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    signature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
        }
    )


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
    periodo_emissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
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
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
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
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
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
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
class TcRespostaIdentNovaNfse:
    class Meta:
        name = "tcRespostaIdentNovaNfse"

    identificacao_nfse: Optional[TcIdentNovaNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GerarNovaNfseResposta:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

    nova_nfse: Optional[TcRespostaIdentNovaNfse] = field(
        default=None,
        metadata={
            "name": "NovaNfse",
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
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    data_hora_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHoraCancelamento",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
class TcInfNovaNfse:
    class Meta:
        name = "tcInfNovaNfse"

    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
class GerarNovaNfseEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    informacao_nfse: Optional[TcInfNovaNfse] = field(
        default=None,
        metadata={
            "name": "InformacaoNfse",
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
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    signature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
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
    class ListaRps:
        rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.sistema.com.br/Nfse/arquivos/nfse_3.xsd"

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
