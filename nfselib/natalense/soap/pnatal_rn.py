from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class Input:
    class Meta:
        name = "input"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Output:
    class Meta:
        name = "output"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class CancelarNfseRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class CancelarNfseResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarLoteRpsRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarLoteRpsResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarNfseRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarNfseResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarSituacaoLoteRpsRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class ConsultarSituacaoLoteRpsResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class RecepcionarLoteRpsRequest(Input):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class RecepcionarLoteRpsResponse(Output):
    class Meta:
        namespace = "https://wsnfsev1.natal.rn.gov.br:8444"


@dataclass
class NfseCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseCancelarNfseInput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )


@dataclass
class NfseCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseCancelarNfseOutput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )
        Fault: Optional["NfseCancelarNfseOutput.Body.Fault"] = field(
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
class NfseConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )


@dataclass
class NfseConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )
        Fault: Optional["NfseConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsInput.Body"] = field(
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
                    "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
                },
            )
        )


@dataclass
class NfseConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
                },
            )
        )
        Fault: Optional["NfseConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseInput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )


@dataclass
class NfseConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseOutput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )
        Fault: Optional["NfseConsultarNfseOutput.Body.Fault"] = field(
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
class NfseConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarSituacaoLoteRpsInput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )


@dataclass
class NfseConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )
        Fault: Optional["NfseConsultarSituacaoLoteRpsOutput.Body.Fault"] = (
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
class NfseRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
            },
        )


@dataclass
class NfseRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "https://wsnfsev1.natal.rn.gov.br:8444",
                },
            )
        )
        Fault: Optional["NfseRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class NfseCancelarNfse:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/CancelarNfse"
    )
    input = NfseCancelarNfseInput
    output = NfseCancelarNfseOutput


class NfseConsultarLoteRps:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/ConsultarLoteRps"
    )
    input = NfseConsultarLoteRpsInput
    output = NfseConsultarLoteRpsOutput


class NfseConsultarNfse:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/ConsultarNfse"
    )
    input = NfseConsultarNfseInput
    output = NfseConsultarNfseOutput


class NfseConsultarNfsePorRps:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/ConsultarNfsePorRps"
    input = NfseConsultarNfsePorRpsInput
    output = NfseConsultarNfsePorRpsOutput


class NfseConsultarSituacaoLoteRps:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/ConsultarSituacaoLoteRps"
    input = NfseConsultarSituacaoLoteRpsInput
    output = NfseConsultarSituacaoLoteRpsOutput


class NfseRecepcionarLoteRps:
    style = "document"
    location = (
        "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/NfseWSServiceV1/"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://wsnfsev1.natal.rn.gov.br:8444/axis2/services/RecepcionarLoteRps"
    input = NfseRecepcionarLoteRpsInput
    output = NfseRecepcionarLoteRpsOutput
