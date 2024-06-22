from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://NFSe.wsservices.systempro.com.br/"


@dataclass
class NfseServiceCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceCancelarNfseInput.Body"] = field(
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
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )


@dataclass
class NfseServiceCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )
        Fault: Optional["NfseServiceCancelarNfseOutput.Body.Fault"] = field(
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
class NfseServiceConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceConsultarNfseFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )


@dataclass
class NfseServiceConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceConsultarNfseFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )
        Fault: Optional["NfseServiceConsultarNfseFaixaOutput.Body.Fault"] = (
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
class NfseServiceEnviarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceEnviarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteRpsSincrono: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )


@dataclass
class NfseServiceEnviarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceEnviarLoteRpsSincronoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteRpsSincronoResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )
        Fault: Optional[
            "NfseServiceEnviarLoteRpsSincronoOutput.Body.Fault"
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
class NfseServiceGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )


@dataclass
class NfseServiceGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )
        Fault: Optional["NfseServiceGerarNfseOutput.Body.Fault"] = field(
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
class NfseServiceSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )


@dataclass
class NfseServiceSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseServiceSubstituirNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://NFSe.wsservices.systempro.com.br/",
            },
        )
        Fault: Optional["NfseServiceSubstituirNfseOutput.Body.Fault"] = field(
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


class NfseServiceCancelarNfse:
    style = "document"
    location = (
        "https://www.nfse.erechim.rs.gov.br:8182/NfseService/NfseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseServiceCancelarNfseInput
    output = NfseServiceCancelarNfseOutput


class NfseServiceConsultarNfseFaixa:
    style = "document"
    location = (
        "https://www.nfse.erechim.rs.gov.br:8182/NfseService/NfseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseServiceConsultarNfseFaixaInput
    output = NfseServiceConsultarNfseFaixaOutput


class NfseServiceEnviarLoteRpsSincrono:
    style = "document"
    location = (
        "https://www.nfse.erechim.rs.gov.br:8182/NfseService/NfseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseServiceEnviarLoteRpsSincronoInput
    output = NfseServiceEnviarLoteRpsSincronoOutput


class NfseServiceGerarNfse:
    style = "document"
    location = (
        "https://www.nfse.erechim.rs.gov.br:8182/NfseService/NfseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseServiceGerarNfseInput
    output = NfseServiceGerarNfseOutput


class NfseServiceSubstituirNfse:
    style = "document"
    location = (
        "https://www.nfse.erechim.rs.gov.br:8182/NfseService/NfseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseServiceSubstituirNfseInput
    output = NfseServiceSubstituirNfseOutput
