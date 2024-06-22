from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class ConsultarNfseExecute:
    class Meta:
        name = "ConsultarNfse.Execute"
        namespace = "http://www.e-nfs.com.br"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarNfseExecuteResponse:
    class Meta:
        name = "ConsultarNfse.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarNfseSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfseSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseExecute: Optional[ConsultarNfseExecute] = field(
            default=None,
            metadata={
                "name": "ConsultarNfse.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class ConsultarNfseSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfseSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseExecuteResponse: Optional[
            ConsultarNfseExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarNfse.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional["ConsultarNfseSoapPortExecuteOutput.Body.Fault"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
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


class ConsultarNfseSoapPortExecute:
    style = "document"
    location = "https://nfse-prd.manaus.am.gov.br/nfse/servlet/aconsultarnfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/ACONSULTARNFSE.Execute"
    input = ConsultarNfseSoapPortExecuteInput
    output = ConsultarNfseSoapPortExecuteOutput
