from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MConsultaNfsePorFaixa:
    class Meta:
        name = "mConsultaNFSePorFaixa"
        namespace = "http://tempuri.org/"

    remessa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class MConsultaNfsePorFaixaResponse:
    class Meta:
        name = "mConsultaNFSePorFaixaResponse"
        namespace = "http://tempuri.org/"

    mConsultaNFSePorFaixaResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaNFSePorFaixa: Optional[MConsultaNfsePorFaixa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaNFSePorFaixaResponse: Optional[
            MConsultaNfsePorFaixaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaOutput.Body.Fault"
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


class ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixa:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9096/ConsultaNFSePorFaixa.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mConsultaNFSePorFaixa"
    input = ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaInput
    output = ConsultaNfsePorFaixaSoapMConsultaNfsePorFaixaOutput
