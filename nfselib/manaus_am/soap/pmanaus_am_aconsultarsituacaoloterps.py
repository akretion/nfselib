from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.e-nfs.com.br"


@dataclass
class ConsultarSituacaoLoteRpsExecute:
    class Meta:
        name = "ConsultarSituacaoLoteRps.Execute"
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
class ConsultarSituacaoLoteRpsExecuteResponse:
    class Meta:
        name = "ConsultarSituacaoLoteRps.ExecuteResponse"
        namespace = "http://www.e-nfs.com.br"

    Outputxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsSoapPortExecuteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarSituacaoLoteRpsSoapPortExecuteInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsExecute: Optional[
            ConsultarSituacaoLoteRpsExecute
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRps.Execute",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )


@dataclass
class ConsultarSituacaoLoteRpsSoapPortExecuteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarSituacaoLoteRpsSoapPortExecuteOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsExecuteResponse: Optional[
            ConsultarSituacaoLoteRpsExecuteResponse
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRps.ExecuteResponse",
                "type": "Element",
                "namespace": "http://www.e-nfs.com.br",
            },
        )
        Fault: Optional[
            "ConsultarSituacaoLoteRpsSoapPortExecuteOutput.Body.Fault"
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


class ConsultarSituacaoLoteRpsSoapPortExecute:
    style = "document"
    location = "https://nfse-prd.manaus.am.gov.br/nfse/servlet/aconsultarsituacaoloterps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.e-nfs.com.braction/ACONSULTARSITUACAOLOTERPS.Execute"
    )
    input = ConsultarSituacaoLoteRpsSoapPortExecuteInput
    output = ConsultarSituacaoLoteRpsSoapPortExecuteOutput
