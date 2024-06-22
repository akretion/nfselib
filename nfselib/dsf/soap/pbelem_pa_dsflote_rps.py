from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"


@dataclass
class Cancelar:
    class Meta:
        name = "cancelar"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    mensagemXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarResponse:
    class Meta:
        name = "cancelarResponse"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    cancelarReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLote:
    class Meta:
        name = "consultarLote"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    mensagemXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteResponse:
    class Meta:
        name = "consultarLoteResponse"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    consultarLoteReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNota:
    class Meta:
        name = "consultarNota"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    mensagemXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNotaResponse:
    class Meta:
        name = "consultarNotaResponse"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    consultarNotaReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSequencialRps:
    class Meta:
        name = "consultarSequencialRps"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    mensagemXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSequencialRpsResponse:
    class Meta:
        name = "consultarSequencialRpsResponse"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    consultarSequencialRpsReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Enviar:
    class Meta:
        name = "enviar"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    mensagemXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnviarResponse:
    class Meta:
        name = "enviarResponse"
        namespace = "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps"

    enviarReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LoteRpsCancelarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsCancelarInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelar: Optional[Cancelar] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )


@dataclass
class LoteRpsCancelarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsCancelarOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarResponse: Optional[CancelarResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )
        Fault: Optional["LoteRpsCancelarOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class LoteRpsConsultarLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarLoteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLote: Optional[ConsultarLote] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )


@dataclass
class LoteRpsConsultarLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarLoteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLoteResponse: Optional[ConsultarLoteResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )
        Fault: Optional["LoteRpsConsultarLoteOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class LoteRpsConsultarNotaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarNotaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNota: Optional[ConsultarNota] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )


@dataclass
class LoteRpsConsultarNotaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarNotaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNotaResponse: Optional[ConsultarNotaResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )
        Fault: Optional["LoteRpsConsultarNotaOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class LoteRpsConsultarSequencialRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarSequencialRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarSequencialRps: Optional[ConsultarSequencialRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )


@dataclass
class LoteRpsConsultarSequencialRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsConsultarSequencialRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarSequencialRpsResponse: Optional[
            ConsultarSequencialRpsResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )
        Fault: Optional["LoteRpsConsultarSequencialRpsOutput.Body.Fault"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class LoteRpsEnviarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsEnviarInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviar: Optional[Enviar] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )


@dataclass
class LoteRpsEnviarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["LoteRpsEnviarOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviarResponse: Optional[EnviarResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://siat.nota.belem.pa.gov.br/WsNFe/LoteRps",
            },
        )
        Fault: Optional["LoteRpsEnviarOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class LoteRpsCancelar:
    style = "rpc"
    location = "http://siat.belem.pa.gov.br:8180/WsNFe/LoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoteRpsCancelarInput
    output = LoteRpsCancelarOutput


class LoteRpsConsultarLote:
    style = "rpc"
    location = "http://siat.belem.pa.gov.br:8180/WsNFe/LoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoteRpsConsultarLoteInput
    output = LoteRpsConsultarLoteOutput


class LoteRpsConsultarNota:
    style = "rpc"
    location = "http://siat.belem.pa.gov.br:8180/WsNFe/LoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoteRpsConsultarNotaInput
    output = LoteRpsConsultarNotaOutput


class LoteRpsConsultarSequencialRps:
    style = "rpc"
    location = "http://siat.belem.pa.gov.br:8180/WsNFe/LoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoteRpsConsultarSequencialRpsInput
    output = LoteRpsConsultarSequencialRpsOutput


class LoteRpsEnviar:
    style = "rpc"
    location = "http://siat.belem.pa.gov.br:8180/WsNFe/LoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoteRpsEnviarInput
    output = LoteRpsEnviarOutput
