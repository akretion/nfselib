from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class ConsultarNfsePorRpsExecute:
    class Meta:
        name = "ConsultarNfsePorRps.Execute"
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
class ConsultarNfsePorRpsExecuteResponse:
    class Meta:
        name = "ConsultarNfsePorRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarNfsePorRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsExecute: Optional[ConsultarNfsePorRpsExecute] = (
            field(
                default=None,
                metadata={
                    "name": "ConsultarNfsePorRps.Execute",
                    "type": "Element",
                    "namespace": "http://www.e-nfs.com.br",
                },
            )
        )


@dataclass
class ConsultarNfsePorRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsExecuteResponse: Optional[
            ConsultarNfsePorRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "ConsultarNfsePorRpsSoapPortExecuteOutput.Body.Fault"
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


class ConsultarNfsePorRpsSoapPortExecute:
    style = "document"
    location = (
        "https://nfse-prd.manaus.am.gov.br/nfse/servlet/aconsultarnfseporrps"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/ACONSULTARNFSEPORRPS.Execute"
    input = ConsultarNfsePorRpsSoapPortExecuteInput
    output = ConsultarNfsePorRpsSoapPortExecuteOutput
