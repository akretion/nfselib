from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class IconsultaNfseRpsConsultarNfseRpscomplementarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IconsultaNfseRpsConsultarNfseRpscomplementarInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRPSComplementar: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class IconsultaNfseRpsConsultarNfseRpscomplementarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IconsultaNfseRpsConsultarNfseRpscomplementarOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRPSComplementarResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "IconsultaNfseRpsConsultarNfseRpscomplementarOutput.Body.Fault"
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
class IconsultaNfseRpsConsultarNfseRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseRpsConsultarNfseRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRPS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class IconsultaNfseRpsConsultarNfseRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaNfseRpsConsultarNfseRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRPSResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "IconsultaNfseRpsConsultarNfseRpsOutput.Body.Fault"
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


class IconsultaNfseRpsConsultarNfseRps:
    URI = "#ConsultaNfseRPSBinding_policy"
    style = "document"
    location = "https://nfse.salvador.ba.gov.br/rps/CONSULTANFSERPS/ConsultaNfseRPS.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/IConsultaNfseRPS/ConsultarNfseRPS"
    input = IconsultaNfseRpsConsultarNfseRpsInput
    output = IconsultaNfseRpsConsultarNfseRpsOutput


class IconsultaNfseRpsConsultarNfseRpscomplementar:
    URI = "#ConsultaNfseRPSBinding_policy"
    style = "document"
    location = "https://nfse.salvador.ba.gov.br/rps/CONSULTANFSERPS/ConsultaNfseRPS.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/IConsultaNfseRPS/ConsultarNfseRPSComplementar"
    )
    input = IconsultaNfseRpsConsultarNfseRpscomplementarInput
    output = IconsultaNfseRpsConsultarNfseRpscomplementarOutput
