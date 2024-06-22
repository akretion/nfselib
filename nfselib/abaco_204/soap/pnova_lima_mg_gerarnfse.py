from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24GerarNfseExecute:
    class Meta:
        name = "A24_GerarNfse.Execute"
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
class A24GerarNfseExecuteResponse:
    class Meta:
        name = "A24_GerarNfse.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24GerarNfseSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24GerarNfseSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_GerarNfseExecute: Optional[A24GerarNfseExecute] = field(
            default=None,
            metadata={
                "name": "A24_GerarNfse.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class A24GerarNfseSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24GerarNfseSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_GerarNfseExecuteResponse: Optional[A24GerarNfseExecuteResponse] = (
            field(
                default=None,
                metadata={
                    "name": "A24_GerarNfse.ExecuteResponse",
                    "type": "Element",
                    "namespace": "http://www.e-nfs.com.br",
                },
            )
        )
        Fault: Optional["A24GerarNfseSoapPortExecuteOutput.Body.Fault"] = (
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


class A24GerarNfseSoapPortExecute:
    style = "document"
    location = "https://www.e-nfs.com.br/e-nfs_novalima/servlet/aa24_gerarnfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/AA24_GERARNFSE.Execute"
    input = A24GerarNfseSoapPortExecuteInput
    output = A24GerarNfseSoapPortExecuteOutput
