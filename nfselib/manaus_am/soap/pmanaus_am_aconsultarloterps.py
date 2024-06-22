from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class ConsultarLoteRpsExecute:
    class Meta:
        name = "ConsultarLoteRps.Execute"
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
class ConsultarLoteRpsExecuteResponse:
    class Meta:
        name = "ConsultarLoteRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarLoteRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarLoteRpsSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsExecute: Optional[ConsultarLoteRpsExecute] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRps.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class ConsultarLoteRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarLoteRpsSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsExecuteResponse: Optional[
            ConsultarLoteRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional["ConsultarLoteRpsSoapPortExecuteOutput.Body.Fault"] = (
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


class ConsultarLoteRpsSoapPortExecute:
    style = "document"
    location = (
        "https://nfse-prd.manaus.am.gov.br/nfse/servlet/aconsultarloterps"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.e-nfs.com.braction/ACONSULTARLOTERPS.Execute"
    input = ConsultarLoteRpsSoapPortExecuteInput
    output = ConsultarLoteRpsSoapPortExecuteOutput
