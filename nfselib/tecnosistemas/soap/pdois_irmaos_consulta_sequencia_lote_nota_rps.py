from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MConsultaSequenciaLoteNotaRps:
    class Meta:
        name = "mConsultaSequenciaLoteNotaRPS"
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
class MConsultaSequenciaLoteNotaRpsresponse:
    class Meta:
        name = "mConsultaSequenciaLoteNotaRPSResponse"
        namespace = "http://tempuri.org/"

    mConsultaSequenciaLoteNotaRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaSequenciaLoteNotaRPS: Optional[
            MConsultaSequenciaLoteNotaRps
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaSequenciaLoteNotaRPSResponse: Optional[
            MConsultaSequenciaLoteNotaRpsresponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsOutput.Body.Fault"
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


class ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRps:
    style = "document"
    location = (
        "http://dois.nfse-tecnos.com.br:9084/ConsultaSequenciaLoteNotaRPS.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mConsultaSequenciaLoteNotaRPS"
    input = ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsInput
    output = (
        ConsultaSequenciaLoteNotaRpssoapMConsultaSequenciaLoteNotaRpsOutput
    )
