from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://notacarioca.rio.gov.br/"


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NfseSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseRequest: Optional[CancelarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )
        Fault: Optional["NfseSoapCancelarNfseOutput.Body.Fault"] = field(
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
class NfseSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsRequest: Optional[ConsultarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )
        Fault: Optional["NfseSoapConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsRequest: Optional[ConsultarNfsePorRpsRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://notacarioca.rio.gov.br/",
                },
            )
        )


@dataclass
class NfseSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[ConsultarNfsePorRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://notacarioca.rio.gov.br/",
                },
            )
        )
        Fault: Optional["NfseSoapConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class NfseSoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRequest: Optional[ConsultarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )
        Fault: Optional["NfseSoapConsultarNfseOutput.Body.Fault"] = field(
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
class NfseSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsRequest: Optional[
            ConsultarSituacaoLoteRpsRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsResponse: Optional[
            ConsultarSituacaoLoteRpsResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )
        Fault: Optional[
            "NfseSoapConsultarSituacaoLoteRpsOutput.Body.Fault"
        ] = field(
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
class NfseSoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseRequest: Optional[GerarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseResponse: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )
        Fault: Optional["NfseSoapGerarNfseOutput.Body.Fault"] = field(
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
class NfseSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsRequest: Optional[RecepcionarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            },
        )


@dataclass
class NfseSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[RecepcionarLoteRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://notacarioca.rio.gov.br/",
                },
            )
        )
        Fault: Optional["NfseSoapRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class NfseSoapCancelarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/CancelarNfse"
    input = NfseSoapCancelarNfseInput
    output = NfseSoapCancelarNfseOutput


class NfseSoapConsultarLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/ConsultarLoteRps"
    input = NfseSoapConsultarLoteRpsInput
    output = NfseSoapConsultarLoteRpsOutput


class NfseSoapConsultarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/ConsultarNfse"
    input = NfseSoapConsultarNfseInput
    output = NfseSoapConsultarNfseOutput


class NfseSoapConsultarNfsePorRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/ConsultarNfsePorRps"
    input = NfseSoapConsultarNfsePorRpsInput
    output = NfseSoapConsultarNfsePorRpsOutput


class NfseSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/ConsultarSituacaoLoteRps"
    input = NfseSoapConsultarSituacaoLoteRpsInput
    output = NfseSoapConsultarSituacaoLoteRpsOutput


class NfseSoapGerarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/GerarNfse"
    input = NfseSoapGerarNfseInput
    output = NfseSoapGerarNfseOutput


class NfseSoapRecepcionarLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://notacarioca.rio.gov.br/RecepcionarLoteRps"
    input = NfseSoapRecepcionarLoteRpsInput
    output = NfseSoapRecepcionarLoteRpsOutput
