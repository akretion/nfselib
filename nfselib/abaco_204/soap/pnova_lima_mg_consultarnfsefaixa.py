from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24ConsultarNfseFaixaExecute:
    class Meta:
        name = "A24_ConsultarNfseFaixa.Execute"
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
class A24ConsultarNfseFaixaExecuteResponse:
    class Meta:
        name = "A24_ConsultarNfseFaixa.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24ConsultarNfseFaixaSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarNfseFaixaSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarNfseFaixaExecute: Optional[
            A24ConsultarNfseFaixaExecute
        ] = field(
            default=None,
            metadata={
                "name": "A24_ConsultarNfseFaixa.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class A24ConsultarNfseFaixaSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarNfseFaixaSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarNfseFaixaExecuteResponse: Optional[
            A24ConsultarNfseFaixaExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "A24_ConsultarNfseFaixa.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "A24ConsultarNfseFaixaSoapPortExecuteOutput.Body.Fault"
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


class A24ConsultarNfseFaixaSoapPortExecute:
    style = "document"
    location = "https://177.101.149.237:9190/e-nfs_novalima/servlet/aa24_consultarnfsefaixa"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.e-nfs.com.braction/AA24_CONSULTARNFSEFAIXA.Execute"
    )
    input = A24ConsultarNfseFaixaSoapPortExecuteInput
    output = A24ConsultarNfseFaixaSoapPortExecuteOutput
