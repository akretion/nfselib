from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfse.recife.pe.gov.br/"


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    inputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://nfse.recife.pe.gov.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NfseV01SoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapCancelarNfseInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )
        Fault: Optional["NfseV01SoapCancelarNfseOutput.Body.Fault"] = field(
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
class NfseV01SoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )
        Fault: Optional["NfseV01SoapConsultarLoteRpsOutput.Body.Fault"] = (
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
class NfseV01SoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarNfsePorRpsInput.Body"] = field(
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
                    "namespace": "http://nfse.recife.pe.gov.br/",
                },
            )
        )


@dataclass
class NfseV01SoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.recife.pe.gov.br/",
                },
            )
        )
        Fault: Optional["NfseV01SoapConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class NfseV01SoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarNfseInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )
        Fault: Optional["NfseV01SoapConsultarNfseOutput.Body.Fault"] = field(
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
class NfseV01SoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarSituacaoLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )
        Fault: Optional[
            "NfseV01SoapConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class NfseV01SoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapGerarNfseInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapGerarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )
        Fault: Optional["NfseV01SoapGerarNfseOutput.Body.Fault"] = field(
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
class NfseV01SoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse.recife.pe.gov.br/",
            },
        )


@dataclass
class NfseV01SoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseV01SoapRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.recife.pe.gov.br/",
                },
            )
        )
        Fault: Optional["NfseV01SoapRecepcionarLoteRpsOutput.Body.Fault"] = (
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


class NfseV01SoapCancelarNfse:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/CancelarNfse"
    input = NfseV01SoapCancelarNfseInput
    output = NfseV01SoapCancelarNfseOutput


class NfseV01SoapConsultarLoteRps:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/ConsultarLoteRps"
    input = NfseV01SoapConsultarLoteRpsInput
    output = NfseV01SoapConsultarLoteRpsOutput


class NfseV01SoapConsultarNfse:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/ConsultarNfse"
    input = NfseV01SoapConsultarNfseInput
    output = NfseV01SoapConsultarNfseOutput


class NfseV01SoapConsultarNfsePorRps:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/ConsultarNfsePorRps"
    input = NfseV01SoapConsultarNfsePorRpsInput
    output = NfseV01SoapConsultarNfsePorRpsOutput


class NfseV01SoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/ConsultarSituacaoLoteRps"
    input = NfseV01SoapConsultarSituacaoLoteRpsInput
    output = NfseV01SoapConsultarSituacaoLoteRpsOutput


class NfseV01SoapGerarNfse:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/GerarNfse"
    input = NfseV01SoapGerarNfseInput
    output = NfseV01SoapGerarNfseOutput


class NfseV01SoapRecepcionarLoteRps:
    style = "document"
    location = "https://nfse.recife.pe.gov.br/WSNacional/nfse_v01.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.recife.pe.gov.br/RecepcionarLoteRps"
    input = NfseV01SoapRecepcionarLoteRpsInput
    output = NfseV01SoapRecepcionarLoteRpsOutput
