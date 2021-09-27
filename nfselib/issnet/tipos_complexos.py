from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.issnet.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    cidade: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cidade",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "total_digits": 7,
        }
    )
    estado: Optional[str] = field(
        default=None,
        metadata={
            "name": "Estado",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "length": 2,
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "total_digits": 8,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    municipio_prestacao_servico: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacaoServico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 7,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcInfConfirmacaoCancelamento:
    class Meta:
        name = "tcInfConfirmacaoCancelamento"

    sucesso: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sucesso",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    lista_mensagem_retorno: Optional["TcInfConfirmacaoCancelamento.ListaMensagemRetorno"] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )

    @dataclass
    class ListaMensagemRetorno:
        mensagem_retorno: List[TcMensagemRetorno] = field(
            default_factory=list,
            metadata={
                "name": "MensagemRetorno",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
                "min_occurs": 1,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    motivo_cancelamento_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotivoCancelamentoNfse",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "min_length": 1,
            "max_length": 300,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "max_occurs": 2,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    inf_confirmacao_cancelamento: Optional[TcInfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfConfirmacaoCancelamento",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "pattern": r"1|2|3|4",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    competencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"^20(?:09|[1-9]\d)(?:0[1-9]|1[0-2])$",
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "pattern": r"1|2|3|4",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
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
                "namespace": "http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd",
                "min_occurs": 1,
            }
        )
