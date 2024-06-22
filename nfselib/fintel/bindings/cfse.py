from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.fintel.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"


@dataclass
class ConsultarDadosCadastro:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    versaoDados: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 4,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 4,
        },
    )


@dataclass
class TccfCnae:
    class Meta:
        name = "tccfCNAE"

    CodigoCNAE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    DescricaoCNAE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfContato:
    class Meta:
        name = "tccfContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfCpfCnpj:
    class Meta:
        name = "tccfCpfCnpj"

    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 14,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfDadosTerminal:
    class Meta:
        name = "tccfDadosTerminal"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    NomeMaquina: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    SerialHD: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    MAC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfEndereco:
    class Meta:
        name = "tccfEndereco"

    Endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 2,
        },
    )
    CodigoPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 4,
            "white_space": "collapse",
        },
    )
    Cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 8,
        },
    )
    NomeCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        },
    )


@dataclass
class TccfIdentificacaoCfse:
    class Meta:
        name = "tccfIdentificacaoCfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Serie: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )


@dataclass
class TccfMensagemRetorno:
    class Meta:
        name = "tccfMensagemRetorno"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfValoresDeclaracaoServico:
    class Meta:
        name = "tccfValoresDeclaracaoServico"

    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    MensagemRetorno: List[TccfMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    MensagemRetorno: List[TccfMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TccfAtividade:
    class Meta:
        name = "tccfAtividade"

    Preferencial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "pattern": r"1|2",
        },
    )
    CodigoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    DescricaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    ListaCNAE: Optional["TccfAtividade.ListaCnae"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )

    @dataclass
    class ListaCnae:
        CNAE: List[TccfCnae] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )


@dataclass
class TccfDadosServico:
    class Meta:
        name = "tccfDadosServico"

    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    CodigoCnae: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    ExigibilidadeISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6|7|8",
        },
    )
    NumeroProcesso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    Valores: Optional[TccfValoresDeclaracaoServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )


@dataclass
class TccfIdentificacaoPrestador:
    class Meta:
        name = "tccfIdentificacaoPrestador"

    CpfCnpj: Optional[TccfCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfIdentificacaoTomador:
    class Meta:
        name = "tccfIdentificacaoTomador"

    CpfCnpj: Optional[TccfCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )


@dataclass
class TccfInfCfse:
    class Meta:
        name = "tccfInfCfse"

    IdentificacaoCfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )


@dataclass
class TccfInfPedidoCancelamento:
    class Meta:
        name = "tccfInfPedidoCancelamento"

    IdentificacaoCfs: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TccfMensagemRetornoLote:
    class Meta:
        name = "tccfMensagemRetornoLote"

    IdentificacaoCfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )


@dataclass
class ConfigurarAtivarTerminal:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    Terminal: Optional[TccfDadosTerminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarCfseEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    IdentificacaoCfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarLoteCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 50,
        },
    )


@dataclass
class EnviarLoteCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    MensagemRetorno: List[TccfMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TccfCupomFiscal:
    class Meta:
        name = "tccfCupomFiscal"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    InfCfse: Optional[TccfInfCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfDadosEmissaoDiariaTerminal:
    class Meta:
        name = "tccfDadosEmissaoDiariaTerminal"

    DataConfiguracao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    IdentificacaoTerminal: Optional[TccfDadosTerminal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    NumeroRecibos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    NumeroTerminal: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        },
    )
    IdentificacaoPrestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )


@dataclass
class TccfDadosPrestador:
    class Meta:
        name = "tccfDadosPrestador"

    IdentificacaoPrestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TccfEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Contato: Optional[TccfContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        },
    )


@dataclass
class TccfDadosTomador:
    class Meta:
        name = "tccfDadosTomador"

    IdentificacaoTomador: Optional[TccfIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Nome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )


@dataclass
class TccfPedidoCancelamento:
    class Meta:
        name = "tccfPedidoCancelamento"

    InfPedidoCancelamento: Optional[TccfInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class TccfPedidoDeclaracaoSemMovimento:
    class Meta:
        name = "tccfPedidoDeclaracaoSemMovimento"

    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TccfPedidoManutencao:
    class Meta:
        name = "tccfPedidoManutencao"

    Prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    UltimoCupom: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class CancelarCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    Pedido: Optional[TccfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnviarInformeManutencao:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    Pedido: Optional[TccfPedidoManutencao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class InformeTrasmissaoSemMovimento:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    Pedido: Optional[TccfPedidoDeclaracaoSemMovimento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class TccfConfirmacaoCancelamento:
    class Meta:
        name = "tccfConfirmacaoCancelamento"

    Pedido: Optional[TccfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TccfConfirmacaoPedidoManutencao:
    class Meta:
        name = "tccfConfirmacaoPedidoManutencao"

    Pedido: Optional[TccfPedidoManutencao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TccfConfirmacaoPedidoSemMovimento:
    class Meta:
        name = "tccfConfirmacaoPedidoSemMovimento"

    Pedido: Optional[TccfPedidoDeclaracaoSemMovimento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataHora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TccfDadosCadastroPrestador:
    class Meta:
        name = "tccfDadosCadastroPrestador"

    InfPrestador: Optional[TccfDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataCadastro: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    DataAtualizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    OptanteSimples: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    AliquotaSimplesNacional: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        },
    )
    ListaAtividadesPrestadas: Optional[
        "TccfDadosCadastroPrestador.ListaAtividadesPrestadas"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )

    @dataclass
    class ListaAtividadesPrestadas:
        AtividadesPrestadas: List[TccfAtividade] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class TccfInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tccfInfDeclaracaoPrestacaoServico"

    InfCfse: Optional[TccfInfCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    ListaServicos: Optional[
        "TccfInfDeclaracaoPrestacaoServico.ListaServicos"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TccfDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    TomadorServico: Optional[TccfDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )

    @dataclass
    class ListaServicos:
        Servico: List[TccfDadosServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
            },
        )


@dataclass
class CancelarCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    Confimacao: Optional[TccfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class ConfigurarAtivarTerminalResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    InformacoesEmissao: Optional[
        "ConfigurarAtivarTerminalResposta.InformacoesEmissao"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )

    @dataclass
    class InformacoesEmissao:
        DadosCadastroPrestador: Optional[TccfDadosCadastroPrestador] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DadosEmissaoDiaria: Optional[TccfDadosEmissaoDiariaTerminal] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        ListaCupomFiscal: Optional[
            "ConfigurarAtivarTerminalResposta.InformacoesEmissao.ListaCupomFiscal"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "max_length": 255,
            },
        )

        @dataclass
        class ListaCupomFiscal:
            Cupom: List[TccfCupomFiscal] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )


@dataclass
class ConsultarDadosCadastroResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    DadosCadastroPrestador: Optional[TccfDadosCadastroPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class EnviarInformeManutencaoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    Confirmacao: Optional[TccfConfirmacaoPedidoManutencao] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class InformeTrasmissaoSemMovimentoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    Confirmacao: Optional[TccfConfirmacaoPedidoSemMovimento] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class TccfCancelamentoCfse:
    class Meta:
        name = "tccfCancelamentoCfse"

    Confirmacao: Optional[TccfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class TccfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tccfDeclaracaoPrestacaoServico"

    InfDeclaracaoPrestacaoServico: Optional[
        TccfInfDeclaracaoPrestacaoServico
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class TccfCompCfse:
    class Meta:
        name = "tccfCompCfse"

    Cfse: Optional[TccfInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    CfseCancelamento: Optional[TccfCancelamentoCfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        },
    )


@dataclass
class TccfLoteCupom:
    class Meta:
        name = "tccfLoteCupom"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    ResponsavelArquivo: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    QuantidadeCfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    ListaCupom: Optional["TccfLoteCupom.ListaCupom"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )

    @dataclass
    class ListaCupom:
        Cupom: List[TccfDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )


@dataclass
class CompCfse(TccfCompCfse):
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"


@dataclass
class EnviarLoteCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    LoteCupom: Optional[TccfLoteCupom] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class EnviarLoteCupomSincronoEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    ChaveTerminal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        },
    )
    LoteCupom: Optional[TccfLoteCupom] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )


@dataclass
class ConsultarCfseResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    compCfse: Optional[CompCfse] = field(
        default=None,
        metadata={
            "name": "CompCfse",
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"1|2|3|4|5",
        },
    )
    ListaCfse: Optional["ConsultarLoteCupomResposta.ListaCfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
    listaMensagemRetornoLote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        },
    )

    @dataclass
    class ListaCfse:
        compCfse: List[CompCfse] = field(
            default_factory=list,
            metadata={
                "name": "CompCfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        listaMensagemAlertaRetorno: Optional[ListaMensagemAlertaRetorno] = (
            field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                },
            )
        )


@dataclass
class EnviarLoteCupomSincronoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
    ListaCfse: Optional["EnviarLoteCupomSincronoResposta.ListaCfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
    listaMensagemRetornoLote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        },
    )

    @dataclass
    class ListaCfse:
        compCfse: List[CompCfse] = field(
            default_factory=list,
            metadata={
                "name": "CompCfse",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        listaMensagemAlertaRetorno: Optional[ListaMensagemAlertaRetorno] = (
            field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                },
            )
        )
