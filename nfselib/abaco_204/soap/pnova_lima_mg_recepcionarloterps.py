from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class A24RecepcionarLoteRpsExecute:
    class Meta:
        name = "A24_RecepcionarLoteRps.Execute"
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
class A24RecepcionarLoteRpsExecuteResponse:
    class Meta:
        name = "A24_RecepcionarLoteRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A24RecepcionarLoteRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24RecepcionarLoteRpsSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_RecepcionarLoteRpsExecute: Optional[
            A24RecepcionarLoteRpsExecute
        ] = field(
            default=None,
            metadata={
                "name": "A24_RecepcionarLoteRps.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class A24RecepcionarLoteRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["A24RecepcionarLoteRpsSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        A24_RecepcionarLoteRpsExecuteResponse: Optional[
            A24RecepcionarLoteRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "A24_RecepcionarLoteRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "A24RecepcionarLoteRpsSoapPortExecuteOutput.Body.Fault"
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


class A24RecepcionarLoteRpsSoapPortExecute:
    style = "document"
    location = "https://www.e-nfs.com.br/e-nfs_novalima/servlet/aa24_recepcionarloterps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.e-nfs.com.braction/AA24_RECEPCIONARLOTERPS.Execute"
    )
    input = A24RecepcionarLoteRpsSoapPortExecuteInput
    output = A24RecepcionarLoteRpsSoapPortExecuteOutput
