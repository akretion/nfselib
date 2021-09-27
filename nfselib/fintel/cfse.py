from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.fintel.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"


@dataclass
class ConsultarDadosCadastro:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    versao_dados: Optional[str] = field(
        default=None,
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "required": True,
            "max_length": 4,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 4,
        }
    )


@dataclass
class TccfCnae:
    class Meta:
        name = "tccfCNAE"

    codigo_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCNAE",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    descricao_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescricaoCNAE",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfContato:
    class Meta:
        name = "tccfContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfCpfCnpj:
    class Meta:
        name = "tccfCpfCnpj"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 14,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfDadosTerminal:
    class Meta:
        name = "tccfDadosTerminal"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    nome_maquina: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeMaquina",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    serial_hd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerialHD",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfEndereco:
    class Meta:
        name = "tccfEndereco"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 2,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "length": 8,
        }
    )
    nome_cidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeCidade",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        }
    )


@dataclass
class TccfIdentificacaoCfse:
    class Meta:
        name = "tccfIdentificacaoCfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[int] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )


@dataclass
class TccfMensagemRetorno:
    class Meta:
        name = "tccfMensagemRetorno"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfValoresDeclaracaoServico:
    class Meta:
        name = "tccfValoresDeclaracaoServico"

    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    mensagem_retorno: List[TccfMensagemRetorno] = field(
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
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    mensagem_retorno: List[TccfMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TccfAtividade:
    class Meta:
        name = "tccfAtividade"

    preferencial: Optional[str] = field(
        default=None,
        metadata={
            "name": "Preferencial",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "pattern": r"1|2",
        }
    )
    codigo_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoServico",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    descricao_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescricaoServico",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    lista_cnae: Optional["TccfAtividade.ListaCnae"] = field(
        default=None,
        metadata={
            "name": "ListaCNAE",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )

    @dataclass
    class ListaCnae:
        cnae: List[TccfCnae] = field(
            default_factory=list,
            metadata={
                "name": "CNAE",
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )


@dataclass
class TccfDadosServico:
    class Meta:
        name = "tccfDadosServico"

    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    codigo_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    exigibilidade_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExigibilidadeISS",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6|7|8",
        }
    )
    numero_processo: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        }
    )
    valores: Optional[TccfValoresDeclaracaoServico] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )


@dataclass
class TccfIdentificacaoPrestador:
    class Meta:
        name = "tccfIdentificacaoPrestador"

    cpf_cnpj: Optional[TccfCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfIdentificacaoTomador:
    class Meta:
        name = "tccfIdentificacaoTomador"

    cpf_cnpj: Optional[TccfCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )


@dataclass
class TccfInfCfse:
    class Meta:
        name = "tccfInfCfse"

    identificacao_cfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoCfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )


@dataclass
class TccfInfPedidoCancelamento:
    class Meta:
        name = "tccfInfPedidoCancelamento"

    identificacao_cfs: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoCfs",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
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
class TccfMensagemRetornoLote:
    class Meta:
        name = "tccfMensagemRetornoLote"

    identificacao_cfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoCfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class ConfigurarAtivarTerminal:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    terminal: Optional[TccfDadosTerminal] = field(
        default=None,
        metadata={
            "name": "Terminal",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarCfseEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    identificacao_cfse: Optional[TccfIdentificacaoCfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoCfse",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarLoteCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    prestador: Optional[TccfIdentificacaoPrestador] = field(
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
class EnviarLoteCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

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
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    mensagem_retorno: List[TccfMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TccfCupomFiscal:
    class Meta:
        name = "tccfCupomFiscal"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    inf_cfse: Optional[TccfInfCfse] = field(
        default=None,
        metadata={
            "name": "InfCfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfDadosEmissaoDiariaTerminal:
    class Meta:
        name = "tccfDadosEmissaoDiariaTerminal"

    data_configuracao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataConfiguracao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    identificacao_terminal: Optional[TccfDadosTerminal] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTerminal",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    numero_recibos: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroRecibos",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    numero_terminal: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroTerminal",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )
    identificacao_prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )


@dataclass
class TccfDadosPrestador:
    class Meta:
        name = "tccfDadosPrestador"

    identificacao_prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TccfEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    contato: Optional[TccfContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        }
    )


@dataclass
class TccfDadosTomador:
    class Meta:
        name = "tccfDadosTomador"

    identificacao_tomador: Optional[TccfIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )


@dataclass
class TccfPedidoCancelamento:
    class Meta:
        name = "tccfPedidoCancelamento"

    inf_pedido_cancelamento: Optional[TccfInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfPedidoDeclaracaoSemMovimento:
    class Meta:
        name = "tccfPedidoDeclaracaoSemMovimento"

    prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfPedidoManutencao:
    class Meta:
        name = "tccfPedidoManutencao"

    prestador: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Motivo",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    ultimo_cupom: Optional[int] = field(
        default=None,
        metadata={
            "name": "UltimoCupom",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class CancelarCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    pedido: Optional[TccfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EnviarInformeManutencao:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    pedido: Optional[TccfPedidoManutencao] = field(
        default=None,
        metadata={
            "name": "Pedido",
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
class InformeTrasmissaoSemMovimento:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    pedido: Optional[TccfPedidoDeclaracaoSemMovimento] = field(
        default=None,
        metadata={
            "name": "Pedido",
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
class TccfConfirmacaoCancelamento:
    class Meta:
        name = "tccfConfirmacaoCancelamento"

    pedido: Optional[TccfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfConfirmacaoPedidoManutencao:
    class Meta:
        name = "tccfConfirmacaoPedidoManutencao"

    pedido: Optional[TccfPedidoManutencao] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfConfirmacaoPedidoSemMovimento:
    class Meta:
        name = "tccfConfirmacaoPedidoSemMovimento"

    pedido: Optional[TccfPedidoDeclaracaoSemMovimento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfDadosCadastroPrestador:
    class Meta:
        name = "tccfDadosCadastroPrestador"

    inf_prestador: Optional[TccfDadosPrestador] = field(
        default=None,
        metadata={
            "name": "InfPrestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_cadastro: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataCadastro",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    data_atualizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataAtualizacao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    optante_simples: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimples",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    aliquota_simples_nacional: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaSimplesNacional",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    lista_atividades_prestadas: Optional["TccfDadosCadastroPrestador.ListaAtividadesPrestadas"] = field(
        default=None,
        metadata={
            "name": "ListaAtividadesPrestadas",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
    class ListaAtividadesPrestadas:
        atividades_prestadas: List[TccfAtividade] = field(
            default_factory=list,
            metadata={
                "name": "AtividadesPrestadas",
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class TccfInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tccfInfDeclaracaoPrestacaoServico"

    inf_cfse: Optional[TccfInfCfse] = field(
        default=None,
        metadata={
            "name": "InfCfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    lista_servicos: Optional["TccfInfDeclaracaoPrestacaoServico.ListaServicos"] = field(
        default=None,
        metadata={
            "name": "ListaServicos",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    prestador: Optional[TccfDadosPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    tomador_servico: Optional[TccfDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
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
    class ListaServicos:
        servico: List[TccfDadosServico] = field(
            default_factory=list,
            metadata={
                "name": "Servico",
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class CancelarCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    confimacao: Optional[TccfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confimacao",
            "type": "Element",
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
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ConfigurarAtivarTerminalResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    informacoes_emissao: Optional["ConfigurarAtivarTerminalResposta.InformacoesEmissao"] = field(
        default=None,
        metadata={
            "name": "InformacoesEmissao",
            "type": "Element",
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
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class InformacoesEmissao:
        dados_cadastro_prestador: Optional[TccfDadosCadastroPrestador] = field(
            default=None,
            metadata={
                "name": "DadosCadastroPrestador",
                "type": "Element",
                "required": True,
            }
        )
        dados_emissao_diaria: Optional[TccfDadosEmissaoDiariaTerminal] = field(
            default=None,
            metadata={
                "name": "DadosEmissaoDiaria",
                "type": "Element",
                "required": True,
            }
        )
        lista_cupom_fiscal: Optional["ConfigurarAtivarTerminalResposta.InformacoesEmissao.ListaCupomFiscal"] = field(
            default=None,
            metadata={
                "name": "ListaCupomFiscal",
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
        class ListaCupomFiscal:
            cupom: List[TccfCupomFiscal] = field(
                default_factory=list,
                metadata={
                    "name": "Cupom",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )


@dataclass
class ConsultarDadosCadastroResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    dados_cadastro_prestador: Optional[TccfDadosCadastroPrestador] = field(
        default=None,
        metadata={
            "name": "DadosCadastroPrestador",
            "type": "Element",
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
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class EnviarInformeManutencaoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    confirmacao: Optional[TccfConfirmacaoPedidoManutencao] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
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
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class InformeTrasmissaoSemMovimentoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    confirmacao: Optional[TccfConfirmacaoPedidoSemMovimento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
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
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class TccfCancelamentoCfse:
    class Meta:
        name = "tccfCancelamentoCfse"

    confirmacao: Optional[TccfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tccfDeclaracaoPrestacaoServico"

    inf_declaracao_prestacao_servico: Optional[TccfInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "InfDeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
class TccfCompCfse:
    class Meta:
        name = "tccfCompCfse"

    cfse: Optional[TccfInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "Cfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    cfse_cancelamento: Optional[TccfCancelamentoCfse] = field(
        default=None,
        metadata={
            "name": "CfseCancelamento",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
        }
    )


@dataclass
class TccfLoteCupom:
    class Meta:
        name = "tccfLoteCupom"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    responsavel_arquivo: Optional[TccfIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "ResponsavelArquivo",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    quantidade_cfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeCfse",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
            "required": True,
        }
    )
    lista_cupom: Optional["TccfLoteCupom.ListaCupom"] = field(
        default=None,
        metadata={
            "name": "ListaCupom",
            "type": "Element",
            "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
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
    class ListaCupom:
        cupom: List[TccfDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "name": "Cupom",
                "type": "Element",
                "namespace": "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )


@dataclass
class CompCfse(TccfCompCfse):
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"


@dataclass
class EnviarLoteCupomEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    lote_cupom: Optional[TccfLoteCupom] = field(
        default=None,
        metadata={
            "name": "LoteCupom",
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
class EnviarLoteCupomSincronoEnvio:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    chave_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChaveTerminal",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    lote_cupom: Optional[TccfLoteCupom] = field(
        default=None,
        metadata={
            "name": "LoteCupom",
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
class ConsultarCfseResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    comp_cfse: Optional[CompCfse] = field(
        default=None,
        metadata={
            "name": "CompCfse",
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
class ConsultarLoteCupomResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "required": True,
            "pattern": r"1|2|3|4|5",
        }
    )
    lista_cfse: Optional["ConsultarLoteCupomResposta.ListaCfse"] = field(
        default=None,
        metadata={
            "name": "ListaCfse",
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
    class ListaCfse:
        comp_cfse: List[CompCfse] = field(
            default_factory=list,
            metadata={
                "name": "CompCfse",
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
class EnviarLoteCupomSincronoResposta:
    class Meta:
        namespace = "http://iss.irati.pr.gov.br/Arquivos/cfse.xsd"

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
    lista_cfse: Optional["EnviarLoteCupomSincronoResposta.ListaCfse"] = field(
        default=None,
        metadata={
            "name": "ListaCfse",
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
    class ListaCfse:
        comp_cfse: List[CompCfse] = field(
            default_factory=list,
            metadata={
                "name": "CompCfse",
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
