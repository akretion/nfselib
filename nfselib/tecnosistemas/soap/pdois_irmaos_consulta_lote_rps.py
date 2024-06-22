from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MConsultaLoteRps:
    class Meta:
        name = "mConsultaLoteRPS"
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
class MConsultaLoteRpsresponse:
    class Meta:
        name = "mConsultaLoteRPSResponse"
        namespace = "http://tempuri.org/"

    mConsultaLoteRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaLoteRpssoapMConsultaLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultaLoteRpssoapMConsultaLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaLoteRPS: Optional[MConsultaLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class ConsultaLoteRpssoapMConsultaLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultaLoteRpssoapMConsultaLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaLoteRPSResponse: Optional[MConsultaLoteRpsresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "ConsultaLoteRpssoapMConsultaLoteRpsOutput.Body.Fault"
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


class ConsultaLoteRpssoapMConsultaLoteRps:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9097/ConsultaLoteRPS.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mConsultaLoteRPS"
    input = ConsultaLoteRpssoapMConsultaLoteRpsInput
    output = ConsultaLoteRpssoapMConsultaLoteRpsOutput
