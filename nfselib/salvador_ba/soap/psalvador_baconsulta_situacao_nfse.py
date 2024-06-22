from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class IconsultaSituacaoNfseConsultarSituacaoNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaSituacaoNfseConsultarSituacaoNfseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class IconsultaSituacaoNfseConsultarSituacaoNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IconsultaSituacaoNfseConsultarSituacaoNfseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "IconsultaSituacaoNfseConsultarSituacaoNfseOutput.Body.Fault"
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


class IconsultaSituacaoNfseConsultarSituacaoNfse:
    URI = "#ConsultaSituacaoNfseBinding_policy"
    style = "document"
    location = "https://nfse.salvador.ba.gov.br/rps/CONSULTASITUACAONFSE/ConsultaSituacaoNfse.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/IConsultaSituacaoNfse/ConsultarSituacaoNfse"
    )
    input = IconsultaSituacaoNfseConsultarSituacaoNfseInput
    output = IconsultaSituacaoNfseConsultarSituacaoNfseOutput
