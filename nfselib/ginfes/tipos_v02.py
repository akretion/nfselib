from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.ginfes.com.br/tipos"


@dataclass
class TcCancelamentoNfse:
    """
    Representa a estrutura de cancelamento de NFS-e.
    """
    data: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Motivo",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcContato:
    """
    Representa forma de contato com a pessoa (física/jurídica)
    """
    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        }
    )


@dataclass
class TcCpfCnpj:
    """
    Número de CPF ou CNPJ.

    :ivar cpf: Número do Cpf
    :ivar cnpj: Número do Cnpj
    """
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )


@dataclass
class TcEndereco:
    """
    Representação completa do endereço.

    :ivar endereco: Endereço
    :ivar numero: Número do endereço
    :ivar complemento: Complemento do Endereço
    :ivar bairro: Nome do bairro
    :ivar cidade: Código da cidade
    :ivar estado: Sigla do estado
    :ivar cep: CEP da localidade
    """
    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "total_digits": 7,
        }
    )
    estado: Optional[str] = field(
        default=None,
        metadata={
            "name": "Estado",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 2,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 8,
            "pattern": r"[0-9]{8}",
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    """
    Representa dados para identificação de intermediário do serviço.
    """
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
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
    :ivar base_calculo: (Valor dos serviços - Valor das deduções -
        descontos incondicionados)
    :ivar aliquota:
    :ivar valor_liquido_nfse: (ValorServicos - ValorPIS - ValorCOFINS -
        ValorINSS - ValorIR - ValorCSLL - OutrasRetençoes -
        ValorISSRetido - DescontoIncondicionado - DescontoCondicionado)
    :ivar valor_iss_retido:
    :ivar desconto_condicionado:
    :ivar desconto_incondicionado:
    """
    valor_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    iss_retido: Optional[int] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    valor_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    outras_retencoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    base_calculo: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "fraction_digits": 4,
        }
    )
    valor_liquido_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    valor_iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    desconto_condicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    desconto_incondicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    """
    Representa dados para identificação de órgão gerador.
    """
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 2,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    """
    Representa dados para identificação do prestador de serviço.
    """
    class Meta:
        name = "tcIdentificacaoPrestador"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoRps:
    """
    Dados de identificação do RPS.
    """
    class Meta:
        name = "tcIdentificacaoRps"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 3,
            "total_digits": 1,
        }
    )


@dataclass
class TcMensagemRetorno:
    """
    Representa a estrutura de mensagem de retorno de serviço.
    """
    class Meta:
        name = "tcMensagemRetorno"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcDadosServico:
    """
    Representa dados que compõe o serviço prestado.
    """
    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "total_digits": 7,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 7,
        }
    )


@dataclass
class TcDadosPrestador:
    """
    Representa dados do prestador do serviço.
    """
    class Meta:
        name = "tcDadosPrestador"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    """
    Representa dados para identificação do tomador de serviço.
    """
    class Meta:
        name = "tcIdentificacaoTomador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcMensagemRetornoLote:
    """
    Representa a estrutura de mensagem de retorno de serviço.
    """
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcDadosTomador:
    """
    Representa dados do tomador de serviço.
    """
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )


@dataclass
class TcNfseSemCancelamento:
    """
    Representa a estrutura da Nota Fiscal de Serviços Eletrônica.
    """
    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
            "total_digits": 2,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_inclusive": 1,
            "max_inclusive": 4,
            "total_digits": 2,
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    incetivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncetivadorCultural",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    competencia: Optional[int] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 6,
        }
    )
    nfse_substituida: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    valor_credito: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )


@dataclass
class TcRps:
    """
    Representa a estrutura de Recibo Provisório de Serviço (RPS)
    """
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
            "total_digits": 2,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_inclusive": 1,
            "max_inclusive": 4,
            "total_digits": 2,
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )


@dataclass
class TcNfse:
    """
    Representa a estrutura de NFS-e incluindo a estrutura de cancelamento da
    mesma, quando existente.
    """
    nfse: Optional[TcNfseSemCancelamento] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        }
    )
    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        }
    )
