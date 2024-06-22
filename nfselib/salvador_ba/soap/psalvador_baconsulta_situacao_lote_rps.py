from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRPS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRPSResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsOutput.Body.Fault"
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


class IconsultaSituacaoLoteRpsConsultarSituacaoLoteRps:
    URI = "#ConsultaSituacaoLoteRPSBinding_policy"
    style = "document"
    location = "https://nfse.salvador.ba.gov.br/rps/CONSULTASITUACAOLOTERPS/ConsultaSituacaoLoteRPS.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/IConsultaSituacaoLoteRPS/ConsultarSituacaoLoteRPS"
    )
    input = IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsInput
    output = IconsultaSituacaoLoteRpsConsultarSituacaoLoteRpsOutput
