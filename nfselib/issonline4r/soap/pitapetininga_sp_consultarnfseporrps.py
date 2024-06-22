from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Abrasf2"


@dataclass
class ConsultarNfsePorRpsExecute:
    class Meta:
        name = "ConsultarNfsePorRps.Execute"
        namespace = "Abrasf2"

    Entrada: Optional[str] = field(
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
        namespace = "Abrasf2"

    Resposta: Optional[str] = field(
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
                    "namespace": "Abrasf2",
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
                "namespace": "Abrasf2",
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
        "https://itapetininga.jlsoft.com.br/Abrasf/aconsultarnfseporrps.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "Abrasf2action/ACONSULTARNFSEPORRPS.Execute"
    input = ConsultarNfsePorRpsSoapPortExecuteInput
    output = ConsultarNfsePorRpsSoapPortExecuteOutput
