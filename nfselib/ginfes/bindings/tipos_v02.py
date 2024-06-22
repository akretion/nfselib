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
        },
    )
    Motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcContato:
    """
    Representa forma de contato com a pessoa (física/jurídica)
    """

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        },
    )


@dataclass
class TcCpfCnpj:
    """
    Número de CPF ou CNPJ.

    :ivar Cpf: Número do Cpf
    :ivar Cnpj: Número do Cnpj
    """

    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )


@dataclass
class TcEndereco:
    """
    Representação completa do endereço.

    :ivar Endereco: Endereço
    :ivar Numero: Número do endereço
    :ivar Complemento: Complemento do Endereço
    :ivar Bairro: Nome do bairro
    :ivar Cidade: Código da cidade
    :ivar Estado: Sigla do estado
    :ivar Cep: CEP da localidade
    """

    Endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Cidade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "total_digits": 7,
        },
    )
    Estado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 2,
            "white_space": "collapse",
        },
    )
    Cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 8,
            "pattern": r"[0-9]{8}",
        },
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    """
    Representa dados para identificação de intermediário do serviço.
    """

    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcValores:
    """
    Representa um conjunto de valores que compõe o documento fiscal.

    :ivar ValorServicos:
    :ivar ValorDeducoes:
    :ivar ValorPis:
    :ivar ValorCofins:
    :ivar ValorInss:
    :ivar ValorIr:
    :ivar ValorCsll:
    :ivar IssRetido:
    :ivar ValorIss:
    :ivar OutrasRetencoes:
    :ivar BaseCalculo: (Valor dos serviços - Valor das deduções -
        descontos incondicionados)
    :ivar Aliquota:
    :ivar ValorLiquidoNfse: (ValorServicos - ValorPIS - ValorCOFINS -
        ValorINSS - ValorIR - ValorCSLL - OutrasRetençoes -
        ValorISSRetido - DescontoIncondicionado - DescontoCondicionado)
    :ivar ValorIssRetido:
    :ivar DescontoCondicionado:
    :ivar DescontoIncondicionado:
    """

    ValorServicos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorDeducoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorInss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorIr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorCsll: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    IssRetido: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    ValorIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    OutrasRetencoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    BaseCalculo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "fraction_digits": 4,
        },
    )
    ValorLiquidoNfse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    ValorIssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    DescontoCondicionado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    DescontoIncondicionado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )


@dataclass
class TcDadosConstrucaoCivil:
    """
    Representa dados para identificação de construção civil.
    """

    class Meta:
        name = "tcDadosConstrucaoCivil"

    CodigoObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoNfse:
    """
    Representa dados que identificam uma Nota Fiscal de Serviços Eletrônica.
    """

    class Meta:
        name = "tcIdentificacaoNfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 15,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    """
    Representa dados para identificação de órgão gerador.
    """

    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 2,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    """
    Representa dados para identificação do prestador de serviço.
    """

    class Meta:
        name = "tcIdentificacaoPrestador"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoRps:
    """
    Dados de identificação do RPS.
    """

    class Meta:
        name = "tcIdentificacaoRps"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 15,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Tipo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 3,
            "total_digits": 1,
        },
    )


@dataclass
class TcMensagemRetorno:
    """
    Representa a estrutura de mensagem de retorno de serviço.
    """

    class Meta:
        name = "tcMensagemRetorno"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcDadosServico:
    """
    Representa dados que compõe o serviço prestado.
    """

    Valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    CodigoCnae: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "total_digits": 7,
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    MunicipioPrestacaoServico: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 7,
        },
    )


@dataclass
class TcDadosPrestador:
    """
    Representa dados do prestador do serviço.
    """

    class Meta:
        name = "tcDadosPrestador"

    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )


@dataclass
class TcIdentificacaoTomador:
    """
    Representa dados para identificação do tomador de serviço.
    """

    class Meta:
        name = "tcIdentificacaoTomador"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcMensagemRetornoLote:
    """
    Representa a estrutura de mensagem de retorno de serviço.
    """

    class Meta:
        name = "tcMensagemRetornoLote"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
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
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TcDadosTomador:
    """
    Representa dados do tomador de serviço.
    """

    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )


@dataclass
class TcNfseSemCancelamento:
    """
    Representa a estrutura da Nota Fiscal de Serviços Eletrônica.
    """

    IdentificacaoNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    DataEmissaoRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
            "total_digits": 2,
        },
    )
    RegimeEspecialTributacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_inclusive": 1,
            "max_inclusive": 4,
            "total_digits": 2,
        },
    )
    OptanteSimplesNacional: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    IncetivadorCultural: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    Competencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "total_digits": 6,
        },
    )
    NfseSubstituida: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    ValorCredito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "max_length": 15,
            "pattern": r"[0-9]{1,15}(\.[0-9]{2})?",
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ginfes.com.br/tipos",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    ConstrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )


@dataclass
class TcRps:
    """
    Representa a estrutura de Recibo Provisório de Serviço (RPS)
    """

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
            "total_digits": 2,
        },
    )
    RegimeEspecialTributacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "min_inclusive": 1,
            "max_inclusive": 4,
            "total_digits": 2,
        },
    )
    OptanteSimplesNacional: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    IncentivadorCultural: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    Status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
            "total_digits": 1,
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ginfes.com.br/tipos",
            },
        )
    )
    ConstrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )


@dataclass
class TcNfse:
    """
    Representa a estrutura de NFS-e incluindo a estrutura de cancelamento da mesma,
    quando existente.
    """

    nfse: Optional[TcNfseSemCancelamento] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
            "required": True,
        },
    )
    Cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos",
        },
    )
