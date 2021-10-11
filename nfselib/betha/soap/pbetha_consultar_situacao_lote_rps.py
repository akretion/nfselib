from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
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
            "namespace": "",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "",
        }
    )
    protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcListaMensagemRetorno:
    class Meta:
        name = "tcListaMensagemRetorno"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_envio: Optional[ConsultarSituacaoLoteRpsEnvio] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsEnvio",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        name = "consultarSituacaoLoteRpsResposta"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
        }
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "namespace": "",
        }
    )
    lista_mensagem_retorno: Optional[TcListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvioResponse:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    consultar_situacao_lote_rps_resposta: Optional[ConsultarSituacaoLoteRpsResposta] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_envio_response: Optional[ConsultarSituacaoLoteRpsEnvioResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsEnvioResponse",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )
        fault: Optional["ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvio:
    style = "document"
    location = "http://e-gov.betha.com.br/e-nota-contribuinte-ws/consultarSituacaoLoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioInput
    output = ConsultarSituacaoLoteRpsConsultarSituacaoLoteRpsEnvioOutput
