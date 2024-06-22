from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://ws.megasoftarrecadanet.com.br"


@dataclass
class Input:
    class Meta:
        name = "input"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Output:
    class Meta:
        name = "output"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "http://ws.megasoftarrecadanet.com.br"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "http://ws.megasoftarrecadanet.com.br"


@dataclass
class GerarNfseRequest(Input):
    class Meta:
        namespace = "http://ws.megasoftarrecadanet.com.br"


@dataclass
class GerarNfseResponse(Output):
    class Meta:
        namespace = "http://ws.megasoftarrecadanet.com.br"


@dataclass
class NfseConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsRequest: Optional[ConsultarNfsePorRpsRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.megasoftarrecadanet.com.br",
                },
            )
        )


@dataclass
class NfseConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[ConsultarNfsePorRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.megasoftarrecadanet.com.br",
                },
            )
        )
        Fault: Optional["NfseConsultarNfsePorRpsOutput.Body.Fault"] = field(
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


@dataclass
class NfseGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseRequest: Optional[GerarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.megasoftarrecadanet.com.br",
            },
        )


@dataclass
class NfseGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseResponse: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.megasoftarrecadanet.com.br",
            },
        )
        Fault: Optional["NfseGerarNfseOutput.Body.Fault"] = field(
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


class NfseConsultarNfsePorRps:
    style = "document"
    location = "https://padrebernardo.megasoftarrecadanet.com.br/padrebernardo/ws/nfseSOAP"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.megasoftarrecadanet.com.br/ConsultarNfsePorRps"
    input = NfseConsultarNfsePorRpsInput
    output = NfseConsultarNfsePorRpsOutput


class NfseGerarNfse:
    style = "document"
    location = "https://padrebernardo.megasoftarrecadanet.com.br/padrebernardo/ws/nfseSOAP"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://ws.megasoftarrecadanet.com.br/GerarNfse"
    input = NfseGerarNfseInput
    output = NfseGerarNfseOutput
