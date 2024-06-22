from dataclasses import dataclass, field
from typing import Optional

from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd0 import (
    Cancelar,
    CancelarResponse,
    Consultar,
    ConsultarLote,
    ConsultarLoteResponse,
    ConsultarResponse,
    Emitir,
    EmitirEmLote,
    EmitirEmLoteResponse,
    EmitirResponse,
)

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class InotaFiscalEletronicaServicoCancelarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoCancelarInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        Cancelar: Optional[Cancelar] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InotaFiscalEletronicaServicoCancelarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoCancelarOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarResponse: Optional[CancelarResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InotaFiscalEletronicaServicoCancelarOutput.Body.Fault"
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


@dataclass
class InotaFiscalEletronicaServicoConsultarLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoConsultarLoteInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarLote: Optional[ConsultarLote] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InotaFiscalEletronicaServicoConsultarLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoConsultarLoteOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarLoteResponse: Optional[ConsultarLoteResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InotaFiscalEletronicaServicoConsultarLoteOutput.Body.Fault"
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


@dataclass
class InotaFiscalEletronicaServicoConsultarInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoConsultarInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        Consultar: Optional[Consultar] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InotaFiscalEletronicaServicoConsultarOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoConsultarOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarResponse: Optional[ConsultarResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InotaFiscalEletronicaServicoConsultarOutput.Body.Fault"
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


@dataclass
class InotaFiscalEletronicaServicoEmitirEmLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoEmitirEmLoteInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        EmitirEmLote: Optional[EmitirEmLote] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InotaFiscalEletronicaServicoEmitirEmLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoEmitirEmLoteOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        EmitirEmLoteResponse: Optional[EmitirEmLoteResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InotaFiscalEletronicaServicoEmitirEmLoteOutput.Body.Fault"
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


@dataclass
class InotaFiscalEletronicaServicoEmitirInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoEmitirInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        Emitir: Optional[Emitir] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InotaFiscalEletronicaServicoEmitirOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["InotaFiscalEletronicaServicoEmitirOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EmitirResponse: Optional[EmitirResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InotaFiscalEletronicaServicoEmitirOutput.Body.Fault"
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


class InotaFiscalEletronicaServicoCancelar:
    URI = "#BasicHttpBinding_INotaFiscalEletronicaServico_policy"
    style = "document"
    location = "https://nfe.osasco.sp.gov.br/EissnfeWebServices/NotaFiscalEletronica.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INotaFiscalEletronicaServico/Cancelar"
    input = InotaFiscalEletronicaServicoCancelarInput
    output = InotaFiscalEletronicaServicoCancelarOutput


class InotaFiscalEletronicaServicoConsultar:
    URI = "#BasicHttpBinding_INotaFiscalEletronicaServico_policy"
    style = "document"
    location = "https://nfe.osasco.sp.gov.br/EissnfeWebServices/NotaFiscalEletronica.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INotaFiscalEletronicaServico/Consultar"
    input = InotaFiscalEletronicaServicoConsultarInput
    output = InotaFiscalEletronicaServicoConsultarOutput


class InotaFiscalEletronicaServicoConsultarLote:
    URI = "#BasicHttpBinding_INotaFiscalEletronicaServico_policy"
    style = "document"
    location = "https://nfe.osasco.sp.gov.br/EissnfeWebServices/NotaFiscalEletronica.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/INotaFiscalEletronicaServico/ConsultarLote"
    )
    input = InotaFiscalEletronicaServicoConsultarLoteInput
    output = InotaFiscalEletronicaServicoConsultarLoteOutput


class InotaFiscalEletronicaServicoEmitir:
    URI = "#BasicHttpBinding_INotaFiscalEletronicaServico_policy"
    style = "document"
    location = "https://nfe.osasco.sp.gov.br/EissnfeWebServices/NotaFiscalEletronica.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INotaFiscalEletronicaServico/Emitir"
    input = InotaFiscalEletronicaServicoEmitirInput
    output = InotaFiscalEletronicaServicoEmitirOutput


class InotaFiscalEletronicaServicoEmitirEmLote:
    URI = "#BasicHttpBinding_INotaFiscalEletronicaServico_policy"
    style = "document"
    location = "https://nfe.osasco.sp.gov.br/EissnfeWebServices/NotaFiscalEletronica.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INotaFiscalEletronicaServico/EmitirEmLote"
    input = InotaFiscalEletronicaServicoEmitirEmLoteInput
    output = InotaFiscalEletronicaServicoEmitirEmLoteOutput
