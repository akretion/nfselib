from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Abrasf2"


@dataclass
class RecepcionarLoteRpsSincronoExecute:
    class Meta:
        name = "RecepcionarLoteRpsSincrono.Execute"
        namespace = "Abrasf2"

    Entrada: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoExecuteResponse:
    class Meta:
        name = "RecepcionarLoteRpsSincrono.ExecuteResponse"
        namespace = "Abrasf2"

    Resposta: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RecepcionarLoteRpsSincronoSoapPortExecuteInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoExecute: Optional[
            RecepcionarLoteRpsSincronoExecute
        ] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsSincrono.Execute",
                "type": "Element",
                "namespace": "Abrasf2",
            },
        )


@dataclass
class RecepcionarLoteRpsSincronoSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RecepcionarLoteRpsSincronoSoapPortExecuteOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoExecuteResponse: Optional[
            RecepcionarLoteRpsSincronoExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsSincrono.ExecuteResponse",
                "type": "Element",
                "namespace": "Abrasf2",
            },
        )
        Fault: Optional[
            "RecepcionarLoteRpsSincronoSoapPortExecuteOutput.Body.Fault"
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


class RecepcionarLoteRpsSincronoSoapPortExecute:
    style = "document"
    location = "https://itapetininga.jlsoft.com.br/Abrasf/arecepcionarloterpssincrono.aspx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "Abrasf2action/ARECEPCIONARLOTERPSSINCRONO.Execute"
    input = RecepcionarLoteRpsSincronoSoapPortExecuteInput
    output = RecepcionarLoteRpsSincronoSoapPortExecuteOutput
