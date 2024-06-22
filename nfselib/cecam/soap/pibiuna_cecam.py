from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class CancelarNotaFiscalEletronica:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfprestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNotaFiscalEletronicaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarNotaFiscalEletronicaResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaItensAtividade:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjCpfRequisitante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlConsultaItensAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaItensAtividadeResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultaItensAtividadeResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaTiposServicos:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjCpfRequisitante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlConsultaServicos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaTiposServicosResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultaTiposServicosResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNotaFiscal:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfprestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNotaFiscalResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNotaFiscalResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscal:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfprestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalDeTeste:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfprestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalDeTesteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteNotaFiscalDeTesteResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteNotaFiscalResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalTomador:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotasTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalTomadorDeTeste:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjcpfTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xmlNotasTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalTomadorDeTesteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteNotaFiscalTomadorDeTesteResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteNotaFiscalTomadorResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteNotaFiscalTomadorResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WsIsseletronicoSoapCancelarNotaFiscalEletronicaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapCancelarNotaFiscalEletronicaInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNotaFiscalEletronica: Optional[
            CancelarNotaFiscalEletronica
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapCancelarNotaFiscalEletronicaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapCancelarNotaFiscalEletronicaOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNotaFiscalEletronicaResponse: Optional[
            CancelarNotaFiscalEletronicaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapCancelarNotaFiscalEletronicaOutput.Body.Fault"
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
class WsIsseletronicoSoapConsultaItensAtividadeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultaItensAtividadeInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaItensAtividade: Optional[ConsultaItensAtividade] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapConsultaItensAtividadeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultaItensAtividadeOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaItensAtividadeResponse: Optional[
            ConsultaItensAtividadeResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapConsultaItensAtividadeOutput.Body.Fault"
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
class WsIsseletronicoSoapConsultaTiposServicosInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultaTiposServicosInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaTiposServicos: Optional[ConsultaTiposServicos] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapConsultaTiposServicosOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultaTiposServicosOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaTiposServicosResponse: Optional[
            ConsultaTiposServicosResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapConsultaTiposServicosOutput.Body.Fault"
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
class WsIsseletronicoSoapConsultarNotaFiscalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultarNotaFiscalInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNotaFiscal: Optional[ConsultarNotaFiscal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapConsultarNotaFiscalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapConsultarNotaFiscalOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNotaFiscalResponse: Optional[ConsultarNotaFiscalResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional[
            "WsIsseletronicoSoapConsultarNotaFiscalOutput.Body.Fault"
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
class WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalDeTeste: Optional[EnviarLoteNotaFiscalDeTeste] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )


@dataclass
class WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalDeTesteResponse: Optional[
            EnviarLoteNotaFiscalDeTesteResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteOutput.Body.Fault"
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
class WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalTomadorDeTeste: Optional[
            EnviarLoteNotaFiscalTomadorDeTeste
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalTomadorDeTesteResponse: Optional[
            EnviarLoteNotaFiscalTomadorDeTesteResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteOutput.Body.Fault"
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
class WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalTomador: Optional[EnviarLoteNotaFiscalTomador] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )


@dataclass
class WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalTomadorResponse: Optional[
            EnviarLoteNotaFiscalTomadorResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorOutput.Body.Fault"
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
class WsIsseletronicoSoapEnviarLoteNotaFiscalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapEnviarLoteNotaFiscalInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscal: Optional[EnviarLoteNotaFiscal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class WsIsseletronicoSoapEnviarLoteNotaFiscalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsIsseletronicoSoapEnviarLoteNotaFiscalOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        EnviarLoteNotaFiscalResponse: Optional[
            EnviarLoteNotaFiscalResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "WsIsseletronicoSoapEnviarLoteNotaFiscalOutput.Body.Fault"
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


class WsIsseletronicoSoapCancelarNotaFiscalEletronica:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/CancelarNotaFiscalEletronica"
    input = WsIsseletronicoSoapCancelarNotaFiscalEletronicaInput
    output = WsIsseletronicoSoapCancelarNotaFiscalEletronicaOutput


class WsIsseletronicoSoapConsultaItensAtividade:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultaItensAtividade"
    input = WsIsseletronicoSoapConsultaItensAtividadeInput
    output = WsIsseletronicoSoapConsultaItensAtividadeOutput


class WsIsseletronicoSoapConsultaTiposServicos:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultaTiposServicos"
    input = WsIsseletronicoSoapConsultaTiposServicosInput
    output = WsIsseletronicoSoapConsultaTiposServicosOutput


class WsIsseletronicoSoapConsultarNotaFiscal:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultarNotaFiscal"
    input = WsIsseletronicoSoapConsultarNotaFiscalInput
    output = WsIsseletronicoSoapConsultarNotaFiscalOutput


class WsIsseletronicoSoapEnviarLoteNotaFiscal:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/EnviarLoteNotaFiscal"
    input = WsIsseletronicoSoapEnviarLoteNotaFiscalInput
    output = WsIsseletronicoSoapEnviarLoteNotaFiscalOutput


class WsIsseletronicoSoapEnviarLoteNotaFiscalDeTeste:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/EnviarLoteNotaFiscalDeTeste"
    input = WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteInput
    output = WsIsseletronicoSoapEnviarLoteNotaFiscalDeTesteOutput


class WsIsseletronicoSoapEnviarLoteNotaFiscalTomador:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/EnviarLoteNotaFiscalTomador"
    input = WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorInput
    output = WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorOutput


class WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTeste:
    style = "document"
    location = (
        "http://177.130.116.50/cecam.issweb/webservices/wsisseletronico.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/EnviarLoteNotaFiscalTomadorDeTeste"
    input = WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteInput
    output = WsIsseletronicoSoapEnviarLoteNotaFiscalTomadorDeTesteOutput
