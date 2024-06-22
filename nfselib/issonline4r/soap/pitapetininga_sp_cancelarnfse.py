from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "Abrasf2"


@dataclass
class CancelarNfseExecute:
    class Meta:
        name = "CancelarNfse.Execute"
        namespace = "Abrasf2"

    Entrada: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CancelarNfseExecuteResponse:
    class Meta:
        name = "CancelarNfse.ExecuteResponse"
        namespace = "Abrasf2"

    Resposta: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CancelarNfseSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CancelarNfseSoapPortExecuteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseExecute: Optional[CancelarNfseExecute] = field(
            default=None,
            metadata={
                "name": "CancelarNfse.Execute",
                "type": "Element",
                "namespace": "Abrasf2",
            },
        )


@dataclass
class CancelarNfseSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CancelarNfseSoapPortExecuteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseExecuteResponse: Optional[CancelarNfseExecuteResponse] = (
            field(
                default=None,
                metadata={
                    "name": "CancelarNfse.ExecuteResponse",
                    "type": "Element",
                    "namespace": "Abrasf2",
                },
            )
        )
        Fault: Optional["CancelarNfseSoapPortExecuteOutput.Body.Fault"] = (
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


class CancelarNfseSoapPortExecute:
    style = "document"
    location = "https://itapetininga.jlsoft.com.br/Abrasf/acancelarnfse.aspx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "Abrasf2action/ACANCELARNFSE.Execute"
    input = CancelarNfseSoapPortExecuteInput
    output = CancelarNfseSoapPortExecuteOutput
