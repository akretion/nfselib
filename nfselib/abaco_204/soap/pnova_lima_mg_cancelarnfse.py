from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24CancelarNfseExecute:
    class Meta:
        name = "A24_CancelarNfse.Execute"
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
class A24CancelarNfseExecuteResponse:
    class Meta:
        name = "A24_CancelarNfse.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24CancelarNfseSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24CancelarNfseSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_CancelarNfseExecute: Optional[A24CancelarNfseExecute] = field(
            default=None,
            metadata={
                "name": "A24_CancelarNfse.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class A24CancelarNfseSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24CancelarNfseSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_CancelarNfseExecuteResponse: Optional[
            A24CancelarNfseExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "A24_CancelarNfse.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional["A24CancelarNfseSoapPortExecuteOutput.Body.Fault"] = (
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


class A24CancelarNfseSoapPortExecute:
    style = "document"
    location = "https://www.e-nfs.com.br/e-nfs_novalima/servlet/acancelarnfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/AA24_CANCELARNFSE.Execute"
    input = A24CancelarNfseSoapPortExecuteInput
    output = A24CancelarNfseSoapPortExecuteOutput
