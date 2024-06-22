from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MEnvioLoteRpssincrono:
    class Meta:
        name = "mEnvioLoteRPSSincrono"
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
class MEnvioLoteRpssincronoResponse:
    class Meta:
        name = "mEnvioLoteRPSSincronoResponse"
        namespace = "http://tempuri.org/"

    mEnvioLoteRPSSincronoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mEnvioLoteRPSSincrono: Optional[MEnvioLoteRpssincrono] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mEnvioLoteRPSSincronoResponse: Optional[
            MEnvioLoteRpssincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoOutput.Body.Fault"
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


class EnvioLoteRpssincronoSoapMEnvioLoteRpssincrono:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9091/EnvioLoteRPSSincrono.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mEnvioLoteRPSSincrono"
    input = EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoInput
    output = EnvioLoteRpssincronoSoapMEnvioLoteRpssincronoOutput
