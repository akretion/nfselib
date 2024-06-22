from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24ConsultarLoteRpsExecute:
    class Meta:
        name = "A24_ConsultarLoteRps.Execute"
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
class A24ConsultarLoteRpsExecuteResponse:
    class Meta:
        name = "A24_ConsultarLoteRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24ConsultarLoteRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarLoteRpsSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarLoteRpsExecute: Optional[A24ConsultarLoteRpsExecute] = (
            field(
                default=None,
                metadata={
                    "name": "A24_ConsultarLoteRps.Execute",
                    "type": "Element",
                    "namespace": "http://www.e-nfs.com.br",
                },
            )
        )


@dataclass
class A24ConsultarLoteRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarLoteRpsSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarLoteRpsExecuteResponse: Optional[
            A24ConsultarLoteRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "A24_ConsultarLoteRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "A24ConsultarLoteRpsSoapPortExecuteOutput.Body.Fault"
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


class A24ConsultarLoteRpsSoapPortExecute:
    style = "document"
    location = (
        "https://www.e-nfs.com.br/e-nfs_novalima/servlet/aa24_consultarloterps"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/AA24_CONSULTARLOTERPS.Execute"
    input = A24ConsultarLoteRpsSoapPortExecuteInput
    output = A24ConsultarLoteRpsSoapPortExecuteOutput
