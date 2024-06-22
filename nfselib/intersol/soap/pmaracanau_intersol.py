from dataclasses import dataclass, field
from typing import Optional

from nfselib.intersol.soap.nfes_xsd_1 import (
    ConsultarLoteRps,
    ConsultarLoteRpsResponse,
    ConsultarNfse,
    ConsultarNfsePorRps,
    ConsultarNfsePorRpsResponse,
    ConsultarNfseResponse,
    ConsultarSituacaoLoteRps,
    ConsultarSituacaoLoteRpsResponse,
    RecepcionarLoteRps,
    RecepcionarLoteRpsResponse,
)

__NAMESPACE__ = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"


@dataclass
class NfesCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
        Fault: Optional["NfesCancelarNfseOutput.Body.Fault"] = field(
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


class NfesCancelarNfse:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesCancelarNfseInput
    output = NfesCancelarNfseOutput


@dataclass
class NfesConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
        Fault: Optional["NfesConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfesConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
                },
            )
        )
        Fault: Optional["NfesConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NfesConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
        Fault: Optional["NfesConsultarNfseOutput.Body.Fault"] = field(
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
class NfesConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsResponse: Optional[
            ConsultarSituacaoLoteRpsResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )
        Fault: Optional["NfesConsultarSituacaoLoteRpsOutput.Body.Fault"] = (
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


@dataclass
class NfesRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
            },
        )


@dataclass
class NfesRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfesRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[RecepcionarLoteRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
                },
            )
        )
        Fault: Optional["NfesRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class NfesConsultarLoteRps:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesConsultarLoteRpsInput
    output = NfesConsultarLoteRpsOutput


class NfesConsultarNfse:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesConsultarNfseInput
    output = NfesConsultarNfseOutput


class NfesConsultarNfsePorRps:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesConsultarNfsePorRpsInput
    output = NfesConsultarNfsePorRpsOutput


class NfesConsultarSituacaoLoteRps:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesConsultarSituacaoLoteRpsInput
    output = NfesConsultarSituacaoLoteRpsOutput


class NfesRecepcionarLoteRps:
    style = "document"
    location = "http://speedgov.com.br:80/wsmar/Nfes"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfesRecepcionarLoteRpsInput
    output = NfesRecepcionarLoteRpsOutput
