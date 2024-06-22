from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MConsultaNfseServicosPrestados:
    class Meta:
        name = "mConsultaNFSeServicosPrestados"
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
class MConsultaNfseServicosPrestadosResponse:
    class Meta:
        name = "mConsultaNFSeServicosPrestadosResponse"
        namespace = "http://tempuri.org/"

    mConsultaNFSeServicosPrestadosResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaNFSeServicosPrestados: Optional[
            MConsultaNfseServicosPrestados
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mConsultaNFSeServicosPrestadosResponse: Optional[
            MConsultaNfseServicosPrestadosResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosOutput.Body.Fault"
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


class ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestados:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9094/ConsultaNFSeServicosPrestados.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mConsultaNFSeServicosPrestados"
    input = (
        ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosInput
    )
    output = (
        ConsultaNfseServicosPrestadosSoapMConsultaNfseServicosPrestadosOutput
    )
