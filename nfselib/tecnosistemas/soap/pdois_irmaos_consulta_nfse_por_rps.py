from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MConsultaNfsePorRps:
    class Meta:
        name = "mConsultaNFSePorRPS"
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
class MConsultaNfsePorRpsresponse:
    class Meta:
        name = "mConsultaNFSePorRPSResponse"
        namespace = "http://tempuri.org/"

    mConsultaNFSePorRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNfsePorRpssoapMConsultaNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultaNfsePorRpssoapMConsultaNfsePorRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        mConsultaNFSePorRPS: Optional[MConsultaNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class ConsultaNfsePorRpssoapMConsultaNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultaNfsePorRpssoapMConsultaNfsePorRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        mConsultaNFSePorRPSResponse: Optional[MConsultaNfsePorRpsresponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional[
            "ConsultaNfsePorRpssoapMConsultaNfsePorRpsOutput.Body.Fault"
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


class ConsultaNfsePorRpssoapMConsultaNfsePorRps:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9095/ConsultaNFSePorRPS.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mConsultaNFSePorRPS"
    input = ConsultaNfsePorRpssoapMConsultaNfsePorRpsInput
    output = ConsultaNfsePorRpssoapMConsultaNfsePorRpsOutput
