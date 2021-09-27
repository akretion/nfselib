from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfselib.betha.nfse_v01 import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
    TcCompNfse,
    TcCpfCnpj,
    TcDadosConstrucaoCivil,
    TcDadosServico,
    TcDadosTomador,
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
    TcInfRps,
    TcLoteRps,
    TcMensagemRetorno,
    TcMensagemRetornoLote,
    TcPedidoCancelamento,
)
from nfselib.betha.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    versao_dados: Optional[str] = field(
        default=None,
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
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
class TcValoresDeclaracaoServico:
    class Meta:
        name = "tcValoresDeclaracaoServico"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class TcValoresNfse:
    class Meta:
        name = "tcValoresNfse"

    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
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
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class Faixa:
        numero_nfse_inicial: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseInicial",
                "type": "Element",
                "required": True,
                "total_digits": 15,
            }
        )
        numero_nfse_final: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseFinal",
                "type": "Element",
                "total_digits": 15,
            }
        )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lote_rps: Optional[TcLoteRps] = field(
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
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    mensagem_retorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcIdentificacaoConsulente:
    class Meta:
        name = "tcIdentificacaoConsulente"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
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
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoIntermediario:
    class Meta:
        name = "tcIdentificacaoIntermediario"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
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
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcRetCancelamento:
    class Meta:
        name = "tcRetCancelamento"

    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseServicoPrestadoEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

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
    periodo_emissao: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
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
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
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
    class PeriodoCompetencia:
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
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lista_nfse: Optional["ConsultarNfseServicoPrestadoResposta.ListaNfse"] = field(
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseServicoTomadoEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    consulente: Optional[TcIdentificacaoConsulente] = field(
        default=None,
        metadata={
            "name": "Consulente",
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
    periodo_emissao: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
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
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
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
    class PeriodoCompetencia:
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
class ConsultarNfseServicoTomadoResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lista_nfse: Optional["ConsultarNfseServicoTomadoResposta.ListaNfse"] = field(
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
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class EnviarLoteRpsSincronoResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

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
    lista_nfse: Optional["EnviarLoteRpsSincronoResposta.ListaNfse"] = field(
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
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
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


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

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
        comp_nfse: Optional[CompNfse] = field(
            default=None,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "required": True,
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
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

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
            comp_nfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
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
        class NfseSubstituidora:
            comp_nfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    identificacao_intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "IdentificacaoIntermediario",
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
            "min_length": 1,
            "max_length": 115,
            "white_space": "collapse",
        }
    )


@dataclass
class TcInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcInfDeclaracaoPrestacaoServico"

    rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    intermediario: Optional[TcDadosIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
            "pattern": r"1|2|3",
        }
    )
    incentivo_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivoFiscal",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
            "pattern": r"1|2|3",
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
class TcDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcDeclaracaoPrestacaoServico"

    inf_declaracao_prestacao_servico: Optional[TcInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "InfDeclaracaoPrestacaoServico",
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
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    rps: Optional[TcDeclaracaoPrestacaoServico] = field(
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
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    substituicao_nfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
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
    class SubstituicaoNfse:
        pedido: Optional[TcPedidoCancelamento] = field(
            default=None,
            metadata={
                "name": "Pedido",
                "type": "Element",
                "required": True,
            }
        )
        rps: Optional[TcDeclaracaoPrestacaoServico] = field(
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
                "name": "Id",
                "type": "Attribute",
                "max_length": 255,
            }
        )
