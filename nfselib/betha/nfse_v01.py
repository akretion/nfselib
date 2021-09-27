from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfselib.betha.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    pedido: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    prestador: Optional[str] = field(
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
        }
    )


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lista_nfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[str] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
        }
    )
    periodo_emissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario_servico: Optional[str] = field(
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
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lista_nfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[str] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    identificacao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    comp_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    prestador: Optional[str] = field(
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
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
        }
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
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
        }
    )
    lista_mensagem_retorno: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    mensagem_retorno: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    nfse_substituicao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )


@dataclass
class TcCondicaoPagamento:
    class Meta:
        name = "tcCondicaoPagamento"

    condicao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Condicao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    qtd_parcela: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdParcela",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    parcelas: Optional[str] = field(
        default=None,
        metadata={
            "name": "Parcelas",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    pedido: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    data_hora_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHoraCancelamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    identificacao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    valores: Optional[str] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    codigo_cnae: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoEstadual",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    identificacao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    nfse_substituida: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    valor_credito: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    prestador_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    tomador_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    intermediario_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    orgao_gerador: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    contrucao_civil: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    identificacao_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcInfRps:
    class Meta:
        name = "tcInfRps"

    identificacao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    natureza_operacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    incentivador_cultural: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    rps_substituido: Optional[str] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    intermediario_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    contrucao_civil: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    condicao_pagamento: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CondicaoPagamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "max_occurs": 5,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    nfse_substituidora: Optional[str] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    quantidade_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
        rps: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
                "min_occurs": 1,
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )


@dataclass
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcParcelas:
    class Meta:
        name = "tcParcelas"

    parcela: Optional[str] = field(
        default=None,
        metadata={
            "name": "Parcela",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    data_vencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataVencimento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    valor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Valor",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    valor_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    valor_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    valor_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    outras_retencoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    base_calculo: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    valor_liquido_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    desconto_incondicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    desconto_condicionado: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lote_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoteRps",
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
        }
    )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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

    inf_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    inf_pedido_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcRps:
    class Meta:
        name = "tcRps"

    inf_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    substituicao_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
