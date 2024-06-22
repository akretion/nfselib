from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class MCancelamentoNfse:
    class Meta:
        name = "mCancelamentoNFSe"
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
class MCancelamentoNfseResponse:
    class Meta:
        name = "mCancelamentoNFSeResponse"
        namespace = "http://tempuri.org/"

    mCancelamentoNFSeResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelamentoNfseSoapMCancelamentoNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CancelamentoNfseSoapMCancelamentoNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mCancelamentoNFSe: Optional[MCancelamentoNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class CancelamentoNfseSoapMCancelamentoNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CancelamentoNfseSoapMCancelamentoNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mCancelamentoNFSeResponse: Optional[MCancelamentoNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "CancelamentoNfseSoapMCancelamentoNfseOutput.Body.Fault"
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


class CancelamentoNfseSoapMCancelamentoNfse:
    style = "document"
    location = "http://dois.nfse-tecnos.com.br:9098/CancelamentoNFSe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/mCancelamentoNFSe"
    input = CancelamentoNfseSoapMCancelamentoNfseInput
    output = CancelamentoNfseSoapMCancelamentoNfseOutput
