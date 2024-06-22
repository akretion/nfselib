from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class InfseconsultasConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfseconsultasConsultarLoteRpsOutput.Body.Fault"] = (
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
class InfseconsultasConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarNfsePorRpsOutput.Body.Fault"
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
class InfseconsultasConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfseconsultasConsultarNfseOutput.Body.Fault"] = (
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
class InfseconsultasConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfseconsultasConsultarSituacaoLoteRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class InfsegeracaoCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfsegeracaoCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfsegeracaoCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoCancelarNfseOutput.Body.Fault"] = field(
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
class InfsegeracaoRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfsegeracaoRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InfsegeracaoRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoRecepcionarLoteRpsOutput.Body.Fault"] = (
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


class InfseconsultasConsultarLoteRps:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarLoteRps"
    input = InfseconsultasConsultarLoteRpsInput
    output = InfseconsultasConsultarLoteRpsOutput


class InfseconsultasConsultarNfse:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfse"
    input = InfseconsultasConsultarNfseInput
    output = InfseconsultasConsultarNfseOutput


class InfseconsultasConsultarNfsePorRps:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfsePorRps"
    input = InfseconsultasConsultarNfsePorRpsInput
    output = InfseconsultasConsultarNfsePorRpsOutput


class InfseconsultasConsultarSituacaoLoteRps:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarSituacaoLoteRps"
    input = InfseconsultasConsultarSituacaoLoteRpsInput
    output = InfseconsultasConsultarSituacaoLoteRpsOutput


class InfsegeracaoCancelarNfse:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/CancelarNfse"
    input = InfsegeracaoCancelarNfseInput
    output = InfsegeracaoCancelarNfseOutput


class InfsegeracaoRecepcionarLoteRps:
    style = "document"
    location = "http://deiss.triunfo.rs.gov.br:90/NFSEWS/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/RecepcionarLoteRps"
    input = InfsegeracaoRecepcionarLoteRpsInput
    output = InfsegeracaoRecepcionarLoteRpsOutput
