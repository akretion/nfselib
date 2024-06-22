from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24ConsultarNfsePorRpsExecute:
    class Meta:
        name = "A24_ConsultarNfsePorRps.Execute"
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
class A24ConsultarNfsePorRpsExecuteResponse:
    class Meta:
        name = "A24_ConsultarNfsePorRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24ConsultarNfsePorRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarNfsePorRpsSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarNfsePorRpsExecute: Optional[
            A24ConsultarNfsePorRpsExecute
        ] = field(
            default=None,
            metadata={
                "name": "A24_ConsultarNfsePorRps.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class A24ConsultarNfsePorRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24ConsultarNfsePorRpsSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_ConsultarNfsePorRpsExecuteResponse: Optional[
            A24ConsultarNfsePorRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "A24_ConsultarNfsePorRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "A24ConsultarNfsePorRpsSoapPortExecuteOutput.Body.Fault"
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


class A24ConsultarNfsePorRpsSoapPortExecute:
    style = "document"
    location = "https://www.e-nfs.com.br/e-nfs_novalima/servlet/aa24_consultarnfseporrps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.e-nfs.com.braction/AA24_CONSULTARNFSEPORRPS.Execute"
    )
    input = A24ConsultarNfsePorRpsSoapPortExecuteInput
    output = A24ConsultarNfsePorRpsSoapPortExecuteOutput
