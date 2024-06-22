from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class IconsultaNfseConsultarNfseComplementarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseConsultarNfseComplementarInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseComplementar: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class IconsultaNfseConsultarNfseComplementarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseConsultarNfseComplementarOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseComplementarResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "IconsultaNfseConsultarNfseComplementarOutput.Body.Fault"
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
class IconsultaNfseConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseConsultarNfseInput.Body"] = field(
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
class IconsultaNfseConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseConsultarNfseOutput.Body"] = field(
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
        Fault: Optional["IconsultaNfseConsultarNfseOutput.Body.Fault"] = field(
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


class IconsultaNfseConsultarNfse:
    URI = "#ConsultaNfseBinding_policy"
    style = "document"
    location = (
        "https://nfse.salvador.ba.gov.br/rps/CONSULTANFSE/ConsultaNfse.svc"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/IConsultaNfse/ConsultarNfse"
    input = IconsultaNfseConsultarNfseInput
    output = IconsultaNfseConsultarNfseOutput


class IconsultaNfseConsultarNfseComplementar:
    URI = "#ConsultaNfseBinding_policy"
    style = "document"
    location = (
        "https://nfse.salvador.ba.gov.br/rps/CONSULTANFSE/ConsultaNfse.svc"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/IConsultaNfse/ConsultarNfseComplementar"
    input = IconsultaNfseConsultarNfseComplementarInput
    output = IconsultaNfseConsultarNfseComplementarOutput
